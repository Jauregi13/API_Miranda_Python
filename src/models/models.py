from abc import ABC, abstractmethod
from ..utils.connectionMySQL import connection
import json
class Model(ABC):    

    @classmethod
    def list(cls,connection):

        cursor = connection.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM %s" %(cls.tableName))

        result = cursor.fetchall()

        return result
    
    @classmethod
    def view(cls,id,connection):

        cursor = connection.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM %s WHERE room_id=%s" %(cls.tableName,id))

        result = cursor.fetchone()

        return result

    @abstractmethod
    def create(self):

        connect = connection()
        cursor = connect.cursor(dictionary=True)
        columns = ','.join(column for column in self.fields.keys() if self.fields[column] != '')
        
        values = ','.join(
            "'{}'".format(json.dumps(value)) if isinstance(value,list) else 
           "'{}'".format(value) if isinstance(value,str) else str(value) for value in self.fields.values() if value != '')
        query = f'INSERT INTO %s (%s) VALUES (%s)' % (self.tableName,columns,values)

        cursor.execute(query)
        connect.commit()

        print(f'%s inserted succesfully' % (type(self).__name__))
    
    @abstractmethod
    def update(self):
        pass
    
    @classmethod
    def delete(cls):
        pass