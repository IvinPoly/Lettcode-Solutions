from collections import Counter
def number(s):
  counter = Counter(s)
  print("".join(f"{counter[ch]}{ch}" for ch in counter))
s = input().strip()
number(s)
