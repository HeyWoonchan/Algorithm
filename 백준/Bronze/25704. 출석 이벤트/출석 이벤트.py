attendStamp = int(input())
price = int(input())

target = [20,15,10,5]
sale = ['*75//100','-2000','*90//100','-500']

result = price
for i in range(4):
    if target[i]>attendStamp:
        continue
    tmp = price
    tmp = eval(str(tmp)+sale[i])
    result = min(result,tmp)
if result<0:
    result=0
    
print(result)