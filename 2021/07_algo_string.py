# 11654
# print(ord(input()))





# 1157

# import string
# origin_string = input()
# upper_string = origin_string.upper()

# alpha_list = list(string.ascii_uppercase)
# cnt_list = list(map(lambda x:upper_string.count(x),alpha_list))
# print(alpha_list, cnt_list)

# max_cnt = max(cnt_list)
# max_char = cnt_list.index(max_cnt)

# if cnt_list.count(max_cnt)==1:
#     print(alpha_list[max_char])
# else:
#     print('?')

#############################

# a=input().upper()
# cnt=[]

# for i in a:
#     b = a.count(i)
#     cnt.append(b)

# print(set(a), cnt, set(cnt))

# if len(set(a)) != len(set(cnt)):
#     print('?')

# else:
#     idx = cnt.index(max(cnt))
#     print(a[idx])

#####################

# input_string = input().lower()
# count_char_list = [0 for _ in range(26)]
# for char in input_string:
#     count_char_list[ord(char) - ord('a')] += 1
# max_count = max(count_char_list)
# max_index_list = []
# for idx, count in enumerate(count_char_list):
#     if max_count == count:
#         max_index_list.append(idx)
# print("?" if len(max_index_list) > 1 else chr(max_index_list[0] + ord('a')).upper())

#################
# alpabet = input().lower()
# alpabet = 'Helle Werld'.lower()

# print(alpabet)
# a_list = list(alpabet)
# a_dic = {}

# for a in a_list:
#     if a in a_dic:
#         a_dic[a] += 1
#     else:
#         a_dic[a] = 1

# print(a_dic)

# a_dic = sorted(a_dic.items(),key=lambda x: x[1],reverse=True)

# print(a_dic)

###############

# words = input().upper()
# unique_words = list(set(words)) 
# print(unique_words)

# cnt_list = []
# for x in unique_words :
#     cnt = words.count(x)
#     cnt_list.append(cnt)  

# print(cnt_list)

# if cnt_list.count(max(cnt_list)) > 1 :  
#     print('?')
# else :
#     max_index = cnt_list.index(max(cnt_list)) 
#     print(unique_words[max_index])



# 1152
# split()
# split(" ") ?

# print(len(input().split()))



# 2941
# a = input()
# idx = 0
# cnt = 0 
# while idx < len(a):
#     if a[idx:idx+2]=='c=':
#         idx += 2
#         cnt += 1
#     elif a[idx:idx+2]=='c-':
#         idx += 2
#         cnt += 1
#     elif a[idx:idx+3]=='dz=':
#         idx += 3
#         cnt += 1
#     elif a[idx:idx+2]=='d-':
#         idx += 2
#         cnt += 1
#     elif a[idx:idx+2]=='lj':
#         idx += 2
#         cnt += 1
#     elif a[idx:idx+2]=='nj':
#         idx += 2
#         cnt += 1
#     elif a[idx:idx+2]=='s=':
#         idx += 2
#         cnt += 1
#     elif a[idx:idx+2]=='z=':
#         idx += 2
#         cnt += 1
#     else:
#         idx += 1
#         cnt += 1
# print(cnt)

########################################

croatia_words = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
input_word = input()

for word in croatia_words:
    input_word = input_word.replace(word, "!")

print(len(input_word))






