import sqlite3

def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection


def create_table(db_name, create_table_sql):
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)


def insert_categories(db_name, categories):
    sql = '''INSERT INTO categories (code, title)
    VALUES (?, ?)'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, categories)
    except sqlite3.Error as e:
        print(e)


sql_to_create_categories_table = '''
CREATE TABLE categories (
    code VARCHAR(2) PRIMARY KEY,
    title VARCHAR(150) NOT NULL
)
'''


def insert_products(db_name, products):
    sql = '''INSERT INTO products (title, category_code, unit_price, stock_quantity, store_id)
    VALUES (?, ?, ?, ?, ?)'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, products)
    except sqlite3.Error as e:
        print(e)


sql_to_create_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(250) NOT NULL,
    category_code INTEGER,
    unit_price FLOAT NOT NULL DEFAULT 0,
    stock_quantity INTEGER NOT NULL,
    store_id INTEGER,
    FOREIGN KEY (category_code) REFERENCES categories (code),
    FOREIGN KEY (store_id) REFERENCES store (store_id)
)
'''


def insert_store(db_name, store):
    sql = '''INSERT INTO store (title)
    VALUES (?)'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (store,))
    except sqlite3.Error as e:
        print(e)


sql_to_create_store_table = '''
CREATE TABLE store (
    store_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL
)
'''


def select_all_store(db_name):
    sql = '''SELECT store_id, title FROM store'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(e)


def select_all_products(db_name, store_id):
    sql = '''SELECT p.title, c.code, p.unit_price, p.stock_quantity
    FROM products as p
    JOIN categories as c ON p.category_code = c.code
    WHERE p.store_id = ?
    '''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (store_id,))
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(e)


def main():
    database_name = 'Dop_lesson.db'

    while True:
        print('Вы можете отобразить список продуктов по выбранному id магазина '
              'из перечня магазинов ниже, для выхода из программы введите цифру 0:')

        stores = select_all_store(database_name)
        for store in stores:
            print(f'{store[0]}. {store[1]}')

        store_id = int(input("Введите id магазина или 0 для выхода: "))
        if store_id == 0:
            print("Выход из программы.")
            break

        products = select_all_products(database_name, store_id)

        for product in products:
            print(f"Название продукта: {product[0]}, Категория: {product[1]}, Цена: {product[2]}, Количество на складе: {product[3]}")


if __name__ == '__main__':
    main()
# database_name = 'Dop_lesson.db'
# my_connection = create_connection(database_name)
# if my_connection is not None:
#     print('Successfully connected to database')


# create_table(database_name, sql_to_create_categories_table)
# insert_categories(database_name, ('FD', 'Food product'))
# insert_categories(database_name, ('EL', 'Electronig'))
# insert_categories(database_name, ('CL', 'Clothes'))
# # create_table(database_name, sql_to_create_products_table)
# insert_products(database_name, ('Chocolet', 'FD', 10.5, 129, 1))
# insert_products(database_name, ('Jins', 'CL', 120.0, 55, 2))
# insert_products(database_name, ('T-shirt', 'CL', 0.0, 15, 1))
# # create_table(database_name, sql_to_create_store_table)
# insert_store(database_name, 'Asia')
# insert_store(database_name, 'Globus')
# insert_store(database_name, 'Spar')
