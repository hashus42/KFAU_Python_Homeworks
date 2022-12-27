import re

total = 0
with open("./additions/regex_sum_1672279.txt") as f:
    for line in f:
        total += sum(map(int, re.findall("\d+", line)))
print(total)