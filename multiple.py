#구구단 함수 정의
def multiple(count):
    a=1
    if count > 0 and count < 10:
        while a < 10:
            calc = count * a
            print(count," X ",a," = ", calc)
            a += 1
        else:
            print("계산이 완료되었습니다")
    else:
        print("잘못된 값을 입력하였습니다")

def second_multiple(count):
    a=1
    if count > 0 and count <10:
        for i in range(1,9):
            print(str(count),"X",str(i),"=",str(count*i))
        print("계산이 완료되었습니다"")
    else:
        print("잘못된 값을 입력하였습니다")


# 1. 구구단 값을 입력한다.
# 2. 구구단 값이 0 이면 구구단을 종료한다.
# 3. 구구단 값이 0이 아니면 식을 진행한다.
# 4. 구구단 값이 0< & 10> 가 아니면 값이 틀렸다고 반환한다.
# 5. 구구단 계산이 완료되면 다시 입력하라는 메시지를 띄운다

multi_count = 1
while multi_count != 0:
    multi_count = int(input("몇단을 입력할까요? :"))
    if multi_count ==0 : break
    print("구구단 ",multi_count ,"단을 ","계산합니다.")
    multi_start = multiple(multi_count)
print("구구단 게임을 종료합니다")
