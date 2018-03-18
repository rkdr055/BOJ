import datetime
def getMonthName(month):
    li=['1월','2월','3월','4월','5월','6월',
        '7월','8월','9월','10월','11월','12월']
    monthName=li[month-1]
    return monthName
def title(year,month):
    print('    ',getMonthName(month),' ',year)
    print('-'*27)
    print('일  월  화  수  목  금  토')
def getStartDay(year,month):
    d=datetime.date(year,month,1)
    return d.weekday()#월요일 0
def getLastDay(year,month):
    if month==12:
       year=year+1
       month=1
    else:
       month=month+1
    d=datetime.date(year,month,1)
    t=datetime.timedelta(days=1)

    k=d-t
    return k.day

def body(year,month):
    startday=getStartDay(year,month)
    lastday=getLastDay(year,month)
    if startday==6:
        s=1
    else:
        s=startday+2
    c=0
    m=0
    for k in range(6):
        for i in range(7):
            c=c+1
            if c<s:
                print('{:>2}'.format(''),end='  ')
            else:
                if lastday>m:
                    m=m+1
                    print('{:>2}'.format(m),end='  ')
        print()

def Dal(year,month):
    title(year,month)
    body(year,month)

def main():
    year=eval(input('연도를 입력하세요(ex. YYYY):'))
    month=eval(input('월을 입력하세요(1~12):'))
    Dal(year,month)
main()
