# Development Notes

Technical development documentation for the Phoenix Nest MARS Suite.

---

## AI-Assisted Development: A Practical Breakdown

This project was built with significant AI assistance. Here's an honest accounting of what that looked like in practice.

### Investment Summary

| Category | Tool | Duration/Usage | Cost |
|----------|------|----------------|------|
| Conversational AI | Claude Pro | ~2 months (Oct-Dec 2025) | ~$150 |
| Conversational AI and Agent Code Creation | GitHub Copilot | ~1 year of development | $400 |
| API Integration | Claude API | Testing/automation workflows | $50 |

### The Human-AI Division of Labor

This wasn't "AI wrote the code" — it was more like having a very fast junior developer who needs constant direction but never gets tired.

#### What AI Handled Well

- **Boilerplate and scaffolding** — Project structure, build scripts, repetitive patterns
- **Algorithm implementation** — Once I explained the DSP math, Claude could implement it quickly
- **Documentation** — First drafts, formatting, consistency
- **Code review** — Catching obvious bugs, suggesting optimizations
- **Test generation** — Creating test cases from specifications
- **Refactoring** — Cleaning up code structure without changing functionality

#### What Required Human Expertise

- **MIL-STD-188-110A knowledge** — AI models don't have this in their training data
- **Architecture decisions** — How components should interact, what abstractions make sense
- **RF domain expertise** — Understanding what signals should look like, debugging acquisition issues
- **Integration testing** — Verifying against real modems (MS-DMT, brain_core)
- **Performance tuning** — Knowing which optimizations actually matter for real-time DSP
- **Direction** — The AI doesn't know what to build next; that requires understanding the problem space

### Workflow Example

A typical development session looked like this:

1. **I identify a need:** "We need wideband AFC for the frequency acquisition"
2. **I explain the problem:** Describe the signal characteristics, constraints, what success looks like
3. **AI drafts implementation:** First pass at the algorithm
4. **I review and correct:** Fix domain-specific errors, adjust for real-world conditions
5. **Iterate:** Refine through conversation until it works
6. **I validate:** Test against actual signals, compare with reference implementations

The AI accelerated steps 3-5 dramatically. Steps 1, 2, and 6 are still entirely human.

### Honest Assessment

**Pros:**
- Development velocity increased ~3-5x for implementation work
- Documentation that I probably wouldn't have written otherwise
- Fewer "stupid" bugs caught early
- Ability to explore multiple approaches quickly

**Cons:**
- AI suggestions sometimes look right but aren't (domain knowledge gap)
- Debugging AI-generated code requires understanding what it was *trying* to do
- Some time spent explaining things to AI that a domain-expert human would already know
- Cost adds up for serious development work

### For Other Developers

If you're considering AI-assisted development for similar projects:

1. **Budget $50-100/month** for serious development work across tools
2. **Domain expertise is still essential** — AI can't replace what it doesn't know
3. **Plan for validation time** — AI code needs testing against reality
4. **Keep humans in the loop** — Architecture and design decisions shouldn't be delegated

The AI is a powerful tool, but it's still a tool. The developer's experience and domain knowledge determine whether the output is useful or just plausible-looking nonsense.

---

## Technical Architecture

*[Additional technical documentation for the modem implementation would go here]*

---

## Contributing

Contributions welcome. Please see individual repository CONTRIBUTING.md files for guidelines.

---

*Developer: Alex Pennington (KY4OLB)*  
*35 years programming experience*  
*15+ years MARS participation*
