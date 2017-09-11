def exam_mean(test1, test2, test3, test4):
    result = (float(test1) + float(test2) + float(test3))/float(test4)
    return(result)

def exam_sum(test1, test2, test3):
    result = (float(test1)+float(test2)+float(test3))
    return(result)

def exam_grade(test1):
    if test1 >= 90 :
        return("A")
    else:
        if test1 >= 80 :
            return("B")
        else:
            if test1 >= 70 :
                return("C")
            else:
                return("D")

user_input0 = input("과목수를 입력하세요 : ")
user_input1 = input("수학점수를 입력해주세요 : ")
user_input2 = input("과학점수를 입력해주세요 : ")
user_input3 = input("영어점수를 입력해주세요 : ")

print("수학점수는 : ", (user_input1), "입니다")
print("과학점수는 : ", (user_input2), "입니다")
print("영어점수는 : ", (user_input3), "입니다")

user_mean = exam_mean(user_input1, user_input2, user_input3, user_input0)
print("평균점수는 : ",round(user_mean,2), "입니다")

user_sum = exam_sum(user_input1, user_input2, user_input3)
print("총 점은 : ", (user_sum), "입니다")

user_grade = exam_grade(user_mean)
print("등급은 : ", user_grade, "입니다")
