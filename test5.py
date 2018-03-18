import calendar
import glob
import hangul_jamo
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
list=[]
list2=[]
printlist=""
year,month,day=map(int,input("생년월일을 입력하세요(ex 1993 10 08) : ").split())

this_year=2018-year

name=input("이름을 입력하세요 : ")

calendar_year=int(input("알고 싶은 해를 입력하세요 : "))
name2=name[1:]
name1=name[0]
name_dec=hangul_jamo.decompose(name)
name_dec1=hangul_jamo.decompose(name1)
name_dec2=hangul_jamo.decompose(name2)
sum=year+month+day
jaum_sum=0
moum_sum=0

for i in range(0,80):
    sumx=str(sum+i)
    birthsum=0
    for i in range(len(sumx)):
        birthsum+=int(sumx[i])
    if birthsum>22:
        birthsum=str(birthsum)
        birthsum=int(birthsum[0])+int(birthsum[1])
    list.append(birthsum)

first_num=list[0]
bi=str(list[0])
if(len(bi)>1):
    birth_num=int(bi[0])+int(bi[1])
else:
    birth_num=int(bi)


#1년수 계산
caye=calendar_year-year
year1=str(list[caye])
sumy=0
while (1):
    if len(year1)<2:
        break
    else:
        for i in year1:
            sumy+=int(i)
        year1=str(sumy)
        sumy=0

#1달수 계산
for i in range(1,13):
    month1=str(int(year1)+i)
    summ=0
    while (1):
        if len(month1)<2:
            break
        else:
            for i in month1:
                summ+=int(i)
                month1=str(summ)
            summ=0
    list2.append(str(month1))

#1년수


year1_1='''새로운 시작과 씨 뿌리는 시간 : 활동적인 해'''

year1_2='''협동과 민감성과 인간관계의 해 : 완만하게 흘러가는 해'''

year1_3='''창조적인 생각, 진실하게 말해야 하고 자기 표현의 해 : 활동적인 해'''

year1_4='''근본으로 돌아가 열심히 일하고 훈련하며건강을 관리하는 해
1년수 3의 생각들을 구체화하는 해 : 생산적이고 잘 유지해 나가야 하는 해'''

year1_5='''변화의 불확실성 위험 감수
자유의 해 1년수 4의 성과물로부터 벗어나는 해 : 적극적인 해'''

year1_6='''가정사와 가족에 대한 의무 다른 사람을 양육해야 하는 해
끊임없는 노력이 요구되는 해'''

year1_7='''내면으로 향하고 휴식과 재평가, 숙고, 영적인 질문을 추구하는 해
홀로 연구하고 독서하는데 시간을 보내는 해'''

year1_8='''존경과 성취, 인정의 해
비즈니스 문제와 재정관리가 주요 이슈, 많은 것을 관리하고 실행해야 하는 바쁜 시간'''

year1_9='''완성과 해방, 용서와 변형의 해
더욱 더 조용해지는 해, 휴식의 기간, 그러나 초반에는 바쁨'''


#1달수


month1_1='''씨뿌리고 시작하기'''

month1_2='''협동하고 인내하기'''

month1_3='''유쾌하고 친구들과 함께하기'''

month1_4='''열심히 일하고 건강관리하기'''

month1_5='''변화를 만들기'''

month1_6='''양육하고 가정을 꾸미기'''

month1_7='''탐색하고 연구하기'''

month1_8='''책임을 지고 돈을 다루기'''

month1_9='''종결하고 보상받기'''


#1일수


day1_1='''어떤 일을 시작하고 자신에게 초점두기'''

day1_2='''인내하고 세부적인 것에 신경쓰기'''

day1_3='''창조적이고 친구들과 함께하기, 의사소통'''

day1_4='''조직화하고 건강에 관심갖기'''

day1_5='''변화를 만들고, 네트워크 증진하기'''

day1_6='''일과 가족이나 가정에 관심갖기'''

day1_7='''휴식과 재평가, 조용한 고독과 명상의 시간'''

day1_8='''돈을 다루기, 책임지기'''

day1_9='''끝맺음하기, 직관을 사용하기'''

#1년수,1달수,1일수
year1_dict={'1':year1_1,'2':year1_2,'3':year1_3,'4':year1_4,'5':year1_5,'6':year1_6,'7':year1_7,'8':year1_8,'9':year1_9}
month1_dict={'1':month1_1,'2':month1_2,'3':month1_3,'4':month1_4,'5':month1_5,'6':month1_6,'7':month1_7,'8':month1_8,'9':month1_9}
day1_dict={'1':day1_1,'2':day1_2,'3':day1_3,'4':day1_4,'5':day1_5,'6':day1_6,'7':day1_7,'8':day1_8,'9':day1_9}

#달력

cal=calendar.calendar(calendar_year)
cal=cal.replace("Mo","월")
cal=cal.replace("Tu","화")
cal=cal.replace("We","수")
cal=cal.replace("Th","목")
cal=cal.replace("Fr","금")
cal=cal.replace("Sa","토")
cal=cal.replace("Su","일")
print_year=str(calendar_year)+"(1년수 : %s)\n\n"+year1_dict[year1]+"\n\n"
cal=cal.replace("         "+str(calendar_year),print_year%year1)

cal=cal.replace("   January","1월(1달수 : "+list2[0]+")")
cal=cal.replace("       February ","2월(1달수 : "+list2[1]+")")
cal=cal.replace("      March","3월(1달수 : "+list2[2]+")")
cal=cal.replace("    April","4월(1달수 : "+list2[3]+")")
cal=cal.replace("          May","5월(1달수 : "+list2[4]+")")
cal=cal.replace("           June","6월(1달수 : "+list2[5]+")")
cal=cal.replace("     July","7월(1달수 : "+list2[6]+")")
cal=cal.replace("         August","8월(1달수 : "+list2[7]+")")
cal=cal.replace("      September","9월(1달수 : "+list2[8]+")")
cal=cal.replace("   October","10월(1달수 : "+list2[9]+")")
cal=cal.replace("        November","11월(1달수 : "+list2[10]+")")
cal=cal.replace("       December","12월(1달수 : "+list2[11]+")")

# 타로 카드 설명


taro_1 ='''카드 : 바보
직업 : 여행가이드, 예술가, 모험, 등반가, 프리랜서, 자유업

본성이 자유로운 사람, 무거운 삶의 과제를 안고 살지만 단순,소박하다.
때로 미숙하고 부주의하다는 평을 듣기도 한다.
하나에 빠지면 열정적으로 몰입한다.'''

taro_2='''카드 : 마법사
직업 : 발명가, 세일즈맨, 치유사, 자영업자, 여성대상 서비스업
       동시통역, 연구개발자

재주가 있는 사람, 독창적·창조적이며 상상력이 뛰어나다.
능수능란하고 재주가 있어 꾀를 부려도 남이 잘 알아채지 못한다.'''

taro_3='''카드 : 고위 여사제
직업 : 교육자, 보모, 상담자, 종교가, 점술가, 타로마스터

지혜로운 사람, 침착·객관적이며 상황판단을 잘한다.
통찰력 있고 직관적으로 행동한다, 인정받고 싶어 한다.
사람을 관념적으로 대할 수 있어 상대의 불만을 사기도 한다.'''

taro_4='''카드 : 여황제
직업 : 금융업 종사자, 주부, 가내수공업, 텔레마켓, 작가, 미용업
       녹지조성이나 전원관련 사업

부드러운 여성, 에너지가 발달
다른 사람을 돌보고 그들이 잘 성장할 수 있도록 돕고자 한다.
성취적 지향적·실용적이다.'''

taro_5='''카드 : 황제
직업 : 건축가, 정치인, 고위간부, 무역업, 부동산관련업, 경영자

가장의 상징으로 가진 것을 지키려 애쓰는 사람. 세속적 힘, 확신, 부유함
안정, 권위 불굴의 정신, 호전적인 면도 있으나 이상적이다.'''

taro_6='''카드 : 신비사제
직업 : 종교, 철학자, 사제나 신부, 전문 컨설턴트
가르치는 사람, 인수합병전문가

진리를 가르치는 일에 관심이 있는 교육자의 상징이다.
자비롭고 친절하며 전통이나 의식을 중요하게 여기고
오래된 생각이나 원칙을 따르고자 한다. 가끔 보수적이라는 말을 듣는다.
원칙을 따르고 존중하며 종교적인 전통을 배우려고 한다.
그리고 지식을 얻고 깊은 의미를 깨닫기 위해 노력한다.'''

