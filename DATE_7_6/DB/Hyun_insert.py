import sqlite3

def Insert_Data():
    conn = sqlite3.connect('my_books.db')  # 데이터베이스 커넥션 생성
    cur = conn.cursor()  # 커서 확보
    insert_sql = 'INSERT INTO ml_class VALUES (?, ?, ?, ?, ?)'


    cur.execute(insert_sql, ('백경규', '1993.09.18', '경기도', '010-3386-6092', '비트 자율주행 시스템'))

    #cur.executemany(insert_sql, books)
    conn.commit()  # 데이터베이스 반영
    conn.close()  # 커넥션 닫기

Insert_Data()