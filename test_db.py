import psycopg2

CONNECTION = "postgres://postgres:admin@localhost:5432/timeseries"

def main():
    conn = psycopg2.connect(CONNECTION)
    SQL = "INSERT INTO health(time, device_id, heartbeat, spo2) VALUES (now(), 'p1', %s, %s);"
    cursor = conn.cursor()

    try:
        data = (99, 99.9)
        cursor.execute(SQL, data)
    except (Exception, psycopg2.Error) as error:
        print(error.pgerror)

    conn.commit()

if __name__ == '__main__':
    main()