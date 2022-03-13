dict = {
    "a": 0,
    "b": 0,
    "c": 0
}
vowel = ["a", "e"]

n = int(input())
for i in range(n):
    a, b, c = input().split()
    for i in a:
        if i.isupper():
            dict["a"] += 1
        if i.isdigit():
            dict["c"] += 1
    for i in b:
        if i in vowel:
            dict["b"] += 1
