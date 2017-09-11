#기본 세팅
kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 0]
eng_score = [49, 79, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]

#사람별 평균을 구해라 (내가 만든 식)
'''
student_result = [0,0,0,0,0]
for i in range(0,5):
    result_sum=0
    for j in range(0,3):
        result_sum = midterm_score[j][i] + result_sum
        print(result_sum)
        student_result[i] = result_sum/3
else:
    print(student_result)
    #student[i] = result_sum/3
'''
# 교수가 만든 식
i = 0
student_result = [0,0,0,0,0]
for subject in midterm_score:
    for score in subject:
        student_result[i] +=  score
        i += 1
    i = 0
else:
    a, b, c, d, e = student_result
    average_student = [a/3, b/3, c/3, d/3, e/3]
    print(average_student)