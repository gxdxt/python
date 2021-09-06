import random

# 사용자는 최소 2명 이상
# input으로 사용자 이름을 정의한다.

Participant = ""
Participants = []
GameType = 1
Cylinder = []
while Participant != "end" :
    Participant = input('참가자의 이름을 입력해 주세요 : ')
    Participants.append(Participant)


# Game type에 대한 설명
print('Game type에 대한 설명.')
print('1번 게임 타입: 실린더를 최초 1회만 돌리는 경우(6 차례 내로 게임이 종료됩니다.)')
print('2번 게임 타입: 실린더를 매 차례마다 돌리는 경우(게임이 오랫동안 지속될 수 있습니다.)')
# 입력된 input의 length를 확인하여 게임에 참여하는 인원을 가늠한다.
GameType = input('원하시는 Game type을 입력해주세요. : (기본값 = 1)')
if GameType != 1 or GameType != 2 :
  print('잘못된 값을 입력하셨습니다. 다시 입력해 주세요.')
  gameType = input('원하시는 Game type을 입력해주세요. : (기본값 = 1)')

if GameType == 1 or GameType == '':
    for index in range(len(Participants)):
        print(Participants[index] + '의 차례입니다.')
        print('실린더를 한 번만 돌리게 됩니다.')
        spin = input('엔터를 누르면, 실린더를 돌립니다.')
        if spin == '\n' :
            # 랜덤으로 총알을 장전합니다.
            target = random.randint(0, 5)
            print('장전을 완료하였습니다.')
            # 실린더를 돌립니다.
            # 어떻게 돌릴지 고민!!!
            # 일단 처음에는 랜덤으로 숫자 선택
            reload = input('엔터를 누르면, 장전을 합니다.')
            if reload == '\n' :
            pick = random.randint(0, 5)
            if target == pick:
                print("BANG!")
                print(Participants[index] + '님이 사망하셨습니다.')
                break;
            else :
                print("puf,,")
                print(Participants[index] + '님은 생존하셨습니다.')
                continue;




if GameType == 2 :
    print('실린더를 매 차례에 돌리게 됩니다.')
    print('실린더를 돌립니다.')
    target = random.randint(0, 5)


# game type을 선택할 수 있는 부분
## 1.
## 2.

# 게임의 시작
# 6개의 탄창에 총알을 하나만 넣고 장전한다.
# 1 ~ 6의 탄창에 무작위로 총알이 들어간다.
# 실린더를 돌리는 action
# 일단 지금은 1 ~ 6을 몇초마다 돌리는 함수
# 첫 번째 사용자가 특정 action을 실시한다.
# 해당 숫자에 총알이 들어있으면, 해당 사용자가 당첨!

# 해당 숫자에 총알이 없으면, 다음 사용자의 차례로 넘어간다.


# 2명이 참여하는 경우
## 1. 실린더를 매 차례마다 돌리는 경우
## 2. 실린더를 돌리지 않고 방아쇠를 당기는 경우
## 2. 처음엔 무조건 돌린다.


# 3명 이상 참여하는 경우
## 1. 실린더를 매 차례마다 돌리는 경우
## 2. 실린더를 돌리지 않고 방아쇠를 당기는 경우

