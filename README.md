# Phoenix Nest MARS Communications Suite

Open-source HF digital communications tools for Military Auxiliary Radio System (MARS) operations.

**Developer:** Alex Pennington (KY4OLB, formerly AAR4TE / NNN0VO)  
**Project Site:** [www.organicengineer.com/projects](https://www.organicengineer.com/projects)  
**Contact:** projects@organicengineer.com

---

## Repositories

| Repository | Description | Status |
|------------|-------------|--------|
| [**pennington_m110a_demod**](https://github.com/Alex-Pennington/pennington_m110a_demod) | MIL-STD-188-110A HF modem - all 11 modes, turbo EQ, MS-DMT compatible | ✅ v1.2.0 |
| [**phoenix_nest_mars**](https://github.com/Alex-Pennington/phoenix_nest_mars) | MARS ops suite: CP, Station Mapper, Crypto, Propagation | ✅ Building |
| [**brain_core**](https://github.com/Alex-Pennington/brain_core) | Paul Brain modem core (reference implementation for testing) | ✅ v1.0.0 |
| [**MARS_GIS**](https://github.com/Alex-Pennington/MARS_GIS) | QGIS project for FEMA region map generation | ✅ Working |
| [**phoenix_sdr**](https://github.com/Alex-Pennington/phoenix_sdr) | SDRplay RSP2 Pro integration - I/Q capture for modem testing | ✅ v0.1.0 |
---

## How It Fits Together

```
┌────────────────────────────────────────────────────────────────┐
│  OPERATOR                                                       │
│      │                                                          │
│      ▼                                                          │
│  Station Mapper ◄─────────────────────────── MARS_GIS          │
│  (phoenix_nest_mars/src/smlinux)              (map images)      │
│      │                                                          │
│      │ V3PROTOCOL (XML/TCP)                                     │
│      ▼                                                          │
│  Communications Processor (CP)                                  │
│  (phoenix_nest_mars/src/cp)                                     │
│      │                                                          │
│      │ MS-DMT Protocol (TCP 4998/4999)                         │
│      ▼                                                          │
│  ┌─────────────────────┐     ┌─────────────────────┐           │
│  │ pennington_m110a    │ OR  │ brain_core          │           │
│  │ (Phoenix Nest)      │     │ (Paul Brain)        │           │
│  │ TCP 4998/4999/5000  │     │ TCP 3998/3999       │           │
│  └──────────┬──────────┘     └──────────┬──────────┘           │
│             │                           │                       │
│             └───────────┬───────────────┘                       │
│                         ▼                                       │
│                    AUDIO / RADIO                                │
└────────────────────────────────────────────────────────────────┘
```

**Runtime Flow:**
1. Start modem server (`pennington_m110a` or `brain_core`)
2. Start CP - connects to modem via MS-DMT protocol
3. Start Station Mapper - connects to CP via V3PROTOCOL
4. Operator uses Station Mapper for NCS operations

**The modems are interchangeable** - both implement MS-DMT protocol so CP doesn't care which is running.

---

## Quick Start

### Option A: Phoenix Nest Modem (recommended)
```bash
git clone https://github.com/Alex-Pennington/pennington_m110a_demod
cd pennington_m110a_demod
.\build.ps1 -Target all
.\server\m110a_server.exe
```

### Option B: Paul Brain Modem (reference)
```bash
git clone https://github.com/Alex-Pennington/brain_core
cd brain_core
.\build.ps1
.\brain_modem_server.exe
```

### Start MARS Operations Suite
```bash
git clone https://github.com/Alex-Pennington/phoenix_nest_mars
cd phoenix_nest_mars/src/cp
qmake CP-standalone.pro && make
./CP

# In another terminal:
cd ../smlinux
qmake StationMapper-linux.pro && make
./StationMapper
```

---

## Component Details

### pennington_m110a_demod
Full MIL-STD-188-110A implementation:
- All 11 data modes (75-4800 bps)
- 7 equalizer options including Turbo EQ
- Web-based test GUI
- MS-DMT compatible TCP server
- GPL-3.0 license

### phoenix_nest_mars
Integrated MARS operations:
- **CP** - Message formatting, traffic routing
- **Station Mapper** - NCS visualization, roster management  
- **Crypto** - KIK/TEK key tape management
- **Propagation** - VOACAP coverage prediction

### brain_core
Paul Brain's original m188110a modem:
- Wrapped as headless TCP server
- Used for comparison/interop testing
- Reference implementation

### MARS_GIS
QGIS project for map generation:
- FEMA region boundaries
- Station coverage areas
- Export images for Station Mapper

---

## Standards & Protocols

| Standard | Description |
|----------|-------------|
| MIL-STD-188-110A | HF data modem (75-4800 bps) |
| MIL-STD-188-110B/C | Updated modem specs |
| STANAG 4539 | NATO equivalent |
| MS-DMT | MARS Digital Modem Terminal protocol |
| V3PROTOCOL | Station Mapper ↔ CP communication |

---

## Support Development

- **GitHub Sponsors:** [github.com/sponsors/Alex-Pennington](https://github.com/sponsors/Alex-Pennington)
- **ARDC Grant:** Application in progress

---

## License

Each repository has its own license - see individual repos for details.

---

*Phoenix Nest LLC — Supporting MARS operations through open-source development*
