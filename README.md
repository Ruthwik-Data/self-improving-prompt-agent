# Self-Improving Prompt Agent

A prompt optimization loop that automatically improves prompts through iterative mutation and evaluation — the same structure used in RLHF, AutoML, and production LLM fine-tuning pipelines, implemented in ~100 lines of Python.

## Problem & Why

Prompt engineering is manual and intuition-driven. Most teams iterate by hand with no systematic way to know if a change actually improved output quality. This project asks: what if the system could evaluate its own prompt and keep only improvements?

## What This Is

A minimal `edit → evaluate → keep/reject → repeat` loop that optimizes a prompt against a scoring function, with full run history logged.

## Architecture

```
prompt.txt  →  loop.py (mutate)  →  judge.py (score)  →  keep if score > best
    ↑                                                           |
    └─────────────────────── iterate ←──────────────────────────────────────────────────────────┘
```

- `prompt.txt` — the artifact being optimized
- `loop.py` — generates candidate mutations (add constraint, clarify audience, specify tone, etc.)
- `judge.py` — scoring function; returns 0.0–1.0
- `results.log` — complete run history with mutation, score, and KEEP/REJECT decision

## Evaluation & Results

10 optimization rounds on a fintech landing page prompt:

| Round | Mutation | Score | Decision |
|-------|----------|-------|----------|
| 1 | Ask for rationale behind design choices | 0.10 | KEEP |
| 2 | Add pricing preview | 0.20 | KEEP |
| 3 | Add pricing preview (duplicate) | 0.20 | REJECT |
| 4 | Include a feature section | 0.30 | KEEP |
| 5 | Ask for rationale (duplicate) | 0.30 | REJECT |
| 6 | Emphasize hierarchy and spacing | 0.50 | KEEP |
| 7 | Define the target audience clearly | 0.60 | KEEP |
| 8 | Include a feature section (duplicate) | 0.60 | REJECT |
| 9 | Specify a strong CTA | 0.70 | KEEP |
| 10 | Mention visual style clearly | **0.80** | KEEP |

**Score: 0.10 → 0.80 across 10 rounds. 3 mutations rejected (no regression).**

**Before:** `"Act as a designer and design a modern landing page for a fintech startup."`

**After:** Same base + target audience definition, hero section, pricing preview, feature section, hierarchy/spacing, strong CTA, visual style, rationale requirement.

## How to Use

```bash
git clone https://github.com/Ruthwik-Data/self-improving-prompt-agent
cd self-improving-prompt-agent
python3 loop.py
# Results written to results.log
```

## Lessons Learned

1. **Optimization is bounded by your evaluation function.** The system gets as good as `judge.py` allows — not better. This is the fundamental constraint in RLHF, AutoML, and every DSPy-style optimizer. Getting the eval right matters more than the loop.
2. **Rejection is signal, not failure.** 3 of 10 mutations were rejected. That's the system working — duplicate mutations don't compound, and the loop maintains the best known state without regression.
3. **The loop structure scales.** Replace `judge.py` with DeepEval metrics and `loop.py` mutations with an LLM, and this becomes DSPy. The architecture is the insight, not the implementation.

## Known Limitations

- Scoring function is heuristic, not grounded in user preference or task performance
- Mutation strategy is rule-based; LLM-generated mutations would explore the space better
- 10 rounds is illustrative, not statistically significant
- No baseline comparison against human-optimized prompts
