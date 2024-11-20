import psycopg2 as psy

def conexio():
    try:
            conn = psy.connect(
                database="postgres",
                user="user_postgres",
                password="pass_postgres",
                host="localhost",
                port="5432"
            )

            connection = conn.cursor()
            print(connection)
            return conn, connection

    except (Exception, psy.Error) as error:
        print("Error",error)
        return(None,None)
