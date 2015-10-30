import cx_Oracle
def create_connection():
    return cx_Oracle.Connection('T702556/T702556@10.123.79.60/georli05')

def create_cursor(con):
    return cx_Oracle.Cursor(con)
