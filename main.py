"""One Letter: Coffee or Tea. A is coffee, B is tea."""
import os

# Coffee: the answer of anyone awake enough to send a letter at all.
LETTER = "A"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LETTER)
