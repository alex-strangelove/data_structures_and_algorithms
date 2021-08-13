
import sqlite3

class  DBmanager:
    
    def create_connection(self, db_file):
    # """ create a database connection to the SQLite database
    #     specified by the db_file
    # :param db_file: database file
    # :return: Connection object or None
    # """
        self.db_file = db_file
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
        except Exception as e:
            print(e)

            return self.conn
        
    def run(self):
            self.conn = self.create_connection(self.database)
            print('run ok!')
            input('Please enter to finish...')        
    def __init__(self):
            self.database = "/home/sl/Development/computure_science/data_structures_and_algoritms/data_structures_and_algorithms/databases/ext2.db"
            self.run()
            pass
        
        





    















def main():
    DBmanager()
    



if __name__ == '__main__':
    main()