import sqlite3

def select_all_name():
    conn = sqlite3.connect('my_books.db')         # 데이터베이스 커넥션 생성
    cur = conn.cursor()                             # 커서 확보

    cur.execute('SELECT * FROM ml_class where name ="백경규"')       # 조회용 SQL 실행

    books = cur.fetchall()                          # 조회한 데이터 불러오기

    for book in books:                              # 데이터 출력하기
        print(book)

    conn.close()                                    # 커넥션 닫기

def select_all_project():
    conn = sqlite3.connect('my_books.db')         # 데이터베이스 커넥션 생성
    cur = conn.cursor()                             # 커서 확보

    cur.execute('SELECT * FROM ml_class where project ="비트 자율주행 시스템"')       # 조회용 SQL 실행

    books = cur.fetchall()                          # 조회한 데이터 불러오기

    for book in books:                              # 데이터 출력하기
        print(book)

    conn.close()                                    # 커넥션 닫기

def select_all_lastname():
    conn = sqlite3.connect('my_books.db')         # 데이터베이스 커넥션 생성
    cur = conn.cursor()                             # 커서 확보

    cur.execute('SELECT * FROM ml_class where name like "백%"')       # 조회용 SQL 실행

    books = cur.fetchall()                          # 조회한 데이터 불러오기

    for book in books:                              # 데이터 출력하기
        print(book)

    conn.close()                                    # 커넥션 닫기


print("name")
select_all_name()
print("project")
select_all_project()
print("lastname")
select_all_lastname()