import psycopg2

USERNAME = 'postgres'
PASSWORD = '1739'
HOSTNAME = 'localhost'
PORTNAME = '5432'
DBNAME = 'HW_WEEK4_DAY4'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, port=PORTNAME, dbname=DBNAME)
cursor = connection.cursor()

class MenuItem:
    def __init__(self, name_id, item_price=0, item_id=None):
        self.name_id = name_id
        self.item_price = item_price
        self.item_id = item_id

    def save(self):
        if self.item_id is None:
            cursor.execute('''
                INSERT INTO Menu_Items (name_id, item_price) VALUES (%s, %s) RETURNING item_id
            ''', (self.name_id, self.item_price))
            self.item_id = cursor.fetchone()[0]
        else:
            cursor.execute('''
                UPDATE Menu_Items SET name_id = %s, item_price = %s WHERE item_id = %s
            ''', (self.name_id, self.item_price, self.item_id))
        connection.commit()

    def delete(self):
        if self.item_id is None:
            raise ValueError("item_id is required")
        cursor.execute('''
            DELETE FROM Menu_Items WHERE item_id = %s
        ''', (self.item_id,))
        connection.commit()

    @staticmethod
    def update(item_id, name=None, price=None):
        if name is not None and price is not None:
            cursor.execute('''
                UPDATE Menu_Items SET name_id = %s, item_price = %s WHERE item_id = %s
            ''', (name, price, item_id))
        elif name is not None:
            cursor.execute('''
                UPDATE Menu_Items SET name_id = %s WHERE item_id = %s
            ''', (name, item_id))
        elif price is not None:
            cursor.execute('''
                UPDATE Menu_Items SET item_price = %s WHERE item_id = %s
            ''', (price, item_id))
        connection.commit()

    @staticmethod
    def close_connection():
        cursor.close()
        connection.close()









            
    






