from abc import ABC, abstractmethod
import mysql.connector
from dotenv import dotenv_values
from decimal import Decimal

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
        print(self.status)
    
    @abstractmethod
    def update(self):
        pass
    
    @classmethod
    def delete(cls):
        pass