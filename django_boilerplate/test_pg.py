import psycopg2

try:
    conn = psycopg2.connect(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        password='Siva@12345',
        dbname='postgres'
    )
    print("CONNECTED SUCCESSFULLY")
    conn.close()
except Exception as e:
    print("ERROR:", e)
