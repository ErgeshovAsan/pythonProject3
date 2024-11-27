import sqlite3


def create_table(db_name, create_table_sql):
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def insert_countries(db_name, countries):
    sql = '''INSERT INTO countries (title)
    VALUES (?)'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (countries,))
    except sqlite3.Error as e:
        print(e)


sql_to_create_countries_table = '''
CREATE TABLE countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(200) NOT NULL
)
'''

def insert_cities(db_name, cities):
    sql = '''INSERT INTO cities (title, area, country_id)
    VALUES (?, ?, ?)'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, cities)
    except sqlite3.Error as e:
        print(e)

sql_to_create_cities_table = '''
CREATE TABLE cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(200) NOT NULL,
    area FLOAT(10) NOT NULL DEFAULT (0),
    country_id INTEGER,
    FOREIGN KEY (country_id) REFERENCES countries (id)
    
)
'''

def insert_students(db_name, students):
    sql = '''INSERT INTO students (first_name, last_name, city_id)
    VALUES (?, ?, ?)'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, students)
    except sqlite3.Error as e:
        print(e)

sql_to_create_students_table = '''
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(200) NOT NULL,
    last_name VARCHAR(200) NOT NULL,
    city_id INTEGER,
    FOREIGN KEY (city_id) REFERENCES cities (id)
)
'''
def select_all_cities(db_name):
    sql = '''SELECT id, title FROM cities'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(e)

def select_all_students(db_name, city_id):
    sql = '''SELECT s.first_name, s.last_name, ct.title as country, c.title as citie, c.area 
    FROM students as s
    JOIN cities as c ON s.city_id = c.id
    JOIN countries as ct ON c.country_id = ct.id
    WHERE s.city_id = ?
    '''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (city_id,))
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(e)

def main():
    database_name = 'hw.db'

    while True:
        print('Вы можете отобразить список учеников по выбранному id города '
              'из перечня городов ниже, для выхода из программы введите 0:')

        cities = select_all_cities(database_name)
        if not cities:
            print("Не удалось загрузить список городов.")
            break
        for city in cities:
            print(f'{city[0]}. {city[1]}')

        city_id = int(input('\nВведите id города: '))
        if city_id == 0:
            print('Выход из программы.')
            break

        students = select_all_students(database_name, city_id)

        for student in students:
            print(f'Имя: {student[0]}, Фамилия: {student[1]}, '
                    f'Страна:: {student[2]}, Город: {student[3]}, Площадь: {student[4]}')


if __name__ == '__main__':
    main()


# create_table(database_name, sql_to_create_countries_table)
# insert_countries(database_name, 'Amerika')
# insert_countries(database_name, 'Russia')
# insert_countries(database_name, 'England')

# create_table(database_name, sql_to_create_cities_table)
# insert_cities(database_name, ('Moscow', 2560, 2))
# insert_cities(database_name, ('Saint-Petersburg', 2050, 2))
# insert_cities(database_name, ('Volgograd', 2050, 2))
# insert_cities(database_name, ('London', 2050, 3))
# insert_cities(database_name, ('Leeds', 2050, 3))
# insert_cities(database_name, ('Chicago', 2050, 1))
# insert_cities(database_name, ('Phoenix', 2050, 1))

# create_table(database_name, sql_to_create_students_table)
# insert_students(database_name, ('John', 'Doe', 1))
# insert_students(database_name, ('Jane', 'Smith', 2))
# insert_students(database_name, ('Alice', 'Johnson', 3))
# insert_students(database_name, ('Bob', 'Brown', 3))
# insert_students(database_name, ('Charlie', 'Williams', 2))
# insert_students(database_name, ('Daisy', 'Jones', 1))
# insert_students(database_name, ('Ella', 'Taylor', 3))
# insert_students(database_name, ('Frank', 'Anderson', 4))
# insert_students(database_name, ('Grace', 'Thomas', 5))
# insert_students(database_name, ('Harry', 'Harris', 6))
# insert_students(database_name, ('Isla', 'Martin', 7))
# insert_students(database_name, ('Jack', 'Thompson', 6))
# insert_students(database_name, ('Kara', 'Garcia', 7))
# insert_students(database_name, ('Leo', 'Martinez', 7))
# insert_students(database_name, ('Mia', 'Robinson', 1))
