def solution(s):
    answer = True
    st = []
    for i in range(len(s)):
        if s[i]=='(':
            st.append(s[i])
        elif s[i]==')':
            if st and st[-1]=='(':
                st.pop()
            else:
                return False
    if st:
        return False
    return True