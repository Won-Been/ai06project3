import os
import sqlite3
import scrap

DTABASE_PATH = os.path.join(os.getcwd(), 'book_data.db')

conn = sqlite3.connect(DTABASE_PATH)
cur = conn.cursor()

#테이블 만들기
creat_table = """
                CREATE TABLE Book (
                    ranking INTEGER PRIMARY KEY,
                    item_id INTEGER,
                    sales_point TEXT,
                    rating FLOAT,
                    genre TEXT
                );"""
drop_table_if_exists = 'DROP TABLE IF EXISTS Book;'


#실행
cur.execute(drop_table_if_exists)
cur.execute(creat_table)



bestseller_id = scrap.get_id() #베스트셀러 id리스트로 가져오기

ranking = 1 #순서대로 베스트셀러 순위 부여하기(맨 처음 나오는 책이 1위)
for ItemId in bestseller_id: #id에 해당하는 정보를 하나씩 넣기
    try:
        cur.execute(
            'INSERT INTO Book VALUES (?,?,?,?,?);',
            (ranking, ItemId, scrap.info(ItemId)[0], scrap.info(ItemId)[1], scrap.info(ItemId)[2])
        )
        ranking += 1
    except AttributeError: #'19세미만 구독불가'인 책은 제외하기
        continue

conn.commit()
cur.close()


