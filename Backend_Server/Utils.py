import pyodbc as pdb
import json
import random

### Connect to SQL Server database ###
# Connect to SQL Server database info
SERVER = 'DUYNGUYEN\SQLEXPRESS'
DATABASE = 'Project'
USERNAME = 'sa'
PASSWORD = '123456'

# Connection string
connectionString = f'''
DRIVER={{ODBC Driver 18 for SQL Server}};
SERVER={SERVER};DATABASE={DATABASE};
UID={USERNAME};
PWD={PASSWORD};
Encrypt=no;
'''

# Connect to SQL Server
conn = pdb.connect(connectionString)

def generate_random_Exam(subject = '%', question_number = 10):
    query_question = f"""
    SELECT TOP {question_number} * FROM Question
    WHERE subject LIKE '{subject}'
    ORDER BY NEWID()
    """
    cursor = conn.cursor()
    cursor.execute(query_question)
    records = cursor.fetchall()
    print(records)

# Test
if __name__ == '__main__':
    generate_random_Exam(subject='Medicine', question_number=20)