taro_7='''카드 : 연인
직업 : 대인서비스직종, 예술가, 네트워크 사업가, 연애코치, 결혼소개업, 연예인
       사회사업가, 자선사업가, 패션, 헤어디자이너

인간관계가 중요한 사람이다.
사랑과 미에 대한 괸심이 높고 자신을 아름답게 잘 꾸미는 능력이 있다.
정서적으로 깊은 감정을 느끼며 다른 사람과 교류하고 싶어 한다.'''

taro_8='''카드 : 전차
직업 : 군인, 경찰, 아나운서, 강사, 전문직 종사자, 여행사
       출판사, 유통업, 홍보, 외교관

목표를 향해 나아가는 사람으로 역경을 극복하려는 의지가 있다.
내면에서 상층되는 영향력들이 있어서 마음이 혼란스러워 결정을 잘 내리지 못한다.
한 가지 일에 집중하기 보다는 여러 가지 일을 동시에 관심을 가질 때가 많으며
이 일들을 해 낼 수 있는 능력도 있다.
하던 일을 성공적으로 해 내도록 마음의 변화에 귀를 기울일 필요가 있다.'''

taro_9='''카드 : 힘
직업 : 조련사, 교육자, 트레이너, 감독, 코치, 운동선수, 치과의사
       수의사, 미용업, 간병인

의유내강형의 사람이다.
화난 사람을 진정시킬 수 있는 방법을 알고 있는 사람이다.
내적인 용기와 결단력, 자기 확신과 도전적인 성향을 갖고 있다.
내면의 두려움과 맞서야 할 과제를 안고 있다.'''

taro_10='''카드 : 은둔자
직업 : 의사, 교수, 수도승, 탐험가, 사색가, 철학가
       기공사, 천문학자, 사주상담가

관심이 내면에 있는 사람이다.
자신의 감정을 잘 억제하며, 사려 깊고 신중하며
다른 사람에게 조언하기를 좋아한다.
행동이 빠르지 않고 고요하며 간혹 침울한 성격으로 발전하는 사람도 있다.'''

taro_11='''카드 : 운명의 수레바퀴
직업 : (돈을 회전 시키는)투자가, 운송업, 엔터테인먼트 사업, 가업을 잇는 것
        영화 영상, 파트타임, 기계공학, 생명공학, 자동차공학, 생물, 미생물

재주 있는 사람이다.
행위의 결과가 자신에게 돌아오니 행동을 잘하며 살아갈 필요가 있다.
진리라고 생각하는 분야를 배워서 타인에게 가르치거나
혹은 공공의 이익을 위해 사용할 필요가 있다.'''

taro_12='''카드 : 정의
직업 : 법조인, 중개인, 분석, 평가와 감정, 에이전시, 임상병리, 회계사

공평무사한 사람이다. 적당한 균형과 조화를 이루고자하는 성격이다.
마음의 평정심을 찾은 사람.
분별력이 있고 판단을 한 다음에는 실천이 빠르다.
올바른 미덕과 명예를 중요시 한다.
대인관계에서 옳고 그름이 앞서니 정서적인 면을 간과할 우려가 있다.'''

taro_13='''카드 : 거꾸로 매달린 사람
직업 : 심리학자, 연구가, 정신과 전문의, 사회봉사가
       의료관련 종사자, 스턴트맨

말과 행동이 다른 사람에 비해 느리다.
둔감한 편이기 때문에 정서적인 표현이 부족하다.
겉으로는 느리지만 내면에서 많은 것이 일어나는 사람이므로
서두르고 재촉하기 보다는 인내심을 가지고 지켜보는 것이 필요하다.'''

taro_14='''카드 : 죽음
직업 : 경찰, 군인, 건설(철거반), 외과의사, 장의사

변형을 일으키는 사람이다.
새로운 것을 위하여 과거의 것을 과감하게 제거하는 사람.
육체적인 죽음을 의미하는 것이 아니라
죽음처럼 뜻밖의 변화를 일으킬 수 있는 면이 있다.
변화를 두려워 하지 않는다.'''

taro_15='''카드 : 절제
직업 : 통신회사, 외환딜러, 항공기 승무원, 해운업, 텔레마케터
       브로커, 커플매니저, 펀드매니저

마음을 잘 절제하고 인내할 줄 아는 사람.
자기 통제와 검소한 태도를 통해 목표를 달성한다.
새로운 환경에 순응하고 주변과 조화를 이루려고 한다.
큰 목표를 위해 다른 사람과 연합하여 성공적인 결합을 이룬다.
역기능적으로 발전할 경우에 빠질 가능성이 있다.'''

taro_16='''카드 : 악마
직업 : 사채업, 브로커, 마술사, 사교계, 유흥관련 종사자
       성과 위주영업, 경마, 교도관, 직장인

집착이 강한 사람이다.
자신과 관련이 있는 대상에 대하여 걱정을 많이 하고 잔소리를 많이 한다.'''

taro_17='''카드 : 탑
직업 : 성형외과, 부동산업, 우주항공, 게임, 소방공무원, 스턴트맨
       건설현장, 군사과학, 영적인 지도자, 재건축업

변화에 대한 충격을 심하게 받는 사람이다.
진실을 갑작스럽게 인식하고 그 진실과 맞지 않을 경우에
자신이 가진 것을 모두 버릴 수 있는 과감한 면이 있다.
과거의 대인 관계를 꾸준히 유지하기 보다는 변화를 추구한다.'''



taro_18='''카드 : 별
직업 : 에술가, 연예인, 디자이너(보석, 미용, 헤어, 의상), 조경사
       방송인, 창작관련, 녹색운동

어둠 속에서 희망의 등불이 되려는 사람이다.
힘들어 하는 대상에 힘이 되어 주고 싶어 한다.
신념이 있고 낙천적이며 긍정적인 생각을 많이 한다.
미래에 대한 희망을 가지고 있다.
그래서 현재 자신이 처한 어려운 상황을 간과할 우려가 있다.'''

taro_19='''카드 : 달
직업 : 집안일, 건축 점성가, 요식업, 수사관, 명상가, 천문학자
       동물, 수의사, 명상가, 최면술사

달의 모양이 변하는 것과 같이 마음이 자주 바뀌고 의심이 많이 사람이다.
자신이 너무 순수하여 남들로부터 잘 속는다고 생각한다.
자신이 내적 변화를 인정하고 즐기는 방법을 찾을 필요가 있다.'''

taro_20='''카드 : 태양
직업 : 증권, 출판업, 육아사업, 동업, 운동선수, 카피라이터, 경마
       태양열 사업 관련, 소아과의사, 고아원, 아동심리학자

어린아이와 같이 순수한 사람이다.
자신의 역량보다 더 큰 일을 해내는 용기와 믿음이 있는 사람이다.
보살핌에 대한 감사를 잊지 말고 살아야 한다.'''

taro_21='''카드 : 심판
직업 : 저널리스트, 고고학자, 아나운서, 성우, 음반, 공연, 이벤트
       목욕관련, 적십자 등 의료단체

옳고 그름에 대한 판단이 바르고 정의로운 사람이다.
옳은 일을 위해서 기끼어 희생을 감수한다.
억울하거나 불쌍한 사람을 보면 적극 개입해서 도와준다.'''

taro_22='''카드 : 세계
직업 : 장식업체, 외국계회사, 패션업계, 동시통역, 홍보회사, 유엔기구
       스타일리스트, 스튜어디스, 비행사, 무역

어떠한 환경에서도 완성을 이루려는 사람이다.
완전함을 이루려는 노력 때문에 완벽주위자라는 말을 듣게 된다.
일의 한쪽 면보다 전체를 보는 경향을 있어 시야가 넓다.
가족이 도움을 구하면 자신의 일인 것처럼 적극적으로 나선다.'''


# 별자리 설명

