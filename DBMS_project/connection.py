import psycopg2

conn = psycopg2.connect(
    database="DBMS", user='postgres', password='Bruce@1045', host='127.0.0.1', port= '5432'
    )
