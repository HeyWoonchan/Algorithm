def solution(n, lost, reserve):
    
    poss = n-len(lost)
    yes = [0]*(n+1)
    
    for i in reserve:
        yes[i]=1
        
    lostt = []
    for i in lost:
        if yes[i]==1:
            yes[i]=0
            poss+=1
        else:
            lostt.append(i)
    
    lostt.sort()
        
        
    for i in lostt:
        if i==1:
            if yes[2]==1:
                yes[2]=0
                poss+=1
        elif i==n:
            if yes[n-1]==1:
                yes[n-1]=0
                poss+=1
        else:
            for d in [-1,1]:
                nn = i+d
                if not (1<=nn<n+1):
                    continue
                if yes[nn]==1:
                    yes[nn]=0
                    poss+=1
                    break
                
                
    return poss