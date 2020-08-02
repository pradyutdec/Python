import ibm_db


def open_connection():
    global dsnStr
    global connection
    global file
    global conn
    conn = ibm_db.connect("DATABASE=DOSPRD01;HOSTNAME=basimrprddatl01.xchanginghosting.com;PORT=60006;PROTOCOL=TCPIP;UID=goelanik;PWD=M4us$m@123;", "", "")
    if conn:
        print("DB2 Connection Build")


def close_connection():
    ibm_db.close(conn)


def process_umr():

    umr = 'B1294P14B295517P'

    umr_querystring = "SELECT hex(OBJECT_ID), U2BF8_UMR, UD768_INSURED, U71B8_REINSURED, " \
                      " U2908_CURRENTBROKERCODE, U34C3_POLICYINCEPTIONDATEFROM, " \
                      " UCC33_POLICYINCEPTIONDATETO FROM DOS.GENERIC " \
                      " WHERE object_class_id = x'523974d000001acbb246231ec63cdb55' " \
                      " and lower(U2BF8_UMR) = lower('" + umr + "')"

    stmt = ibm_db.exec_immediate(conn, umr_querystring)
    result = ibm_db.fetch_tuple(stmt)
    loop = 1
    while result and loop == 1:
        umr = result[1]
        umr_sid = "x'" + str(result[0]) + "'"
        loop = 0
        print(umr, " processing started with UMR SID as ", umr_sid)


def list_of_umr():
    process_umr()


def main():
    print("Program Started")

    open_connection()
    list_of_umr()
    close_connection()


if __name__ == '__main__':
    main()