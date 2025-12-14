# Phoenix Nest MARS Suite - Copilot Instructions

## Project Overview

This is a **documentation and coordination hub** for the Phoenix Nest MARS Communications Suite—an open-source MIL-STD-188-110A HF modem with MELP-e voice codec support. The actual code lives in separate repositories; this repo contains project-level documentation, development guides, and AI coding primers.

**Goal:** Enable MELP-e voice over HF radio by first validating the MIL-STD-188-110A transport layer.

## Repository Ecosystem

| Repository | Purpose |
|------------|---------|
| `pennington_m110a_demod` | Phoenix Nest MIL-STD-188-110A modem (all 12 modes) |
| `phoenix_sdr` | SDRplay RSP2 Pro integration for I/Q capture |
| `brain_core` | Charles Brain's Cm110s modem wrapped as TCP server (reference) |
| `phoenix_nest_mars` | MARS operations suite (under development) |
| `MARS_GIS` | QGIS project for FEMA region maps || `MARS-History-Project` | SME Interview System - AI-powered knowledge capture from HF experts |
## Key Technical Parameters

When working on modem-related documentation or specifications:
- **Internal sample rate:** 9600 Hz
- **Audio I/O rate:** 48000 Hz (5x interpolation)
- **Carrier frequency:** 1800 Hz
- **Soundblock size:** 1920 samples (200ms)
- **PCM format:** 48 kHz, 16-bit signed mono

## Phoenix SDR — WWV Beta Testing (phoenix_sdr repo)

Current focus: **WWV tick detection** validates the SDR capture chain before modem integration.

**Requirements:** SDRplay RSP2 Pro, SDRplay API v3.x, Windows 10/11, HF antenna

**Quick start (tune slightly off-center to avoid DC hole):**
```powershell
# 5 MHz (night) | 10 MHz (day) | 15 MHz (daytime long distance)
cmd /c ".\bin\simple_am_receiver.exe -f 5.000450 -g 59 -l 0 -o | .\bin\waterfall.exe"
```

**Display:** Split-screen with FFT waterfall (left) and 7 frequency bucket bars (right). Bar 5 (1000 Hz) flashes purple on tick detection.

**Keyboard controls:** `D` toggle detection, `S` stats, `0` gain adjust, `1-7` threshold select, `+/-` adjust, `Q` quit

**What validates success:**
- Ticks detected every ~1000ms (950-1050ms acceptable)
- Purple flash on bar 5 with each tick
- Average interval converging to 1000ms
- Note: Seconds 29 and 59 have NO tick (intentional WWV gap)

**Build:** `.\build.ps1` (requires MinGW/GCC, SDL2)

## TCP Interface Commands (brain_core & Phoenix Nest)

Both modems use matching TCP interfaces for cross-testing:
- **Control port:** 3999 (brain_core) / 4999 (Phoenix Nest)
- **Data port:** 3998 (brain_core) / 4998 (Phoenix Nest)
- Key command: `CMD:RXAUDIOINJECT:<path>` enables software-only interoperability testing

## AI-Assisted Development Context

This project documents AI coding workflows. When referencing or updating AI guidance:
- AI handles: boilerplate, algorithm implementation, documentation, test generation
- Human handles: MIL-STD-188-110A domain knowledge, architecture decisions, RF validation
- AI tools don't have MIL-STD-188-110A in training data—always provide spec context

## Documentation Standards

- Keep markdown consistent with existing files (use tables for structured data)
- Include accessibility notes where relevant (project supports OpenDyslexic font)
- Technical accuracy is critical—this is military-adjacent communications
- Reference specific repositories when discussing code or implementations

## What NOT to Include

Per [AI_Coding_Tools_Primer.md](AI_Coding_Tools_Primer.md#section-5-security-considerations):
- No classified information, COMSEC material, or key management details
- No specific operational procedures, callsigns, frequencies, or net schedules
- No FOUO/CUI material
