def is_positive_number(variable):
    try:
        variable = int(variable)
        if isinstance(variable, int) == True and variable > 0:
            return(1)
        else:
            return(0)
    except ValueError:
        return(0)

def get_factorial_value(variable):
    result = 1
    while variable != 0:
        result = result * (variable)
        variable = variable - 1        
    return(result)
#mywork
#프로그램 시작

def main():
    print("이 프로그램은 factorial 계산기 입니다.")
    while 1:
        input_variable = input("계산할 숫자를 입력해 주세요 :")
        if input_variable == "0": break
        prove_num = is_positive_number(input_variable)
        if prove_num == 1:
            print("계산된 값은", get_factorial_value(int(input_variable)),"입니다")
        if prove_num == 0:
            print("값을 잘못 입력하였습니다, 다시 입력해주세요.")      
    print("이 프로그램을 이용해주셔서 감사합니다.")
        
if __name__ == "__main__":
    main()
