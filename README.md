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

## Repositories

| Repository | Description |
|------------|-------------|
| [**mars-suite**](https://github.com/Alex-Pennington/mars-suite) | Public home of the suite. Ask every question, modem questions included, in [mars-suite issues](https://github.com/Alex-Pennington/mars-suite/issues). Releases will be published here. |
| [**phoenix_nest_mars**](https://github.com/Alex-Pennington/phoenix_nest_mars) | Message core: Communications Processor (message handling), Station Mapper Linux, and VOACAP-based propagation prediction. The appliance code is on branch [`feat/appliance-core`](https://github.com/Alex-Pennington/phoenix_nest_mars/tree/feat/appliance-core). |

---

## Earlier work

Earlier public repositories from this project:

- [pennington_m110a_demod](https://github.com/Alex-Pennington/pennington_m110a_demod): MIL-STD-188-110A HF modem
- [brain_core](https://github.com/Alex-Pennington/brain_core): TCP wrapper around the Brain reference modem, for cross-modem testing
- [phoenix_sdr](https://github.com/Alex-Pennington/phoenix_sdr): original SDR monolith, archived and split into the phoenix-* repos below
- [phoenix-kiss-fft](https://github.com/Alex-Pennington/phoenix-kiss-fft): FFT library for signal processing
- [phoenix-sdr-core](https://github.com/Alex-Pennington/phoenix-sdr-core): SDRplay hardware interface, decimation, TCP control
- [phoenix-waterfall](https://github.com/Alex-Pennington/phoenix-waterfall): SDL2 waterfall display with WWV detection
- [phoenix-wwv](https://github.com/Alex-Pennington/phoenix-wwv): WWV detection library (tick, marker, BCD decoding)
- [phoenix-sdr-net](https://github.com/Alex-Pennington/phoenix-sdr-net): network streaming of I/Q data
- [phoenix-sdr-utils](https://github.com/Alex-Pennington/phoenix-sdr-utils): SDR utilities (I/Q playback, WWV analysis, telemetry logging)
- [phoenix-reference-library](https://github.com/Alex-Pennington/phoenix-reference-library): technical documentation (WWV specs, NTP driver36)
- [MARS_GIS](https://github.com/Alex-Pennington/MARS_GIS): QGIS project and Python scripts for FEMA region maps
- [MARS-History-Project](https://github.com/Alex-Pennington/MARS-History-Project): SME interview system for knowledge capture

---

## Features

- **Full MIL-STD-188-110A implementation** — All 12 waveform modes (75-4800 bps) with turbo equalization
- **Direct SDR receive** — SDRplay RSP2 Pro I/Q input at 2 MSPS with multi-stage decimation
- **WWV time signal detection** — Tick, marker, and BCD time code decoding validates SDR chain
- **Cross-modem interoperability** — 9/12 modes validated with brain_core (G4GUO) reference
- **MELP-e voice codec support** — Codec2 open-source alternative included
- **MARS operations tools** — CP (Communications Processor), Station Mapper, VOACAP propagation
- **Advanced equalization** — 7 equalizers (DFE, MLSE, RLS, Turbo) for varying channel conditions
- **Modular architecture** — 7 focused Phoenix SDR repos for reusability
- **Knowledge capture** — AI-powered SME interview system for institutional history
- **GIS mapping** — QGIS integration for FEMA region visualization

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
| [phoenix_nest_mars README](https://github.com/Alex-Pennington/phoenix_nest_mars/blob/main/README.md) | Message core documentation |
| [mars-suite issues](https://github.com/Alex-Pennington/mars-suite/issues) | Questions and support |

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
- **Charles Brain (G4GUO)** — brain_core reference implementation, PC-ALE, cross-modem interoperability validation
- **David Mills** — NTP driver36 architecture that inspired WWV detection design
- The MARS community

---

*Last updated: December 21, 2025*
