import re

text = ("On 14 March 2026, Dr. Smith sent 3 reports to the NLP Lab. "
        "The meeting started at 10:30 and ended at 12:15. "
        "For information, write to nlp-lab@example.org.")


months = (r"(?:January|February|March|April|May|June|July|August|"
          r"September|October|November|December)")

patterns = {
    "dates":    rf"\b\d{{1,2}}\s+{months}\s+\d{{4}}\b",
    "times":    r"\b(?:[01]?\d|2[0-3]):[0-5]\d\b",
    "integers": r"\b\d+\b",
    "email":    r"\b[\w.+-]+@[\w-]+(?:\.[\w-]+)+\b",
}

for name, pat in patterns.items():
    matches = re.findall(pat, text)
    print(f"{name}: {matches}")
    print(f"  count: = {len(matches)}")