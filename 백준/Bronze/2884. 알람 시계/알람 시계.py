hh,mm = map(int,input().split())
fromZero = (hh*60+mm-45)%(60*24)
print(fromZero//60, fromZero%60)