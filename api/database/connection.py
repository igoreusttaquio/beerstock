import sqlite3

class Connection(object):
    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()
    

    def find(self, query, params=(), get_result=False):
        resultset = None
        if params:
            resultset = self.cursor.execute(query, params)
        else:
            resultset = self.cursor.execute(query)
        
        if get_result:
            return resultset.fetchone()
        else:
            resultset = None
            return resultset
    

    def find_all(self, query, params=()):
        resultset = None
        if params:
            resultset = self.cursor.execute(query, params)
        else:
            resultset = self.cursor.execute(query)
        
        if resultset:
            return resultset.fetchall()
        else:
            return None


    def create(self, query,params=()):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return True


    def insert(self, query,params=()):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return True
    

    def update(self, query,params=(), get_result=False):
        resultset = None
        if params:
            resultset = self.cursor.execute(query, params)
        else:
            resultset = self.cursor.execute(query)
        
        if get_result:
            return resultset
        else:
            resultset = None
            return resultset


    def delete(self, query, params=()):
        if params: 
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return True


    def close(self):
        self.connection.close()
        self.cursor = None

    
    def commit(self):
        self.connection.commit()


    def rollback(self):
        self.connection.rollback()