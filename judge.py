def score_prompt(prompt: str, data_path=None) -> float:
    prompt_l = prompt.lower()

    criteria = [
        "target audience",
        "hero",
        "cta",
        "visual style",
        "hierarchy",
        "spacing",
        "trust",
        "feature",
        "pricing",
        "rationale",
    ]

    score = 0
    for c in criteria:
        if c in prompt_l:
            score += 1

    return score / len(criteria)


if __name__ == "__main__":
    with open("prompt.txt", "r") as f:
        prompt = f.read()
    print("Score:", score_prompt(prompt))