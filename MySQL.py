from mysql.connector import connect, Error

class Student:
  def __init__(self, sId, sName, birth, points):
    self.id = sId
    self.name = sName
    self.birthDate = birth
    self.totalPoints = points

  def toString(self):
    return "Student: " + str(self.id) + ", " + self.name + ", " + str(self.birthDate) + ", " + str(self.totalPoints)


def connectToDB(dbName):
  try:
    conn = connect(
      host="localhost",
      user="root",
      password="1234",
      database = dbName
    )
  except Error as err:
    print("Error message: " + err.msg)
    conn = None
  return conn

def connectWithConfig(fileName):
  try:
    conn = connect(option_files='config.cnf')
  except Error as err:
    print("Error message: " + err.msg)
    conn = None
  return conn

def createTable(conn, tableName):
  cursor = conn.cursor()
  sqlString = "create table " + tableName + "( id integer primary key,"
  sqlString += "name varchar(20));"

  cursor.execute(sqlString)

def createNewStudent(conn, st):
  sqlString = "insert into Students values(" + str(st.id) + ", '"
  sqlString += st.name + "', '" + st.birthDate + "', " + str(st.totalPoints) + ");"
  cursor = conn.cursor()
  cursor.execute(sqlString)
  conn.commit()

def findStudentByName(conn, sName):
  sqlString = "select * from Students where name = '" + sName + "';"
  cursor = conn.cursor()
  cursor.execute(sqlString)
  res = cursor.fetchmany(size = 1)
  if res == []:
    return None
  return Student(res[0][0], res[0][1], res[0][2], res[0][3])

##########################
conn = connectToDB("test")
#createNewStudent(conn, Student(222, 'Israel Levi', '2000-02-12', 8))
s = findStudentByName(conn, "Israel Levi")
print(s.toString())
conn.close()


#
# cursor = conn.cursor()
# # sqlString = "create table Emps( id integer primary key,"
# # sqlString += "name varchar(20));"
#
# #cursor.execute(sqlString)
# # cursor.execute("show tables;")
# # for x in cursor:
# #     print(x)
#
# # sqlString = "insert into emps (id, name) values"
# # sqlString += "(222, 'David'),"
# # sqlString += "(333, 'Moshe'),"
# # sqlString += "(444, 'Dafna');"
# # cursor.execute(sqlString);
# # conn.commit()
# # print('done')
# #
# sqlString = "select * from Emps;"
# cursor.execute(sqlString)
# rows = cursor.fetchall()
# for row in rows:
#   print(row)
# # for x in cursor:
# #     print(x)
#
# # headRows = cursor.fetchmany(size = 2)
# # remaining = cursor.fetchall()
# #
# # # print(cursor.column_names, cursor.rowcount, cursor.lastrowid)
# # print(remaining)