import mysql.connector as mydb


def show_databases():
    # コネクションの作成
    connector = mydb.connect(
        host='localhost',
        port='3306',
        user='root',
        password='',
        database=''
    )

    print('connected??: {}'.format(connector.is_connected()))
    cursor = connector.cursor()
    show_databases_sql = "show databases"
    cursor.execute(show_databases_sql)
    for (show_databases_sql) in cursor:
        print(show_databases_sql[0])


if __name__ == "__main__":
    show_databases()
