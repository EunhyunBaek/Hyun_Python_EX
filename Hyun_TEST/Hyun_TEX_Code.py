import json
import sqlite3

class Student_InFo:
    NUMBER_OF_PEOPLE = 15
    ZERO_COUNT = 0
    MINUS_FLAGS=-1
    Info = list()
    def Set_Info_Data(self):

        while(Student_InFo.NUMBER_OF_PEOPLE>Student_InFo.ZERO_COUNT):
            name = input("이름")
            first_result    = input("First_Result")
            second_result   = input("Second_Result")
            third_result    = input("Third_Result")
            total_result    = int(first_result)+int(second_result)+int(third_result)
            average_result  = int(total_result)/3

            Student_InFo.Info.append([
                                        name,
                                        int(first_result),
                                        int(second_result),
                                        int(third_result),
                                        int(total_result),
                                        float(average_result)
            ])
            Student_InFo.NUMBER_OF_PEOPLE-=1

    def Get_Info_Data(self):
        if(len(Student_InFo.Info)>Student_InFo.ZERO_COUNT):
            for b in Student_InFo.Info:
                print(b)
        else:
            print("Data가 존재하지 않습니다.")

    def Set_Json_Data(self):
        with open('data.json', 'w') as f:
            json.dump(Student_InFo.Info, f, ensure_ascii=False)

    def Get_Json_Data(self):
        with open('data.json') as data_file:
            Student_InFo.Info = json.load(data_file)
            for list_of_json_data in Student_InFo.Info:
                print(list_of_json_data)

    def Create_DataBase(self):
        # my_books 테이블 생성
        conn = sqlite3.connect('Student_Info.db')  # 데이터베이스 커넥션 생성
        conn.execute('''CREATE TABLE if not exists Student_Info (
                                       Name text,
                                       First_Result integer,
                                       Second_Result integer,
                                       Third_Result integer,
                                       Total_Result integer,
                                       Average_Result float
                               )'''
                    )

    def Set_DataBase_Data(self):
        for list_of_data in Student_InFo.Info:
            conn = sqlite3.connect('Student_Info.db')  # 데이터베이스 커넥션 생성
            sql = "INSERT INTO Student_Info VALUES (?, ?, ?, ?, ?, ?)"
            #sql = "INSERT INTO Student_Info (Name,First_Result,Second_Result,Third_Result,Total_Result,Average_Result)VALUES (?, ?, ?, ?, (First_Result + Second_Result+Third_Result),(First_Result1 + Second_Result+Third_Result)/3.0)"
            print(list_of_data)
            print(sql)
            conn.execute(sql,list_of_data)
            conn.commit()  # 데이터베이스 반영
            conn.close()  # 커넥션 닫기


    def Get_People_Data(self):
        conn = sqlite3.connect('Student_Info.db')  # 데이터베이스 커넥션 생성
        cur = conn.cursor()
        name=input("검색할 사람 이름:")
        sql = "select name, (First_Result + Second_Result + Third_Result)/ 3.0 as avg, (First_Result + Second_Result + Third_Result) as sum from Student_Info where name = "+ "'%s'"%name
        print(sql)
        cur.execute(sql)
        score = cur.fetchone()  # 조회한 데이터 불러오기
        print(score)
        conn.commit()  # 데이터베이스 반영
        conn.close()  # 커넥션 닫기

sinfo=Student_InFo

sinfo.Set_Info_Data(0)
sinfo.Get_Info_Data(0)
sinfo.Set_Json_Data(0)
sinfo.Get_Json_Data(0)
sinfo.Create_DataBase(0)
sinfo.Set_DataBase_Data(0)
sinfo.Get_People_Data(0)