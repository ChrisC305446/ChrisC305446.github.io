import sys

words = []

for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    words.append(line)

words.sort()
print(words)
