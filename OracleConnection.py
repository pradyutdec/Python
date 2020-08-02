import cx_Oracle

def open_connection():
    global dsnStra
    global connection
    global file

    dsnStr = cx_Oracle.makedsn("10.5.148.17", "1521", "IMRPRDCP")
    connection = cx_Oracle.connect(user="GOELA", password="Ocean7##", dsn=dsnStr, threaded=True)

    if connection:
        print("Oracle Connection Build")


def close_connection():
    connection.close()


def process_umr():

    umr = 'B1294P14B295517P'
    cursor_UMR = connection.cursor()
    umr_querystring = "SELECT CREATED_TIME, NAME, SID FROM IMANAGE.WKS_WORKSPACE WHERE NAME = '" + umr + "'"
    cursor_UMR.execute(umr_querystring)
    umr_all_result = cursor_UMR.fetchall()
    for umr_result in umr_all_result:
        umr = umr_result[1]
        umr_sid = umr_result[2]
        print(umr, " processing started with SID id as ", umr_sid)


def list_of_umr():
        process_umr()


def main():
    print("Program Started")
    open_connection()
    list_of_umr()
    close_connection()


if __name__ == '__main__':
    main()