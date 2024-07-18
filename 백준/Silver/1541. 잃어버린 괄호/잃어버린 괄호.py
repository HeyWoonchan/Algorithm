input_str=input()

nums_arr = input_str.split('-')

final =[]
for i in range(len(nums_arr)):
    tmp = nums_arr[i].split('+')
    for j in range(len(tmp)):
        tmp[j]=int(tmp[j])
    final.append(sum(tmp))

result = final[0]
for i in range(1,len(final)):
    result-=final[i]
print(result)


