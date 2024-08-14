def solution(people, limit):

    
    people.sort()
    answer = 0
    i,j = 0, len(people)-1
    while i<j:
        if people[i] + people[j] <= limit:
            i+=1
        j-=1
        answer+=1
    
        
    return answer+1 if i==j else answer