import mysql.connector #import mysql

################# Function #####################
def sh_dbs():
    mycursor.execute("SHOW DATABASES")
    print("=======================================")
    for x in mycursor:
        str1 = str(x)
        str1 = str(str1[2:len(str1) - 3])
        print("| " + str1)
    print("=======================================")
def sh_tb():
    mycursor.execute("SHOW TABLES")
    print("=======================================")
    for x in mycursor:
        str1 = str(x)
        str1 = str(str1[2:len(str1) - 3])
        print("| " + str1)
    print("=======================================")
def cr_tb():
 sh_dbs()
 namedb = input("Database name : ")
 nametb = input("Table name : ")
 table = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21']
 type = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21']
 max = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21']
 data = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']
 x = 1
 k = 0
 a = input("Number of columns created : ")
 s = 0
 h = 1
 a = int(a)
 if a > 20:
    print("Your input exceed max limit, Enter valid input")
    print()
    cr_tb()
 elif a > 0 < 20:
    while  x <= a:
        table[x] = input("Name Columns : ")
        def tp_menu():
          print("===========Choose type data===========\n"
              "|1. CHAR (Max : 255char.)\n"
              "|2. VARCHAR (Max : 255char.)\n"
              "|   Convert to Text if up to 255char.\n"
              "|3. LONG TEXT (Max : 4trillions)\n"
              "|4. INT (-2trillions - 2trillions)\n"
              "|5. FLOAT (small)\n"
              "|6. DOUBLE (large)\n"
              "|7. DECIMAL (double in string)\n"
              "======================================")
        tp_menu()
        inp = input("Type Data : ")
        if inp == '1':
            type[x] = "CHAR"
        elif inp == '2':
            type[x] = "VARCHAR"
        elif inp == '3':
            type[x] = "LONGTEXT"
        elif inp == '4':
            type[x] = "INT"
        elif inp == '5':
            type[x] = "FLOAT"
        elif inp == '6':
            type[x] = "DOUBLE"
        elif inp == '7':
            type[x] = "DECIMAL"
        else:
            print("Your input invalid, Enter valid input....")
            tp_menu()
        max[x] = input("Maximal input character : ")
        x += 1
        while k < x:
            if s < x:
                data[k]= table[s] +" "+ type[s] +"("+ max[s]+")"+ ", "
            while h < k:
                data[k] = data[k-1] + data[k]
                h += 1
            k += 1
            s += 1
 else:
     print("Your input invalid, Enter valid input")
     print()
     cr_tb()
 exa = ("CREATE TABLE "+namedb+"."+nametb+" ("+str(data[k-1][0:len(data[k-1])-2])+")")
 mycursor.execute(exa)
 print("Table", nametb,"Success Created...\n"
       "======================================")
def crt_dbs(name):
    crt_dbs = "CREATE DATABASE " + name
    mycursor.execute(crt_dbs)
def ch_dbs(dbs):
    ch_dbs = "USE " + dbs
    mycursor.execute(ch_dbs)
def dr_dbs(dbs):
    dr_dbs = "DROP DATABASE " + dbs
    mycursor.execute(dr_dbs)
    print("Database " + dbs + " has been successfully deleted")
def dr_tb(tb):
    dr_tb = "DROP TABLE " + tb
    mycursor.execute(dr_tb)
    print("Table " + tb + " has been successfully deleted")

def quest():
    question = input("Back to menu ? (Y/N) : ")
    print("=======================================")

    if (question == 'y') or (quest == 'Y'):
        menu()
    elif (question == 'n') or (quest == 'N'):
        out()
        exit()
    else:
        print("Sorry your input not valid !!")
        print("=======================================")
        print()
        quest()
def out():
    print()
    print("Thank for you because you use this Program :)")

#Menu Program
def menu():
    print()
    print("===================Menu Action Choose=================")
    print("|1. Show Databases.")
    print("|2. Show Tables.")
    print("|3. Create Database.")
    print("|4. Create Tables.")
    print("|5. Login Database more.")
    print("|6. Dalete Database.")
    print("|7. Dalete Table.")
    print("|8. Exit.")
    print("======================================================")
    put = input("what do you want to execute? (Choose Number) : ")

    # Condition Menu
    if put == '1':
        sh_dbs()
        quest()
    elif put == '2':
        sh_tb()
        quest()
    elif put == '3':
        namedb = input("Database Name : ")
        crt_dbs(namedb)
        sh_dbs()
        quest()
    elif put == '4':
        cr_tb()
        quest()
    elif put == '5':
        sh_dbs()
        namedb = input("Database Name for change Database : ")
        ch_dbs(namedb)
        print("You in Database %s" %namedb)
        quest()
    elif put == '6':
        sh_dbs()
        namedb = input("Database Name : ")
        dr_dbs(namedb)
        sh_dbs()
        quest()
    elif put == '7':
        sh_tb()
        nametb = input("Table Name for Deleted : ")
        dr_tb(nametb)
        sh_tb()
        quest()
    elif put == '8':
        out()
        exit()
    else:
        print("=======================================")
        print("your input is not find in Menu ")
        menu()

#Decription
def describ():
    print("================================================================\n"
          "|That Program Simple Mysql Control with Python. \n"
          "|That Program Only Control Your local Database with Server : \n"
          "|1. 127.0.0.1 \n"
          "|2. ::1 \n"
          "|3. localhost \n"
          "|Please enter your Server, Username and Password Database Correct \n"
          "=================================================================")

#Input Mysql Connector
describ()
print("\n")
print("============Login Databases============")
server = input("Server : ")
username = input("Username : ")
password = input("Password : ")
database = input("Database : ")
print("=======================================")

print(server,password,database)
#connector mysql in python
mydb = mysql.connector.connect(
  host = server,
  user = username,
  passwd = password,
  db = database
)
mycursor = mydb.cursor()
menu()
