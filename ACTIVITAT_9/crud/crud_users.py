#lectura dels usuaris existents a la db
def readUsers(conn):
    connection = conn.cursor()
    connection.execute("select * from users;")
    conn.commit()
    users=connection.fetchall()
    return users