양='''양자리(3월 21일 ~ 4월 19일)

정의감이 남다른 양자리는 뜨거운 열정, 자신감을 가지고 있는데
자신만의 신념이 있으며 이 신념이 아주아주 강합니다.
하지만 양자리는 불 같은 성격으로 인해 비난을 받기도 하지만
천진난만함이 있기 때문에 화가 오래 가지는 않습니다.

장점 - 리더쉽이 있다, 에너지가 넘친다,
       다른 사람을 훌륭하게 도와 그들의 꿈을 이루게 해준다
       도전을 받아들인다, 타인의 가장 좋은 면을 본다
       타인을 위해 위험을 무릅쓴다, 약자를 보호한다
       명확하다, 사랑하는 사람을 위해 목숨도 바친다
       모두가 포기할지라도 자신만은 포기 하지 않는다.

단점 - 최고가 아니면 못산다, 성급하다
       다른사람에게 미치는 영향을 고려하지 않는다
       참을성이 부족하다, 말을 안 듣는다, 이기적이다, 충동적이다

인체 – 머리, 얼굴 윗부분, 뇌하수체

직업 – 불, 칼, 금속류 취급(군인, 스포츠, 기자, 엔지니어)'''

황소='''황소자리(4월 20일 ~ 5월 20일)

실용성, 현실성이 있는 황소자리는 오감이 발달한 사람들이 많습니다.
또한 신중하고 느긋함을 가지고 있는데 이런 성격 때문에 밖으로 나가는 것보다는
집에서 노느 것을 좋아하는 사람이 많습니다.

장점 - 주의와 사려가 깊다, 믿음직스럽다, 우아하고 예술적이다
       다른 사람의 말을 잘 들어준다, 다른 이들의 재능을 인정한다
       재치가 비상하다, 젠틀하다, 시간관념 철저하다

단점 - 제멋대로이다, 완고하고 고집부린다, 물질만능주의이다, 행동이 굼뜨다
       말을 잘 안한다, 생각을 너무 많이해서 행동이 미뤄진다, 지루하다, 둔감하다

인체 - 얼굴아랫 부분, 목, 인후, 성대, 갑상선

직업 - 귀중품, 재정, 금융, 회계, 부동산, 농업, 원예, 요리, 성악, 건축, 실내장식'''

쌍둥이='''쌍둥이자리(5월 21일 ~ 6월 21일)

소통하기를 좋아하는 쌍둥이자리는 유머감각이 있고 예리하지만
인내심이 부족할 수 있어 낡은 것보다는 새로운 것을 좋아하며
순간적인 대체능력이 좋고, 호기심이 많은 성격을 가지고 있습니다.

장점 - 호기심이 왕성하다, 재미있는 성격이다, 유쾌하다, 매력적이다
       다재다능하다, 생기가 넘친다, 행동이 빠르다, 선입견이 없다.

단점 - 침착하지 못하다, 싫증을 잘 낸다, 비실용적인 면이 있다
       변덕쟁이이다, 무책임하다.

인체 - 어깨, 팔, 손, 흉선, 허파

직업 - 통역, 운수업, 커뮤니케이션, 교사, 상업일반, 세일즈, 관고, 출판, 통신'''

게='''게자리(6월 22일 ~ 7월 22일)

가정적인 성격을 가진 게자리는 차분한 성격으로 주변사람들이 좋아하며
공감능력이 뛰어나지만 이로 인해 우울감이 자주 들기도 합니다.
사랑을 할 때에는 솔직하게 애정표현을 할 줄 아나
겁이 많은 성격으로 어려운 상황을 책임지려 하지 않는 경향도 나타납니다.

장점 - 끈기있다, 빈틈이 없다, 친절하다, 가정적이다, 기억력이 뛰어나다
       남을 도우려 한다, 배려심이 있다, 무엇이 필요한지 잘 안다.

단점 - 소유욕이 강하다, 쉽게 상처 받는다, 시무룩해한다, 까다롭다
       자신을 모욕하면 계속 물고 늘어진다, 이기적이다, 권력을 남용한다.

인체 – 젖가슴, 위, 간

직업 – 도, 소매업, 부동산, 상담, 숙박업, 요식업, 양육, 영양, 원예, 가구 인테리어'''

사자='''사자자리(7월 23일 ~ 8월 22일)

사람의 이목을 끄는 리더십이 있는 사자자리는 늘 주인공이 됩니다.
남에게 조언해 주는 것을 좋아하지만, 자신을 숨기는 것을 못해
얼굴이 감정표현이 다 드러나 곤란할 때가 있을 수 있습니다.

장점 - 정직하고 충직하다, 밝다, 가정에 대한 자부심이 있다, 생기발랄하다
       다정다감하다, 책임감이 있다, 용기 있다

단점 - 고집이 강하다, 남을 무시한다, 거만하다, 독선적이다
       뽐내기를 좋아한다, 무관심하다, 배려심이 없다
       눈에 띄려고 발버둥친다, 다른사람을 평가절하한다.

인체 – 등, 척추, 심장

직업 – 연극, 영화, 예술, 모델, 장식, 스포츠, 기획광고, 증권 중개'''

처녀='''처녀자리(8월 23일 ~ 9월 23일)

총명함과 사람들과 대화를 할 줄 아는 처녀자리는 꼼꼼하고 정확한 사람으로
완벽주의라고 오해를 받지만 사실 굉장히 도덕적인 사람입니다
또한 수줍음을 타는 성격에 상대방을 답답하게 만들기도 하지만
특유의 매력을 가지고 있는 사람입니다.

장점 - 젠틀하다, 다른사람에게 잘 공감한다, 정리정돈을 잘한다,
       박학다식하다, 위트있다, 마음이 따뜻하다, 근면성실하다, 헌신적이다.

단점 - 부지런하지 못한 사람을 혐오한다, 까다롭다, 독단적이다, 자주 우울하다
       신경과민, 감정을 드러내지 않는다, 끝없이 요구한다.

인체 – 아랫배, 소장, 비장, 췌장

직업 – 서비스업, 전문기술직, 인쇄, 정밀기계, 의약, 간호, 사무비서직
       평론, 재단, 원예, 교육'''

천칭='''천칭자리(9월 24일 ~ 10월 22일)

온순한 성격을 가지고 있는 천칭자리는 사교성이 아주 좋습니다.
주변에 친구가 많지만 우유부단한 성격 때문에 곤경에 처하기도 합니다.
천칭자리는 책을 좋아합니다.

장점 - 협조적이다, 좋은 동료이다, 예술적 감각이 뛰어나다, 세련미가 넘친다
       사랑스럽고 로맨틱하다, 센스 있다, 페어플레이, 대화가 잘 통한다
       훌륭한 중재자이다, 지적이다.

단점 - 자아도취에 빠진다, 게으르다, 우유부단하다, 권모술수를 부린다
       거만하고 경솔하다.

인체 – 허리, 골반, 콩팥, 신장, 난소

직업 – 예술, 정치, 외교, 법률, 대리인, 협동사업, 매니저, 브로커, 세일즈'''

전갈='''전갈자리(10월 23일 ~ 11월 22일)

겉으로는 차분하지만 마음은 뜨거운 전갈자리는 12별자리 성격 중 자존심이 가장 셈
이로 인해 종종 다툼이 있을 수 있지만 뜨거운 성격으로 체험하고 느끼는 것을
좋아하는 사람이 많습니다.

장점 - 탐구적인 자세이다, 통찰력있다, 보호하려는 마음이 있다, 끈기있다
       사람을 끌어당기는 매력이 있다, 세밀하다, 감정이 풍부하다, 감각적이다
       집중력이 강하다, 남을 인정한다.

단점 - 자기 파괴적이다, 무정하다, 의심과 질투가 많다, 소유욕이 강하다
       화를 잘 낸다, 자주 우울하다, 교활하다, 복수심이 강하다.

인체 – 생식기, 항문, 배설기관

직업 – 군인, 경찰, 외과의사, 보험, 정신분석, 장의사, 식육점, 정화조 하수구 관계업
       흥신소, 과학연구, 사회자본'''

사수='''사수자리(11월 23일 ~ 12월 24일)

별자리 중 낙천적인 성격으로 사수자리는 아주 좋은 성격들을 가지고 있습니다.
하지만 좋고, 싫음을 분명히 하기 때문에 솔직한 성격들이 대부분이며
솔직한 성격 때문에 주변에서 상처를 입기도 합니다.

장점 - 솔직하다, 남과 터놓고 지낸다, 낙관적이다, 사람들의 장점을 잘 본다
       정직하고 공평하다, 천진난만하다, 모두에게 자극제가 된다, 감각적이다.

단점 - 따지는 것을 좋아한다, 참을성이 없다, 광신도이다, 도박심리가 있다
       자신의 재능을 인정하지 않는 사람에게 비판적이다
       계획을 잘 못 세운다, 무책임하다, 실수를 자주한다.

인체 – 엉덩이, 허벅지, 좌골신경

직업 – 종교, 철학, 강연, 여행, 선전공보업무, 외국관련업, 자유업'''

