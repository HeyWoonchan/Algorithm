import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = sys.stdin.readline()

Pn =''.join(['I' if i % 2 == 0 else 'O' for i in range((2*N)+1)])

#kmp
#make table

#https://velog.io/@rhdmstj17/KMP-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-python-%EB%AC%B8%EC%9E%90%EC%97%B4-%ED%83%90%EC%83%89-%EA%B0%80%EC%9E%A5-%EC%89%BD%EA%B2%8C-%EC%9D%B4%ED%95%B4%ED%95%B4%EB%B3%B4%EA%B8%B0
#참조

def KMP_table(pattern):
    lp = len(pattern)
    tb = [0 for _ in range(lp)]

    pidx = 0
    for idx in range(1,lp):
        while pidx > 0 and pattern[pidx] != pattern[idx]:
            pidx = tb[pidx-1]

        if pattern[idx] == pattern[pidx]:
            pidx +=1
            tb[idx]=pidx

    return tb

def KMP(word, pattern):
    table = KMP_table(pattern)

    results = []

    pidx=0

    for idx in range(len(word)):
        while pidx >0 and word[idx] != pattern[pidx]:
            pidx = table[pidx-1]
        if word[idx]==pattern[pidx]:
            if pidx == len(pattern)-1:
                results.append(idx-len(pattern)+2)
                pidx = table[pidx]
            else:
                pidx+=1
    return results

result = KMP(S, Pn)
print(len(result))