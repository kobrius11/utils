import sqlite3


class DBControler():
    def __init__(self):
        self.__con = None

    def connect_db(self, dbname):
        self.__con = sqlite3.connect(dbname)
        return self
    
    def create_table(self, table_name, *cols):
        cols = ", ".join(*cols)
        self.__con.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({cols})")
        self.__con.commit()
        return self

    def insert(self, table_name, data):

        self.__con.execute(
            f"INSERT INTO {table_name} VALUES(?, ?)", data
        )
        self.__con.commit()
        return self
    
    def select(self, table_name, username):
        cursor = self.__con.cursor()
        res = cursor.execute(
        f"""
            SELECT
                password
            FROM {table_name}
            WHERE
                username = ?
        """, (username, ))
        return res

    def close(self):
        self.__con.close()
        return self