염소='''염소자리(12월 25일 ~ 1월 19일)

목표지항적인 성격으로 리더적인 성향을 가지고 있습니다.
또한 규칙과 질서를 중요하게 여기기 때문에 아주 예의가 바릅니다.
부지런한 성격이지만 때로는 융통성이 없다는 말을 듣기도 합니다.
이러한 성격 때문에 짝사랑을 하는 경우가 종종 있습니다.

장점 - 체계화를 잘한다, 열심이 일한다, 현실적이다, 빈틈이 없다, 두려움이 없다
       높지만 현실적인 기준을 가지고 있다, 좋은 충고를 한다
       전통을 지킨다, 권위를 존중한다

단점 - 무조건 자기것이 최고라고 여긴다, 이기적이다, 남을 혹사 시킨다
       남을 용서하지 않는다, 걱정이 많다, 매우 비관적이다, 운명론자이다.

인체 – 무릎, 관절, 피부, 뼈, 손발톱, 담낭

직업 – 공공행정, 조각가, 정치, 경영 관리직, 공예'''

물병='''물병자리(1월 20일 ~ 2월 18일)

대부분 독창적인 사람들이 많아 활발한 지적활동을 합니다.
철학도 중요시 하지만 개인의 성향을 존중할 줄 아는 사람이지만
이런 자연스러운 모습 때문에 사람들에게 비판을 받기도 합니다.
하지만 혁신적인 아이디어나, 파격행보를 표현할 줄 아는 사람으로
늘 미래에서 꿈을 꾸며 살고 있는 미래 지향적인 사람입니다.

장점 - 대화가 잘 통한다, 사려 깊고 배려 깊다, 협조적이다
       믿음직해서 타인에게 의지가 된다, 과학적인 사고를 한다
       생각과 행동이 자주적이다, 창의력이 풍부하다.

단점 - 좋은 아이디어를 남과 공유하지 않는다, 요령이 없고 무례하다, 심술궃다
       취향이 별나다, 자기중심적이다, 자신감이 없다
       남의 사생활에 관심을 가진다.

인체 – 발목, 복사뼈, 순환기계통, 부갑상선

직업 – 민간사무, 공공단체업무, 작사, 작곡, 극작가
       무선통신관련업무, 항공, 비행, 상담, 공학'''

물고기='''물고기자리(2월 19일 ~ 3월 20일)

수줍음이 많지만 예술적인 성향을 가진 물고기자리의 별자리 성격은
타인을 도울 줄 아는 사람으로 봉사하기를 좋아하며 상상력이 풍부하기 때문에
예술인이 되거나 착한 마음으로 성직자가 되기도 합니다.

장점 - 사랑이 넘친다, 배려심이 있다, 남을 의심하지 않는다, 호의적이다
       곤란한 사람을 도우려 한다, 로맨틱하다, 자비롭다, 타인을 깊이 이해한다.

단점 - 자기 연민에 빠진다, 어리버리하다, 의존적이다, 자주 우울하다
       현실 감각 상실,모든 일을 자기 탓으로 한다
       큰 잘못을 하여 남들 입소문에 오른다.

인체 – 발, 체액, 임파선

직업 – 연극, 영화, 예술, 병원, 형무소, 요양원, 박물관, 도서관, 승려, 수도사'''


#별자리 계산
if month==3:
    if day >=21:
        Constellation='양자리'
    else:
        Constellation='물고기자리'
elif month==4:
    if day>=20:
        Constellation='황소자리'
    else:
        Constellation='양자리'
elif month==5:
    if day>=21:
        Constellation='쌍둥이자리'
    else:
        Constellation='황소자리'
elif month==6:
    if day>=22:
        Constellation="게자리"
    else:
        Constellation='쌍둥이자리'
elif month==7:
    if day>=23:
        Constellation='사자자리'
    else:
        Constellation='게자리'
elif month==8:
    if day>=23:
        Constellation='처녀자리'
    else:
        Constellation='사자자리'
elif month==9:
    if day>=24:
        Constellation='천칭자리'
    else:
        Constellation='처녀자리'
elif month==10:
    if day>=23:
        Constellation='전갈자리'
    else:
        Constellation='천칭자리'
elif month==11:
    if day>=23:
        Constellation='사수자리'
    else:
        Constellation='전갈자리'
elif month==12:
    if day>=25:
        Constellation='염소자리'
    else:
        Constellation='사수자리'
elif month==1:
    if day>=20:
        Constellation='물병자리'
    else:
        Constellation='염소자리'
elif month==2:
    if day>=19:
        Constellation='물고기자리'
    else:
        Constellation='물병자리'

#타로 dict
taro_dict={1:taro_1, 2:taro_2, 3:taro_3, 4:taro_4, 5:taro_5, 6:taro_6, 7:taro_7, 8:taro_8, 9:taro_9, 10:taro_10,11:taro_11, 12:taro_12, 13:taro_13, 14:taro_14, 15:taro_15, 16:taro_16, 17:taro_17, 18:taro_18, 19:taro_19, 20:taro_20, 21:taro_21, 22:taro_22}

#별자리 dict
Constellation_dict={"양자리":양,"황소자리":황소,"쌍둥이자리":쌍둥이,"게자리":게,"사자자리":사자,"처녀자리":처녀,"천칭자리":천칭,"전갈자리":전갈,"사수자리":사수,"염소자리":염소,"물병자리":물병,"물고기자리":물고기}

#모음 dict
moum_dict={'ㅏ':1,'ㅑ':2,'ㅓ':3,'ㅕ':4,'ㅗ':5,'ㅛ':6,'ㅜ':7,'ㅠ':8,'ㅡ':9,'ㅣ':1,'ㅐ':2,"ㅒ":3,'ㅔ':4,'ㅖ':5,'ㅘ':6,'ㅙ':7,'ㅚ':6,'ㅝ':10,'ㅞ':11,'ㅟ':8,'ㅢ':10,'a':1,'e':5,'i':9,'o':6,'u':3}

#자음 dict
jaum_dict={'ㄱ':1,'ㄴ':2,'ㄷ':3,'ㄹ':4,'ㅁ':5,'ㅂ':6,'ㅅ':7,'ㅇ':8,'ㅈ':9,'ㅊ':1,'ㅋ':2,'ㅌ':3,'ㅍ':4,'ㅎ':5,'b':2,'c':3,'d':4,'f':6,'g':7,'h':8,'j':1,'k':2,'l':3,'m':4,'n':5,'p':7,'q':8,'r':9,'s':1,'t':2,'v':4,'w':5,'x':6,'y':7,'z':8}


#풀네임 자음 모음 도출(운명수)

for i in name_dec:
    if i in moum_dict:
        moum_sum+=moum_dict[i]
    if i in jaum_dict:
        jaum_sum+=jaum_dict[i]
    total_name=moum_sum+jaum_sum

#이름 자음 모음 합(성장수)

sum_name2=0
for i in name_dec2:
    if i in moum_dict:
        sum_name2+=moum_dict[i]
    if i in jaum_dict:
        sum_name2+=jaum_dict[i]

#성 자음 모음 합(姓)

sum_name1=0
for i in name_dec1:
    if i in moum_dict:
        sum_name1+=moum_dict[i]
    if i in jaum_dict:
        sum_name1+=jaum_dict[i]


#운명수 계산
character=str(jaum_sum)
sumc=0
while (1):
    if character=='11' or character=='22':
        break
    elif len(character)<2:
        break
    else:
        for i in character:
            sumc+=int(i)
        character=str(sumc)
        sumc=0

#영혼수 계산
soul=str(moum_sum)
sums=0
while (1):
    if soul=='11' or soul=='22' or soul=='33':
        break
    elif len(soul)<2:
        break
    else:
        for i in soul:
            sums+=int(i)
        soul=str(sums)
        sums=0

#운명수 계산
des=str(total_name)
sumd=0
while (1):
    if des=='11' or des=='22' or des=='33':
        break
    elif len(des)<2:
        break
    else:
        for i in des:
            sumd+=int(i)
        des=str(sumd)
        sumd=0

#인생여정수 계산
life=str(sum)
suml=0
while (1):
    if life=='11' or life=='22':
        break
    elif len(life)<2:
        break
    else:
        for i in life:
            suml+=int(i)
        life=str(suml)
        suml=0

