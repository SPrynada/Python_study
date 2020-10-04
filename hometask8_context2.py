import sqlite3

class DataConn:

    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):

        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):

        self.conn.close()
        if exc_val:
            raise


if __name__ == '__main__':
    db = 'lesson8.db'

    with DataConn(db) as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE parking SET car_price = car_price + 2000 WHERE id = 2')
        cursor.execute('SELECT car_model, car_price FROM parking')
        print(cursor.fetchall())