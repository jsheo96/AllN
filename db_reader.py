import sqlite3

class DBReader():
    def __init__(self, db_name='news.db'):
        self.db_name = db_name
        self.con = sqlite3.connect(self.db_name)
        self.cursor = self.con.cursor()

    def get(self): # get all news in database
        self.cursor.execute('SELECT * FROM news')
        result = self.cursor.fetchall()
        return result

if __name__ == "__main__":
    db_reader = DBReader()
    news_list = db_reader.get()
    print(news_list[0])