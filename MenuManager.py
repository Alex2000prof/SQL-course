import psycopg2
from HW_WEEK4_DAY4 import MenuItem

USERNAME = 'postgres'
PASSWORD = '1739'
HOSTNAME = 'localhost'
PORTNAME = '5432'
DBNAME = 'HW_WEEK4_DAY4'

class MenuManager:
    @classmethod
    def get_by_name(cls, name_id):
        connection = psycopg2.connect(
            host=HOSTNAME,
            user=USERNAME,
            password=PASSWORD,
            port=PORTNAME,
            dbname=DBNAME
        )
        cursor = connection.cursor()
        try:
            cursor.execute('''
                SELECT * FROM Menu_Items WHERE name_id = %s
            ''', (name_id,))
            item = cursor.fetchone()
            if item:
                return {
                    'item_id': item[0],
                    'name_id': item[1],
                    'item_price': item[2]
                }
            return None
        finally:
            cursor.close()
            connection.close()
    
    @classmethod
    def all_items(cls):
        connection = psycopg2.connect(
            host=HOSTNAME,
            user=USERNAME,
            password=PASSWORD,
            port=PORTNAME,
            dbname=DBNAME
        )
        cursor = connection.cursor()
        try:
            cursor.execute('''
                SELECT * FROM Menu_Items
            ''')
            items = cursor.fetchall()
            return [
                {
                    'item_id': item[0],
                    'name_id': item[1],
                    'item_price': item[2]
                }
                for item in items
            ]
        finally:
            cursor.close()
            connection.close()



