from itertools import permutations

s =input("Enter the string:")
perm=sorted(s)
for p in permutations(perm):
    print("".join(p))
