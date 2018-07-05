import datetime
import locale

def H_DATE_TIME():
    current =   datetime.datetime.now()
    print(current)
    past    =   datetime.datetime(1999,12,31)
    print(current>past)#현재 날짜가 과거보다 큰가?
    diff=current-past
    print(diff)
    print(diff.days,diff.seconds,diff.microseconds)
print()
print("H_DATE_TIME")
H_DATE_TIME()

def H_DETE_PLUS():
    current = datetime.datetime.now()
    print(current)
    diff=datetime.timedelta(days=30,seconds=0,microseconds=0)
    print(current+diff)
print()
print("H_DETE_PLUS")
H_DETE_PLUS()

def H_DATE_STRFTIME():
    current=datetime.datetime.now()
    print(current.strftime('%Y/%m/%d'))
    """
    ERROR
    UnicodeEncodeError: 'locale' codec can't encode character '\uc6d4' in position 11: encoding error
    why err??
    참고 : Windows에서는 Locale로 인해 UnicodeEncodeError가 발생할 수 있다
    다음과 같이 조치한다
    import locale
    locale.setlocale(locale.LC_ALL,'ko_KR.UTF_8')
    """
    locale.setlocale(locale.LC_ALL, 'ko_KR.UTF_8')
    print(current.strftime('%Y년 %m월 %d일'))
    print(current.strftime('%(YEAR)Y (MONTH)%m (DAY)%d'))
    print(current.strftime('%Y-%m-%d    %H-%M-%S'))
print()
print("H_DATE_STRFTIME")
H_DATE_STRFTIME()