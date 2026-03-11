peoplePer1m2, partyArea = map(int,input().split())
peopleInArticle = list(map(int,input().split()))
print(*map(lambda x: x-peoplePer1m2*partyArea, peopleInArticle))