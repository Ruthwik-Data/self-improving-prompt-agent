import random
from pathlib import Path
from judge import score_prompt

PROMPT_FILE = Path("prompt.txt")

MUTATIONS = [
    " Define the target audience clearly.",
    " Include a strong hero section.",
    " Add trust indicators such as testimonials or logos.",
    " Include a feature section.",
    " Add pricing preview.",
    " Specify a strong CTA.",
    " Mention visual style clearly.",
    " Emphasize hierarchy and spacing.",
    " Ask for rationale behind design choices.",
    " Request structured output in sections."
]

def mutate(prompt: str) -> tuple[str, str]:
    addition = random.choice(MUTATIONS)
    return prompt + addition, addition.strip()

def main(rounds=10):
    current = PROMPT_FILE.read_text().strip()
    best_score = score_prompt(current)

    print(f"Start score: {best_score:.2f}")

    with open("results.log", "w") as log:
        for i in range(rounds):
            candidate, summary = mutate(current)
            candidate_score = score_prompt(candidate)

            if candidate_score > best_score:
                current = candidate
                best_score = candidate_score
                PROMPT_FILE.write_text(current)
                decision = "KEEP"
            else:
                decision = "REJECT"

            line = f"Round {i+1} | mutation={summary} | score={candidate_score:.2f} | best={best_score:.2f} | {decision}"
            print(line)
            log.write(line + "\n")

    print("\nFinal score:", best_score)
    print("\nFinal prompt:\n")
    print(current)

if __name__ == "__main__":
    main()