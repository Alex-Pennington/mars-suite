# AI Coding Tools Primer

**A Practical Guide for HF/MARS Communications Developers**

*Version 1.0 – December 2025*

---

## About This Document

This document is intended to be read with the [OpenDyslexic font](https://opendyslexic.org/), a free typeface designed to help increase readability for readers with dyslexia. The font uses weighted bottoms on letters to help indicate direction and reduce letter confusion from flipping and swapping.

**To use OpenDyslexic:**
- **Browser:** Install the [OpenDyslexic Chrome extension](https://chromewebstore.google.com/detail/opendyslexic-for-chrome/cdnapgfjopgaggbmfgbiinmmbdcglnam) or [Firefox add-on](https://addons.mozilla.org/en-US/firefox/addon/opendyslexic-font-everywhere/)
- **System-wide:** Download from [opendyslexic.org](https://opendyslexic.org/) and install on Windows, macOS, Linux, iOS, or Android
- **GitHub:** Use a browser extension to override fonts on all sites

The font is completely free for personal, educational, and commercial use.

---

## Introduction

This primer is written for experienced developers who are new to AI-assisted coding tools. If you've been writing code for decades and haven't yet integrated AI tools into your workflow, this guide will help you get started without the marketing fluff.

AI coding assistants are not magic, and they're not going to replace your expertise. What they will do is dramatically speed up certain tasks, help you work through problems, and reduce the tedium of boilerplate code. Think of them as a knowledgeable junior developer who types very fast and never gets tired, but needs your guidance and review.

**A note on accessibility:** Modern AI tools include robust voice input capabilities. If typing has become difficult, voice input through these platforms provides an effective alternative for both conversation and code dictation.

---

## Section 1: Available Tools

### Claude (Anthropic)

Claude is a conversational AI that excels at understanding context and providing detailed explanations alongside code. Access it at [claude.ai](https://claude.ai) or through the API.

**Strengths:**
- Excellent at understanding complex requirements and multi-step problems
- Strong at explaining code and walking through logic
- Good at maintaining context across long conversations
- Handles multiple programming languages well
- Voice input available through web and mobile interfaces

**Best for:** Architecture discussions, debugging complex issues, learning new concepts, code review, writing documentation, and extended problem-solving sessions.

### GitHub Copilot

Copilot integrates directly into your IDE (VS Code, Visual Studio, JetBrains, etc.) and provides real-time code suggestions as you type.

**Strengths:**
- Inline suggestions while you code
- Understands your current file and project context
- Good at completing repetitive patterns
- Tab to accept, keep typing to refine

**Best for:** Day-to-day coding, boilerplate generation, API usage patterns, and test writing.

### Which to Use When

Use Claude when you need to think through a problem, understand unfamiliar code, or have a back-and-forth discussion about implementation approaches. Use Copilot when you're actively writing code and want autocomplete on steroids. Many developers use both: Claude for planning and problem-solving, Copilot for implementation.

---

## Section 2: Effective Prompting for DSP and Signal Processing

Getting good results from AI tools requires clear communication. The AI has broad knowledge but lacks the specific domain context you carry. Your job is to bridge that gap.

### The Golden Rule: Provide Context

AI tools work best when you tell them what you're trying to accomplish, not just what you want them to do. For specialized domains like HF communications, this context is critical.

**Bad Prompt:**
> "Write a function to do frequency correction."

**Good Prompt:**
> "I'm implementing a MIL-STD-188-110A HF modem. I need to do fine frequency correction on incoming 1800 baud PSK symbols after initial acquisition. The signal has already been through a coarse AFC loop. I'm working in Python with NumPy, processing at 8000 samples/sec. Can you help me implement a decision-directed PLL for the fine correction?"

### Key Elements to Include

- **The standard or specification** you're implementing (MIL-STD-188-110A, MIL-STD-188-141B, etc.)
- **Sample rates and symbol rates** involved
- **Modulation type** (PSK, QAM, FSK, OFDM)
- **Where in the signal chain** this code fits
- **Language and libraries** you're using
- **Real-world constraints** (real-time requirements, memory limits, etc.)

### Iterative Refinement

Don't expect perfect code on the first try. Plan to have a conversation:

1. Start with your requirements and get initial code
2. Test it against known signals or reference implementations
3. Come back with specific issues: "The loop bandwidth is too wide, it's tracking noise"
4. Refine until it works

### Example: Asking About Unknown Algorithms

When you encounter code or algorithms from other implementations (like analyzing reference modems), AI can help you understand them:

> "I'm looking at this frequency acquisition code from an existing modem implementation. It uses a multi-channel approach with several parallel correlators. Can you explain how this algorithm works and why it might be more robust than a simple FFT-based approach? Here's the relevant code section: [paste code]"

---

## Section 3: Limitations and Gotchas

AI tools have real limitations, especially in specialized domains. Understanding these will save you time and frustration.

### What AI Doesn't Know Well

- **MIL-STD specifications:** AI has limited exposure to MIL-STD-188-110A, 110B, 110C, 141B, and related standards. You'll need to provide specific details from the specs or feed in relevant sections.
- **Proprietary waveforms:** Government and military waveform specifics that aren't in public documentation.
- **MARS-specific procedures:** Operational procedures, net structures, and MARS-specific implementations.
- **Niche hardware interfaces:** Specific radio APIs, CAT control protocols for older equipment, etc.

### What AI Gets Wrong

- **Numeric precision:** AI can make subtle errors in DSP math, especially with phase calculations, normalization factors, and bit ordering. Always verify the math.
- **Endianness and bit packing:** Gets confused about MSB/LSB ordering, especially in protocol implementations.
- **Real-time constraints:** May suggest algorithms that are correct but too slow for real-time processing.
- **Hallucination:** May confidently state incorrect information about standards or invent API calls that don't exist.

### How to Work Around Limitations

- **Feed the specs:** Paste relevant sections of MIL-STD documents directly into your prompts. The AI will work with what you provide.
- **Test against known-good signals:** Always verify generated DSP code against reference signals or existing implementations.
- **Cross-reference implementations:** If you have working code from another project (like Brain Core or PC-ALE), use it as a reference point in your discussions.
- **Ask for explanations:** Request that the AI explain its reasoning. This helps you catch errors and understand the approach.

---

## Section 4: Code Review Workflow

The most effective pattern is: **AI assists, human verifies**. Your domain expertise is irreplaceable.

### Recommended Workflow

1. **Describe the problem** with full context (see Section 2)
2. **Get initial code** from the AI
3. **Review for correctness:** Does the algorithm match your understanding of the spec?
4. **Review for edge cases:** What happens at boundaries, with noise, with weak signals?
5. **Test with real data:** Run against known signals, compare with reference implementations
6. **Iterate:** Fix issues by discussing them with the AI, explaining what went wrong
7. **Document:** Have the AI help write comments and documentation explaining the final implementation

### What to Watch For

- Magic numbers without explanation
- Assumptions about data format that don't match your pipeline
- Off-by-one errors in indexing
- Phase wrapping issues
- Sample rate mismatches
- Complex/real conversion errors

### The Expert's Advantage

With 35+ years of experience, you know what correct looks like. You know how HF signals behave in practice. The AI doesn't have that intuition. Your job is to guide the AI with your expertise and verify its output against your knowledge. The AI types the code; you ensure it's right.

---

## Section 5: Security Considerations

When working on military-adjacent communications projects, security awareness is essential.

### What NOT to Share with AI Tools

- Classified information of any kind
- COMSEC material or key management details
- Specific operational procedures that aren't public
- Callsigns, frequencies, or net schedules for active operations
- Any FOUO (For Official Use Only) or CUI (Controlled Unclassified Information) material

### What IS Generally Safe

- Publicly available MIL-STD specifications
- General DSP algorithms and signal processing techniques
- Open-source code and implementations
- Amateur radio techniques and frequencies
- Generic programming questions

### Data Retention Awareness

AI services may retain conversation data for training or improvement. When in doubt, don't include it. For sensitive project work, consider using API access with appropriate data handling agreements rather than consumer web interfaces.

---

## Section 6: GitHub for Collaborative Development

If you've been coding for decades but haven't used Git or GitHub, this section provides the essentials for working on team projects like Phoenix Nest.

### Core Concepts

| Term | Definition |
|------|------------|
| **Repository (repo)** | A project folder tracked by Git. Contains all code, history, and branches. |
| **Clone** | Downloading a complete copy of a repository to your local machine. |
| **Commit** | A saved snapshot of your changes with a description of what you changed and why. |
| **Branch** | A parallel version of the code where you can work without affecting the main codebase. |
| **Pull Request (PR)** | A request to merge your changes into the main branch, allowing others to review first. |
| **Merge** | Combining changes from one branch into another. |

### Initial Setup (One Time)

1. Install Git from [git-scm.com](https://git-scm.com)
2. Create a GitHub account at [github.com](https://github.com)
3. Configure your identity:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```
4. Set up SSH keys (GitHub has guides for this) or use HTTPS with a personal access token

### Daily Workflow for Team Projects

**Starting work (get latest changes):**
```bash
git pull origin main
```

**Create a branch for your work:**
```bash
git checkout -b feature/my-new-feature
```

**After making changes, stage and commit:**
```bash
git add .
git commit -m "Add frequency correction algorithm"
```

**Push your branch to GitHub:**
```bash
git push origin feature/my-new-feature
```

**Create a Pull Request:** Go to GitHub, find your branch, click "New Pull Request"

### GitHub Releases

Releases are tagged versions of the software that users can download. They provide stable snapshots of the project at specific points.

**As a user/tester:** Go to the repository page, click "Releases" in the right sidebar, download the version you need.

**As a developer creating a release:**

1. Tag your commit: `git tag -a v1.0.0 -m "Version 1.0.0"`
2. Push the tag: `git push origin v1.0.0`
3. Go to GitHub → Releases → "Draft a new release"
4. Select your tag, write release notes describing changes
5. Attach any binary files (executables, archives) if needed
6. Publish the release

### Best Practices for Team Development

- **Pull before you start working** to get everyone's latest changes
- **Make small, focused commits** with clear messages
- **Use branches** for features and fixes, don't commit directly to main
- **Write meaningful commit messages** that explain WHY, not just what
- **Review each other's code** via Pull Requests before merging
- **Use Issues** to track bugs and feature requests

---

## Section 7: Practical Example from Phoenix Nest Development

This section provides a real-world example of how AI tools assisted in developing the Phoenix Nest MARS Suite.

### The Problem

Implementing wideband AFC (Automatic Frequency Control) for a MIL-STD-188-110A modem. The challenge: HF signals can be offset by hundreds of Hz due to ionospheric Doppler and oscillator drift. The modem needs to find and track the signal across a wide acquisition range.

### The Approach

1. **Research:** Used Claude to discuss different AFC approaches, comparing FFT-based acquisition vs. multi-channel correlators
2. **Reference analysis:** Fed in code snippets from existing implementations to understand their approach
3. **Implementation:** Iteratively developed the algorithm with AI assistance, testing each stage
4. **Verification:** Tested against known-good signals and reference modems
5. **Documentation:** AI helped write technical documentation explaining the algorithm

### What Worked

- AI was excellent at explaining DSP concepts and suggesting algorithm structures
- Providing MIL-STD specification details in the prompts dramatically improved results
- Iterative refinement based on test results was essential
- AI caught some issues that human review missed, and vice versa

### What Required Human Expertise

- Understanding how the algorithm fits into the overall modem architecture
- Tuning parameters for real-world HF channel conditions
- Verifying correctness against the actual MIL-STD requirements
- Making architectural decisions about trade-offs

---

## Conclusion

AI coding tools are a force multiplier, not a replacement for expertise. After 35 years of writing code, I've found these tools genuinely useful—not because they know more than I do about HF communications, but because they can quickly generate boilerplate, explain unfamiliar code, help debug issues, and serve as a tireless collaborator for working through problems.

**The key insights:**

- Your domain expertise is irreplaceable—use it to guide and verify
- Provide context generously—the AI doesn't know what you know
- Iterate and refine—expect conversation, not perfect first answers
- Test everything—AI makes mistakes, especially in specialized domains
- Use the right tool for the task—Claude for discussion, Copilot for inline coding

Welcome to the team. Now let's build something.

---

*Prepared for the MARS/HF Development Community*

*December 2025*
