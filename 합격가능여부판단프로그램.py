score = [] #이름, 점수 관리할 리스트
s=[]#등급에 대한 리스트
std=[]
z=0
def aa(): #선택 메뉴를 담는 함수
    print("안녕하세요. ㅇㅇ대학교 ㅇ학과 합격을 판단하는 프로그램입니다.")
    print("점수 계산의 기준은 2022학년도 대학수학능력시험입니다.")
    print("성적 포함 영역: 국어, 수학, 영어")
    print("\n메뉴를 선택해주세요. \n")
    choice = int(input("<1> 입력 \n<2> 합격 가능성 여부 확인 \n<3> 성적과 합격 가능성 한눈에 확인하기 \n<4> 종료 \n번호를 입력하세요:"))
    return choice

while True:
    print("*"*40)

    choice=aa()
    if choice == 4: #<3> 종료
        break #<3> 입력시 실행 멈춤
    elif choice ==3:
      print("입력된 수험번호의 성적과 합격가능성을 출력하겠습니다.")
      for i in std:
        print("*"*40)
        for n in i:
          print(n)
    elif choice == 1: #수험번호와 성적을 입력받고, 입력 받을 때 리스트에 보관함
        print("*"*40)
        
        number = input("수험번호를 입력하세요: ")
        print("\n**수험번호", number,  "확인되었습니다.**")

        korean = int(input("\n국어 성적을 입력하세요: "))
        if korean   >= 84: #국어 성적이 84점 이상일 때 아래 코드 출력
            grade_korean = "\n2022학년도 대학수학능력시험 국어등급은 1등급입니다."
            s.append(1)
            
        elif korean >= 78: #84점 미만 78점 이상일 때 아래 코드 출력
            grade_korean = "\n2022학년도 대학수학능력시험 국어등급은 2등급입니다."
            s.append(2)
        elif korean >= 71: #78점 미만 71점 이상일 때 아래 코드 출력
            grade_korean = "\n2022학년도 대학수학능력시험 국어등급은 3등급입니다."
            s.append( 3 )
        elif korean >= 64: #71점 미만 64점 이상일 때 아래 코드 출력
            grade_korean = "\n2022학년도 대학수학능력시험 국어등급은 4등급입니다."
            s.append( 4 )
        elif korean >= 54: #64점 미만 54점 이상일 때 아래 코드 출력
            grade_korean = "\n2022학년도 대학수학능력시험 국어등급은 5등급입니다."
            s.append( 5 )
        elif korean >= 42: #54점 미만 42점 이상일 때 아래 코드 출력
            grade_korean = "\n2022학년도 대학수학능력시험 국어등급은 6등급입니다."
            s.append( 6)
        elif korean >= 31: #42점 미만 31점 이상일 때 아래 코드 출력
            grade_korean = "\n2022학년도 대학수학능력시험 국어등급은 7등급입니다."
            s.append( 7)
        elif korean >= 22: #31점 미만 22점 이상일 때 아래 코드 출력
            grade_korean = "\n2022학년도 대학수학능력시험 국어등급은 8등급입니다."
            s.append( 8)
            
        else:
            grade_korean = "\n2022학년도 대학수학능력시험 국어등급은 9등급입니다."
            s.append( 9)

        print(grade_korean) #국어 등급 출력


        math = int(input("\n수학 성적을 입력하세요: "))
        if math   >= 84: #수학 성적이 89점 이상일 때 아래 코드 출력
            grade_math = "\n2022학년도 대학수학능력시험 수학등급은 1등급입니다."
            s.append(1)
            
        elif math >= 78: #8 9점 미만 77점 이상일 때 아래 코드 출력
            grade_math = "\n2022학년도 대학수학능력시험 수학등급은 2등급입니다."
            s.append(2)
            
        elif math >= 71: #77점 미만 65점 이상일 때 아래 코드 출력
            grade_math = "\n2022학년도 대학수학능력시험 수학등급은 3등급입니다."
            s.append(3)
            
        elif math >= 64: #65점 미만 51점 이상일 때 아래 코드 출력
            grade_math = "\n2022학년도 대학수학능력시험 수학등급은 4등급입니다."
            s.append(4)
            
        elif math >= 54: #51점 미만 34점 이상일 때 아래 코드 출력
            grade_math = "\n2022학년도 대학수학능력시험 수학등급은 5등급입니다."
            s.append(5)
            
        elif math >= 42: #34점 미만 21점 이상일 때 아래 코드 출력
            grade_math = "\n2022학년도 대학수학능력시험 수학등급은 6등급입니다."
            s.append(6)
            
        elif math >= 31: #21점 미만 14점 이상일 때 아래 코드 출력
            grade_math = "\n2022학년도 대학수학능력시험 수학등급은 7등급입니다."
            s.append(7)
            
        elif math >= 22: #14점 미만 9점 이상일 때 아래 코드 출력
            grade_math = "\n2022학년도 대학수학능력시험 수학등급은 8등급입니다."
            s.append(8)
            
        else:
            grade_math = "\n2022학년도 대학수학능력시험 수학등급은 9등급입니다."
            s.append(9)
            
        print(grade_math) #수학 등급 출력

        english = int(input("\n영어 성적을 입력하세요: "))
        if english   >= 90: #영어 성적이 90점 이상일 때 아래 코드 출력
            grade_english = "\n2022학년도 대학수학능력시험 영어등급은 1등급입니다."
            s.append(1)
            
        elif english >= 80: #90점 미만 80점 이상일 때 아래 코드 출력
            grade_english = "\n2022학년도 대학수학능력시험 영어등급은 2등급입니다."
            s.append(2)
            
        elif english >= 70: #80점 미만 70점 이상일 때 아래 코드 출력
            grade_english = "\n2022학년도 대학수학능력시험 영어등급은 3등급입니다."
            s.append(3)
            
        elif math >= 60: #70점 미만 60점 이상일 때 아래 코드 출력
            grade_english = "\n2022학년도 대학수학능력시험 영어등급은 4등급입니다."
            s.append(4)
            
        elif math >= 50: #60점 미만 50점 이상일 때 아래 코드 출력
            grade_english = "\n2022학년도 대학수학능력시험 영어등급은 5등급입니다."
            s.append(5)
            
        elif math >= 40: #50점 미만 40점 이상일 때 아래 코드 출력
            grade_english = "\n2022학년도 대학수학능력시험 영어등급은 6등급입니다."
            s.append(6)
            
        elif math >= 30: #40점 미만 30점 이상일 때 아래 코드 출력
            grade_english = "\n2022학년도 대학수학능력시험 영어등급은 7등급입니다."
            s.append(7)
            
        elif math >= 20: #30점 미만 20점 이상일 때 아래 코드 출력
            grade_english = "\n2022학년도 대학수학능력시험 영어등급은 8등급입니다."
            s.append(8)
            
        else:
            grade_english = "\n2022학년도 대학수학능력시험 영어등급은 9등급입니다."
            s.append(9)
            
        print(grade_english) #영어 등급 출력

        score.append( [korean, math, english] )

    elif choice == 2:

        for a in score:
            avg = (korean+math+english)

            if 229 <= avg: #여기서 229는 2022학년도 정시합격자의 수능최고성적 평균 값입니다.
                result = ("\n축하합니다! 수험번호 ", number," ㅇㅇ대학교 ㅇㅇ학과에 합격할 가능성이 높습니다!")
            elif 203 <= avg: #여기서 203은 2022학년도 정시합격자의 수능최저성적 평균 값입니다.
                result = ("\n수험번호", number," ㅇㅇ대학교 ㅇㅇ학과에에 합격할 가능성이 높지 않습니다!")
            else:
                result = ("\n수험번호", number," ㅇㅇ대학교 ㅇㅇ학과에 합격할 가능성이 거의 없습니다!")

            print(f"{result}")
        std.append([])
        std[z].append(number) 
        std[z].append(grade_english) 
        std[z].append(grade_math) 
        std[z].append(grade_korean) 
        std[z].append(result) 
        z=z+1
        
