import sqlite3

conn = sqlite3.connect('twitoff.sqlite3')
curs = conn.cursor()

def user_table_schema():
""" function to generate table schema"""
    create_table = """
        CREATE TABLE Users (
            user_id PRIMARY KEY,
            username TEXT,
        );
    """

    curs.execute(creat_table)
    curs.close()
    conn.commit()

def twit_table_schema():
    """ Generates table schema"""
    create_table = """
        CREATE TABLE Tweets (
            twit_id SERIAL PRIMARY KEY
            tweet VARCHAR(280)
        );
    """
    curs.execute(create_table)
    curs.close()
    conn.commit()

def insert_data(tablename, schema, data):
""" Inserts data in table"""
    insert = """
        INSERT INTO""" + str(tablename) 
        + str(schema) +
        """ VALUES""" + str(data[:]) + ';'

    curs.execute(insert)
    curs.close()
    conn.commit()


user_table_data =[
    ('user_1'),
    ('user_2'),
]


twit_table_data = [
    ('The Cowboys win! What a excellent game of football!'),
    ('Check out my new single: Beyond Me. Out in Stores Jan 1st'),
]
