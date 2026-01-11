temps=list(map(float,input().split()))
avg=sum(temps)/10
stanDev=0
for t in temps:
    stanDev+=(t-avg)**2
stanDev/=9
stanDev=stanDev**(0.5)
if stanDev<=1.0:
    print("COMFY")
else:
    print("NOT COMFY")