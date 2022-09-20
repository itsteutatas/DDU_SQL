import mysql.connector
from tkinter import *

# This is def vulnerable to SQLi but oh well

localConfig = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'landlysthoteldb'
}

cn = mysql.connector.connect(**localConfig)
print(cn)
cr = cn.cursor()

# Variables for the SQL statements. Will be changed at their respective functions
roomID = 0
emailID = 0
contactID = 0
guestID = 0
fname = ""
lname = ""
zipcode = 0
address = ""
phone = 0
email = ""
start_date = ""
end_date = ""

# SQL STATEMENT DECLARATIONS
freeRooms = "SELECT * FROM rooms WHERE NOT booked;"
takenRooms = "SELECT * FROM rooms WHERE booked;"
showGuest = "SELECT * FROM guest;"
setRoomBooked = f"UPDATE rooms SET booked = 1 WHERE roomID == {roomID};"
registerEmail = f"INSERT INTO emails (email) VALUES ({email});"  # TODO: Get emailID from this and use it below
registerContact = f"INSERT INTO contact_info (phonenumber, emailID) VALUES ({phone}, {emailID});"  # TODO: Get contactID from this and use it below
registerGuest = f"INSERT INTO guest (zipcode, address, fname, lname, contactID) VALUES ({zipcode}, {address}, {fname}, {lname}, {contactID});"
registerBooking = f"INSERT INTO bookings (roomID, start_date, end_date, guestID) VALUES ({roomID}, {start_date}, {end_date}, {guestID});"

''' HOW TO EXECUTE AND GET RESULTS. The print index gets the last entry and therefore we can get the latest ID
cr.execute(showGuest)
res = cr.fetchall()
print(res[-1])
'''

# TODO: Get IDs needed from using SELECT and saving the latest ones ID to the var?

def dbSetup():
    pass

def bookRoom():
    pass

def roomSetup():
    r0 = Button(win, height=10, width=20, bg="green")
    r0.place(x=300, y=485)
    r1 = Button(win, height=5, width=15, bg="green")
    r1.place(x=300, y=345)
    r2 = Button(win, height=5, width=15, bg="green")
    r2.place(x=300, y=255)
    r3 = Button(win, height=5, width=15, bg="green")
    r3.place(x=300, y=115)
    r4 = Button(win, height=4, width=16, bg="green")
    r4.place(x=355, y=40)
    r5 = Button(win, height=10, width=20, bg="green")
    r5.place(x=515, y=40)
    # TODO: EVERYTHING BELOW NEEDS TO BE SHIFTED. WILL FIX IN REFRESH
    r6 = Button(win, height=5, width=15, bg="green")
    r6.place(x=548, y=255)
    r7 = Button(win, height=5, width=15, bg="green")
    r7.place(x=548, y=345)
    r8 = Button(win, height=5, width=15, bg="green")
    r8.place(x=548, y=480)
    r9 = Button(win, height=5, width=15, bg="green")
    r9.place(x=480, y=570)

def refreshRooms():
    currentFloor = int(win.call(imgLabel.cget('image'), 'cget', '-file')[7])
    if currentFloor == 1: # Add another button
        pass
    else: # Remove button if present
        pass
    cr.execute(takenRooms)
    fetched = cr.fetchall()
    res = [row[4] for row in fetched]
    print(res)
    for i in res:
        roomNum = str(i)[2]
        eval('r' + roomNum).config(bg="red")

def floorUp():
    try:
        newImg = list(win.call(imgLabel.cget('image'), 'cget', '-file'))
        tmpNum = int(newImg[7]) + 1
        newImg[7] = str(tmpNum)
        newImg = "".join(newImg)
        finalImg = PhotoImage(file=newImg)
        imgLabel.configure(image = finalImg)
        imgLabel.image = finalImg
        refreshRooms()
    except TclError:
        pass

def floorDown():
    try:
        newImg = list(win.call(imgLabel.cget('image'), 'cget', '-file'))
        tmpNum = int(newImg[7]) - 1
        newImg[7] = str(tmpNum)
        newImg = "".join(newImg)
        finalImg = PhotoImage(file=newImg)
        imgLabel.configure(image=finalImg)
        imgLabel.image = finalImg
        refreshRooms()
    except TclError:
        pass


win = Tk()
win.geometry("1000x700")
frame = Frame(win, width=900, height=670)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)
win.title('Hotel Landlyst')
BG = PhotoImage(file='images/100.png')
imgLabel = Label(frame, image = BG)
imgLabel.pack()
upImg = PhotoImage(file='images/up_arrow.png')
upB = Button(win, image = upImg, height=75, width=75, command=floorUp)
upB.place(x=868, y=150)
downImg = PhotoImage(file='images/down_arrow.png')
downB = Button(win, image =downImg, height=75, width=75, command=floorDown)
downB.place(x=868, y=450)
roomSetup()
refreshRooms()
win.mainloop()
