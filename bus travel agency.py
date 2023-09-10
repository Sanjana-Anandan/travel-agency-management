import mysql.connector as sql
from datetime import datetime

conn=sql.connect (host='localhost',user='root', password='passwOrd',database='travel_booking')
cl=conn.cursor ()
conn.autocommit==True
if conn.is_connected():
    print("connected successfully")
else:
    print("not connected")

def login_info():
    ans=True
    while ans:
        a=input("Do you want to login? (yes/no):")
        if a=='no' or a=='NO' or a=='No':
            print("************REDIRECTING TO MAIN MENU************")
            print("\n")
            ans=False

        elif a=='yes' or a=='YES' or a=='Yes':
            a=int (input ('Enter your phone number: '))
            u=("select name from accounts where Phone_number="+str(a)+";")
            cl.execute(u)
            datan=cl.fetchall()
            s=cl.rowcount
            s=abs(s)
            if s!=1:
                print("************ERROR: ACCOUNT DOESNT EXIST************")
                ans=False
            else:
                datan=datan[0]
                datan=list(datan)
                datan=datan[0]
                datan=str(datan)
                y="select password from accounts where Phone_number=({})".format(a)
                cl.execute(y)
                data=cl.fetchall()
                data=data[0]
                data=list(data)
                data=data[0]
                b=int(input("Enter your password: "))

                if b==data:
                    print("LOGGED IN!")
                    print("HI",datan,"!!")
                    print("How can I help you? ")
                    print("\n")

                    ans=True
                    while ans:
                        print('''      MENU:
        press 11 to book for boarding
        press 12 for bill verification
        press 13 for travel log
        press 14 to exit''')
                        ch=int(input("Enter your choice (11/12/13/14): "))

                        if ch==14:
                            print("************LOGGED OUT************")
                            print('\n')
                            ans=False

                        elif ch==11:
                            your_location=input ("Your_location: ")
                            your_destination=input ("Your_destination: ")
                            ampm=input("Enter am/pm: ")
                            if (ampm!='am') and (ampm != 'pm'):
                                print("invalid input")
                            time =input ("time to start board:  ")
                            print("travel time: ",time+ampm)
                            urgency=input ("urgency (yes/no): ")
                            import datetime
                            while (1):
                                trav_date=input("date of travel: (YYYY/MM/DD): ")
                                d1 = datetime.datetime.strptime(trav_date, "%Y/%m/%d")
                                d2 = datetime.datetime.now()
                                if d2>d1:
                                    print("INVALID INPUT")
                                    continue
                                else:
                                    break

                            cl.execute ("insert into customer_bookings values (" + str(a) +",' " +your_location + " ' ,' "+your_destination+ " ' ,' "+time+ " ' ,' "+urgency+" ',' "+today+" ',' "+trav_date+" ') ")
                            print("************AT YOUR SERVICE AT ", time+ampm, "************")
                            print('\n')
                            continue


                        elif ch==12:
                            Dist=int (input ('distance travelled [in kms]='))
                            bill=Dist*5
                            print ('your payment : Rs.',bill)
                            print('\n')
                            continue

                        elif ch==13:
                            cl.execute ("select your_location, your_destination, time, urgency, trav_date from customer_bookings where phone_number like '"+str(a)+"';")
                            data=cl.fetchall()
                            for row in data:
                                cur_time()
                                print('location\t',"destination\t","time\t\t","urgency\t","travel date")
                                print (row[0],'\t',row[1],'\t',row[2],'\t',row[3],'\t',row[4])
                            conn.commit ()
                            print('\n')
                            continue

                        else:
                            print("************INVALID CHOICE************")
                            print('\n')
                            ans=False

                else:
                    print("************INVALID PASSWORD************")
                    print('\n')
        else:
            print("************INVALID CHOICE************")
            print('\n')


def create_acc():
    ans=True
    while ans:
        phone_number=int (input ('Phone Number: '))
        name=str (input ("Name: "))
        print("Enter a numeric password")
        password =str (input ( 'password[10]: '))
        cl.execute ("insert into accounts (Phone_number, password, name ) values (" +str (phone_number) +",' " +password + "',' "+name+" ')")
        conn.commit ()
        print ("************ACCOUNT SUCCESSFULLY CREATED************")
        print('\n')
        ans=False


def del_acc():
    ans=True
    while ans:
        phone_number=int (input ("enter your phone_number: "))
        y="select password from accounts where Phone_number=({})".format(phone_number)
        cl.execute(y)
        data=cl.fetchall()
        data=data[0]
        data=list(data)
        data=data[0]
        b=int(input("Enter your password: "))
        if b==data:
            cl.execute ("delete from customer_bookings where phone_number ="+str (phone_number)+";")
            cl.execute ("delete from accounts where phone_number ="+str (phone_number)+";")
            conn.commit ()
            print ("************ACCOUNT DELETED SUCCESSFULLY************")
            print('\n')
            ans=False
        else:
            print("************INVALID PASSWORD************")
            print("\n")
            ans=False

def cur_time():
    now=datetime.now().strftime('%H:%M:%S')
    now1=datetime.now().strftime('%Y-%m-%d')
    print("BOOKING DATE: ",now1)
    print("BOOKING TIME: ",now)

def main_loop():
   while True:
        print (" 12A TRAVEL AGENCY ")
        print('''      MENU:
        Press 1 to Login
        Press 2 Create account
        press 3 delete account
        Press 4 to Exit''')
        ch=int (input ('Enter your choice(1/2/3/4): '))
        if ch ==1:
            login_info()
            import atexit
            atexit.register(main_loop)
        elif ch==2:
            create_acc()
            import atexit
            atexit.register(main_loop)
        elif ch==3:
            del_acc()
            import atexit
            atexit.register(main_loop)
        elif ch==4:
            print("************THANK YOU, VISIT AGAIN!!************")
            import sys
            sys.exit()
        else:
            print("INVALID INPUT")
            print('\n')

from time import gmtime, strftime
n=strftime("%a, %d %b %Y", gmtime())
n=str(n)
print(n)
print('\n')
today=n[5:]

main_loop()






