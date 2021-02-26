import mysql.connector as mydb


def show_databases():
    '''
    This is a simple program that connects to mysql and executes sql "show databases" to list the databases.
    '''
    connector = mydb.connect(
        host='localhost',
        port='3306',
        user='', # Your team's user name
        password='', # Your team's password
        database=''
    )

    print('connected?: {}'.format(connector.is_connected()))
    cursor = connector.cursor()
    show_databases_sql = "show databases"
    cursor.execute(show_databases_sql)

    print('{}:'.format(show_databases_sql))
    for (show_databases_sql) in cursor:
        print(show_databases_sql[0])


if __name__ == '__main__':
    show_databases()
