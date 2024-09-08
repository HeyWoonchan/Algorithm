def solution(citations):
    ans = 0
    left = 0
    right = 100001
    while left<=right:
        h = (left+right)//2
        print("nowh:",h)
        over_h = 0
        under_h = 0
        for j in range(len(citations)):
            if citations[j]>=h:
                over_h+=1
            elif citations[j]<=h:
                under_h+=1
        print(h,"번 이상 인용된 논문:",over_h)
        if over_h>=h and over_h+under_h==len(citations):
            left=h+1
        elif over_h<h:
            right = h-1
        else:
            left = h+1
                
    return right