# 프로그래밍1
# arr = [1,2,2,2,3,3]

# def solution1(arr):
#     arr123 = [0,0,0]
#     for i in arr:
#         if i == 1:
#             arr123[0] += 1
#         elif i == 2:
#             arr123[1] += 1
#         else:
#             arr123[2] += 1
#     amax = arr123[0]
#     for a in arr123:
#         if a > amax:
#             amax = a
#     arr123 = [amax-arr123[0],amax-arr123[1],amax-arr123[2]]
#     return arr123

# print(solution1(arr))


###############################################################

# i1 = ["r 10", "a 23", "t 124", "k 9"]	
# m1 = ["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45", "JUICE rra 55", "WATER a 20"]
# s1 = ["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"]
# # 1161

# i2 = ["x 25", "y 20", "z 1000"]	
# m2 = ["AAAA xyxy 15", "TTT yy 30", "BBBB xx 30"]	
# s2 = ["BBBB 3", "TTT 2"]	
# # -80

# def solution2(ings, menu, sell):
#     price = 0
#     bmenu = {}

#     for m in menu:
#         c = int(m.split()[2])
#         for i in ings:
#             a = int(m.split()[1].count(i.split()[0])*int(i.split()[1]))
#             c = c-a
#         bmenu[m.split()[0]] = c
#     print(bmenu)

#     for s in sell:
#         price += (bmenu[s.split()[0]])*int(s.split()[1])
    
#     print(price)
#     return price

# solution2(i1, m1, s1)


########################################################

# grid1 = ['1','234','56789']
# grid2 = ['a','man','drink','water11']

# def solution3(grid, clockwise):
#     if clockwise:
#         return clockwise1(grid)
#     else:
#         return clockwise1(clockwise1(grid))

# def clockwise1(grid):
#     leng = len(grid)
#     changed_arr = ['' for _ in range(leng)]
#     for i,g in enumerate(grid):
#         gridarr = list(g)
#         # print(gridarr)
#         for idx,char in enumerate(gridarr):
#             place = leng - 1 - i + ((idx+1)//2)
#             changed_arr[place] = char + changed_arr[place]
#             print(changed_arr)

#     return changed_arr



# print(solution3(grid1, True))
# print(solution3(grid2, False))



# b = grid1[0]+'a'

# b = ['' for _ in range(5)]
# b[3] = b[3]+'2'
# print(b)

# print(5//2)

#################################


# time1 = 3.5	
# list1 = [ ["홍콩", "11PM", "9AM"], ["엘에이", "3PM", "2PM"] ]

# def solution4(time, plans):
#     for place in plans:
#         ptime = 0
#         # 출발시각
#         dt = place[1]
#         if dt[-2:]=="PM":
#             dt = int(dt[:-2]) + 12
#         else:
#             dt = int(dt[:-2])
#         #돌아온시각
#         at = place[2]
#         if at[-2:]=="PM":
#             at = int(at[:-2]) + 12
#         else:
#             at = int(at[:-2])
#         # 금요일휴가시간
#         if dt<9.5:
#             ptime += 8.5
#         elif dt<18:
#             ptime += 18-dt    
#         # 월요일 휴가시간
#         if at>18:
#             ptime += 5
#         elif at>13:
#             ptime += at-13   
#         #시간비교
#         if time>=ptime:
#             result = place[0]
#     return result

# print(solution4(time1, list1))

#################################

test_case = [ ["홍콩", "11PM", "9AM"], ["엘에이", "3PM", "2PM"] ]
def solution(time, plans):
    friday_checkout_time = 18
    monday_checkin_time = 13
    travel_country = []
    for plan in plans:
        depart_time = int(plan[1][:-2])
        need_time_for_friday = (depart_time + (12 if plan[1].find("PM") > 0 else 0)) - friday_checkout_time
        arrive_time = int(plan[2][:-2])
        need_time_for_monday = monday_checkin_time - (arrive_time + (12 if plan[2].find("PM") > 0 else 0))
        if time + (need_time_for_friday + need_time_for_monday) >= 0:
            travel_country.append(plan[0])
    return travel_country
print(solution(3.5, test_case))




