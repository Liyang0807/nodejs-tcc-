import mysql.connector
from mysql.connector import Error


try:
    connection = mysql.connector.connect(
        host='localhost',          
        database='Jo', 
        user='root',       
        password='') 

    sql = "INSERT INTO movies (TITLE) VALUES (%s);"
    new_data = ("Jack",)
    cursor = connection.cursor()
    cursor.execute(sql, new_data)


    connection.commit() 

except Error as e:
    print(e)

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        
