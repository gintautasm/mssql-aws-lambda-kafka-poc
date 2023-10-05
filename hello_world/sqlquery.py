import pymssql
from time import time
import json

SQL_QUERY = """
SELECT [BusinessEntityID]
      ,[PasswordHash]
      ,[PasswordSalt]
      ,[rowguid]
      ,[ModifiedDate]
  FROM [AdventureWorks2017].[Person].[Password]
"""

def listToProcess():
    t1 = time()

    conn = pymssql.connect(
        #server='host.docker.internal',
        server='mssql-db',
        user='sa',
        password='yourStrong(!)Password',
        database='AdventureWorks2017',
        as_dict=True
    )

    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)

    records = cursor.fetchall()

    t2 = time()
    print(f'Function executed in {(t2-t1):.4f}s')

    return records

#listToProcess()1


