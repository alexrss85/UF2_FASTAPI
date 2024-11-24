import psycopg2 as psy

#conexió a la db
def conexio():
    try:
            conn = psy.connect(
                database="postgres",
                user="user_postgres",
                password="pass_postgres",
                host="localhost",
                port="5432"
            )

            conection = conn.cursor()
            return conn

    except (Exception, psy.Error) as error:
        print("Error",error)
        return(None,None)
