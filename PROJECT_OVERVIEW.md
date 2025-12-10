# Phoenix Nest MARS Suite — Project Overview

## Why This Project Exists

The goal is simple: **get MELP-e (Mixed Excitation Linear Prediction - Enhanced) voice codec working over HF radio.**

MELP-e is the military-standard vocoder used for secure voice communications. It compresses voice down to bit rates low enough to transmit over HF channels (2400 bps and below). But the vocoder is only half the problem — you also need a modem to carry those bits across the air.

That modem is MIL-STD-188-110A.

## The Transport Layer Problem

Before we can test MELP-e voice, we need to verify that our MIL-STD-188-110A modem implementation actually works — that it can successfully exchange data with other 110A modems in the wild.

The most widely-used amateur/MARS implementation is Paul Brain's Cm110s modem core, which powers AF-DM (Air Force Digital Modem), MS-DMT (by Steve Hajducek), and other tools. Steve Hajducek's work on MS-DMT is what originally brought this project to our attention and set us on this path. If Phoenix Nest's modem can talk to Brain's modem, it can talk to most of the 110A ecosystem.

**The interoperability requirement:**
- Phoenix Nest TX → Brain RX: Must decode correctly
- Brain TX → Phoenix Nest RX: Must decode correctly

If both directions work, we have a verified transport layer. Then we can layer MELP-e on top and start testing actual voice.

## Why Software Testing Wasn't Possible Before

The obvious way to test interoperability is over RF: set up two radios, transmit from one, receive on the other. But this introduces variables — propagation, noise, equipment differences — that make it hard to isolate software bugs from RF problems.

The right approach is to verify in software first:
1. Generate TX audio from one modem
2. Feed that audio directly into the other modem's receiver
3. Check if it decodes correctly

Simple in theory. The problem: **AF-DM and MS-DMT have no way to inject audio into their receivers.**

These are GUI applications designed to work with soundcards. They have no command-line interface for testing, no way to feed a PCM file to the decoder, no scripted test capability. If you want to test whether your TX will decode on Brain's RX, you have to actually transmit it over the air.

This made systematic software verification impossible.

## What We Built

### brain_core — Headless Server with RX Inject

We took Paul Brain's Cm110s modem library (the same DSP core that AF-DM uses) and wrapped it in a headless TCP server. No GUI, no soundcard dependencies — just a network interface for control and data.

**The key addition: `CMD:RXAUDIOINJECT:<path>`**

This command feeds a PCM audio file directly into the modem's receiver chain. The audio goes through the same DSP pipeline it would if it came from a soundcard — demodulation, equalization, Viterbi decoding, de-interleaving — and decoded data comes out the other end.

This capability didn't exist before. We created it specifically to enable software-only interoperability testing.

**Other features:**
- TCP control port (3999) for commands
- TCP data port (3998) for TX/RX data
- Automatic PCM capture of all TX audio
- Same command set as Phoenix Nest for easy cross-testing
- All source code included (modem core + wrapper)

Repository: https://github.com/Alex-Pennington/brain_core

### mars-suite — Phoenix Nest Implementation

Our own MIL-STD-188-110A implementation with the same TCP interface. Built from scratch based on the MIL-STD specification, with reference to Brain's implementation for timing and preamble structure details.

**Features:**
- Full 110A modem (75 bps through 2400 bps, short and long interleave)
- Headless TCP server (matching brain_core interface)
- RX audio inject capability
- TX PCM capture
- Designed for MELP-e integration

Repository: https://github.com/Alex-Pennington/mars-suite

## The Testing Methodology

With both modems supporting RX inject and TX capture, we can now do full cross-verification in software:

### Test 1: Phoenix Nest TX → Brain RX

```
1. Connect to Phoenix Nest server (control: 4999, data: 4998)
2. Send test data to data port
3. Set mode: CMD:DATA RATE:600S
4. Transmit: CMD:SENDBUFFER
5. Collect PCM file from ./tx_pcm_out/

6. Connect to brain_core server (control: 3999, data: 3998)
7. Inject PCM: CMD:RXAUDIOINJECT:<path_to_pcm>
8. Read decoded data from data port
9. Compare to original test data
```

If the decoded data matches, Phoenix Nest's TX is Brain-compatible.

### Test 2: Brain TX → Phoenix Nest RX

```
1. Connect to brain_core server
2. Send test data, set mode, transmit
3. Collect PCM file

4. Connect to Phoenix Nest server
5. Inject PCM: CMD:RXAUDIOINJECT:<path_to_pcm>
6. Read decoded data
7. Compare to original
```

