# Phoenix Nest MARS Communications Suite

Open-source HF digital communications tools for Military Auxiliary Radio System (MARS) operations.

**Developer:** Alex Pennington (KY4OLB, formerly AAR4TE / NNN0VO)  
**Project Site:** [www.organicengineer.com/projects](https://www.organicengineer.com/projects)  
**Contact:** projects@organicengineer.com

---

## Current Status (December 2025)

| Component | Status | Notes |
|-----------|--------|-------|
| **MIL-STD-188-110A Modem** | ✅ v1.6.1 | Build 325, cross-modem interop validated |
| **Phoenix SDR Suite** | ✅ v0.3.0 | 7-repo modular architecture |
| **WWV Time Detection** | ✅ Working | Tick/marker/BCD decoding operational |
| **Beta Testing** | 🟡 Open | Looking for testers with SDRplay hardware |

**Next Milestone:** Real-world OTA signal capture and decode validation

---

## Overview

The Phoenix Nest MARS Suite is an open-source implementation of MIL-STD-188-110A HF modem with MELP-e voice codec support. This project provides amateur radio operators and MARS members with professional-grade digital communications tools without licensing costs.

---

## Phoenix SDR Repositories

The Phoenix SDR system has been split into focused, modular repositories:

| Repository | Description | Status |
|------------|-------------|--------|
| [**phoenix-kiss-fft**](https://github.com/Alex-Pennington/phoenix-kiss-fft) | FFT library for signal processing | ✅ v0.1.0 |
| [**phoenix-reference-library**](https://github.com/Alex-Pennington/phoenix-reference-library) | Technical documentation (WWV specs, NTP driver36) | ✅ v0.1.0 |
| [**phoenix-sdr-core**](https://github.com/Alex-Pennington/phoenix-sdr-core) | SDRplay RSP2 Pro hardware interface, decimation, TCP control | ✅ v0.1.0 |
| [**phoenix-waterfall**](https://github.com/Alex-Pennington/phoenix-waterfall) | SDL2 waterfall display with WWV detection | ✅ v0.1.0 |
| [**phoenix-wwv**](https://github.com/Alex-Pennington/phoenix-wwv) | WWV detection library (tick, marker, BCD decoding) | ✅ v0.1.0 |
| [**phoenix-sdr-net**](https://github.com/Alex-Pennington/phoenix-sdr-net) | Network streaming (sdr_server, signal_relay, splitter) | ✅ v0.1.0 |
| [**phoenix-sdr-utils**](https://github.com/Alex-Pennington/phoenix-sdr-utils) | Utilities (iqr_play, wwv_analyze, telem_logger) | ✅ v0.1.0 |

### Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        Phoenix Nest MARS Suite                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌─────────────────┐                                                       │
│   │  phoenix-kiss-  │  FFT library (dependency for all signal processing)  │
│   │      fft        │                                                       │
│   └────────┬────────┘                                                       │
│            │                                                                │
│   ┌────────┴────────┐                                                       │
│   │ phoenix-sdr-    │  SDRplay hardware interface                          │
│   │     core        │  └─ Decimation, TCP control, I/Q streaming           │
│   └────────┬────────┘                                                       │
│            │                                                                │
│   ┌────────┼────────────────────────────────┐                              │
│   │        │                                │                              │
│   ▼        ▼                                ▼                              │
│ ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                      │
│ │   phoenix-   │  │   phoenix-   │  │   phoenix-   │                      │
│ │  waterfall   │  │     wwv      │  │   sdr-net    │                      │
│ │              │  │              │  │              │                      │
│ │ SDL2 display │  │ Detection    │  │ TCP/UDP      │                      │
│ │ + WWV detect │  │ library      │  │ streaming    │                      │
│ └──────────────┘  └──────────────┘  └──────────────┘                      │
│                                                                             │
│   ┌──────────────────────────────────────────────────┐                     │
│   │              phoenix-sdr-utils                    │                     │
│   │  iqr_play, wwv_analyze, telem_logger, gps_time   │                     │
│   └──────────────────────────────────────────────────┘                     │
│                                                                             │
│   ┌──────────────────────────────────────────────────┐                     │
│   │          phoenix-reference-library               │                     │
│   │  Technical documentation, WWV specs, references  │                     │
│   └──────────────────────────────────────────────────┘                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Other MARS Repositories

| Repository | Description | Status |
|------------|-------------|--------|
| [**pennington_m110a_demod**](https://github.com/Alex-Pennington/pennington_m110a_demod) | MIL-STD-188-110A HF modem - all 12 modes, turbo EQ, MS-DMT compatible | ✅ v1.6.1 b325 |
| [**phoenix_sdr_controller**](https://github.com/Alex-Pennington/phoenix_sdr_controller) | SDL2 Windows GUI for TCP SDR control - presets, DC offset | ✅ v0.3.0 |
| [**phoenix_nest_mars**](https://github.com/Alex-Pennington/phoenix_nest_mars) | MARS ops suite: CP, Propagation (voacapl), Station Mapper | 🔨 Building |
| [**brain_core**](https://github.com/Alex-Pennington/brain_core) | Charles Brain (G4GUO) modem TCP server (ports 3998/3999) | ✅ Reference |
| [**MARS_GIS**](https://github.com/Alex-Pennington/MARS_GIS) | QGIS Python scripts for FEMA region map generation | ✅ Active |
| [**MARS-History-Project**](https://github.com/Alex-Pennington/MARS-History-Project) | SME Interview System v1.0.0 - Flask/Claude AI/Google TTS | ✅ v1.0.0 |

---

## Features

- Full MIL-STD-188-110A implementation (all 12 waveform modes)
- **Direct SDR receive** via SDRplay RSP2 Pro (I/Q input at 2 MSPS)
- **WWV time signal detection** — tick, marker, and BCD time code decoding
- MELP-e voice codec support (Codec2 open-source alternative included)
- MS-DMT protocol compatibility for interoperability testing
- Cross-modem validation using brain_core reference implementation
- Advanced frequency correction and wideband AFC
- Modular architecture for component reuse

---

## I/Q Pipeline Status

The SDR receive chain is validated and ready:

```
SDRplay RSP2 Pro → phoenix-sdr-core → phoenix-waterfall → WWV Detection
     (2 MSPS)        (decimation)       (display)         (phoenix-wwv)
                          │
                          └──→ phoenix-sdr-net → Remote clients
```

**Test Results:**
| Test Suite | Pass | Total |
|------------|------|-------|
| IQSource format conversion | 10 | 10 |
| IQFileSource .iqr loading | 11 | 11 |
| I/Q pipeline loopback | 10 | 10 |
| **Total** | **31** | **31** |

---

## Beta Testing

Want to help test? See the [Beta Testing Guide](https://github.com/Alex-Pennington/phoenix-waterfall/blob/main/docs/BETA_TESTING.md) for instructions.

**Current Focus:** WWV tick detection — validates SDR capture chain before modem integration.

**What you need:**
- SDRplay RSP2 Pro (or compatible)
- Windows 10/11 PC
- SDRplay API v3.x installed
- HF antenna (any antenna that can receive 5-15 MHz)

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
| [SDR Core README](https://github.com/Alex-Pennington/phoenix-sdr-core/blob/main/README.md) | SDRplay integration docs |
| [WWV Detection](https://github.com/Alex-Pennington/phoenix-wwv/blob/main/README.md) | WWV detection library |
| [Reference Library](https://github.com/Alex-Pennington/phoenix-reference-library/blob/main/README.md) | Technical documentation |

---

## Development Cost Tracking

This project was developed using AI-assisted coding tools. In the interest of transparency, here's the running cost breakdown:

### Subscription Costs (3 months: Oct-Dec 2025)

| Subscription | Monthly | 3 Months |
|--------------|---------|----------|
| Claude Max | $100 | $300 |
| GitHub Copilot | $50 | $150 |
| **Subtotal** | | **$450** |

### API/Usage Costs by Component

| Component | Repository | Cost | Notes |
|-----------|------------|------|-------|
| **Pennington Modem Core** | pennington_m110a_demod | $150 | Full 110A implementation, 12 modes |
| **Phoenix SDR Suite** | phoenix-* repos | $75 | SDR interface, WWV detection, waterfall |
| **Brain Core Wrapper** | brain_core | $20 | TCP/IP wrapper for reference modem |
| **HF Channel Simulator** | (in modem repo) | $5 | Watterson model, CCIR presets |
| **Subtotal** | | **$250** | |

### Total Investment

| Category | Amount |
|----------|--------|
| Subscriptions (3 months) | $450 |
| API/Usage Costs | $250 |
| **Grand Total** | **$700+** |

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

---

## Getting Started

1. Clone the repositories you need
2. Install SDRplay API v3.x (for hardware support)
3. Build using the provided build scripts
4. See individual repository READMEs for detailed instructions

## License

AGPL-3.0 for Phoenix SDR components. See LICENSE file in each repository for specific terms.

## Acknowledgments

- **Steve Hajducek (N2CKH)** — MS-DMT, MARS-ALE, Chief Navy MARS staff for ALE/MIL-STD development, introduction to this project space
- **Charles Brain (G4GUO)** — brain_core reference implementation, PC-ALE
- **David Mills** — NTP driver36 architecture that inspired WWV detection design
- The MARS community

---

*Last updated: December 21, 2025*
