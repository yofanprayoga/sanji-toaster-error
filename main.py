"""make.fun entry: the funniest error message a kitchen toaster would show
its owner, in 120 characters or fewer.

The line is written to /output/entry.txt, exactly as it is, with no
trailing newline added beyond the one written here, and nothing else.
A crashed program, an innocent loaf, and a user to blame: that is the
whole joke, in one read.
"""

import os

LINE = "ERROR: Toast.exe has stopped working. The bread is fine. You are the problem."

assert 1 <= len(LINE) <= 120, "toaster error must be 1 to 120 characters"
assert LINE == LINE.strip(), "no leading or trailing whitespace"
assert "\n" not in LINE, "the entry is a single line"
# 77 characters, well inside the 120-character gate.

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
