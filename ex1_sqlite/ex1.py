import random
import sqlite3

PATH_TO_DB_FILE = 'test.db'
### data is from https://www.mockaroo.com/
BASE_DATA = [
        {"id": 1, "name": "Georgena Maken", "age": 25, "email": "gmaken0@parallels.com", "address": "02 Muir Way"},
        {"id": 2, "name": "Kirbee McCorry", "age": 36, "email": "kmccorry1@meetup.com", "address": "9091 Farmco Drive"},
        {"id": 3, "name": "Phyllida Sancto", "age": 47, "email": "psancto2@thetimes.co.uk", "address": "99202 Lerdahl Pass"},
        {"id": 4, "name": "Meghann Montilla", "age": 58, "email": "mmontilla3@cmu.edu", "address": "758 Clyde Gallagher Way"},
        {"id": 5, "name": "Cory Cridlon", "age": 14, "email": "ccridlon4@pagesperso-orange.fr", "address": "179 Sauthoff Trail" },
        {"id": 6, "name": "Bette-ann Kryska", "age": 21, "email": "bkryska5@behance.net","address": "74 Mallory Crossing"}
    ]


def create_table(conn):
    """
    Manage table creation.
    This method can be called on each execution of the app.
    'IF NOT EXISTS' is used to prevent errors if table exists.
    """
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS COMPANY (
            ID INT PRIMARY KEY     NOT NULL,
            NAME           TEXT    NOT NULL,
            AGE            INT     NOT NULL,
            EMAIL          CHAR(50) NOT NULL UNIQUE,
            ADDRESS        CHAR(50),
            SALARY         REAL
            );
        """)
    conn.commit()
    cur.close()


def insert_data(conn):
    """
    To insert data into company table using the BASE_DATA constant. 
    """
    cur = conn.cursor()
    for b_data in BASE_DATA:
        ### lets add a random float to the d_data dictionary.
        b_data.update({'salery': round(random.uniform(18000.00, 92000.00), 2)})
        cur.execute("""
            INSERT INTO COMPANY (ID, NAME, AGE, EMAIL, ADDRESS, SALARY)
             VALUES (:id, :name, :age, :email, :address, :salery);
             """, b_data)
        conn.commit()
    cur.close()


def report_data(conn):
    """
    Report on the data in the database before running anyting new.
    """
    cur = conn.cursor()
    cur.execute("select id, name, age, email, address, salary from company order by name asc;")
    row_count = 0
    for row_count, row in enumerate(cur):
        ### Sometimes it is good to prefix your fields so the vars don't conflit with any others.
        c_id, c_name, c_age, c_email, c_address, c_salary = row
        print(f"{c_id:>3}) {c_name[:20]:<20} {c_age:<3} {c_email[:20]:<20} {c_address[:20]:<20} ${c_salary:<10}")
    return row_count


def main():
    print("Starting application.")
    conn = sqlite3.connect(PATH_TO_DB_FILE)
    create_table(conn)
    row_count = report_data(conn)
    if not row_count:
        insert_data(conn)
    print("End of application.")


if __name__ == "__main__":
    main()

