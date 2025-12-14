# Phoenix Nest MARS Communications Suite

Open-source HF digital communications tools for Military Auxiliary Radio System (MARS) operations.

**Developer:** Alex Pennington (KY4OLB, formerly AAR4TE / NNN0VO)  
**Project Site:** [www.organicengineer.com/projects](https://www.organicengineer.com/projects)  
**Contact:** projects@organicengineer.com

---

## Current Status (December 2025)

| Component | Status | Notes |
|-----------|--------|-------|
| **MIL-STD-188-110A Modem** | ✅ Ready | All 12 modes, cross-modem validated |
| **SDR I/Q Pipeline** | ✅ Ready | 31/31 tests passing, awaiting real-world captures |
| **phoenix_sdr (SDRplay)** | ✅ Ready | RSP2 Pro interface, .iqr recording |
| **Beta Testing** | 🟡 Open | Looking for testers with SDRplay hardware |

**Next Milestone:** Real-world OTA signal capture and decode validation

---

## Overview

The Phoenix Nest MARS Suite is an open-source implementation of MIL-STD-188-110A HF modem with MELP-e voice codec support. This project provides amateur radio operators and MARS members with professional-grade digital communications tools without licensing costs.

## Repositories

| Repository | Description | Status |
|------------|-------------|--------|
| [**pennington_m110a_demod**](https://github.com/Alex-Pennington/pennington_m110a_demod) | MIL-STD-188-110A HF modem - all 12 modes, turbo EQ, MS-DMT compatible | ✅ Active |
| [**phoenix_sdr**](https://github.com/Alex-Pennington/phoenix_sdr) | SDRplay RSP2 Pro integration - I/Q capture for direct SDR receive | ✅ Active |
| [**phoenix_nest_mars**](https://github.com/Alex-Pennington/phoenix_nest_mars) | MARS ops suite: CP, Station Mapper, Crypto, Propagation | 🔨 Building |
| [**brain_core**](https://github.com/Alex-Pennington/brain_core) | Charles Brain (G4GUO) modem core (reference implementation for testing) | ✅ Reference |
| [**MARS_GIS**](https://github.com/Alex-Pennington/MARS_GIS) | QGIS project for FEMA region map generation | ✅ Working |
| [**MARS-History-Project**](https://github.com/Alex-Pennington/MARS-History-Project) | SME Interview System - AI-powered knowledge capture from HF experts | ✅ Active |

## Features

- Full MIL-STD-188-110A implementation (all 12 waveform modes)
- **Direct SDR receive** via SDRplay RSP2 Pro (I/Q input at 2 MSPS)
- MELP-e voice codec support (Codec2 open-source alternative included)
- MS-DMT protocol compatibility for interoperability testing
- Cross-modem validation using brain_core reference implementation
- Advanced frequency correction and wideband AFC

---

## I/Q Pipeline Status

The SDR receive chain is validated and ready:

```
SDRplay RSP2 Pro → phoenix_sdr → .iqr file → IQFileSource → IQSource → Demodulator
     (2 MSPS)                                              (decimate)    (48 kHz)
```

**Test Results:**
| Test Suite | Pass | Total |
|------------|------|-------|
| IQSource format conversion | 10 | 10 |
| IQFileSource .iqr loading | 11 | 11 |
| I/Q pipeline loopback | 10 | 10 |
| **Total** | **31** | **31** |

**What's Proven:**
- Signal amplitude preserved (rms_ratio = 1.00)
- int16 quantization quality (82.2 dB SNR)
- Format consistency (planar == interleaved)
- .iqr file round-trip integrity

---

## Beta Testing

Want to help test? See the [Beta Testing Guide](https://github.com/Alex-Pennington/phoenix_sdr/blob/main/docs/BETA_TESTING_GUIDE.md) for instructions.

**Current Focus:** WWV tick detection — validates SDR capture chain before modem integration.

**What you need:**
- SDRplay RSP2 Pro (or compatible)
- Windows 10/11 PC
- SDRplay API v3.x installed
- HF antenna (any antenna that can receive 5-15 MHz)

**Quick start (tune slightly off-center to avoid DC hole):**
```powershell
# 5 MHz (night) | 10 MHz (day) | 15 MHz (daytime long distance)
cmd /c ".\bin\simple_am_receiver.exe -f 5.000450 -g 59 -l 0 -o | .\bin\waterfall.exe"
```

**What validates success:**
- Ticks detected every ~1000ms (950-1050ms acceptable)
- Purple flash on bar 5 (1000 Hz) with each tick
- Average interval converging to 1000ms
- Note: Seconds 29 and 59 have NO tick (intentional WWV gap)

---

## Quick Links

| Document | Description |
|----------|-------------|
| [Modem README](https://github.com/Alex-Pennington/pennington_m110a_demod/blob/master/README.md) | Main modem documentation |
| [SDR README](https://github.com/Alex-Pennington/phoenix_sdr/blob/main/README.md) | SDRplay integration docs |
| [Beta Testing Guide](https://github.com/Alex-Pennington/phoenix_sdr/blob/main/docs/BETA_TESTING_GUIDE.md) | Step-by-step testing instructions |
| [I/Q Integration Design](https://github.com/Alex-Pennington/phoenix_sdr/blob/main/docs/IQ_INPUT_DESIGN.md) | Technical design for SDR→modem interface |

---

## Development Cost Tracking

This project was developed using AI-assisted coding tools. In the interest of transparency, here's the running cost breakdown:

### Subscription Costs (3 months: Oct-Dec 2025)

| Subscription | Monthly | 3 Months |
|--------------|---------|----------|
| Claude Max | $100 | $300 |
| GitHub Copilot | $50 | $150 |
| **Subtotal** | | **$450** |

*Note: Claude Max occasionally requires $5-10 overage bumps to maintain usage limits.*

### API/Usage Costs by Component

| Component | Repository | Cost | Notes |
|-----------|------------|------|-------|
| **Pennington Modem Core** | pennington_m110a_demod | $150 | Full 110A implementation, 12 modes |
| **SDRplay Integration** | phoenix_sdr | $50 | RSP2 Pro interface, I/Q pipeline |
| **Brain Core Wrapper** | brain_core | $20 | TCP/IP wrapper for reference modem |
| **HF Channel Simulator** | (in modem repo) | $5 | Watterson model, CCIR presets |
| **Subtotal** | | **$225** | |

### Total Investment

| Category | Amount |
|----------|--------|
| Subscriptions (3 months) | $450 |
| API/Usage Costs | $225 |
| **Grand Total** | **$675+** |

### What AI Does vs. Human Expertise

**AI accelerates:**
- Boilerplate code generation
- Documentation drafting
- Algorithm implementation from specifications
- Code refactoring and test generation

**Human expertise required:**
- MIL-STD-188-110A domain knowledge (AI doesn't know this standard)
- Architecture decisions and design choices
- Validation against real RF signals
- Integration with existing MARS infrastructure
- 35 years of programming experience directing the work

The AI doesn't know MIL-STD-188-110A from a ham sandwich. What it *can* do is rapidly implement algorithms once you explain them, catch bugs, and handle the tedious parts. The domain expertise, the "what to build and why," and the validation — that's still entirely human.

### Why Track This?

1. **Transparency** — Other developers should know how this was built
2. **Reproducibility** — Similar projects can estimate their own AI tooling costs  
3. **Honest expectations** — AI coding assistance is powerful but not magic

---

## Getting Started

See individual repository READMEs for installation and usage instructions.

## License

This project is open source. See LICENSE file in each repository for specific terms.

## Acknowledgments

- **Steve Hajducek (N2CKH)** — MS-DMT, MARS-ALE, Chief Navy MARS staff for ALE/MIL-STD development, introduction to this project space
- **Charles Brain (G4GUO)** — brain_core reference implementation, PC-ALE
- The MARS community

---

*Last updated: December 12, 2025*