#완성수 계산
comp=str(int(life)+int(des))
sump=0
while (1):
    if comp=='11' or comp=='22' or comp=='33':
        break
    elif len(comp)<2:
        break
    else:
        for i in comp:
            sump+=int(i)
        comp=str(sump)
        sump=0

#성장수 계산
grow=str(sum_name2)
sumg=0
while (1):
    if grow=='11' or grow=='22' or grow=='33':
        break
    elif len(grow)<2:
        break
    else:
        for i in grow:
            sumg+=int(i)
        grow=str(sumg)
        sumg=0

#성 계산
first=str(sum_name1)
sumf=0
while (1):
    if len(first)<2:
        break
    else:
        for i in first:
            sumf+=int(i)
        first=str(sumf)
        sumf=0





#1일수 계산
day1=str(int(month1)+day)
sumd=0
while (1):
    if len(day1)<2:
        break
    else:
        for i in day1:
            sumd+=int(i)
        day1=str(sumd)
        sumd=0


#운명수


jaum_1='''지배적이고 힘차 보이는, 창조적인, 확신과 자기신회가 있어 보이는, 용기 있는
집단에 종속되지 않는, 세련되고 전문적인 이미지를 투사하는
디자이너의 의상을 입지만 자신의 패션 스타일을 고집하는
밝고 때론 대담한 무늬의 의상을 입는 경향이 있는, 지나치게 완벽주의 옷차림
몸에 꼭 맞는 옷 즐겨 입음.'''

jaum_2='''내성적이면서 부끄러움이 많은, 신중하게 한 발짝 물러나 지켜보는, 깨끗한
깔끔해 보이는, 협동적이고 타인을 기쁘게 하기 위해 노력하는
조용하고 평화로우며 외교적인, 겸손한, 예술적으로 보이는, 지나치게 꼼꼼해 보이는
이성에겐 좋은 동반자로 생각되는, 매력적인, 주목을 받으면 당황하는
까다로워 보일 수 있는, 타인의 관심을 피할 수 있는 무난한 스타일을 선호하는
경청하는, 논쟁과 갈등을 피하는, 보호 받기를 원하는 것처럼 보이는
지나치게 몰개성적으로 보임, 부드럽게 흘러내리는 장신구
독특한 색상의 의상착용.'''

jaum_3='''재미있어 보이는, 사람을 끌어당기는 매력의 소유자, 친근하고 활기찬
파티에 목숨 건, 수다쟁이, 즐겁고 매력 넘치는, 외향적이고 사교적인
때론 지나치게 각광을 받으려고 하는, 매력적인 외모, 긍정적인 관점
매순간마다 열광하는, 재치있는 언어능력, 훌륭한 유머감각
색상과 스타일 모두 뛰어난 의상선택, 지나치게 과장해 말하거나 많은 말을 하는 경향
질투심을 잘 통제해야 함.'''

jaum_4='''간편한 활동복 차림을 좋아하는, 착실하고 한결같으며, 정직한 시민처럼 보이는
원칙을 강조하는, 결과가 부정적이더라도 지름길로 가지 않는
실용적이면서 경제적이고 오래 입을 수 있는 의상을 선택하는
태도와 유행에 있어서 보수적인, 검소하고 소박한, 근면하고 일벌레인
믿을 수 있고 진실하며 책임감 있는, 부끄러움이 많고 내성적인
시시해 보이는 일들을 즐기는 것이 어렵다는 것을 아는 지루한 사람으로 인식
완고함과 엄격함.'''

jaum_5='''성적으로 매력적인, 활력 넘치고 재치있는, 변화와 다양성을 선호하는
선택의 자유가 선호순위 1위인, 최신유행에 맞춰 감각 있게 옷을 입는
밝고 반짝이는 색상의 옷을 입는, 사교적이며 원기 왕성한
사람들을 끌어당기는 매력의 소유자, 어려보이는, 완전히 그 순간을 살아가는
관능적이며 오감만족을 즐기는, 이동하는 것을 좋아하는
유능한 네트워크의 달인으로 대화를 즐기는, 진취적인 사고를 지닌
오늘을 살아가는 사람, 여행 만병통치약(책임회피로 보임)'''

jaum_6='''친절한 파티 주최자들, 완벽주의자와 이상주의자, 방어적이면서 신뢰할만한
자신의 책임이 아닌 것도 해주려고 하는, 다른 사람들을 위한 상담과 조언
가정적인 예술적 재능과 사물을 아름답게 꾸미기 좋아하는, 뛰어난 색채감
멋지고 편안한 느낌의 의상을 선호하는, 칭찬받으려는 욕구, 타고난 선생님
동정심있고 사람들에게 확신을 고무시키는
외모에 무관심하거나 집안 정리 안 될 수도 있음.'''

jaum_7='''신비와 비밀의 분위기를 즐기는, 생각에 몰두하는 것처럼 보이는
인지력과 관찰력 있는, 지적인, 엄숙하면서도 내성적인, 냉담한
한정된 취향의 옷만 입는, 옷매무새가 있고 단정한, 오래된 것을 좋아하는
통찰력이 있고 내면을 향하는, 독특하고 때론 기괴한 취향의
처음에는 다가가기가 어려운, 신비주의와 철학적인
만약 다가가 애기한다면 매우 좋은 대화상대인, 훌륭한 스타일이 중요한
매우 개인적인, 다른 사람들이 부정적 회의적 냉소적으로 봄.'''

jaum_8='''성공적으로 보이는 의상, 유창하고 권력이 있어 보이는, 야망의, 힘을 발산하는
실제 삶보다 더 위대해 보이는, 권위, 고급 의상과 악세사리를 한
통제하려고 하는, 비즈니스 마인드, 조직화된, 비전을 지닌
자신의 권한을 위임하는 법을 아는, 확신 있고 경쟁적이며 공격적인, 지적인
원숙한, 전통적인, 차갑고 형식적이며, 재치없고 권위주의적인 사람으로 보임.'''

jaum_9='''관대하면서 가끔씩은 지나친 호의인, 참을성 많고 자비심 있는, 철학적인
따뜻하고 친절하며 잘 보살펴주는, 이상주의적이고 로맨틱한, 정서적이고 직관적인
행운있는, 잘 설레는, 성취하는, 빠른 결정을 못 내리는, 상처 받기 쉬운
형이상학적이고 거리가 있는 듯한, 세상에 대해 매우 박식한
사람들을 물질적인 성취결과 판단하지 않는, 인정있는
다른 사람들에게 매우 사랑받고 존경받는
극적인 연출력을 돋보이게 하는 깜짝 놀랄만한 의상을 입는
불의에 대해서는 가차 없는, 언제나 동안으로 보이는
다른 사람들의 문제 관여함으로서 자신의 감정은 억압된 심한 정신적 불균형 초래
검정색 좋아함, 밝은 색을 입어라.'''

jaum_11='''비전을 보는, 영감있는, 천재적인, 다른 사람보다 더욱 영적으로 보이는
독창적이고 예술적이며 독특한 옷을 입는, 개인주의적인, 인생의 풍미가 느껴지는
창조적이며, 혁신적인, 긴장하는, 자신의 현실을 창조하는
세부사항까지 잘 다루는 능력, 초감각을 가진, 직관, 싸이킥
텔레파시 능력이 있는, 지나치게 의존하는 사람으로 보임
긴장하고 우울하고 예민한 모습으로 보임.'''

jaum_22='''경쟁에서 후광을 얻은, 수퍼우먼이나 수퍼맨으로서 강한 인상을 주는
목적의식이 강한, 결정력있는, 견고하고 안정된, 실용적이며, 창조적인
물질적인 성공을 가져오는, 상식적으로 문제에 접근하는, 문제 해결사
건설자, 마치 세상을 통제하는 듯이 보이는, 달인의, 효율적이고
외교적으로 보이는, 맞춤의 보수적인 스타일의 의상을 입는, 정직한, 생산적인
심각한, 책임감있는, 계획하고 리스트를 작성하며
목표를 설정하고 점검하기를 좋아하는, 일중독
삶을 여유롭게 즐기는 모습 보여주기를.'''


#성격수

moum_1='''리더가 되기를 원함, 다른 사람들을 통제하려 하고 명령 복종을 싫어하며
고집불통에 의지력과 야망, 독립심, 애정문제는 로맨스가 중요
파트너가 매력적이고, 영리하며, 독립적인 성향을 가지기를 원함
때론 매우 차갑고 소원해 보이는데 자기 보호이다.
바보와 일하느니 차라리 혼자 한다.
프로젝트를 생각해 내고 시작하길 원한다.'''

