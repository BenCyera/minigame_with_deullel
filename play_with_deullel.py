import random
import time

# 멘트의 전체적인 딜레이 타임 조절
def ment_1(a) :
    time.sleep(1)
    return a

def ment_3(b) :
    time.sleep(3)
    return b

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
        ment_1(print(f"\n{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다."))
        if other.hp == 0:
            ment_1(print(f"\n\n{other.name}가 쓰러졌습니다."))


    # 플레이어의 마법공격
    def magic_attack(self, other):
        self.mp = max(self.mp -50, 0)
        if self.mp == 0:
            print("보유 중인 MP가 모자랍니다! 마법공격을 사용할 수 없습니다!")
            return

        damage = random.randint(self.magic-15, self.magic+15)
        other.hp = max(other.hp - damage, 0)
        ment_1(print(f"\n{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다."))
        if other.hp == 0:
            ment_1(print(f"\n\n{other.name}가 쓰러졌습니다."))


    # 플레이어와 몬스터의 상태정보
    def show_status(self, other):
        ment_1(print(f"\n{self.name}의 상태: HP {self.hp}/{self.max_hp} | MP {self.mp}/{self.max_mp}"))
        ment_1(print(f"{other.name}의 상태: HP {other.hp}/{other.max_hp}"))


# 플레이어와 몬스터의 인스턴스, 스테이터스 할당
ment_1(print("\n당신은 길을 걷다가 길냥이를 발견하고 헤벌레 다가갑니다..."))
ment_1(print("\n하지만 귀여운 길냥이에게 눈이 멀어 공명의 함정에 빠지게 됩니다!"))
ment_3(print(""" 

 .∧＿∧      ∧_∧.
(`・ω・)つ)゜Д゜)・゜
(つ　   ｒ⊂　⊂)'
｜　 _つ ⊂_⊂ノ
`し´
"""))
ment_3(print("\n...한참 후 깨어난 당신의 눈앞에는 귀여운 표지판이 있습니다.\n"))

ment_3(print("""

                             ∧ ﾍ　
　　                     /⌒ (`･ω･)
            |￣￣￣￣￣￣￣￣∪￣`∪￣￣￣￣￣￣￣￣￣￣￣`|
               이곳은 들레의 숲. 함부로 나대지 말 것.
            |＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿|
                              |   |
                              |   |

"""))


# 플레이어와 몬스터 인스턴스(객체), 클래스 지정
p = Character(ment_1(input('당신의 이름을 알려주세요 : ')), 1000, 50, 60, 300)
m = Character("들레", 1500, 60, 0, 0)


# 플레이어의 이름 입력 후 게임 시작 멘트
ment_3(print("""
             
            .　　　☆ *　. 　☆
            　　☆　. ∧＿∧　∩　* ☆
            - 등 -- ( ・∀・)/ . -- 장 -！！
            　　　. ⊂　　 ノ* ☆
            　　☆ * (つ ノ .☆
            　　　　 (ノ
                 
"""))
ment_1(print(f"{p.name}의 앞에 들레가 나타났다!"))


# 반복문 실행의 조건 정해주기. 플레이어 또는 몬스터의 hp가 0보다 많을 때 계속 반복하기
while p.hp or m.hp > 0 :
    p.show_status(m)
    ment_1(print(f'\n{p.name}의 선공! \n1.일반공격 2.마법공격(MP:-50) / 번호를 입력해주세요!'))
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
        ment_1(print(f"{p.name}이(가) 들레에게 당했다!"))
        ment_3(print(""" 
                            ∧ ﾍ
             ∧ ﾍ 찰싹　　　　(´·ω·`)　　찰싹
        　 (´·ω·`)　Ｕ☆ミ　(´·ω·`)
        　　　⊂彡☆))Д´)☆ミ⊃　찰싹
        　  ﾍ　∧　∩彡☆ ☆ミ∩  ﾍ　∧
        　(　　　　)　 찰싹　(　　　　)
        　찰싹

        """))
        ment_1(print("당신은 이제 평생 냥이들의 전용 캔따개가 되어야한다..."))
        ment_3(print(""" 
                
       .　┌○┐
        　│멍｜ﾊ,,ﾊ
        　│청｜ﾟωﾟ )
        　│이_|　／/
        　└○┘ (⌒)
        　　　し⌒

        """))
        break
    elif m.hp == 0 :
        ment_1(print(f"{p.name}이(가) 들레를 이겼다!"))
        ment_3(print(""" 
                             ∧ ﾍ
             ∧ ﾍ 찰싹　　　∧(´·ω·`)　　찰싹
        　 (´·ω·`)　Ｕ☆ミ　(´·ω·`)
        　　　⊂彡☆))Д´)☆ミ⊃　찰싹
        　  ﾍ　∧　∩彡☆ ☆ミ∩  ﾍ　∧
        　(　　　)　 찰싹 (　　　)
        　찰싹

        """))
        ment_1(print("들레는 이제 우리집으로!"))
        break
    
    
    # 필수적으로 반복되는 while문의 요소는 break 여부 뒤에 배치
    ment_1(print(f'들레의 할퀴기! {p.name}은(는) 얌전히 맞아주었다!'))
    m.attack(p)
    
    # 게임 종료 조건의 if문과 조건별 출력 멘트
    if p.hp == 0 :
        ment_1(print(f"{p.name}이(가) 들레에게 당했다!"))
        ment_3(print(""" 
                              ∧ ﾍ
             ∧ ﾍ 찰싹　　　　(´·ω·`)　찰싹
        　 (´·ω·`)　Ｕ☆ミ　(´·ω·`)
        　　　⊂彡☆))Д´)☆ミ⊃　찰싹
        　  ﾍ　∧　∩彡☆ ☆ミ∩ ﾍ　∧
        　　(　　)　 찰싹 (　　　)
        　찰싹

        """))
        ment_3(print("당신은 이제 평생 냥이들의 전용 캔따개가 되어야한다..."))
        ment_1(print(""" 
                
       .　┌○┐
        　│멍｜ﾊ,,ﾊ
        　│청｜ﾟωﾟ )
        　│이_|／ /
        　└○┘ (⌒)
        　　　し⌒

        """))
        ment_3(print("THE END..."))
        break
    elif m.hp == 0 :
        ment_1(print(f"{p.name}이(가) 들레와 서경몬을 이겼다! \n들레는 이제 우리집으로!"))
        ment_3(print(""" 
                            ∧ ﾍ
             ∧ ﾍ 찰싹　　　　(´·ω·`)　　찰싹
        　 (´·ω·`)　Ｕ☆ミ　(´·ω·`)
        　　　⊂彡☆))Д´)☆ミ⊃　찰싹
        　  ﾍ　∧　∩彡☆ ☆ミ∩  ﾍ　∧
        　(　　　　)　 찰싹　(　　　　)
        　찰싹

        """))
        ment_1(print("나쁜 자식... 감히 고양이를 학대해?"))
        ment_3(print(f""" 
        ┏┯┯┯┯┯┓
        ┃│││││┃ 당신은 깜빵에 갇혀 마땅하다
        ┃│ (=Д=) ┃
        ┃││ф ф│┃
        ┗┷┷┷┷┷┛
        """))
        break