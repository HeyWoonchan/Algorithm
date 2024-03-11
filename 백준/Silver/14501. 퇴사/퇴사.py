# 퇴사
N = int(input())

job_list = [list(map(int, input().split())) for _ in range(N)]

# 0일부터 시작한다고 가정
max_pay = 0


def sol(nowday, pay, lastday):
    global max_pay

    #print("지금 하는 일 - %d일 시작 일, %d 일 소요, 지금까지 수행한 pay = %d"%(nowday, job_list[nowday][0],pay))

    if nowday + job_list[nowday][0] <= lastday: # 현재 일이 마지막날까지 할수있는 일인지 확인
        #print("지금 하는 일은 마지막날 전에 끝낼 수 있음, 수행시작")
        pay += job_list[nowday][1]
    else:
        #print("지금 하는 일은 마지막날 전에 못끝냄 ----실행종료")
        return
    max_pay = max(max_pay, pay)
    next_day = nowday + job_list[nowday][0] #다음일을 시작할 수 있는 날짜 계산

    #print("일할 수 있는 다음 날짜 - %d"%(next_day))
    for k in range(lastday - next_day):  #다음일을 시작할 수 있는 날짜부터 끝날까지 작업 수행
        sol(next_day+k, pay, lastday)

result = 0
for i in range(N):
    max_pay=0
    sol(i,0,N)
    result = max(result, max_pay)
    #print("%d부터 시작한 결과는 %d,  이제 종료"%(i,max_pay))

print(result)