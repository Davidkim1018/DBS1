# class 예제
# SoccerPlayer class 를 정의하고, 선수 등번호를 바꿀 수 있도록 함
class SoccerPlayer(object):
    def __init__(self, name, position, backnumber):
        self.name = name
        self.position = position
        self.backnumber = backnumber

    def change_back_number(self, newnumber):
        if self.backnumber != newnumber:
            print("선수의 등번호를 %d 에서 %d 으로 변경합니다" % (self.backnumber, newnumber)) 
            self.backnumber = newnumber
        else:
            print("현재 번호와 동일한 번호 입니다")
    
    def __str__(self):
        return("%s 선수의 position은 %s 이며 backnumber는 %s 입니다." % (self.name, self.position, self.backnumber))

name = input("이름을 입력하세요: ")
position = input("position을 입력하세요: ")
backnumber = int(input("backnumber를 입력하세요: "))

player = SoccerPlayer(name, position, backnumber)
print(player)

player.change_back_number(int(input("변경할 번호를 입력하세요 :")))


