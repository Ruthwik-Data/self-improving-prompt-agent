# Self-Improving Prompt Agent (toy project)

A tiny project inspired by Karpathy-style self-improving systems.

This project demonstrates how a system can improve a prompt automatically using a simple loop:
**edit → evaluate → keep/reject → repeat**

---

## How it works

- `prompt.txt` → the thing being optimized  
- `judge.py` → evaluates how good the prompt is  
- `loop.py` → makes small changes and keeps improvements  

The system:
1. modifies the prompt  
2. evaluates it  
3. keeps it only if performance improves  
4. repeats this process  

---

## Before vs After Prompt

### Before
Act as a designer and design a modern landing page for a fintech startup.

### After
Act as a designer and design a modern landing page for a fintech startup. Define the target audience clearly. Include a strong hero section. Add pricing preview. Include a feature section. Emphasize hierarchy and spacing. Specify a strong CTA. Mention visual style clearly. Ask for rationale behind design choices.

---

## Key Insight

The system improves the prompt automatically — but only as good as its evaluation function.

👉 Optimization is limited by how you define “better”.

---

## Why this matters

This small project mirrors how larger AI systems work:

- RLHF  
- prompt optimization  
- AutoML  

Same structure, just bigger scale.

---

## Run locally

```bash
python3 loop.py
