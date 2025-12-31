import sys
input = sys.stdin.readline
N = int(input())
st = []
def isEmpty():
    if len(st)>0:
        return False
    return True

for _ in range(N):
    a = input().rstrip()
    if a.split(maxsplit=1)[0]=='push':
        st.append(int(a.split()[-1]))
    elif a=='top':
        if isEmpty():
            print(-1)
        else:
            print(st[-1])
    elif a=='size':
        print(len(st))
    elif a=='empty':
        if len(st)==0:
            print(1)
        else:
            print(0)
    elif a=='pop':
        if isEmpty():
            print(-1)
        else:
            print(st.pop())