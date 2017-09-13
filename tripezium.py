#사다리꼴 넓이 구하기 함수
def addition(x,y):
    return x + y

def dividedby_2(x):
    return x/2

def main():
    base_line = float(input("밑변의 길이는?"))
    upper_edge = float(input("윗변의 길이는?"))
    height = float(input("높이는?"))
    
    area = dividedby_2(addition(base_line,upper_edge))*height
    print("넓이는",area)

#if name을 통해 해당 함수 명이 동일할 때에만 실행하도록 만듬
if __name__ == "__main__":
    main()

