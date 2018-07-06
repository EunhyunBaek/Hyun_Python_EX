import sqlite3
from Hyun_Python_EX.DATE_7_6.DB.Hyun_select import select_all_name

def update_address(na,ad):
    conn = sqlite3.connect('my_books.db')  # 데이터베이스 커넥션 생성
    # cur = conn.cursor()  # 커서 확보
    update_sql = "update ml_class set address='%s'"%ad+" where name = '%s'"%na
    print(update_sql)

    conn.execute(update_sql)  # 조회용 SQL 실행
    conn.commit()
    conn.close()  # 커넥션 닫기

print("업데이트")
ls=input("이름:")
ad=input("주소:")
update_address(ls,ad)