import adodbapi

class Client():
    def __init__(self):
        self.connStr = """Provider=WinCCOLEDBProvider.1; Catalog=%s; Data Source=%s; uid='slider';pwd='slider'"""
    def connection(self, host, database):
        self.myConnStr = self.connStr % (database, host)#host=self.host, database
        self.myConn = adodbapi.connect(self.myConnStr)
    def query(self, **queryParams):
        self.cur  = self.myConn.cursor()
        self.cur.execute ("TAG:R,("+queryParams['tagId']+"), "+queryParams['dateStart']+","+queryParams['dateEnd'])
        return  self.cur.fetchall()
    def close(self):
        self.cur.close()
        self.myConn.close() 
    def unique(self, result):
        dictIdVal = {}
        for i in result:
            dictIdVal[i[0]] = i[2]
        return dictIdVal
