import mysql.connector


def start():
    
    mydb = mysql.connector.connect(
        host='localhost', user='root', passwd='password')
    mycursor = mydb.cursor()

    mycursor.execute('SHOW DATABASES;')
    for db in mycursor:
        print(db)
    usedatabase = (input(str("Choose your Database or create one")))
    mydb = mysql.connector.connect(
        host='localhost', user='root', passwd='password', database=usedatabase)
    print(mydb)
    if (mydb):
        print('conection successful')
    else:
        print('conection unsuccessful')

    mycursor = mydb.cursor()

    mycursor.execute('SHOW TABLES;')
    print("Your tables: \n\n")
    for tb in mycursor:
        print(tb)


    while True:
        command = str(input("Enter commands now or input 'bye' to leave\n"))
        if command != 'bye':
            mycursor.execute(command)
            for tb in mycursor:
                print(tb)
        else:
            break