moum_2='''조화를 갈망 갈등을 견딜 수 없어 리더가 되려고 하지 않는다.
양 측면 바라볼 수 있는 특별한 능력, 다른 사람을 민감하게 고려 편안하게 만듦
온정적이고 사랑스러운 영혼이며, 애정문제는 최선을 다해 베풀어 주려고 노력하며
가끔씩은 자기 자신을 망각할 정도로 지나치게 베풀어 주기도 한다.
타인으로부터 비난은 심한 상처
솔로보다는 결혼, 연애를 통해서 더욱 행복해질 수 있음.
헌신자적 동반자 프로젝트를 위한 것들을 함께 모아가길 원한다. '''

moum_3='''가슴 안에서는 다른 사람들을 최상의 상태에 다다를 수 있도록 격려하고
웃음을 선사하며, 열정을 뿜으면서 타인을 행복하게 하려는 욕망이 꿈틀댄다.
삶 그 자체를 사랑함
애정은 유희적, 생각의 변화가 잦은데 재미를 추구하는 경향
프로젝트에 대해 디자인하고 토론하길 원한다.'''

moum_4='''계획을 통해 체계적인 방식으로 인생을 살아가고
실용적인 방식으로 일해 나가려는 욕망
일의 목표와 점검, 분명한 경계를 정하는 것과 관심
스스로 통제할 수 있는 상황에 두는 방식,
애정문제는 감정적인 접근마저도 매우 실용적인 방식으로 행함
프로젝트를 계획하고 실용화하며 관리하길 원한다.'''

moum_5='''제약에서 벗어나 열정적으로 변화와 여행을 수반하려는 욕망
변화무쌍함과 자극을 경험하길 원함, 애정문제 섹스란 관능, 격력
특별함에 의해 지배, 성적인 자극에 이끌림, 딴따라에 끌림
프로젝트 관련 네트워크를 만들어 판매하길 원한다.'''

moum_6='''아름다움과 조화와 가정, 이해심과 충성심, 헌신과 애정, 신의의 특징
자신의 가족과 가정을 보호하고 돌보며 사랑하길 원함, 애정문제는 매우 이상주의적인
장미, 촛불, 헤어져도 매달리지 않음.'''

moum_7='''은둔자, 독신자, 성직자, 수녀, 적막과 고요, 평화, 혼자 독서하는 것을 즐김
서로 비밀이 잘 유지될 수 있고 독특한 신념 라이프스타일마저도 유지
예민한 영혼의 소유자대개는 지성이나 고차원적인 인식능력을 발달시키려고 노력함
멀리서도 모든 것을 감지, 프로젝트를 더욱 더 분석하기 원한다.'''

moum_8='''보스가 되기를 바람, 복잡한 감정적인 연애보다는 비즈니스에 몰두
가정뿐만 아니라 세상에서도 중요한 사람이 되기를 원함. 보스가 되길 원한다.'''

moum_9='''연민과 동정심으로 가득한 영혼
가슴 깊은 곳에서는 세상에 대한 사랑과 높은 이상과 힘으로 영향력을 미치며
직관적이며, 자비로운 공감력 높음,
애정문제는 사랑스럽고 이상주의적이며, 소울 메이트를 찾아 나서며
강렬한 사랑은 끝도 없이, 프로젝트를 끝내고 모든 사람에게 나눠주길 원한다.'''

moum_11='''극단적으로 예민하기에 신경증이 있거나 정신적으로 문제 있을 수 있음
감정적 기복 심함, 시대를 뛰어넘는 지혜와 이해력과 예지력을 가짐,
가슴 속 깊이 모든 관계가 편안해 지길 갈망함, 예감이 발달
고대지식과 영적지혜를 가져오는 임무를 지닌 오래된 영혼이며
동시대인들 보다 더 큰 지혜를 가진 사람,
애정문제는 온화하고 달콤하며 상대방을 즐겁게 해주길 원함
결코 2인자는 되지 않으려 한다
어떠한 관계라도 영적인 특성을 불러오는데 다른 세상에 대해 알고 있기 때문.
프로젝트를 개선하기를 원한다.'''

moum_22='''인류의 이익과 지속적으로 존재할 수 있는 것을 현실화해 나가길 갈망
큰 규모의 개혁 리더십을 통해 정신적으로 설득해 나갈 수 있는 능력의 소유자 미래학자들
지구의 삶에 더욱 실제적인 물질적 토대가 안정될 수 있도록 구축해 나가게 된다.
신중하기 때문에 실용적이며, 명확한 목표를 지니고 삶이 안정되어 있는 파트너를 선호
같은 꿈을 공유할 연인 원함
영원히 지속될 만한 기념비적인 프로젝트를 만들길 원한다.'''

moum_33='''도움을 필요로 하는 모든 이들에게 무조건적인 사랑을 베풀기를 갈망
기쁨과 사랑이 넘치며, 보호와 관심, 도움이 필요한 사람들을 어루만져줌.
사랑의 진동을 가장 최상의 수준인 우주 삼라만상에 대한 자비심으로 끌어올린다.
프로젝트를 죽을 때까지 사랑하고 모든 사람들에게 가르치길 원한다.'''


#운명수


des_1='''자아를 개발해 리더가 되는 것, 인생목적은 용기
새롭게 시작하며, 독창적이며 혁신적으로 임무를 완수해 나가는 것
자기 정체성을 확립하고 의지력을 돈독히 하는 것과
확실한 의사결정력을 필요로 한다. 홀로서기, 스스로 생각하기
자신의 특성을 완전히 이해하는 것,
새로운 생각과 대상, 독특한 행동방식들을 통해 펼쳐질 것이다.
확신 결여, 지체하는 버릇, 먼저 리더로서 역량을 키워라.'''

des_2='''현생의 사업은 조화를 창조하는 일
인생 목적은 균형을 이루고 협동하며
인내하는 조직의 일원이 되는 것
대인관계 기술을 개발하는 것이 필요. 우유부단, 평화 중재자.'''


des_3='''사명은 사람들에게 활력을 주고 영감을 고무하는 일
목적은 ‘즐거움은 전파력을 갖는다는 것’
기회는 타고난 재능인 언어를 통해
자신의 감정을 표현해 나가는 것을 배우고
경쾌함과 재치를 지니는 것을 통해 펼쳐짐.
기분파, 비판적, 표현하고 적극적이며 용기있게 임하라.'''


des_4='''사명은 지속적인 가치를 지닌 것을 건설하는 일
실용적인 삶의 방식을 취하고 열심히 일하는 것
안전을 위해 질서와 관습 이용
목표를 위한 기회의 장은 전통적인 가치를 표현하는 것을 배우고
느려도 꾸준하고 안정감 있게 생활해 나가는 것을 통해 펼쳐질 것이다.
완고하고 의심이 많음, 관리와 조직화를 위해 살도록 예정됨
모든 일에 초석을 세우고 그것을 기반으로 건설해 나가라.'''


des_5='''사명은 적응, 변화, 진보이다.
목적은 자유를 추구하고 자신을 이끌 수 있는 것이면 무엇이든지
자신의 호기심을 따라가는 것이다.
자신의 타고난 재능이나 사람들을 끌어들이는 자석같은 매력을 사용함.
자유로운 영혼이 되는 법을 배우는 것, 들떠있거나 불만족이 가득
자유와 해방을 위해 전진해 나가라.'''


des_6='''사명은 봉사, 목적은 가족을 돌보고 사람들을 사랑하는 것
자신을 둘러싼 세상과 조화를 창조하기 위해
미(美)나 공동체에 대한 사랑 드러내기,
관대한 표현과 다른 사람들에게 안락함을 주는 것을
배우는 것을 통해 펼쳐질 것이다. 상호의존적이고 자학하는 경향
양육과 아름답게 가꾸는 것을 위해 조화롭게 사랑하라.'''


des_7='''사명은 분석과 탐구
목표는 깊게 연구해 자신이 맞닥뜨린 것에 대해 완성해 나가는 것
내면이 지혜를 알기 위해 타고난 연구능력과 완벽주의적인 방식 사용,
예리한 관찰력과 사고력과 분별력을 배우는 것을 통해 펼쳐질 것이다
냉소적, 회의적, 전문가가 되어 지혜를 가르쳐라.'''


