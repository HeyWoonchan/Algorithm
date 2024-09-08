def is_alright(string):
    st = []
    for i in string:
        if i=='(':
            st.append(i)
        else:
            if st and st[-1]=='(':
                st.pop()
            else:
                return False
    
    if st:
        return False
    else:
        return True
    
def is_balanced(string):
    check = [0,0]
    for i in string:
        if i=='(':
            check[0]+=1
        else:
            check[1]+=1
    return check[0]==check[1]

def solution(p):
    
    if len(p)==0:
        return ''
    u = ''
    v = ''
    for i in range(len(p)+1):
        if is_balanced(p[:i]):
            u = ''.join(p[:i])
            v = ''.join(p[i:])
            if u!='':
                break
    if is_alright(u):
        a = solution(v)
        return u+a
    else:
        result = '(' + solution(v) + ')'
        tmp = list(u)
        for i in range(1,len(tmp)-1):
            if tmp[i]=='(':
                tmp[i]=')'
            else:
                tmp[i]='('
        result += ''.join(tmp[1:len(tmp)-1])
        return result
    

