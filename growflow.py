# -*- coding:utf-8 -*-

def sum_of_list(list_data):
    result = 0
    for i in range(0,len(list_data)):
        result = list_data[i] + result
    return result

def number_of_cases(list_data):
    if list_data == float or int:
        temp_list = ''.join(map(str, list_data))
        #temp_list = list(str(list_data)) <- 요걸로하면 아래에서 , 까지 넣어버림
    
    #내가 짠 방법
    # output = []
    # for x in temp_list:
    #     if x not in output and (output.append(x)):
    #         output.append(x)
    # temp_list = output
    
    #일반적인 고수들이 쓰는방법
    temp_list = list(sorted(set(temp_list)))

    result = []
    for i in range(0,len(temp_list)):
        j = i
        while i <= j and j < len(temp_list):
            result.append(temp_list[i] + temp_list[j])
            j += 1
    return(result)    

def binary_converter(decimal_number):
    main_value = decimal_number
    result = ''
    while main_value > 0:
        rest_value = main_value%2
        main_value = main_value//2
        result = str(rest_value) + result
    return(result)



# main 함수
def main():
    result_sum = sum_of_list([1,2,3,4,5])
    print(result_sum)
    result_number = number_of_cases([1,2,3,4,5,5,5,4])
    print(result_number)
    result_binary = binary_converter(1450)
    print(result_binary)

# main 함수 호출조건
if __name__ == "__main__":
    main()