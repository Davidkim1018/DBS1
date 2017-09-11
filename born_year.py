import datetime

# calc_year 함수 정의
def calc_year(year):
    now = datetime.datetime.now()
    now_year = int(now.strftime('%Y'))
    age = now_year - year + 1
    if age <= 26 and age >= 20:
        return("대학생")
    elif age < 20 and age >= 17:
        return("고등학생")
    elif age < 17 and age >= 14:
        return("중학생")
    elif age < 14 and age >= 8:
        return("초등학생")
    else:
        return("학생이 아닙니다")

#년도 입력받음
born_year = int(input("당신이 태어난 년도를 입력하세요 : "))

#계산
calculation = calc_year(born_year)

#출력함
print(calculation)
