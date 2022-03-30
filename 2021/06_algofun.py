# # 15596
# def solve(a:list):
#     return sum(a)

##########################

# def sum_num(numbers):
#     total_num = 0
#     for num in numbers:
#         total_num += num
#     return total_num

# print(sum_num([1,2,3,4,5,6,3,2,4,5,2,43]))

# 4673

# g = list(range(1,10001))

# for a in range(10000):
#     b = (a//1000)%10
#     c = (a//100)%10
#     d = (a//10)%10
#     e = (a%10)
#     f = a+b+c+d+e

#     if f in g:
#         g.remove(f)

# for i in g:
#     print(i)

# ######################

# def d(n):
#     result = n
#     for i in range(4):
#         result += (n // 10 ** i) % 10
#     return result

# a = set(x for x in range(1, 10001))
# b = set(d(x) for x in range(1, 10001))

# for i in sorted(a-b):
#     print(i)


# 1065

a = int(input())
count = 0
for i in range(1,a+1):
    if i < 100:
        count += 1
    elif i < 1000:
        b = (i//100)%10
        c = (i//10)%10
        d = (i)%10
        if (b-c)==(c-d):
            count += 1
print(count)

##############################

input_num = int(input())
count = 0
for num in range(1, input_num+1):
    place_len = len(str(num))
    value_list = []
    diff = 0
    if place_len < 3:
        count += 1
    else:
        for place_value in range(place_len):
            value_list.append((num // 10 ** place_value) % 10)
        for n in range(place_len-1):
            if n == 0:
                diff = value_list[n] - value_list[n+1]
            else:
                if diff is not value_list[n] - value_list[n+1]:
                    break
        else:
            count += 1
print(count)


##################################

def one_number(number):
    cnt = 99
    if number < 100:
        return number
    elif number >= 100 and number <= 1000:
        for i in range(100, number+1):
            a = str(i)
            if int(a[0]) - int(a[1]) == int(a[1]) - int(a[2]):
                cnt += 1
    return cnt

#################################

num = int(input())

k = 0
for i in range(1, num+1):
    num_list = list(map(int, str(i)))
    if i < 100:
        k += 1 
    elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
        k += 1 
print(k)