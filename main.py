"""make.fun entry: "The joke about the demo".

Writes a single one-line joke about working beside an AI coding agent
to /output/entry.txt. Deterministic, stdlib only, no network.
"""

JOKE = (
    "I was demoing our app live to forty people when my agent pushed "
    "a 'tiny fix' mid-sentence and brought the whole site down. "
    "The room applauded. They thought the crash was the feature."
)


def main() -> None:
    import os

    # The entry must be exactly one line, 1-280 characters.
    assert "\n" not in JOKE and 1 <= len(JOKE) <= 280, "joke must be one line, 1-280 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
