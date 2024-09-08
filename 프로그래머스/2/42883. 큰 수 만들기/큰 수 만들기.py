def solution(number, k):
    st = []
    for i in number:
        while k>0 and len(st)>0 and i>st[-1]:
            st.pop()
            k-=1
        st.append(i)
    while k>0:
        st.pop()
        k-=1
    answer = ''.join(st)
    return answer