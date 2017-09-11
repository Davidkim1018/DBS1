import random

guess_number = random.randint(1,100)
print("숫자를 맞춰보세요 (1~100)")

user_input = int(input("숫자를 입력하세요 :"))
user_count = 1

while user_input != guess_number:
    if user_input > guess_number:
        print("더 낮습니다")
    if user_input < guess_number:
        print("더 높습니다")
    user_input = int(input("다시 입력해보세요 : "))
    user_count += 1

print("축하합니다. 정답은", guess_number, "입니다.")
print("정답을", user_count, "만에 맞추셨네요")
