# Phoenix Nest MARS Communications Suite - Beta Operations Plan & Tester Requirements

Welcome to the Phoenix Nest MARS Communications Suite Beta Program. This document outlines the Standard Operating Procedures (SOPs) required for participation.

Our objective is to rapidly develop and stabilize reliable MIL-STD-188-110A HF modem communications software for MARS (Military Auxiliary Radio System) operations. To achieve this mission efficiently, we require strict adherence to the protocols outlined below. The ability to follow these protocols is a prerequisite for participation.

---

## 1. Participation Requirements & Scope

Participation in this phase requires technical self-sufficiency and strict adherence to the established workflow. This is a technical development environment, not a user support forum.

- **Mandatory Competence:** Testers are expected to navigate GitHub, locate documentation, follow instructions independently, and submit structured feedback.
- **Operational Scope:** This beta is for testing the SDR Controller GUI, SDR Server & Waterfall applications, and WWV timing detection capabilities as defined in the associated documentation.
- **No General Support:** The development team cannot provide individual training on basic GitHub usage or general IT support.

---

## 2. Accessing Software & Documentation (SOP)

The only valid source for working software and current documentation is the GitHub Releases tab.

| Artifact | Location (SOP) | Notes |
|----------|----------------|-------|
| Working Software | Releases Tab | Only download tagged releases (`v1.0.0`, `v1.1.0`, etc.). These are the stabilized builds. |
| Documentation | Releases Documentation | Documentation changes with every release; use the specific file bundled with your downloaded version. |
| Active Development | `feature/wwv-timing` branch | This is where things break, change, and get rebuilt constantly. Do not use this branch unless you are contributing source code. |

---

## 3. Feedback Protocol: Submitting Issues via GitHub

All formal communication regarding bugs, feature requests, or performance must occur within the GitHub Issue Tracker.

**Any feedback submitted via email, private forums, or chat messages will be disregarded.**

### 3.1. How to Report a Bug (SOP)

We require detailed, reproducible bug reports. Use the "Issues" tab and select the `[BUG REPORT]` template.

| Field | Required Content |
|-------|------------------|
| Steps to Reproduce | A numbered list of exact steps taken (1, 2, 3...) that cause the issue. |
| Actual Result | Exactly what happened (e.g., "The application crashed with error code 500"). |
| Expected Result | What should have happened (e.g., "A successful connection message appeared"). |
| Version Tested | The specific release tag you downloaded (e.g., `v1.0.2`). |
| Hardware Configuration | SDR device model, audio interface, and relevant system specs. |

### 3.2. Where to Submit

- **Phoenix Nest MARS Suite Issues:** [github.com/PhoenixNestLLC/mars-suite/issues]
- **SDR Server & Waterfall Issues:** [github.com/PhoenixNestLLC/mars-suite/issues] (use `[WATERFALL]` or `[SDR-SERVER]` label)
- **WWV Timing Module Issues:** [github.com/PhoenixNestLLC/mars-suite/issues] (use `[WWV-TIMING]` label)

---

## 4. Development Branch Reference

| Branch | Purpose |
|--------|---------|
| `main` | Stable releases only |
| `develop` | Integration branch for upcoming release |
| `feature/wwv-timing` | WWV 5ms pulse detection & timing discipline development |
| `feature/constellation` | Constellation diagram and signal analysis tools |

---

## 5. Related Projects & Acknowledgments

This suite builds upon foundational work from:

- **Steve Hajducek (N2CKH)** - MS-DMT, MARS-ALE
- **Charles Brain (G4GUO)** - brain_core modem, PC-ALE, PC-HFDL

---

*Phoenix Nest LLC - KY4OLB*
