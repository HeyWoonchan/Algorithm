gradeDict = {"A+": 4.3, "A0": 4.0, "A-":3.7, "B+": 3.3, "B0": 3.0, "B-": 2.7, "C+": 2.3, \
             "C0": 2.0, "C-": 1.7, "D+": 1.3, "D0": 1.0, "D-": 0.7, "F": 0.0}

N = int(input())
sum = 0
hsum = 0
for i in range(N):
    _, h, g = input().split()
    h = int(h)
    hsum+=h
    sum+=h*gradeDict[g]
sum/=hsum
# print(sum)
if sum*100-int(sum*100)==0.5:
    sum+=0.001
print("%.2f"%sum) 