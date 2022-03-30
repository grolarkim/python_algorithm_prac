# log01 = ["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"]
# a = "02:20"
# log02 = ["01:00", "08:00", "15:00", "15:04", "23:00", "23:59"]
# b = "02:44"

# def soulution05(log):
#     idx = 0
#     cnt = 0
#     while idx < len(log):
#         # 공부의 시작 시간, 끝 시간
#         start_time = int(log[idx][:2])*60 + int(log[idx][-2:])
#         end_time = int(log[idx+1][:2])*60 + int(log[idx+1][-2:])
#         # 조건문
#         if end_time - start_time > 105:
#             cnt += 105
#         elif end_time - start_time >= 5:
#             cnt = cnt + (end_time - start_time)
#         idx += 2
#     # 비어있으면 0붙이도록 zfill사용
#     result = "{}:{}".format(str(cnt//60).zfill(2), str(cnt%60).zfill(2))
#     return result

# print(soulution05(log01))
# print(soulution05(log02))

#################################

# import datetime

# time_com = ["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"]

# def test_time(s):
#     return datetime.datetime.strptime(s, "%H:%M")

# no_t = test_time("00:00")
# no_save_time = test_time("00:05") - no_t
# over_save_time = test_time("01:45") - no_t
# result_time = no_t

# for t in range(len(time_com)):
#     if t % 2 == 0 or t == 0:
#         start_time = test_time(time_com[t])
#         end_time = test_time(time_com[t + 1])
#         # print(dateval1, dateval2, t)
#         add_time = end_time - start_time

#         # print(add_time.seconds)
#         # print(no_save_time.seconds)
#         # print(no_t)
#         if add_time.seconds >= no_save_time.seconds:
#             if add_time.seconds <= over_save_time.seconds:
#                 result_time = result_time + add_time
#             else:
#                 result_time = result_time + over_save_time

# print(result_time.strftime('%H:%M'))



# str01 = 'aaabbaaa'
# str02 = 'wowwow'

# def solution6(s):
#     # 첫번째 글자를 세고 시작해서 리스트에 1있음
#     cnt_arr = [1]
#     arr_idx = 0
#     idx = 0
#     # 반복문을 통해 카운트리스트에 숫자 세기
#     while idx + 1 < len(s):
#         # 조건문으로 앞뒤 문자가 다르다면 리스트를 늘리고 늘어난 곳으로 리스트인덱스 이동
#         if s[idx] != s[idx+1]:
#             cnt_arr.append(0)
#             arr_idx += 1
#         cnt_arr[arr_idx] += 1
#         idx += 1
#     # 만약 시작과 끝이 같다면 마지막의 값을 뺴서 첫번째에 더함
#     if s[0] == s[-1]:
#         cnt_arr[0] += cnt_arr.pop()
#     # 정렬
#     cnt_arr.sort()
#     return cnt_arr

# print(solution6(str01))
# print(solution6(str02))


##########################


# s='wowwow'
# a=list(s)
# a_reverse = list(reversed(s))
# # print(a)
# # print(a_reverse)
# for i in range(len(a)):
#     if a[0] == a_reverse[0]:
#         del a_reverse[0]
#         a_reverse.append(a[0])
# a_reverse = list(reversed(a_reverse))
# print(a_reverse)

# cnt = 0
# for j in range(len(a_reverse)-1):
#     if a_reverse[j] != a_reverse[j+1]:
#         cnt +=1
#         print(j)

# list_cnt =[0]*(cnt+1)


# print(list_cnt)


desc = '지그재그로 이동하면서 1씩 증가'

def solution7(rows, columns):
    # 0으로 이루어진 행렬 만듦
    result = []
    for i in range(rows):
        result.append([0]*columns)

    odd_even = 0
    cur_r = 0
    cur_c = 0
    cur_cnt = 0


    while True:
        # 탈출조건 1 행열에 0이 없으면 종료
        exit_arr = []
        for i in range(rows):
            if 0 not in result[i]:
                exit_arr.append(0)
        if len(exit_arr)==rows:
            break
        # 탈출조건 2 무한히 순환하면 종료
        if cur_r == 0 and cur_c == 0 and odd_even == 0 and cur_cnt != 0:
            break
        # 현재 위치에 숫자 입력
        cur_cnt += 1
        result[cur_r][cur_c] = cur_cnt
        # 홀짝이냐에 따라 이동방향 변환
        if odd_even==0:
            if cur_c < columns-1:
                cur_c += 1
            else:
                cur_c = 0
            odd_even = 1
        else:
            if cur_r < rows-1:
                cur_r += 1
            else:
                cur_r = 0
            odd_even = 0

    return result

print(solution7(3,4))
print(solution7(3,3))
print(solution7(2,4))



