"""The Funniest Excuse for Skipping a Meeting -- make.fun one-liner entry.

The joke is a meeting about the meeting itself. "Double-booked" is the
most familiar excuse in office life, but the conflicting appointment is
not a dentist or a dentist-adjacent cliche -- it is a second meeting
whose only job is to decide whether this meeting should exist at all.
The punchline, "frankly that one sounds more useful", lands the real
insult: the meeting being skipped is so pointless that even a meeting
about its right to exist would be a better use of time. No setup is
needed beyond the word "double-booked", every office worker has sat
in the meeting that should have been an email, and the twist is fresh
-- the excuse is not a disaster or an errand, it is bureaucracy eating
itself.
"""

import os

# The entry: the funniest one-line excuse for skipping a pointless
# meeting. The classic "double-booked" excuse, except the clash is a
# meeting about whether this very meeting should exist -- and the
# punchline admits the meta-meeting sounds more useful than the one
# being skipped.
LINE = "Sorry, I'm double-booked: there's a meeting about whether this meeting should exist, and frankly that one sounds more useful."


def validate(text):
    """Check that a candidate entry line meets the competition rules.

    Raises ValueError unless ``text`` is a non-blank single-line ASCII
    string of 1 to 200 characters, with no leading or trailing space, no
    double spaces, and no control characters.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1 to 200 characters")
    if not text.isascii():
        raise ValueError("entry must be ASCII only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        raise ValueError("entry must not contain control characters")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing space")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="ascii") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
