import sys
input = sys.stdin.readline
K = int(input())
st = []
for _ in range(K):
    a = int(input())
    if a==0:
        st.pop()
    else:
        st.append(a)
print(sum(st))