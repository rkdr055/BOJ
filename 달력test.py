list=[]
year,month,day=map(int,input().split())
this_year=2018-year
sum=year+month+day
for i in range(0,80):
    sumx=str(sum+i)
    birthsum=0
    for i in range(len(sumx)):
        birthsum+=int(sumx[i])
    if birthsum>22:
        birthsum=str(birthsum)
        birthsum=int(birthsum[0])+int(birthsum[1])
    list.append(birthsum)


year1=str(list[this_year])
sumy=0
while (1):
    if len(year1)<2:
        break
    else:
        for i in year1:
            sumy+=int(i)
        year1=str(sumy)
        sumy=0

month1=str(int(year1)+month)
summ=0
while (1):
    if len(month1)<2:
        break
    else:
        for i in month1:
            summ+=int(i)
        month1=str(summ)
        summ=0

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

year_1='''새로운 시작과 씨 뿌리는 시간 : 활동적인 해'''

year_2='''협동과 민감성과 인간관계의 해 : 완만하게 흘러가는 해'''

year_3='''창조적인 생각, 진실하게 말해야 하고, 자기 표현의 해 : 활동적인 해'''

year_4='''근본으로 돌아가 열심히 일하고 훈련하며건강을 관리하는 해, 1년수 3의 생각들을 구체화하는 해 : 생산적이고 잘 유지해 나가야 하는 해'''

year_5='''변화의 불확실성 위험 감수, 자유의 해 1년수 4의 성과물로부터 벗어나는 해 : 적극적인 해'''

year_6='''가정사와 가족에 대한 의무 다른 사람을 양육해야 하는 해 : 끊임없는 노력이 요구되는 해'''

year_7='''내면으로 향하고 휴식과 재평가, 숙고, 영적인 질문을 추구하는 해 : 홀로 연구하고 독서하는데 시간을 보내는 해'''

year_8='''존경과 성취, 인정의 해 : 비즈니스 문제와 재정관리가 주요 이슈, 많은 것을 관리하고 실행해야 하는 바쁜 시간'''

year_9='''완성과 해방, 용서와 변형의 해 : 더욱 더 조용해지는 해, 휴식의 기간, 그러나 초반에는 바쁨'''

month_1='''씨뿌리고 시작하기'''

month_2='''협동하고 인내하기'''

month_3='''유쾌하고 친구들과 함께하기'''

month_4='''열심히 일하고 건강관리하기'''

month_5='''변화를 만들기'''

month_6='''양육하고 가정을 꾸미기'''

month_7='''탐색하고 연구하기'''

month_8='''책임을 지고 돈을 다루기'''

month_9='''종결하고 보상받기'''

day_1='''어떤 일을 시작하고 자신에게 초점두기'''

day_2='''인내하고 세부적인 것에 신경쓰기'''

day_3='''창조적이고 친구들과 함께하기, 의사소통'''

day_4='''조직화하고 건강에 관심갖기'''

day_5='''변화를 만들고, 네트워크 증진하기'''

day_6='''일과 가족이나 가정에 관심갖기'''

day_7='''휴식과 재평가, 조용한 고독과 명상의 시간'''

day_8='''돈을 다루기, 책임지기'''

day_9='''끝맺음하기, 직관을 사용하기'''










