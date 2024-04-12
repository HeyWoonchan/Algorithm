N,M = map(int,input().split())
marr = [list(map(int, input().split()))for _ in range(N)]


# 1번 테트로미노
one = [[1,1,1,1]]
one_90 = [[1],[1],[1],[1]]
one_list = [one, one_90]

# 2번 테트로미노
two_list = [[1,1],[1,1]]

# 3번 테트로미노
three = [[1,0],
         [1,0],
         [1,1]]
three_list = [three]
for i in range(3):
    three_list.append(list(map(list,zip(*three_list[i][::-1]))))

three1 = [[0,1],
          [0,1],
          [1,1]]
three1_list = [three1]
for i in range(3):
    three1_list.append(list(map(list,zip(*three1_list[i][::-1]))))
three_list = three_list+three1_list

# 4번 테트로미노
four = [[1,0],
        [1,1],
        [0,1]]
four_list = [four]
for i in range(3):
    four_list.append(list(map(list,zip(*four_list[i][::-1]))))
four1 = [[0,1],
          [1,1],
          [1,0]]
four1_list = [four1]
for i in range(3):
    four1_list.append(list(map(list,zip(*four1_list[i][::-1]))))
four_list = four_list+four1_list
# 5번 테트로미노
five = [[1,1,1],
        [0,1,0]]
five_list= [five]
for i in range(3):
    five_list.append(list(map(list,zip(*five_list[i][::-1]))))


# 맵 순회하며 최댓값 찾기
# for r in range(N):
#     for c in range(M):
def main():
    #1번 모양
    total_sum = 0
    for i in range(len(one_list)):
        row_len = N-len(one_list[i])+1
        col_len = M-len(one_list[i][0])+1
        for r in range(row_len):
            for c in range(col_len):
                sub_sum = 0
                for tr in range(len(one_list[i])):
                    for tc in range(len(one_list[i][0])):
                        sub_sum += marr[r+tr][c+tc]*one_list[i][tr][tc]
                total_sum = max(total_sum, sub_sum)

    # 2번 모양
    row_len = N-len(two_list)+1
    col_len = M-len(two_list[0])+1
    for r in range(row_len):
        for c in range(col_len):
            sub_sum = 0
            for tr in range(len(two_list)):
                for tc in range(len(two_list[0])):
                    sub_sum += marr[r+tr][c+tc]*two_list[tr][tc]
            total_sum = max(total_sum, sub_sum)


    # 3번 모양
    for i in range(len(three_list)):
        row_len = N-len(three_list[i])+1
        col_len = M-len(three_list[i][0])+1
        for r in range(row_len):
            for c in range(col_len):
                sub_sum = 0
                for tr in range(len(three_list[i])):
                    for tc in range(len(three_list[i][0])):
                        sub_sum += marr[r+tr][c+tc]*three_list[i][tr][tc]
                total_sum = max(total_sum, sub_sum)

    # 4번 모양
    for i in range(len(four_list)):
        row_len = N-len(four_list[i])+1
        col_len = M-len(four_list[i][0])+1
        for r in range(row_len):
            for c in range(col_len):
                sub_sum = 0
                for tr in range(len(four_list[i])):
                    for tc in range(len(four_list[i][0])):
                        sub_sum += marr[r+tr][c+tc]*four_list[i][tr][tc]
                total_sum = max(total_sum, sub_sum)

    # 5번 모양

    for i in range(len(five_list)):
        row_len = N-len(five_list[i])+1
        col_len = M-len(five_list[i][0])+1
        for r in range(row_len):
            for c in range(col_len):
                sub_sum = 0
                for tr in range(len(five_list[i])):
                    for tc in range(len(five_list[i][0])):
                        sub_sum += marr[r+tr][c+tc]*five_list[i][tr][tc]
                total_sum = max(total_sum, sub_sum)

    print(total_sum)

main()