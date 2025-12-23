import sys
input = sys.stdin.readline

n = int(input())
a = input().rstrip()
b = input().rstrip()

c = []
for i in a:
    if i=="0":
        c.append("1")
    else:
        c.append("0")

c = "".join(c)
if n%2==1:
    result = b==c
else:
    result = b==a

if result:

    print("Deletion succeeded")
else:
    print("Deletion failed")