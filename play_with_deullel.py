import random


# 플레이어와 몬스터의 공통 클래스
class Character:
    def __init__(self, name, hp, power, magic, mp):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power
        self.magic = magic
        self.mp = mp
        self.max_mp = mp


    # 플레이어와 몬스터의 일반공격
    def attack(self, other):
        damage = random.randint(self.power-10, self.power+10)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")


    # 플레이어의 마법공격
    def magic_attack(self, other):
        self.mp = max(self.mp -50, 0)
        if self.mp == 0:
            print("보유 중인 MP가 모자랍니다! 마법공격을 사용할 수 없습니다!")
            return

        damage = random.randint(self.magic-15, self.magic+15)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")


    # 플레이어와 몬스터의 상태정보
    def show_status(self, other):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp} | MP {self.mp}/{self.max_mp}")
        print(f"{other.name}의 상태: HP {other.hp}/{other.max_hp}")


# 플레이어와 몬스터의 인스턴스, 스테이터스 할당
p = Character(input('플레이어의 이름을 입력하세요 : '), 1000, 40, 50, 500)
m = Character("서경몬", 800, 30, 0, 0)


# 플레이어의 이름 입력 후 게임 시작 멘트
print(f"{p.name}의 앞에 서경몬이 나타났다!")


# 반복문 실행의 조건 정해주기. 플레이어 또는 몬스터의 hp가 0보다 많을 때 계속 반복하기
while p.hp or m.hp > 0 :
    p.show_status(m)
    print(f'{p.name}의 선공! \n1.일반공격 2.마법공격(MP:-50) / 번호를 입력해주세요!')
    choice = input()
    if choice == '1':
        p.attack(m)
    elif choice == '2':
        p.magic_attack(m)
        if p.mp == 0 : continue
    else:
        print('잘못 입력하셨습니다.')
    
    
    # 게임 종료 조건의 if문과 조건별 출력 멘트
    if p.hp == 0 :
        print(f"{p.name}이(가) 들레와 서경몬에게 당했다! \n서경몬(본체가 들레)의 승리!")
        break
    elif m.hp == 0 :
        print(f"{p.name}이(가) 들레와 서경몬을 이겼다! \n들레는 이제 우리집으로!")
        break
    
    
    # 필수적으로 반복되는 while문의 요소 중 불필요한 요소는 break 여부 뒤에 배치
    print('서경몬의 들레 소환술! 들레가 할퀴기를 시전했다!')
    m.attack(p)