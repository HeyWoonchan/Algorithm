def main():
    x, y, z, x2, y2, z2 = map(int,input().split())
    print(abs(x-x2)+abs(y-y2)+z+z2)

if __name__=="__main__":
    TC = int(input())
    for _ in range(TC):
        main() 