des_8='''사명은 자신에 대한 완전한 통제, 목적은 성취와 성공
경영에 대한 기술을 사용, 권위를 표현하고 자신의 저력을 발견하며
비전을 내다보는 법을 배우는 것을 통해 펼쳐질 것이다.
무자비, 거만
성공을 위해 살도록 자신을 통제하고 능수능란한 리더십을 발휘하라.'''



des_9='''사명은 무조건적으로 온전히 사랑하는 것
목적은 보편적인 형제애를 갈망, 이타심과 민감성
치유 기술을 사용, 자기변혁과 치유
관용과 용서를 배우는 것을 통해 펼쳐질 것이다. 쉽게 속는 호인(허당)
편협한 사람, 지평을 넓히기 위한 삶을 위해 다른 사람에게 다가가서 도와줘라.'''

des_11='''사람들의 영감을 고무시키고 의식을 상승하는 일
자신의 직관력이 인류 대의를 위해 사용되어야 하는 것을 인식하고
다른 사람들의 삶을 개혁하고 상승시키며, 변형해 주는 일을 하게 됨.
시련이 와도가르치는 능력을 개발하고 시련을 극복하는 것을
배우는 것으로부터 펼쳐질 것이다.
참을성 없고 비판적이며, 예민함, 영감에 찬 리더.'''

des_22='''사명은 꿈을 실현하고 인류를 위한 계획과 프로젝트를 실행하는 일
목적은 영적인 원리가 작동하는 물질세계 안에서
실용적인 방식을 통해 계획을 실현해 나가는 것이다.
자신의 효율성과 경쟁력을 재고 자신의 천성에 기초하면서 진실해 지는 과정을 통해
결코 포기하지 않는 법을 배우는 것에서 펼쳐질 것이다.
완고하고, 다른 사람들의 결점을 쉽게 받아들일 수 없음,
건설의 달인으로 물질세계에 영적인 법칙을 가져오는 사람.'''

des_33='''사명은 인류의 진일보를 위해 더 높은 차원의 사랑을 기쁘게 베풀어주는 것
목적은 사랑하는 마음으로 타인을 위해 봉사
삶이란 재미와 사랑으로 가득하다는 것을 사람들에게 가르쳐주는 일, 기쁨과 빛
사랑과 봉사를 펼칠 수 있는 곳의 리더가 되는 것을 통해 펼쳐질 것이다
지나치게 감정적이며, 자신이 직면하는 가난과 결핍에 의해 사기가 저하됨
치유의 달인으로 사랑이야말로 진정한 치유사임을 모두에게 가르쳐라.'''


#인생여정수


life_1='''독립의 길, 자수성가, 리더십, 개척자.
자신의 독특한 발상을 활용할 수 있는 환경과 개척자 정신이 직업
성공, 비즈니스, 건강과 엔터테인먼트 산업,
정부기관, 서점 관련일 10/1 완성,재탄생 .완전한 익힘
19/1 우주적 지혜를 신성하게 사용하는 법 배워서 힘의 남용 개정'''

life_2='''균형과조화의 길, 협동과 타협이 가져다주는, 장점을 배우게 됨
화합(타고난 사교가), 명상가, 평화중재자, 섬세함을 요하는 일
보좌하는 역할, 자료수집 민감성 활용하는 일.'''

life_3='''창조와 자발성의 길, 낙관성과 열정, 타인의 영감을 고무, 언변가
재치, 밝은 에너지, 마치 생생한 그림을 보듯이 명료하게 전달하는 언어력
예술성과 관련된 일, 작가, 디자이너, 일러스트레이터, 무용가, 배우.'''

life_4='''근면하고 체계적으로 일하는 길
충성심과 규칙준수 신뢰를 배우는 게임
구조물을 건설, 타고난 건서가, 안전, 느리지만 꾸준하게
시스템이나 건설 매니저, 경리나 회계사, 행정, 교육, 비즈니스
문서나 생산물의 관리, 조심스럽게 관리
체계화될 필요와 지속적인 가치를 지닌 일'''

life_5='''인생이란 변화의 게임, 자유의 투사, 타고난 혁신가
자유무역수완, 세일즈와 마케팅, 다양한 종류의 판촉활동에 능숙
대중 상대하는 일, 신생업종, 의사소통, 광고
명성을 얻거나 세일즈와 관련되는 일
일상적인 일보다는 활력적인 일, 탐정, 미스테리물의 작가
여행 관련 작업 14/5 질서와 안정성을 통해 자유의 남용 개정'''

life_6='''다른 사람을 도와주려는 마음, 자리이타(自利利他)
타고난 상담가(공감하고 돌보려는 마음), 상담사, 고문, 선생님, 치유사
가정과 일 사이에 균형을 이루는 법을 배우게 될 것
자신을 둘러싼 세상을 아름답게 만들기 위해 노력, 서비스업
다른 사람들을 위해 보다 안락하고 편안하며
우아한 삶을 만들어가기 위해 노력
의료업, 가구상, 리모델링, 장식, 미용업, 가족경영이나 가내공업, 동물조련
교육업, 정원 가꾸기 양육과 가정의 수인'''

life_7='''분석하는 삶, 미스테리와 설명할 수 없는 대상을 탐구
영적 지혜를 타인과 공유, 탐구자, 컴퓨터 프로그래머, 첨단기술전문가
분석과 연역적 추론, 경리나 회계사, 법률관련 계열, 교육업, 종교지도자
16/7 영적 재탄생을 통해 책임감과 사랑의 남용을 개정'''

life_8='''돈(물질)과 진정한 가치(비물질적인)간에 차이를 분별해 나가는 삶
장인의 길, 자신의 타고난 힘과 권위를 가지고 일하는 법 배워야함.
책임자의 지위, 보스, 큰 조직, CEO, CFO,임원, 파이낸셜 상담, 부동산 중개인
스포츠 감독, 재판과, 병원장, 은행장'''

life_9='''우주 삼라만상이 상호 연결되어 있다는 것 이해하는 삶
자비와 관용을 배우는 우주적 사랑의 길, 관용, 타고난 치유사, 글, 작곡
회화나 조각, 국제 무역, 예술, 교육, 건강
구호나 치유 사업을 기획하거나 인도주의 단체에 참가'''

life_11='''인류에게 영성과 영감을 고취시키게 될 것
사람들이 쉽게 다가올 수 있도록 하기 위해서 영감에 찬 리더,
카리스마적인 리더이자, 자석처럼 끌어당기는 매력의 소유자
사람들에게 강한 감동과 전율 느끼게 만듦.'''

life_22='''꿈을 실현하는 여정, 영감을 드러내는 사람들 건설의 달인
인류공영에 적극적인 창조자, 기획자, 조직가, 배우, 외교관, 대사, 대통령
큰 규모 사업체의 고위임원, 자신의 분야에서 전문가로서 인정받게 됨.
성공이란 조화와 협동뿐 아니라 인류공헌이라는 이상을 실현하는 것을 배움'''

#완성수

comp_1='''권위있는 삶, 적극적 삶, 건강 회복 빠름, 리더'''

comp_2='''중재자, 예술적인 재능'''

comp_3='''타고난 열정과 열광하는 특성, 우정이 중요하며
세상과 조화로울 때 재정적으로 안정'''

comp_4='''존경 받고 진실, 책임감, 실수에 대한 책임을 지지 않으려고 할 때도 있음'''

comp_5='''자유가 가장 중요, 여행, 새로운 것을 탐험, 영원한 젊음'''

comp_6='''복지, 가족의 가치, 활동무대 부엌'''

comp_7='''은둔자적이고 분석적인 자신만의 독특한 방식을 살아감
구루가 되어가는, 분석가'''

comp_8='''성공, 성취'''

comp_9='''완벽한, 자비심, 진정한 우주적 사랑 발견, 봉사
내려놓는 법, 하심, 치유사'''

comp_11='''예민하고 긴장하기 때문에 식이요법 필요, 면역 시스템 보호 필요,
심령적이고 직관적인 지혜, 명상가, 협상가 중재자 시련'''

comp_22='''내면의 안정과 힘, 도전에 강, 전문가, 다양한 능력 요구하는 직업, 시련'''

comp_33='''애정과 기쁨, 사랑 문제 해결 능력으로 인류에 공헌, 인류를 돌보는 일,
상호 의존성과 결혼 실패 등은 시련'''


#성장수

grow_1='''최상의 성장은 자기주장과 개인주의자로 살아가는 경로를 따라 진행된다.'''

