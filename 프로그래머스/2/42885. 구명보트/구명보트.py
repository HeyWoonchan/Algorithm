def solution(people, limit):
    people.sort()
    i = 0
    j = len(people)-1
    ans= 0
    while i<j:
        tmp = people[i]+people[j]
        if tmp>limit:
            j-=1
            ans+=1
        else:
            i+=1
            j-=1
            ans+=1
        if i==j:
            ans+=1
            break
        
    return ans