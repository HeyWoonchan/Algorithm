
def check(recv):
    st = []
    for s in recv:
        # print(st)
        if s=='(' :
            st.append(s)
        if s==')':
            if not st or st[-1]!='(':
                return False
            st.pop()
    if st:
        return False
    return True
N = int(input())
for _ in range(N):
    a = input()
    result = check(a)
    if result:
        print('YES')
    else:
        print('NO')