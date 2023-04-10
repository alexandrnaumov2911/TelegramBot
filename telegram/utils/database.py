import sqlite3


def create_table():

    with sqlite3.connect('database.db') as connection:
        cur = connection.cursor()
        cur.execute(
            f""" 
                   CREATE TABLE IF NOT EXISTS user(
                   user_id INT PRIMARY KEY, 
                   chat_id INT,
                   username TEXT);   
               """
        )
        cur.execute(
            f""" 
                    CREATE TABLE IF NOT EXISTS user_message(
                    num INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INT,
                    message TEXT);
            """
        )
        connection.commit()
