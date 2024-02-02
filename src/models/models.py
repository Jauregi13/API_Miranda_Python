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
        
        cursor.execute("SELECT * FROM %s WHERE id=%s" %(cls.tableName,id))

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

        connect = connection()
        cursor = connect.cursor(dictionary=True)
        values = ','.join(f"{key} = '{value}'" if isinstance(value,str) else 
        f"{key} = '{json.dumps(value)}'" if isinstance(value,list) else f"{key} = {value}"
        for key,value in self.fields.items() if value)

        id = list(self.fields.keys())[0]
        where_clause = f"%s = '%s'" % (id,self.fields[id])

        query = f'UPDATE %s SET %s WHERE %s' % (self.tableName, values,where_clause)
        print(query)
        cursor.execute(query)
        connect.commit()

        print(f'%s updated succesfully' % (type(self).__name__))
    
    @classmethod
    def delete(cls,id):

        connect = connection()
        cursor = connect.cursor(dictionary=True)

        query = f'DELETE FROM %s WHERE id = %s' % (cls.tableName,id)
        cursor.execute(query)
        connect.commit()
        print(f'%s deleted succesfully' % (cls.__name__))