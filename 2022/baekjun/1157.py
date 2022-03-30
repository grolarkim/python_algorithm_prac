import string
origin_string = input()
upper_string = origin_string.upper()
# print(upper_string)
alpha_list = list(string.ascii_uppercase)
cnt_list = list(map(lambda x:upper_string.count(x),alpha_list))
# print(cnt_list)
max_cnt = max(cnt_list)
max_char = cnt_list.index(max_cnt)
if cnt_list.count(max_cnt)==1:
    print(alpha_list[max_char])
else:
    print('?')