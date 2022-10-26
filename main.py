import mysql.connector


if __name__ == "__main__":
    connect = mysql.connector.connect(host="5.183.188.132", user="db_vgu_student", password="thasrCt3pKYWAYcK", database="db_vgu_test")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM category")
    result = cursor.fetchall()
    for x in result:
        print(x)
    