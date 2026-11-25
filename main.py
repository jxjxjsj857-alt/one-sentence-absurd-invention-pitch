"""One-Sentence Absurd Invention Pitch.

Writes a single sentence (117 characters) pitching a ridiculous invention
that fixes a tiny everyday annoyance to /output/entry.txt.
"""

import os

PITCH = (
    "A toothpaste tube that rolls itself up from the bottom and slaps "
    "your hand every time you squeeze it from the middle."
)


def main() -> None:
    assert 1 <= len(PITCH) <= 220, "pitch must be 1-220 characters"
    assert PITCH.count(".") == 1, "pitch must be a single sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
