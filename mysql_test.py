import MySQLdb


def show_databases():
    connector = MySQLdb.connect(
            user='root',
            passwd='',
            host='localhost',
            db='')

    cursor = connector.cursor()
    show_databases_sql = "show databases"
    cursor.execute(show_databases_sql)
    for (show_databases_sql) in cursor:
        print(show_databases_sql[0])


if __name__ == "__main__":
    show_databases()
