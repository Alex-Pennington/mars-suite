# Development Notes

Technical development documentation for the Phoenix Nest MARS Suite.

---

## AI-Assisted Development

This project uses AI-assisted coding tools. For cost tracking and breakdown, see the **Development Cost Tracking** section in [README.md](README.md).

### The Human-AI Division of Labor

This wasn't "AI wrote the code" — it was more like having a very fast junior developer who needs constant direction but never gets tired.

#### What AI Handles Well

- **Boilerplate and scaffolding** — Project structure, build scripts, repetitive patterns
- **Algorithm implementation** — Once I explain the DSP math, AI can implement it quickly
- **Documentation** — First drafts, formatting, consistency
- **Code review** — Catching obvious bugs, suggesting optimizations
- **Test generation** — Creating test cases from specifications
- **Refactoring** — Cleaning up code structure without changing functionality

#### What Requires Human Expertise

- **MIL-STD-188-110A knowledge** — AI models don't have this in their training data
- **Architecture decisions** — How components should interact, what abstractions make sense
- **RF domain expertise** — Understanding what signals should look like, debugging acquisition issues
- **Integration testing** — Verifying against real modems (MS-DMT, brain_core)
- **Performance tuning** — Knowing which optimizations actually matter for real-time DSP
- **Direction** — The AI doesn't know what to build next; that requires understanding the problem space

### Workflow Example

A typical development session:

1. **I identify a need:** "We need wideband AFC for frequency acquisition"
2. **I explain the problem:** Describe signal characteristics, constraints, success criteria
3. **AI drafts implementation:** First pass at the algorithm
4. **I review and correct:** Fix domain-specific errors, adjust for real-world conditions
5. **Iterate:** Refine through conversation until it works
6. **I validate:** Test against actual signals, compare with reference implementations

The AI accelerates steps 3-5 dramatically. Steps 1, 2, and 6 are still entirely human.

### For Other Developers

If you're considering AI-assisted development for similar projects:

1. **Budget $50-100/month** for serious development work across tools
2. **Domain expertise is still essential** — AI can't replace what it doesn't know
3. **Plan for validation time** — AI code needs testing against reality
4. **Keep humans in the loop** — Architecture and design decisions shouldn't be delegated

The AI is a powerful tool, but it's still a tool. The developer's experience and domain knowledge determine whether the output is useful or just plausible-looking nonsense.

---

## Technical Architecture

See individual repository documentation:

- [Modem Architecture](https://github.com/Alex-Pennington/pennington_m110a_demod/blob/master/README.md)
- [SDR Integration Design](https://github.com/Alex-Pennington/phoenix_sdr/blob/main/docs/IQ_INPUT_DESIGN.md)

---

## Contributing

Contributions welcome. Please see individual repository CONTRIBUTING.md files for guidelines.

---

*Developer: Alex Pennington (KY4OLB)*  
*35 years programming experience*  
*15+ years MARS participation*
