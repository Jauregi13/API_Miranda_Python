
import mysql.connector
from dotenv import dotenv_values



def connection():

    mydb = mysql.connector.connect(
        host=dotenv_values(".env")["HOST"],
        user=dotenv_values(".env")["USER"],
        password=dotenv_values(".env")["PASSWORD"],
        database=dotenv_values(".env")["DATABASE"]
    )

    return mydb