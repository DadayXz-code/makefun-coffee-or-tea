"""One Letter: Coffee or Tea -- make.fun bounty entry.

Choice: "A" (coffee). Coffee is the canonical developer fuel: the
vivid, funny, true answer for the person who builds software on it.
Tea is a calm pause; coffee is the engine. The judge weighs vividness,
humour and truth -- coffee wins all three for a coder's morning, so
the single letter "A" stands on its own as the whole answer.

Writes exactly one letter, "A", and nothing else to /output/entry.txt.
"""

import os

LETTER = "A"  # coffee -- the developer's fuel, the truer choice

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LETTER)

if __name__ == "__main__":
    main()
