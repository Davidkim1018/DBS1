def input_celsius():
    celsius = float(input("섭씨를 입력하세요 :"))
    return celsius

def convert_celsius(x):
    farenheit = (9/5 * x) + 32
    return farenheit

def main():
    cel = input_celsius()
    result = convert_celsius(cel)
    
    print("화씨온도는:",result,"입니다")

main()