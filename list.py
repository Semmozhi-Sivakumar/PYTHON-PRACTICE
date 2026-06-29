word = input("Enter a word: ")

rev = ""

for ch in word:
    rev = ch + rev

print(rev)