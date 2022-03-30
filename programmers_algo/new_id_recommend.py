def solution(new_id):
    answer = ''
    return answer

new_id = '...!@BaT#*..y.abcdefghijklm'
# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
string01 = new_id.lower()
print(string01)

# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
def is_correct(char):
    if char.isdecimal() or char.islower() or char =='-' or char == '_' or char == '.':
        return True
    else:
        return False
string02 = ''.join( x for x in string01 if is_correct(x))
print(string02)

# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
string03 = string02.replace('..','.')
print(string03)

# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
if string03 == '':
    string04 = string03
else:
    if string03[0] == '.':
        string03 = string03[1:]
    if string03[-1] == '.':
        string04 = string03[:-2]
    else:
        string04 = string03

# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
if string04 == '':
    string05 = "a"
else:
    string05 = string04
print(string05)
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
if len(string05)>15:
    string06 = string05[:15]
    if string06[-1] =='.':
        string06 == string06[:14]
else:
    string06 = string05
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

while len(string06) < 3:
    string06 = string06 + string06[-1]

print(string06)




