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
    
    output = []
    for x in temp_list:
        if x not in output and (output.append(x)):
            output.append(x)
    temp_list = output
    
    result = []
    for i in range(0,len(temp_list)):
        j = i
        while i <= j and j < len(temp_list):
            result.append(temp_list[i] + temp_list[j])
            j += 1
    return(result)    






# main 함수
def main():
    result_sum = sum_of_list([1,2,3,4,5])
    print(result_sum)
    result_number = number_of_cases([1,2,3,4,5,5,5,4])
    print(result_number)

# main 함수 호출조건
if __name__ == "__main__":
    main()