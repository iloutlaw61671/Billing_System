
import sqlcmd
from tkinter import *
import mysql.connector
mydb = mysql.connector.connect(
    host='localhost', user='root', passwd='password',database = 'my_data')
mycursor = mydb.cursor()

total=0
print(mydb)
if (mydb):
    print('conection successful')
else:
    print('conection unsuccessful')

sqlcmd.start()


def display(results,i):
   
    i+=1
    print("displaying..")
    final=" NAME: {0} \n  ID: {1} \n COST: {2} \n  REVIEW(5): {3}".format(results[0],results[1],results[2],results[3])
     #getting my product deets
    resultlabel = Label(window, text = final, font=('calibre',10, 'bold'))
    resultlabel.grid(row=3,column=i)
    #totalfn(results[2])





    
    


def search():
    item=product.get()
    print(item)
    mycursor.execute('SELECT * FROM PRODUCT_INFO WHERE Item_name= "{0}"'.format(item))
    results=[]
    for i in mycursor:
        for j in i:
            results.append(j)
    print(results)
    search.var=results[2]
    display(results,2) 
   

 
def total_display():
    global total 
    total=total+search.var
    
    total_label = Label(window, text = str(total), font=('calibre',10, 'bold'))
    total_label.grid(row=1,column=5)

         

    


     




window=Tk()

window.geometry("600x300")

product=StringVar()
#totalfn()


search_label = Label(window, text = 'Search for an item', font=('calibre',10, 'bold'))
totlabel = Label(window, text = 'TOTAL', font=('calibre',10, 'bold'))


search_entry = Entry(window,textvariable = product, font=('calibre',10,'normal'))




btn=Button(window,text = 'Find', command = search)


addbtn=Button(window,text = 'ADD', command = total_display)

addbtn.grid(row=0,column=3)

search_label.grid(row=0,column=0)
search_entry.grid(row=1,column=0)
btn.grid(row=2,column=1)
totlabel.grid(row=0,column=5)


window.mainloop()
