#11_1
user_input = input("임의의 숫자 5개를 입력하세요:")
number_list = list(map(int, user_input.split()))
print("입력받은 숫자 리스트:", number_list)

#11_2
user_input = input("임의의 숫자 5개를 입력하세요:")
number_list = list(map(int, user_input.split()))
char = input("리스트에 추가 할 문자 1개를 입력하세요:")
number_list.append(char)
print("업데이트 된 리스트:", number_list)

#12
user_input = =input("임의의 숫자 5개를 입력하세요:")
number_list = list(map(int, user_input.split()))
del number_list[-2:]
print("마지막 두 개 값을 삭제:", number_list)

#13
user_input = =input("임의의 숫자 5개를 입력하세요:")
number_list = list(map(int, user_input.split()))
for index, value in enumerate(number_list, start=101):
    print(f"{index}:{value}")

#14
a = [10, 20, 30, 40, 30, 20, 10]
count_20 = a.count(20)
print("숫자 20은 몇개인가요:", count_20)

#15
user_input = input("임의의 숫자 10개를 입력하세요:")
number_list = list(map(int, user_input.split()))
min_value = min(number_list)
max_value = max(number_list)
print("최저값:", min_value)
print("최고값:", max_value)

#16
user_input = input("임의의 숫자 10개를 입력하세요:")
number_list = list(map(int, user_input.split()))
min_value = min(number_list)
max_value = max(number_list)
number_list.remove(min_value)
number_list.remove(max_value)
total = sum(number_list)
print("최저값과 최고값을 제외한 나머지 값들의 합:", total)

#17
a = [10, 20, 30, 40, 30, 20, 10]
a = [x for x in a if x != 20]
print("20을 모두 제거한 리스트:")

#18
number = [x for x in range(1, 6)]
print(number)

#19
num = [x for x in range(1, 21) if x % 2 ==1]
print(num)

#20
start, end = map(int, input("정수 2개를 입력하세요:").split())
two = [2 ** i for i in range (start, end + 1)]
del two[1]
del two[-2]
print(two)

#21
text = input()
modified_text = text.replace("Hello","Hi")
print(modified_text)

#22
chars = input("문자 4개를 연속해서 입력하세요:")
if len(char) != 4:
    print("문자를 정확히 4개 입력해주세요.:")
else:
    result = '/'.join(chars)
    print(result)

#23
name = input("성을 영어로 입력해주세요:")
name_lower = name.lower()
print(name_lower.rjust(10))