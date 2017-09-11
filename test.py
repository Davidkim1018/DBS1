import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

for i in range(1,10):
    print(i)

decimal = int(input("10진수를 입력하세요"))
result = ""
loop_counter = 0
while decimal > 0 :
    remainder = decimal % 2
    decimal = decimal // 2
    result = str(remainder) + result
    print("----------", loop_counter,"--------")
    print(remainder)
    print(decimal)
    print(result)
    loop_counter += 1
print(result)
