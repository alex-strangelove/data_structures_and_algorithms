import sqlite3

def create_new_table(conn, table_name):
    pass


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)

    return conn


def delete_task(conn, id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = 'DELETE FROM tasks WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id))
    conn.commit()
    return
    


def delete_all_tasks(conn):
    """
    Delete all rows in the tasks table
    :param conn: Connection to the SQLite database
    :return:
    """
    sql = 'DELETE FROM tasks'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return

# Something wrong here below: 
def print_table_all(conn):
    get_db_list = []
    cur = conn.cursor()
    db_list_all = cur.execute("SELECT * FROM tasks;").fetchall() 
    for db in db_list_all:
        get_db_list.append(db)
        print(db)
        # return list(get_db_list)

def add_task(conn, new_id):
    new_id = "\'" +  new_id + "\'"
    sql = "insert into tasks values({new_id});".format(new_id=new_id)
    print(sql)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    print('Database successfully updated!')
    return
    


def main():
    database = "/home/sl/Development/computure_science/data_structures_and_algoritms/data_structures_and_algorithms/databases/ext2.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("""\n
              Welcome to database ext2.db\n
              list of tables: tasks\n
              Avaiable options: \n
              1. Create new table\n
              2. Add value to tasks\n
              3. Delete value from tasks\n
              4. NB! Delete all info from tasks!\n
              5. Print table tasks\n
              6. Exit\n
              """)
        usr_in = input('Please enter number of next step: ')
        if usr_in == '1':
            pass
        elif usr_in == '2':
            print('Please enter value to database')
            usr_in = input('Value: ')
            add_task(conn, usr_in)
            conn.close()
            input('DB updated!\npress enter to continue...')
            main()
        elif usr_in == '3':
            pass
        elif usr_in == '4':
            pass
        elif usr_in == '5':
            print_table_all(conn)
            input('Press enter to continue...')
            main()
        elif usr_in == '6':
            print('Good Bye!...')
            return
        else:
            conn.close()
            input('Wrong selection\nTry again!\nPress enter to continue...')
            main()
        
        
        # name = "Boroda"
        # add_task(conn, name )
        # print_table_all(conn)
        # delete_task(conn, 2);
        # delete_all_tasks(conn);


if __name__ == '__main__':
    main()