grow_2='''최상의 성장은 다른 사람과의 관계에 있다.'''

grow_3='''최상의 성장은 언어력과 창조성을 사용하는데 있다.'''

grow_4='''최상의 성장은 공포와 안전이라는 주제와 관련된다.'''


grow_5='''최상의 성장은 자유에 대한 책임에 있다.'''

grow_6='''최상의 성장은 사랑을 통해 온다.'''

grow_7='''최상의 성장은 신비주의와 영적인 지식을 통해 온다.'''

grow_8='''최상의 성장은 돈의 관리와 권력(권위)에 대한 책임을 통해 온다.'''

grow_9='''최상의 성장은 자비와 용서를 통해 온다.'''

grow_11='''최상의 성장은 직관을 가지고
우주원리를 실용적으로 응용해 나가는 것을 통해 온다.'''

grow_22='''최상의 성장은 직관을 가지고
우주원리를 실용적으로 응용해 나가는 것을 통해 온다.'''

grow_33='''최상의 성장은 감정에 대해 달통함으로써
자기희생을 하려는 성향을 순교자가 되지 않고서도 승화하는데서 온다.'''


#성


first_1='''시작, 새로운 아이디어, 창조력
잠재력,활동의 근원, 원시적인 충동들, 약속
어떤 상황이 시작되려 하거나 이미 시작된 초기 단계
1은 근원, 모든 것의 시작과 끝을 나타내는 수'''

first_2='''협력, 관계, 양극단, 반대되는 힘들의 균형과 조화
이원성, 선택, 결정, 기다리는 기간, 일시적 중지
결정 또는 선택의 시간, 이원성과 연합 사이에서 균형을 찾을 시간'''

first_3='''종합, 성장, 창조성, 풍부, 협동, 우정, 예술적 표현
계획 수정, 행동을 취할 준비, 단결과 단체 활동이 강조된다.
진행 중인 계획을 첫 번째나 두 번째 단계에서 수정하라. 목표의 초기 성취'''

first_4='''기초, 훈련, 일, 질서, 안정성, 견고성, 현실적 성취, 실제적 달성
이전 3의 수준에서 상상하고 계획한 것들이 구체화되기 시작한다.
기초는 안정적이고 건고하다.'''

first_5='''새로운 주기, 변화, 전진, 이동, 조정, 미세, 불안정, 도전
다양성, 자유, 용기, 변화가 필요함.
4수준에서 구체화되기 시작한 모든 것에 대한 조절 및 미세 조율
불확실성을 예상하되 그것 역시 지나갈 것임을 알아라.'''

first_6='''균형, 건강, 변화에 직면해서의 조화
만족, 이완, 소원 성취, 마음의 평정
5수준에서 나타난 도전에 맞서 승리하라. 조화와 균형이 나타난다.
용기를 내라. 생각하는 것보다 목표에 가까이 있다.'''

first_7='''영성, 지혜, 완전한 질서, 대우주, 종교, 행운, 마법, 다양한 선택

6수준의 세속적인 문제들에 맞서 승리하고 수많은 기회들이 당신에게 열린다.'''

first_8='''재생, 부활, 재평가, 갈무리, 우선순위 정하기

유지할 것과 버릴 것을 결정하기, 재생과 새로워짐을 생각하라'''

first_9='''끝맺기, 통합, 이동, 유연성, 성취, 달성

8수준에서 만났던 상황들을 완성하고 그 상황들을 삶 속에 통합한다.'''





character_dict={'1':jaum_1,'2':jaum_2,'3':jaum_3,'4':jaum_4,'5':jaum_5,'6':jaum_6,'7':jaum_7,'8':jaum_8,'9':jaum_9,'11':jaum_11,'22':jaum_22}
soul_dict={'1':moum_1,'2':moum_2,'3':moum_3,'4':moum_4,'5':moum_5,'6':moum_6,'7':moum_7,'8':moum_8,'9':moum_9,'11':moum_11,'22':moum_22,'33':moum_33}
des_dict={'1':des_1,'2':des_2,'3':des_3,'4':des_4,'5':des_5,'6':des_6,'7':des_7,'8':des_8,'9':des_9,'11':des_11,'22':des_22,'33':des_33}
life_dict={'1':life_1,'2':life_2,'3':life_3,'4':life_4,'5':life_5,'6':life_6,'7':life_7,'8':life_8,'9':life_9,'11':life_11,'22':life_22}
comp_dict={'1':comp_1,'2':comp_2,'3':comp_3,'4':comp_4,'5':comp_5,'6':comp_6,'7':comp_7,'8':comp_8,'9':comp_9,'11':comp_11,'22':comp_22,'33':comp_33}
grow_dict={'1':grow_1,'2':grow_2,'3':grow_3,'4':grow_4,'5':grow_5,'6':grow_6,'7':grow_7,'8':grow_8,'9':grow_9,'11':grow_11,'22':grow_22,'33':grow_33}
first_dict={'1':first_1,'2':first_2,'3':first_3,'4':first_4,'5':first_5,'6':first_6,'7':first_7,'8':first_8,'9':first_9}

printlist+="\n\n-----생명수-----\n"+str(first_num)+"\n\n-----탄생수-----\n"+str(birth_num)
printlist+='\n\n-----------------------------------성격 카드---------------------------------\n\n'+taro_dict[first_num]
printlist+='\n\n----------------------------------영혼 카드----------------------------------\n\n'+taro_dict[birth_num]
printlist+="\n\n------------------------------------별자리-----------------------------------\n\n"+Constellation_dict[Constellation]
printlist+="\n\n----------------------------------성격수 (%s)---------------------------------\n\n"%character
printlist+=character_dict[character]
printlist+='\n\n----------------------------------혼의수 (%s)---------------------------------\n\n'%soul
printlist+=soul_dict[soul]
printlist+='\n\n----------------------------------운명수 (%s)---------------------------------\n\n'%des
printlist+=des_dict[des]
printlist+='\n\n--------------------------------인생여정수 (%s)-------------------------------\n\n'%life
printlist+=life_dict[life]
printlist+='\n\n----------------------------------완성수 (%s)---------------------------------\n\n'%comp
printlist+=comp_dict[comp]
printlist+='\n\n----------------------------------성장수 (%s)---------------------------------\n\n'%grow
printlist+=grow_dict[grow]
printlist+='\n\n-----------------------------------성姓 (%s)----------------------------------\n\n'%first
printlist+=first_dict[first]
printlist+='\n\n------------------------------------달력-------------------------------------\n\n\n'
printlist+=cal
printlist+='\n\n----------------------------------1달수 의미---------------------------------\n\n'
printlist+="1일 경우 : "+month1_1
printlist+="\n\n2일 경우 : "+month1_2
printlist+="\n\n3일 경우 : "+month1_3
printlist+="\n\n4일 경우 : "+month1_4
printlist+="\n\n5일 경우 : "+month1_5
printlist+="\n\n6일 경우 : "+month1_6
printlist+="\n\n7일 경우 : "+month1_7
printlist+="\n\n8일 경우 : "+month1_8
printlist+="\n\n9일 경우 : "+month1_9
printlist+='\n\n----------------------------------1일수 의미---------------------------------\n\n'
printlist+="1일 경우 : "+day1_1
printlist+="\n\n2일 경우 : "+day1_2
printlist+="\n\n3일 경우 : "+day1_3
printlist+="\n\n4일 경우 : "+day1_4
printlist+="\n\n5일 경우 : "+day1_5
printlist+="\n\n6일 경우 : "+day1_6
printlist+="\n\n7일 경우 : "+day1_7
printlist+="\n\n8일 경우 : "+day1_8
printlist+="\n\n9일 경우 : "+day1_9
printlist+='\n\n-----------------------------------------------------------------------------\n'


print(printlist)



#표 이미지 호출

pyo1=Image.open("D:1~40.jpg")
pyo2=Image.open("D:41~80.jpg")
point1=Image.open("D:point.jpg")

#표 합성

for i in range(80):

    if i<40:
        area=(94+i*40,63+(list[i]-1)*26,116+i*40,82+(list[i]-1)*26)
        pyo1.paste(point1,area)
    else:
        area=(94+(i-40)*40,63+(list[i]-1)*26,116+(i-40)*40,82+(list[i]-1)*26)
        pyo2.paste(point1,area)

#표 출력

pyo1.show()
pyo2.show()

while(1):
    continue