class ContextManager:
    def __init__(self):
        print('init method called')
        
    def __enter__(self):    
        print("enter method")
        return self
    
    def __exit__(self,exc_type,exc_value,exc_traceback):
        print('exit method')
        
with ContextManager():
    print("ggggggg")      

# File management using context Manager   
class FileManager():
    def __init__(self ,filename,mode):
        self.filename =filename
        self.mode=mode
        self.file=None
        
    def __enter__(self):
        self.file=open(self.filename,self.mode)
        return self.file
    
    def __exit__(self,exc_type,exc_value,exc_traceback):
        self.file.close()
with FileManager('test.txt','w') as f:
    f.write('Test')
print(f.closed)             

#Database management using Context Manager
"""
import config
import MySQLdb
import MySQLdb.cursors as mc
import _mysql_exceptions
import contextlib 
DictCursor =mc.DictCursor
SSCursor = mc.SSCursor
SSDictCursor =mc.SSDictCursor
Cursor =mc.Cursor


@contextlib.contextmanager
def connection(cursorclass=Cursor,host= config.HOST,user=config.USER,passwd=config.PASS,dbname=config.MYDB,driver=MySQLdb):
    connection=driver.connect(host=host,user=user,passwd=passwd,db=dbname,cursorclass=cursorclass)
    
    try:
        yield connection
    except Exception:
        connection.rollback()
        raise
    else:
        connection.commit()
    finally:
        connection.close()     
@contextlib.contextmanager
def cursor(cursorclass=Cursor,host= config.HOST,user=config.USER,passwd=config.PASS,dbname=config.MYDB,driver=MySQLdb):
    with connection(host,user,passwd,dbname,cursorclass) as conn:
        cursor=conn.cursor()
        try:
            yield cursor
        finally:
            cursor.close()
           
with cursor(SSDictCursor) as cur:
    print(cur)
    connection = cur.connection
    print(connection)
    sql='select* from table'
    cur.execute(sql)
    for row in cur:
        print(row)                
               
        
"""
    
# multiprocessing and Multi threading
import time
import threading
import multiprocessing
def tell(seconds):
    print(f"Starting function for {seconds} seconds.")
    time.sleep(seconds)
    print(f"Function completed after {seconds} seconds.")
def run():
    threads = []
    for duration in [4, 6, 9]:
        t = threading.Thread(target=tell, args=(duration,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
def walk():
    processes = []
    for duration in [3, 5, 2]:
        p = multiprocessing.Process(target=tell, args=(duration,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
print("Running with multithreading:")
run()
print("\nRunning with multiprocessing:")
walk()
        
    
        
    