# Problem: A - a-e-i-o-u-y - https://codeforces.com/gym/522079/problem/A

length = int(input())
word = input()

vowel = "aeiouy"

stack = []

for letter in word:
    if letter in vowel and stack and stack[-1] in vowel:
        continue
    else:
        stack.append(letter)


print("".join(stack))
