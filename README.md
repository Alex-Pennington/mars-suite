# Phoenix Nest MARS Communications Suite

Open-source HF digital communications tools for Military Auxiliary Radio System (MARS) operations.

**Developer:** Alex Pennington (KY4OLB, formerly AAR4TE / NNN0VO)  
**Project Site:** [www.organicengineer.com/projects](https://www.organicengineer.com/projects)  
**Contact:** projects@organicengineer.com

---

## Overview

The Phoenix Nest MARS Suite is an open-source implementation of MIL-STD-188-110A HF modem with MELP-e voice codec support. This project provides amateur radio operators and MARS members with professional-grade digital communications tools without licensing costs.

## Repositories

| Repository | Description | Status |
|------------|-------------|--------|
| [**pennington_m110a_demod**](https://github.com/Alex-Pennington/pennington_m110a_demod) | MIL-STD-188-110A HF modem - all 11 modes, turbo EQ, MS-DMT compatible | ✅ Active |
| [**phoenix_nest_mars**](https://github.com/Alex-Pennington/phoenix_nest_mars) | MARS ops suite: CP, Station Mapper, Crypto, Propagation | ✅ Building |
| [**brain_core**](https://github.com/Alex-Pennington/brain_core) | Charles Brain (G4GUO) modem core (reference implementation for testing) | ✅ Reference |
| [**MARS_GIS**](https://github.com/Alex-Pennington/MARS_GIS) | QGIS project for FEMA region map generation | ✅ Working |

## Features

- Full MIL-STD-188-110A implementation (all 11 waveform modes)
- MELP-e voice codec support
- MS-DMT protocol compatibility for interoperability testing
- Cross-modem validation using brain_core reference implementation
- Advanced frequency correction and wideband AFC

---

## Development Methodology & AI Assistance

This project was developed using AI-assisted coding tools. In the interest of transparency, here's what that means:

### AI Tools Used

| Tool | Purpose | Investment |
|------|---------|------------|
| Claude Pro (Anthropic) | Architecture, DSP algorithms, documentation, code review | ~$40 |
| GitHub Copilot | In-editor code completion and suggestions | $400 |
| Claude API | Automated testing and integration workflows | $50 |
| **Total** | | **~$490** |

### What AI Did vs. What I Did

**AI accelerated:**
- Boilerplate code generation
- Documentation drafting
- Algorithm implementation from specifications
- Code refactoring and optimization suggestions
- Test case generation

**Human expertise required:**
- MIL-STD-188-110A domain knowledge (the AI doesn't know this standard)
- Architecture decisions and design choices
- Validation against real RF signals
- Integration with existing MARS infrastructure
- 35 years of programming experience directing the work

The AI doesn't know MIL-STD-188-110A from a ham sandwich. What it *can* do is rapidly implement algorithms once you explain them, catch bugs, and handle the tedious parts. The domain expertise, the "what to build and why," and the validation — that's still entirely human.

### Why Disclose This?

1. **Transparency** — Other developers should know how this was built
2. **Reproducibility** — Similar projects can estimate their own AI tooling costs  
3. **Honest expectations** — AI coding assistance is powerful but not magic; it still requires domain expertise to direct effectively

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

*Last updated: December 2025*
