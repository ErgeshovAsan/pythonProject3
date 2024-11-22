import sqlite3


def create_table(db_name, create_table_sql):
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def insert_product(db_name, product):
    sql = '''INSERT INTO products(product_title, price, quantity)
    VALUES (?, ?, ?)'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, product)
    except sqlite3.Error as e:
        print(e)

def update_product_quantity(db_name, product):
    sql = '''UPDATE products SET quantity = ? where id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, product)
    except sqlite3.Error as e:
        print(e)

def update_product_price(db_name, product):
    sql = '''UPDATE products SET price = ? where id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, product)
    except sqlite3.Error as e:
        print(e)

def delete_product(db_name, id):
    sql = '''DELETE FROM products where id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (id,))
    except sqlite3.Error as e:
        print(e)

def select_all_product(db_name):
    sql = '''SELECT * FROM products'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)

def select_product_cheaper_and_more_limit(db_name, cheaper_and_more_limit):
    sql = '''SELECT * FROM products WHERE price <= ? AND quantity >= ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, cheaper_and_more_limit)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)

def select_product_product_title(db_name, product_title):
    sql = '''SELECT * FROM products WHERE product_title LIKE ? '''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            pattern = f'%{product_title}%'
            cursor.execute(sql, (pattern,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)

sql_to_create_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT(10,2) NOT NULL DEFAULT (0.0),
    quantity INTEGER NOT NULL DEFAULT (0)
)
'''

database_name = 'hw.db'
# insert_product(database_name, ('Liquid soap with the smell of vanilla', 55.5, 10))
# insert_product(database_name, ('Baby soap', 60, 12))
# insert_product(database_name, ('Liquid soap with the smell of rose', 57.9, 9))
# insert_product(database_name, ('A chocolate bar with nuts', 55, 10))
# insert_product(database_name, ('A chocolate bar with hazelnuts', 62, 13))
# insert_product(database_name, ('Chocolate bar with raisins', 60, 15))
# insert_product(database_name, ('Chocolate bar with caramel', 60.5, 15))
# insert_product(database_name, ('Chocolate bar with caramel', 56.5, 16))
# insert_product(database_name, ('Chocolate bar with strawberries', 70.5, 12))
# insert_product(database_name, ('Oatmeal cookies', 76, 10))
# insert_product(database_name, ('Chocolate cookies', 67, 11))
# insert_product(database_name, ('Strawberry cookies', 74.8, 11))
# insert_product(database_name, ('Vanilla-scented shampoo', 60.7, 10))
# insert_product(database_name, ('Shampoo with the smell of a tulip', 57.5, 20))
# insert_product(database_name, ('Baby shampoo', 55.5, 20))

# update_product_quantity(database_name, (16, 3))
# update_product_price(database_name, (66, 5))
# delete_product(database_name, 6)
# select_all_product(database_name)
# select_product_cheaper_and_more_limit(database_name, (65, 13))
select_product_product_title(database_name, 'soap')