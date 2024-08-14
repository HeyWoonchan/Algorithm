def solution(number, k):
    st = []
    for num in number:
        while st and st[-1]<num:
            if k>0:
                st.pop()
                k-=1
            else:
                break
        st.append(num)
    if k>0:
        for i in range(k):
            st.pop()
        
    return ''.join(st)