If this also passes, Phoenix Nest's RX is Brain-compatible.

### Test 3: Mode Sweep

Repeat tests 1 and 2 for all supported modes:
- 75S, 75L (75 bps short/long interleave)
- 150S, 150L
- 300S, 300L
- 600S, 600L
- 1200S, 1200L
- 2400S, 2400L

### Test 4: Loopback Verification

Each modem should also pass its own loopback test (TX → RX within the same implementation) to verify internal consistency.

## What We Learned (So Far)

### The 288-Symbol Problem

During initial testing, Phoenix Nest TX was not decoding on Brain RX. Analysis revealed:

| Property | Brain TX | Phoenix Nest TX |
|----------|----------|-----------------|
| Symbol count | 3,360 | 3,072 |
| Difference | **288 symbols** | |

The missing 288 symbols are a calibration burst at the start of transmission. Brain's implementation includes:
1. AGC settling time
2. Soft power ramp-up
3. Calibration pattern before the standard preamble

Phoenix Nest was jumping straight to full power with the standard preamble. Brain's receiver, expecting the calibration burst, wasn't synchronizing correctly.

**Fix applied:** Phoenix Nest TX now includes the 288-symbol calibration burst with soft ramp-up envelope.

### Key Parameters Confirmed

From reverse-engineering AF-DM/MS-DMT and testing against Brain's implementation:

| Parameter | Value |
|-----------|-------|
| Internal sample rate | 9600 Hz |
| Audio I/O rate | 48000 Hz (5x interpolation) |
| Carrier frequency | 1800 Hz |
| Soundblock size | 1920 samples (200ms) |
| Symbol rate (600 bps) | 2400 symbols/sec |

## The Path Forward

### Phase 1: Modem Verification (Current)
- [x] brain_core server with RX inject
- [x] Phoenix Nest server with matching interface
- [x] Automated loopback tests
- [x] Cross-modem TX comparison tools
- [ ] Full mode sweep verification
- [ ] Document any remaining interop issues

### Phase 2: RF Validation
- [ ] Over-the-air testing with actual radios
- [ ] Real channel conditions (noise, multipath, fading)
- [ ] Volunteer testers with HF equipment

### Phase 3: MELP-e Integration
- [ ] MELP-e encoder/decoder implementation
- [ ] Voice → MELP-e → 110A TX chain
- [ ] 110A RX → MELP-e → Voice chain
- [ ] End-to-end voice testing

### Phase 4: Real-World Deployment
- [ ] GUI application for operators
- [ ] Integration with existing MARS workflows
- [ ] Field testing on MARS nets

## Technical Reference

### TCP Interface (Both Modems)

**Control Port Commands:**

| Command | Description |
|---------|-------------|
| `CMD:DATA RATE:<mode>` | Set mode (e.g., "600S", "1200L") |
| `CMD:SENDBUFFER` | Transmit buffered data |
| `CMD:RESET MDM` | Reset modem state |
| `CMD:KILL TX` | Abort transmission |
| `CMD:RXAUDIOINJECT:<path>` | Inject PCM file to RX |
| `CMD:QUERY:STATUS` | Get modem status |
| `CMD:QUERY:VERSION` | Get version string |

**Data Port:**
- Send bytes to queue for transmission
- Receive decoded bytes after RX

**PCM Format:**
- 48000 Hz sample rate
- 16-bit signed integers
- Mono

### Repository Structure

```
mars-suite/
├── src/                 # Phoenix Nest modem source
├── tests/               # Automated test scripts
├── docs/                # Technical documentation
└── README.md

brain_core/
├── m188110a/            # Paul Brain's Cm110s library
├── src/                 # TCP server wrapper
├── tx_pcm_out/          # TX audio captures
├── loopback_test.py     # Self-test script
├── compare_tx_output.py # Cross-modem comparison
└── README.md
```

## Contributing

We're looking for:
- Beta testers with HF radios and audio interfaces
- Code review on the modem implementations
- MELP-e expertise
- Documentation improvements

Contact: alex.pennington@organicengineer.com

## Credits

- **Paul Brain** — Original Cm110s MIL-STD-188-110A modem core
- **Steve Hajducek** — MS-DMT, whose work set us on this path
- **Perry (AFA4NQ)** — AF-DM GUI wrapper
- **Phoenix Nest LLC** — brain_core server, mars-suite, MELP-e integration

## License

- brain_core wrapper: GPL-3.0-or-later (Phoenix Nest LLC)
- Cm110s modem core: Original license applies (see m188110a/)
- mars-suite: GPL-3.0-or-later (Phoenix Nest LLC)
