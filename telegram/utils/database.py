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
                CREATE TABLE IF NOT EXISTS messages_from_users(
                num INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INT,
                chat_id INT,
                message TEXT);
            """
        )

        cur.execute(
            f"""
                CREATE TABLE IF NOT EXISTS block_list(
                user_id INTEGER PRIMARY KEY,
                timestamp INTEGER,
                reason TEXT);
            """
        )

        cur.execute(
            f"""
                CREATE TABLE IF NOT EXISTS complaint_book(
                user_id INT,
                timestamp INT,
                username TEXT,
                reason TEXT);
            """
        )

        connection.commit()
