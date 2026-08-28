import mysql.connector as ms
import random
#import tabulate
import time as t
x=ms.connect(host='localhost',user='root',passwd='mysqlpythonconnect123',database='joevil')
if x.is_connected():
    cur=x.cursor()
    cur.execute('use joevil')
    def loading():
         print('-'*50)
         print('loading.........')
         print('-'*50)
    def new_patient():
        #Details to be inputted by the Receptionist/patient attender
        loading()
        name=input('Enter patient name')
        a=random.randint(501,10005)
        age=int(input('Enter patient age'))
        do=input('Enter patient DOB(yyyy/mm/dd)')
        mf=input('Enter gender M/F')
        fname=input('Enter father name')
        mname=input('Enter mother name')
        phno=int(input('Enter mobile no'))
        email=input('Enter email')
        add=input('Enter full address')
        weig=int(input('Enter measured weight'))
        he=int(input('Enter measured height'))
        temp=int(input('Enter measured body temperature(in C)'))
        print('\t','KINDLY NOTE YOUR PATIENT ID',a)
        cur.execute("insert into patientdetails values ('{}',{},{},'{}','{}','{}','{}','{}',{},'{}',{},{},{})".format(name,a,age,do,mf,add,fname,mname,phno,email,weig,he,temp))
        x.commit()
        cho=input('\t','Do you want to display your records??(y/n)')
        if cho.lower()=='y':
            loading()
            print('\t','Patient details:')
            cur.execute("select * from patientdetails ifexists where Patientname='{}'".format(name))
            d=cur.fetchall()
            h=['Patient Name','Patientid','Age','Date of birth','Gender','Father name','Mother name','Contact No','Email','Patient address','Weight','Height','Body temperature']
            print(tabulate.tabulate(d,h,tablefmt='psql'))
        elif cho.lower()=='n':
            None
    def search_patient():
        cur.execute('select patientid from patientdetails')
        pidfetch=cur.fetchall()
        try:
            loading()
            ans='y'
            while ans=='y':
                pid=int(input('Enter patient id to search'))
                cur.execute('select * from patientdetails where Patientid={}'.format(pid))
                d=cur.fetchall()
                if d!=():
                    print('Loading.............')
                    print('_-_-_-_-_-_-_-_-_Patient Details for Patient id',pid,'_-_-_-_-_-_-_-_-_')
                    h=['Patient Name','Patientid','Age','Date of birth','Gender','Patient address','Father name','Mother name','Contact No','Email','Weight','Height','Body temperature']
                    print(tabulate.tabulate(d,h,tablefmt='psql'))
                    break
                else:
                    print('\t','!!PATIENT DETAILS NOT FOUND!!')
                    break
        except:
            print('!!DETAILS of patient is not found,please enter correct patient id!!')
    def new_doctor():
        #to be filled by the one who applied for the post of doctor
        loading()
        na=input('Enter doctor name')
        q=input('Enter qualification')
        sp=input('Enter specialist in...')
        ag=int(input('Enter age'))
        d=input('Enter DOB(yyyy/mm/dd)')
        r=random.randint(1,500)
        em=input('Enter email')
        ge=input('Enter gender')
        c=int(input('Enter contact no'))
        j=input('Enter dateofjoin')
        address=input('Enter address')
        salary=int(input('enter current salary for which the doctor is appointed'))
        cur.execute("insert into doctor_details values({},'{}','{}',{},'{}','{}','{}',{},'{}','{}','{}','{}')".format(r,na,q,ag,d,em,j,salary,c,ge,sp,address))
        x.commit()
        cur.execute("select * from doctor_details ifexists where doctor_name='{}'".format(na))
        c=input('\t','Do you want to display the details of Doctor(y/n)')
        print('Loading.............')
        if c.lower()=='y':
            loading()
            print('\t','Details of Dr.',na)
            dat=cur.fetchall()
            data=['Doctor id','doctorname','Qualification','Age','Date of birth','Email','Date of Join','Salary','Contact no','Gender','Specialist','Address']
            print(tabulate.tabulate(dat,data,tablefmt='psql'))
        else:
            None
    def search_doctor():
        try:
            loading()
            ans='y'
            while ans.lower()=='y':
                ue=int(input('Enter doctor id to search'))
                cur.execute('select * from doctor_details where doctorid={}'.format(ue))
                print('Loading.............')
                print('_-_-_-_-_-_-_-_-_Doctor details for doctor id',ue,'_-_-_-_-_-_-_-_-_')
                dat=cur.fetchall()
                data=['Doctor id','doctorname','Qualification','Age','Date of birth','Email','Date of Join','Salary','Contact no','Gender','Specialist','Address']
                print(tabulate.tabulate(dat,data,tablefmt='psql'))
                ans=input('Do you want to search more?y/n')
        except:
            print('\t','!!DOCTOR DEAILS NOT FOUND PLEASE ENTER CORRECT DOCTOR ID!!')
    def display_doctor():
        loading()
        print('\t','Here is the list of Our top Doctors of Our  APJ hospital')
        cur.execute('select doctor_name,specialist,qualification from doctor_details')
        fet=cur.fetchall()
        row=['DOCTOR NAME','SPECIALIST IN','QUAIFICATION']
        print(tabulate.tabulate(fet,row,tablefmt='psql'))
    def rooms():
        tim=t.localtime()
        print('\tWelcome to APJ HOSPITTAL ROOMS....!!!')
        print('➟About rooms in APJ hospital')
        print("-We offer 8 different room and bed types. We have 345 beds including 251 in-patient beds (including isolation rooms. Each in-patient room has direct access to sunlight, and soft, bright interiors to aid patient recovery. Medical infrastructure and patient care is standard acrossirrespective of the room type. All rooms have a customised bed head panel, provision for medical gases, facilities for patient attendants, a bedside nurse call system, in-washroom area, and are friendly for differently abled people.")
        print('Chooose from the below:')
        ans='y'
        while ans=='y':
            print('-'*50)
            print('1➟View Types Of Room')
            print('2➟Book A Room')
            print('3➟Cancel Booking')
            print('4➟Check The Room Availability')
            print('5➟Raise Complaint')
            print('6➟View Booked Rooms')
            print('7➟Go Back')
            print('-'*50)
            ch=int(input('Enter choice:'))
            print('-'*50)
            if ch==1:
                print('-'*50)
                print('loading.........')
                print('-'*50)
                print('-'*50)
                print('Room type:Economy Room')
                print('cost:2,100/-')
                print("Description:The Economy rooms have been designed to accommodate 4 and 5 patients in a room. Each room has sofa cum beds for attendants, nurse call at each patient's bedside, Wi-Fi, and piped music. The rooms are large and spacious with adequate space for patient movement, in line with international standards")
                print('-'*50)
                print('Room type:Economy Plus Room')
                print('cost:2,700/-')
                print("Description:The Economy plus rooms have been designed to accommodate 3 patients in a room. Each room has sofa cum beds for attendants, nurse call at each patient's bedside, Wi-Fi, and piped music. The rooms are large and spacious with adequate space for patient movement, in line with international standards")
                print('-'*50)
                print('Room type:Twin-Sharing Room')
                print('cost:3,200/-')
                print("Description:The Twin-Sharing rooms have two patient beds, a sleeping arrangement for the patient attendant, Wi-Fi, and a separate television for each patient. The large and comfortable rooms are in line with international standards and provide generous space for patient movement..")
                print('-'*50)
                print('Room type:Deluxe Room')
                print('cost:8,000/-')
                print("Description:The Deluxe rooms are self-contained single rooms with an entertainment system, Wi-Fi facility, and a couch for the patient attendant.")
                print('-'*50)
                print('Room type:Premium Deluxe')
                print('cost:11,000/-')
                print("Description:The Premium Deluxe rooms are self-contained single rooms with an entertainment system, Wi-Fi facility, high-quality amenities and a couch for the patient attendant.")
                print('-'*50)
                print('Room type:Junior Suite')
                print('cost: 15,000/-')
                print("Description:The Junior Suite is a well-appointed, large, single room with an entertainment system, Wi-Fi facility, high-quality amenities and a sofa cum bed.")
                print('-'*50)
                print('Room type:The Grand Suite')
                print('cost:22,500/-')
                print("Description:The suite comprises a patient room with an entertainment system, a Wi-Fi facility, and a guest entertaining room furnished with a sofa cum bed, massage chair and a separate bathroom. It comes serviced with a butler on call, an entertainment system, a fruit platter on arrival and other high-quality amenities")
                print('-'*50)
                print('Room type:Presidential Suite')
                print('cost:Price on Request')
                print("Description:The Presidential Suite is designed to provide a blend of luxury and privacy for the patient and his or her family. The 970-square-feet suite has a separate patient room, a family room and a staff room for security and other patient staff. Each room has a separate entry to ensure the privacy and comfort of the family without compromising direct medical access. The suite has a private balcony offering a stunning view of the South Mumbai skyline. It comes serviced with a butler on call, an entertainment system, a fruit platter on arrival, a selection of magazines, and other high-quality amenities.")
                print('-'*50)
            elif ch==2:
                rtb=0
                loading()
                print('\t','Choose from the below')
                cur.execute('select distinct(roomtype) from rooms')
                da=cur.fetchall()
                hea=['ROOM TYPE']
                print(tabulate.tabulate(da,hea,tablefmt='psql'))
                print('-'*50)
                rob=input('Enter Roomtype you want:')
                print('-'*50)
                if rob.lower()=='economy room':
                    loading()
                    pid=int(input('Enter patient id:'))
                    day=int(input('Enter no days:'))
                    n=input('Enter patient name:')
                    u=input('Enter phone number:')
                    da=input('Enter booking date (yyyy/mm/dd):')
                    if int(da[0:4])>=tim[0]:
                        if int(da[5:7])>=tim[1] and int(da[5:7])<=12:
                            ay='Economy-room-'+str(day)+'-days'
                            pr=(2100+(5/100))*day
                            a=random.randint(101,110)
                            print('\t','ROOM BOOKED,YOUR ROOM NUMBER IS:',a)
                            cur.execute("update rooms set availability_status='BOOKED' where roomno={}".format(a))
                            cur.execute("insert into booked_rooms values({},'{}',{},'{}',{},'{}','{}',{})".format(pid,n,a,rob,day,da,u,pr))
                            x.commit()
                            print('\t','Check the details')
                            print('\t','BILL SUMMARY FOR PATIENT ID:',pid)
                            cur.execute('select * from booked_rooms where Room_no={}'.format(a))
                            fe=cur.fetchall()
                            he=['PATIENT ID','PATIENT NAME','ROOM NO','ROOM TYPE','NO OF DAYS','DATE OF BOOKING','PHONE NO','TOTAL PRICE']
                            print(tabulate.tabulate(fe,he,tablefmt='psql'))
                            rtb+=pr
                            cur.execute("insert into bill values('{}',{},'{}',{},{})".format(ay,2100,'5%GST',pr,pid))
                            print('-'*60)
                            print('\t','KINDLY NOTE THE TOTAL AMOUNT','Rs.',pr,'/-')
                            print('-'*60)
                        else:
                            print('\t','!!Enter a valid month or enter a month in future!!')
                    else:
                        print('\t','!!Enter a year in future!!')
                elif rob.lower()=='economy plus room':
                    loading()
                    pid=int(input('Enter patient id:'))
                    day=int(input('Enter no days:'))
                    n=input('Enter patient name:')
                    u=input('Enter phone number:')
                    pr=(2700+(5/100))*day
                    da=input('Enter booking date (yyyy/mm/dd)')
                    if int(da[0:4])>=tim[0]:
                        if int(da[5:7])>=tim[1]and int(da[5:7])<=12:
                            ay='Economy-plus-room-'+str(day)+'-days'
                            a=random.randint(111,120)
                            print('ROOM BOOKED,YOUR ROOM NUMBER IS:',a)
                            cur.execute("update rooms set availability_status='BOOKED' where roomno={}".format(a))
                            cur.execute("insert into booked_rooms values({},'{}',{},'{}',{},'{}','{}',{})".format(pid,n,a,rob,day,da,u,pr))
                            x.commit()
                            print('Check the details')
                            print('\t','BILL SUMMARY FOR PATIENT ID:',pid)
                            cur.execute('select * from booked_rooms where Room_no={}'.format(a))
                            fe=cur.fetchall()
                            he=['PATIENT ID','PATIENT NAME','ROOM NO','ROOM TYPE','NO OF DAYS','DATE OF BOOKING','PHONE NO','TOTAL PRICE']
                            print(tabulate.tabulate(fe,he,tablefmt='psql'))
                            cur.execute('Select total_price from booked_rooms where Patient_id={}'.format(pid))
                            cur.execute("insert into bill values('{}',{},'{}',{},{})".format(ay,2700,'5%GST',tr,pid))
                            rtb+=pr
                            print('-'*60)
                            print('\t','KINDLY NOTE THE TOTAL AMOUNT','Rs.',tr,'/-')
                            print('-'*60)
                        else:
                            print('\t','!!Please input a valid month or enter a month in future!!')
                    else:
                        print('\t','!!Please enter a year in future!!')
                elif rob.lower()=='twin-sharing room':
                    loading()
                    pid=int(input('Enter patient id'))
                    day=int(input('Enter no days'))
                    n=input('Enter patient name')
                    u=input('Enter phone number')
                    pr=(3200+(5/100))*day
                    da=input('Enter booking date (yyyy/mm/dd)')
                    if int(da[0:4])>=tim[0]:
                        if int(da[5:7])>=tim[1] and int(da[5:7])<=12:
                            ay='Twin-sharing-room-'+str(day)+'-days'
                            a=random.randint(201,210)
                            print('ROOM BOOKED,YOUR ROOM NUMBER IS:',a)
                            cur.execute("update rooms set availability_status='BOOKED' where roomno={}".format(a))
                            cur.execute("insert into booked_rooms values({},'{}',{},'{}',{},'{}','{}',{})".format(pid,n,a,rob,day,da,u,pr))
                            x.commit()
                            print('\t','Check the details')
                            print('\t','BILL SUMMARY FOR PATIENT ID:',pid)
                            cur.execute('select * from booked_rooms where Room_no={}'.format(a))
                            fe=cur.fetchall()
                            he=['PATIENT ID','PATIENT NAME','ROOM NO','ROOM TYPE','NO OF DAYS','DATE OF BOOKING','PHONE NO','TOTAL PRICE']
                            print(tabulate.tabulate(fe,he,tablefmt='psql'))
                            cur.execute('Select total_price from booked_rooms where Patient_id={}'.format(pid))
                            cur.execute("insert into bill values('{}',{},'{}',{},{})".format(ay,3200,'5%GST',rt,pid))
                            rtb+=pr
                            print('-'*60)
                            print('\t','KINDLY NOTE THE TOTAL AMOUNT','Rs.',rt,'/-')
                            print('-'*60)
                        else:
                            print('\t','!!Please enter a valid month or enter a month in future!!')
                    else:
                        print('\t','!!Please enter a year in future!!')
                elif rob.lower()=='deluxe room':
                    loading()
                    pid=int(input('Enter patient id:'))
                    day=int(input('Enter no days:'))
                    n=input('Enter patient name:')
                    u=input('enter phone number:')
                    pr=(8000+(5/100))*day
                    da=input('Enter booking date (yyyy/mm/dd):')
                    if int(da[0:4])>=tim[0]:
                        if int(da[5:7])>=tim[1] and int(da[5:7])<=12:
                            a=random.randint(301,310)
                            ay='Deluxe-room-'+str(day)+'-days'
                            print('\t','ROOM BOOKED,YOUR ROOM NUMBER IS:',a)
                            cur.execute("update rooms set availability_status='BOOKED' where roomno={}".format(a))
                            cur.execute("insert into booked_rooms values({},'{}',{},'{}',{},'{}','{}',{})".format(pid,n,a,rob,day,da,u,pr))
                            x.commit()
                            print('Check the details')
                            print('\t','BILL SUMMARY FOR PATIENT ID:',pid)
                            cur.execute('select * from booked_rooms where Room_no={}'.format(a))
                            fe=cur.fetchall()
                            he=['PATIENT ID','PATIENT NAME','ROOM NO','ROOM TYPE','NO OF DAYS','DATE OF BOOKING','PHONE NO','TOTAL PRICE']
                            print(tabulate.tabulate(fe,he,tablefmt='psql'))
                            cur.execute('Select total_price from booked_rooms where Patient_id={}'.format(pid))
                            tp=cur.fetchall()
                            rtb+=pr
                            cur.execute("insert into bill values('{}',{},'{}',{},{})".format(ay,8000,'5%GST',tr,pid))
                            print('-'*60)
                            print('\t','KINDLY NOTE THE TOTAL AMOUNT','Rs.',rt,'/-')
                            print('-'*60)
                        else:
                            print('\t','!!Please enter a valid month or enter a month in future!!')
                    else:
                        print('\t','!!Please enter a year in future!!')
                elif rob.lower()=='premium deluxe':
                    loading()
                    pid=int(input('Enter patient id:'))
                    d=int(input('Enter no days:'))
                    n=input('Enter patient name:')
                    u=input('enter phone number:')
                    pr=(1100+(5/100))*d
                    da=input('Enter booking date (yyyy/mm/dd):')
                    if int(da[0:4])>=tim[0]:
                        if int(da[5:7])>=tim[1] and int(da[5:7])<=12:
                            a=random.randint(401,410)
                            ay='Premiun-deluxe-room-'+str(d)+'-days'
                            print('\t','ROOM BOOKED,YOUR ROOM NUMBER IS:',a)
                            cur.execute("update rooms set availability_status='BOOKED' where roomno={}".format(a))
                            cur.execute("insert into booked_rooms values({},'{}',{},'{}',{},'{}','{}',{})".format(pid,n,a,rob,d,da,u,pr))
                            x.commit()
                            print('\t','Check the details')
                            print('\t','BILL SUMMARY FOR PATIENT ID:',pid)
                            cur.execute('select * from booked_rooms where Room_no={}'.format(a))
                            fe=cur.fetchall()
                            he=['PATIENT ID','PATIENT NAME','ROOM NO','ROOM TYPE','NO OF DAYS','DATE OF BOOKING','PHONE NO','TOTAL PRICE']
                            print(tabulate.tabulate(fe,he,tablefmt='psql'))
                            cur.execute('Select total_price from booked_rooms where Patient_id={}'.format(pid))
                            tp=cur.fetchall()
                            rtb+=pr
                            cur.execute("insert into bill values('{}',{},'{}',{},{})".format(ay,11000,'5%GST',rt,pid))
                            print('-'*60)
                            print('\t','KINDLY NOTE THE TOTAL AMOUNT','Rs.',rt,'/-')
                            print('-'*60)
                        else:
                            print('\t','!!Please enter a valid month or enter a month in future!!')
                    else:
                        print('\t','!!Please enter a year in future!!')
                elif rob.lower()=='junior suite':
                    loading()
                    pid=int(input('Enter patient id'))
                    d=int(input('Enter no days'))
                    n=input('Enter patient name')
                    u=input('enter phone number')
                    pr=(15000+(5/100))*d
                    da=input('Enter booking date (yyyy/mm/dd)')
                    ay='junior-suite-room-'+str(d)+'-days'
                    if int(da[0:4])>=tim[0]:
                        if int(da[5:7])>=tim[1] and int(da[5:7])<=12:
                            a=random.randint(501,505)
                            print('ROOM BOOKED,YOUR ROOM NUMBER IS:',a)
                            cur.execute("update rooms set availability_status='BOOKED' where roomno={}".format(a))
                            cur.execute("insert into booked_rooms values({},'{}',{},'{}',{},'{}','{}',{})".format(pid,n,a,rob,d,da,u,pr))
                            x.commit()
                            print('Check the details')
                            print('\t','BILL SUMMARY FOR PATIENT ID:',pid)
                            cur.execute('select * from booked_rooms where Room_no={}'.format(a))
                            fe=cur.fetchall()
                            he=['PATIENT ID','PATIENT NAME','ROOM NO','ROOM TYPE','NO OF DAYS','DATE OF BOOKING','PHONE NO','TOTAL PRICE']
                            print(tabulate.tabulate(fe,he,tablefmt='psql'))
                            cur.execute('Select total_price from booked_rooms where Patient_id={}'.format(pid))
                            cur.execute("insert into bill values('{}',{},'{}',{},{})".format(ay,15000,'5%GST',rt,pid))
                            rtb+=pr
                            print('-'*60)
                            print('\t','KINDLY NOTE THE TOTAL AMOUNT','Rs.',rt,'/-')
                            print('-'*60)
                        else:
                            print('please enter a valid  month or enter a month in future')
                    else:
                        print('please enter a year in future')
                elif rob.lower()=='the grand suite':
                    loading()
                    pid=int(input('Enter patient id'))
                    d=int(input('Enter no days'))
                    n=input('Enter patient name')
                    u=input('enter phone number')
                    pr=(22500+(5/100))*d
                    ay='The-grand-suite-room-'+str(d)+'-days'
                    da=input('Enter booking date (yyyy/mm/dd)')
                    if int(da[0:4])>=tim[0]:
                        if int(da[5:7])>=tim[1] and int(da[5:7])<=12:
                            a=random.randint(506,510)
                            print('ROOM BOOKED,YOUR ROOM NUMBER IS:',a)
                            cur.execute("update rooms set availability_status='BOOKED' where roomno={}".format(a))
                            cur.execute("insert into booked_rooms values({},'{}',{},'{}',{},'{}','{}',{})".format(pid,n,a,rob,d,da,u,pr))
                            x.commit()
                            print('Check the details')
                            print('\t','BILL SUMMARY FOR PATIENT ID:',pid)
                            cur.execute('select * from booked_rooms where Room_no={}'.format(a))
                            fe=cur.fetchall()
                            he=['PATIENT ID','PATIENT NAME','ROOM NO','ROOM TYPE','NO OF DAYS','DATE OF BOOKING','PHONE NO','TOTAL PRICE']
                            print(tabulate.tabulate(fe,he,tablefmt='psql'))
                            cur.execute('Select total_price from booked_rooms where Patient_id={}'.format(pid))
                            cur.execute("insert into bill values('{}',{},'{}',{},{})".format(ay,22500,'5%GST',tr,pid))
                            rtb+=pr
                            print('-'*60)
                            print('\t','KINDLY NOTE THE TOTAL AMOUNT','Rs.',rt,'/-')
                            print('-'*60)
                        else:
                            print('enter a valid month or enter a month in future')
                    else:
                        print('enter a year in future')
                elif rob.lower()=='presidential suite':
                    loading()
                    pid=int(input('Enter patient id'))
                    d=int(input('Enter no days'))
                    n=input('Enter patient name')
                    u=input('enter phone number')
                    pr=(25000+(5/100))*d
                    ay='Presidential-suite-room-'+str(d)+'-days'
                    da=input('Enter booking date (yyyy/mm/dd)')
                    if int(da[0:4])>=tim[0]:
                        if int(da[5:7])>=tim[1] and int(da[5:7])<=12:
                            a=random.randint(601,610)
                            print('ROOM BOOKED,YOUR ROOM NUMBER IS:',a)
                            cur.execute("update rooms set availability_status='BOOKED' where roomno={}".format(a))
                            cur.execute("insert into booked_rooms values({},'{}',{},'{}',{},'{}','{}',{})".format(pid,n,a,rob,d,da,u,pr))
                            x.commit()
                            print('Check the details')
                            print('\t','BILL SUMMARY FOR PATIENT ID:',pid)
                            cur.execute('select * from booked_rooms where Room_no={}'.format(a))
                            fe=cur.fetchall()
                            he=['PATIENT ID','PATIENT NAME','ROOM NO','ROOM TYPE','NO OF DAYS','DATE OF BOOKING','PHONE NO','TOTAL PRICE']
                            print(tabulate.tabulate(fe,he,tablefmt='psql'))
                            cur.execute('Select total_price from booked_rooms where Patient_id={}'.format(pid))
                            cur.execute("insert into bill values('{}',{},'{}',{},{})".format(ay,25000,'5%GST',tr,pid))
                            rtb+=pr
                            print('-'*60)
                            print('\t','KINDLY NOTE THE TOTAL AMOUNT','Rs.',rt,'/-')
                            print('-'*60)
                        else:
                            print('enter a valid month or enter a month in future')
                    else:
                        print('please enter a year in future')
                else:
                    None
            elif ch==3:
                 loading()
                 alb=int(input('Enter already booked room no'))
                 cur.execute('select room_no from booked_rooms')
                 a=cur.fetchall()
                 u=0
                 for i in a:
                     for j in i:
                         if alb==j:
                             u+=j
                             cur.execute('delete from booked_rooms where room_no={}'.format(alb))
                             cur.execute("update rooms set availability_status='NOT BOOKED' where roomno={}".format(alb))
                             print('DATA DELETED')
                             x.commit()
                             break
                 else:
                     print('!!!!!!!!!Enter a valid book no!!!!!!!!')
            elif ch==4:
                loading()
                print('List of available/non-available rooms')
                cur.execute('select * from rooms')
                da=cur.fetchall()
                a=['ROOMNO','ROOMTYPE','PRICE PER DAY','AVAILABILITY STATUS']
                print(tabulate.tabulate(da,a,tablefmt='psql'))
            elif ch==5:
                print('-'*50)
                print('loading.........')
                print('-'*50)
                print('~~~~WE ARE VERY SORRY FOR THE INCONVENIENCE THAT YOU FACED KINDLY TELL US BELOW~~~~')
                compl=input('Please tell us the complaint')
                pid=input('Enter patient id:')
                rno=int(input('Enter room no:'))
                cur.execute("insert into complaint values('{}',{},{})".format(compl,pid,rno))
                x.commit()
                print('')
                print('####COMPLAINT REGISTERED####')
                print('')
                print('WE MAKE SURE THAT OUR TEAM WILL CONTACT YOU SOON AND SOLVE THE ISSUE')
                print('')
            elif ch==6:
                loading()
                print('THESE ARE THE ROOMS SO FAR BOOKED:')
                cur.execute("select * from rooms where availability_status='BOOKED'")
                da=cur.fetchall()
                a=['ROOMNO','ROOMTYPE','PRICE PER DAY','AVAILABILITY STATUS']
                print(tabulate.tabulate(da,a,tablefmt='psql'))
            elif ch==7:
                break
            ans=input('Enter y to continue')
    def new_nurse():
        loading()
        wa=input('ENTER NURSE NAME:')
        q=input('ENTER YOUR QUALIFICATION')
        ag=int(input('ENTER AGE:'))
        d=input('ENTER YOUR DOB(YYYY/MM/DD):')
        g=input('ENTER GENDER(M/F):')
        r=random.randint(1234,5000)
        sal=int(input('ENTER CURRENT SALARY FOR WHICH THE NURSE'))
        AD=input('ENTER ADDRESS:')       
        ct=input('ENTER CONTACT NO:')
        cur.execute("insert into nursedetails values('{}',{},'{}',{},'{}','{}','{}','{}','{}')".format(wa,r,q,ag,d,g,sal,AD,ct))
        x.commit()
        cur.execute("select * from NURSEDETAILS where NURSENAME='{}'".format(wa))
        c=input('DO YOU WANT TO DISPLAY THE EXISTING DETAILS OF THE NURSE (Y/N)')
        print('\t','KINDLY NOTE YOUR NURSEID',r)
        print('='*50)
        print('loading.........')
        print('='*50)
        if c.lower()=='y':
            loading()
            print('\t','DETAILS OF NURSE',wa)
            cur.execute('select * from nursedetails where nurseid={}'.format(r))
            dhu=cur.fetchall()
            da=['NURSENAME','NURSEID','QUALIFICATION','AGE','DOB','GENDER','SALARY''ADDRESS','CONTACT_NO']
            print(tabulate.tabulate(dhu,da,tablefmt='psql'))
        else:
            None
    def ambulance_driver():
        loading()
        ans='y'
        while ans=='y':
            print('-'*50)
            print('CHOOSE FROM THE BELOW MENU')
            print('\t','1➟Add new driver')
            print('\t','2➟View existing drivers')
            print('\t','3➟Delete record of a driver')
            print('\t','4➟Update record of a driver')
            print('\t','5➟Check license validity')
            print('\t','6➟Exit')
            print('-'*50)
            ch=int(input('Enter the choice 1/2/3/4/5'))
            print('-'*50)
            if ch==1:
                loading()
                print('Kindly fill the following details:')
                driname=input('Enter your full name:')
                age=input('Enter your age:')
                dobdriver=input('Enter Date of birth(yyyy/mm/dd):')
                cno=input('Enter contact no:')
                add=input('Enter your residential address:')
                liid=input('Enter license id:')
                driid=random.randint(1006,2000)
                vali=input('Enter validity(yyyy/mm/dd):')
                cur.execute("insert into ambdrivers values('{}',{},{},'{}','{}','{}','{}','{}')".format(driname,driid,age,dobdriver,add,cno,liid,vali))
                x.commit()
                print('\t','Kindly note your driverid:',driid)
                cio=input('\t','Do u want to display the driver details(y/n)')
                print('Loading............')
                if cio.lower()=='y':
                    loading()
                    print('\t','Details of Driver:',driname)
                    cur.execute("select * from ambdrivers ifexists where driver_name='{}'".format(driname))
                    headings=['Driver name','Driverid','Age','DOB','Address','Contact no','Licenseid','validity']
                    fetchdetails=cur.fetchall()
                    print(tabulate.tabulate(fetchdetails,headings,tablefmt='psql'))
                else:
                    None
            elif ch==2:
                loading()
                l3='d'
                while l3=='d':
                    print('-'*50)
                    print('SELECT FROM THE FOLLOWING')
                    print('1.Show all the driver list')
                    print('2.Search for particular driver')
                    print('3.Exit')
                    print('-'*50)
                    ach=int(input('Enter choie'))
                    if ach==1:
                        print('ALL EXISTING DRIVERS')
                        cur.execute('select * from ambdrivers')
                        fetch2=cur.fetchall()
                        headings2=['Driver name','Driverid','Age','DOB','Address','Contact no','Licenseid','validity']
                        print(tabulate.tabulate(fetch2,headings2,tablefmt='psql'))
                    elif ach==2:
                        try:
                            sear=int(input('Enter driver id to search:'))
                            cur.execute('select * from ambdrivers ifexists where driver_id={}'.format(sear))
                            print('Loading...............')
                            print('Details of Driver for driver id:',sear)
                            hings=['Driver name','Driverid','Age','DOB','Address','Contact no','Aadhar no','Licenseid','validity']
                            fetchdet=cur.fetchall()
                            print(tabulate.tabulate(fetchdet,hings,tablefmt='psql'))
                        except:
                            print('DRIVER DETAILS NOT FOUND PLEASE ENTER CORRECT DRIVER ID')
                    elif ach==3:
                        break
            elif ch==3:
                try:
                    loading()
                    did=int(input('Enter driver id to delete'))
                    cur.execute('delete from ambdrivers where driver_id={}'.format(did))
                    x.commit()
                    print('Record of driver for driver id:',did,'deleted successfully')
                except:
                    print('Please enter a valid driver id')
            elif ch==4:
                try:
                    loading()
                    pidi=int(input("Enter driver id to update"))
                    an='a'
                    while an.lower()=='a':
                        print('-'*50)
                        print('Select which record you want to update')
                        print('NOTE:Driver id cant be updated/changed')
                        print('\t','1➟Name')
                        print('\t','2➟Age')
                        print('\t','3➟Contact no')
                        print('\t','4➟Address')
                        print('\t','5➟license validity,Note:Make sure you update the record in this section frequently')
                        print('\t','6➟Exit')
                        print('-'*50)
                        choi=int(input('Enter choice for the record to be updated'))
                        print('-'*50)
                        if choi==1:
                            loading()
                            newname=input('Enter new name')
                            cur.execute("update ambdrivers set driver_name='{}' where driver_id={}".format(newname,pidi))
                            x.commit()
                            print('Name updated successfully')
                            print('Details of driver',newname,'after updation')
                            cur.execute('select * from ambdrivers ifexists where driver_id={}'.format(pidi))
                            hings=['Driver name','Driverid','Age','DOB','Address','Contact no','Licenseid','validity']
                            fetchdet=cur.fetchall()
                            print(tabulate.tabulate(fetchdet,hings,tablefmt='psql'))
                        elif choi==2:
                            loading()
                            newage=int(input('Enter new age'))
                            cur.execute('update ambdrivers set age={} where driver_id={}'.format(newage,pidi))
                            x.commit()
                            print('Age updated successfully')
                            print('Details of driver after updation:')
                            cur.execute('select * from ambdrivers ifexists where driver_id={}'.format(pidi))
                            hings=['Driver name','Driverid','Age','DOB','Address','Contact no','Licenseid','validity']
                            fetchdet=cur.fetchall()
                            print(tabulate.tabulate(fetchdet,hings,tablefmt='psql'))
                        elif choi==3:
                            loading()
                            newno=int(input('Enter new contact number'))
                            cur.execute('update ambdrivers set contact_number={} where driver_id={}'.format(newno,pidi))
                            x.commit()
                            print('Contact number updated successfully')
                            print('Details of driver after updation')
                            cur.execute('select * from ambdrivers ifexists where driver_id={}'.format(pidi))
                            hings=['Driver name','Driverid','Age','DOB','Address','Contact no','Licenseid','validity']
                            fetchdet=cur.fetchall()
                            print(tabulate.tabulate(fetchdet,hings,tablefmt='psql'))
                        elif choi==4:
                            loading()
                            newadd=input('enter new address')
                            cur.execute("update ambdrivers set address='{}' where driver_id={}".format(newadd,pidi))
                            x.commit()
                            print('-'*50)
                            print('ADDRESS UPDATED SUCCESSFULLY')
                            print('Details of driver after updation')
                            cur.execute('select * from ambdrivers ifexists where driver_id={}'.format(pidi))
                            hings=['Driver name','Driverid','Age','DOB','Address','Contact no','Licenseid','validity']
                            fetchdet=cur.fetchall()
                            print(tabulate.tabulate(fetchdet,hings,tablefmt='psql'))
                        elif choi==5:
                            loading()
                            newval=input('Enter new validity')
                            cur.execute("update ambdrivers set validity='{}' where driver_id={}".format(newval,pidi))
                            x.commit()
                            print('Validity updated successfully')
                            print('Details of driver after updation')
                            cur.execute('select * from ambdrivers ifexists where driver_id={}'.format(pidi))
                            hings=['Driver name','Driverid','Age','DOB','Address','Contact no','Licenseid','validity']
                            fetchdet=cur.fetchall()
                            print(tabulate.tabulate(fetchdet,hings,tablefmt='psql'))
                        elif ch==6:
                            break
                        break
                except:
                    print('Please enter correct value')
            elif ch==5:
                loading()
                pid=int(input('Enter driver id'))
                d=t.localtime()
                dol=str(str(d[0])+'/'+str(d[1])+'/'+str(d[2]))
                cur.execute('select validity from ambdrivers ifexists where driver_id={}'.format(pid))
                detval=cur.fetchall()
                l=''
                for i in detval:
                    for j in i:
                        l+=j
                if l>dol:
                    print('l=',l)
                    print(str(dol))
                    print('\t','!!!License validity expired,Renew immediately!!!')
                else:
                    print('\t','**License not yet expired,but keep in track of the date')
            elif ch==6:
                break
            ans=input('Press y if you want to go back to the menu')
    def medicines():
        loading()
        print('\t','Choose from the below')
        ans='y'
        while ans=='y':
            print('-'*50)
            print('\t','1➟CHECK MEDICINE STOCK')
            print('\t','2➟UPDATE STOCK')
            print('\t','3➟DELETE STOCK(EXPIRED ONES)')
            print('\t','4➟ADD STOCK')
            print('\t','5➟EXIT')
            print('-'*50)
            ch=int(input('Enter your choice'))
            print('-'*50)
            if ch==1:
                loading()
                e='a'
                while e=='a':
                    print('-'*50)
                    print('\t','Choose from below')
                    print('\t','1➟Search for a particular medicine')
                    print('\t','2➟Display all stocks')
                    print('\t','3➟Exit')
                    print('-'*50)
                    u=int(input('enter your choice'))
                    print('-'*50)
                    if u==1:
                        try:
                            print('-'*50)
                            print('loading.........')
                            print('-'*50)
                            print('Caution:Enter the medicine name clearly')
                            med=input('Enter Medicine name')
                            cur.execute("Select Medicinename,Medicinequantity from medicine ifexists where MedicineName='{}'".format(med))
                            a=cur.fetchall()
                            h=['Medicine name','Quantity']
                            print(tabulate.tabulate(a,h,tablefmt='psql'))
                        except:
                            print('MEDICINE NOT FOUND,ENTER THE CORRECT MEDICINE NAME')
                    elif u==2:
                        print('-'*50)
                        print('loading.........')
                        print('-'*50)
                        print('Entire stock of medicine')
                        cur.execute('select * from medicine ifexists')
                        d=cur.fetchall()
                        h=['Medicine name','Price','Quantity']
                        print(tabulate.tabulate(d,h,tablefmt='psql'))
                    elif u==3:
                        break
                    e=input('Enter a if you want to continue')
            elif ch==2:
                loading()
                l1='s'
                while l1.lower()=='s':
                    print('-'*50)
                    print('\t','Select what you want to update')
                    print('\t','1➟Medicine name')
                    print('\t','2➟Medicine price')
                    print('\t','3➟Medicine quantity')
                    print('\t','4➟Exit')
                    print('-'*50)
                    ch2=int(input('select your choice'))
                    print('-'*50)
                    if ch2==1:
                        try:
                            loading()
                            print('Caution:Enter the details correctly')
                            medn=input('Enter new medicine name')
                            old=input('Enter old name')
                            cur.execute("update medicine set medicinename='{}'where medicinename='{}'".format(medn,old))
                            print('-'*50)
                            print('MEDICINE NAME UPDATED!!')
                            print('-'*50)
                        except:
                            print('ENTER THE DETAILS CORRECTLY')
                    elif ch2==2:
                        try:
                            loading()
                            print('Caution:Enter the details correctly')
                            new=int(input('Enter new price'))
                            med=input('Enter medicine name')
                            cur.execute("update medicine set MedicinePrice={} where medicinename='{}'".format(new,med))
                            print('-'*50)
                            print('MEDICINE PRICE UPDATED!!')
                            print('-'*50)
                        except:
                            print('Enter the details correctly medicine not found')
                    elif ch2==3:
                        try:
                            loading()
                            print('Caution:Enter the details correctly')
                            newq=int(input('Enter new quantity'))
                            medna=input('Enter medicine name')
                            cur.execute("update medicine set Medicinequantity={} where Medicinename='{}'".format(newq,medna))
                            print('-'*50)
                            print('MEDICINE QUANTITY UPDATED')
                            print('-'*50)
                        except:
                            print('Enter the details correctly medicine not found')
                    else:
                        break
                    l1=input('Enter S to continue')
            elif ch==3:
                try:
                    loading()
                    ent=input('Enter medicine name to delete')
                    cur.execute("delete from medicine where medicinename='{}'".format(ent))
                    print('-'*50)
                    print('MEDICINE DELETED')
                    print('-'*50)
                except:
                    print('Enter the details correctly medicine not found')
            elif ch==4:
                loading()
                nampro=input('Enter medicine name')
                pou=int(input('Enter medicine stock'))
                r=input('Enter medicine cost')
                cur.execute("insert into medicine values('{}',{},{})".format(nampro,pou,r))
                x.commit()
                print('\t','ADDED SUCCESSFULLY!!!')
            elif ch==5:
                break
            y=input('enter y to continue')
    def nursignup():
        l4='j'
        while l4.lower()=='j':
            print('-'*50)
            print("CHOOSE FROM THE BELOW MENU")
            print('\t','1➟View NURSE details')
            print('\t','2➟Update NURSE details')
            print('\t','3➟Delete NURSE details')
            print('\t','4➟Exit')
            print('-'*50)
            chow2=int(input('Select your choice 1/2/3'))
            if chow2==1:
                loading()
                pidin=int(input('Enter Nurse id to search'))
                print('NURSE DETAILS')
                cur.execute('SELECT * FROM NURSEDETAILS where nurseid={}'.format(pidin))
                fe=cur.fetchall()
                h=['NURSENAME','NURSEID','QUALIFICATION','AGE','DOB','GENDER','SALARY','ADDRESS','CONTACT_NO']
                print(tabulate.tabulate(fe,h,tablefmt='psql'))
            elif chow2==2:
                loading()
                pidi=int(input('##KINDLY INPUT YOUR NURSEID##:'))
                loop='l'
                while loop.lower()=='l':
                    print('-'*50)
                    print('Choose which you want to update')
                    print('\t','[MENU]')
                    print('\t','1➟Name')
                    print('\t','2➟Age')
                    print('\t','3➟Phone number')
                    print('\t','4➟Address')
                    print('\t','5➟salary')
                    print('\t','6➟exit')
                    print('-'*50)
                    ucho=int(input('Enter choice'))
                    print('-'*50)
                    if ucho==1:
                        loading()
                        nnamp=input('Enter new name')
                        cur.execute("update NURSEDETAILS set NURSENAME='{}' where NURSEID='{}'".format(nnamp,pidi))
                        x.commit()
                        print('Name updated successfully')
                        print('Details of nurse',nnamp,'after updation')
                        cur.execute('select * from nursedetails where nurseID={}'.format(pidi))
                        nada=cur.fetchall()
                        head=['NURSE NAME','NURSE ID','QUALIFICATION','AGE','DOB','GENDER','SALARY','NURSE ADDRESS','CONTACT NO']
                        print(tabulate.tabulate(nada,head,tablefmt='psql'))
                    elif ucho==2:
                        loading()
                        newage=int(input('enter new age'))
                        cur.execute('update nursedetails set age={} where nurseID'.format(newage,pidi))
                        x.commit()
                        print('Age updated successfully')
                        print('Details of NURSE after updation:')
                        cur.execute('select * from nursedetails ifexists  where nurseID={}'.format(pidi))
                        head=['NURSE NAME','NURSE ID','QUALIFICATION','AGE','DOB','GENDER','SALARY','NURSE ADDRESS','CONTACT NO']
                        fetchdet=cur.fetchall()
                        print(tabulate.tabulate(fetchdet,head,tablefmt='psql'))
                    elif ucho==3:
                        loading()
                        newno=int(input('Enter new contact number'))
                        cur.execute('update nursedetails set contactno={} where nurseID={}'.format(newno,pidi))
                        x.commit()
                        print('Contact number updated successfully')
                        print('Details of nurse after updation')
                        cur.execute('select * from nursedetails where nurseid={}'.format(pidi))
                        head=['NURSE NAME','NURSE ID','QUALIFICATION','AGE','DOB','GENDER','SALARY','NURSE ADDRESS','CONTACT NO']
                        fetchdet=cur.fetchall()
                        print(tabulate.tabulate(fetchdet,head,tablefmt='psql'))
                    elif ucho==4:
                        loading()
                        newadd=input('enter new address')
                        cur.execute("update nursedetails set nurseaddress='{}' where nurseID={}".format(newadd,pidi))
                        x.commit()
                        print('!!!!!!!!!Address updated successfully!!!!!!!!!!')
                        print('Details of nurse after updation')
                        cur.execute('select * from nursedetails where nurseid={}'.format(pidi))
                        head=['NURSE NAME','NURSE ID','QUALIFICATION','AGE','DOB','GENDER','SALARY','NURSE ADDRESS','CONTACT NO']
                        fetchdet=cur.fetchall()
                        print(tabulate.tabulate(fetchdet,head,tablefmt='psql'))
                    elif ucho==5:
                        loading()
                        newsal=input('enter new salary')
                        cur.execute("update nursedetails set salary='{}' where nurseid='{}'".format(newsal,pidi))
                        x.commit()
                        print('!!!!!!!!!salary updated successfully!!!!!!!!!!')
                        print('Details of nurse after updation')
                        cur.execute('select * from nursedetails where nurseid={}'.format(pidi))
                        head=['NURSE NAME','NURSE ID','QUALIFICATION','AGE','DOB','GENDER','SALARY','NURSE ADDRESS','CONTACT NO']
                        fetchdet=cur.fetchall()
                        print(tabulate.tabulate(fetchdet,head,tablefmt='psql'))
                    elif ucho==6:
                        break
            elif chow2==3:
                loading()
                pidi=int(input('##KINDLY INPUT YOUR NURSEID TO DELETE##:'))
                a='o'
                while a.lower()=='o':
                    cur.execute('delete from nursedetails where nurseid={}'.format(pidi))
                    x.commit()
                    print('\t','DATA DELETED')
                    break
            elif chow2==4:
                break
    def worker_canteen():
        print('='*98)
        print('='*40,'WELCOME TO CANTEEN','='*38)
        print('='*98)
        d=t.localtime()
        ans='y'
        cb=0
        while ans=='y':
            print('-'*50)
            print('PRESS 1 IF YOU ARE A DOCTOR')
            print('PRESS 2 IF YOU ARE A NURSE')
            print('PRESS 3 IF YOU WANT TO EXIT')
            print('-'*50)
            ch=int(input('ENTER YOUR CHOICE:'))
            print('-'*50)
            loading()
            if ch==1:
                dcb=0
                do=int(input('ENTER YOUR DOCTOR ID:'))
                loading()
                print('CHOOSE FROM THE BELOW MENU')
                if d[3]<11:
                    cur.execute('select * from breakfast')
                    a=cur.fetchall()
                    h=['ITEM_NO','ITEM_NAME','ITEM_PRICE']
                    print(tabulate.tabulate(a,h,tablefmt='psql'))
                    M='YES'
                    while M.lower()=='yes':
                        print('press 1 SELECT ITEM')
                        print('press 2 EXIT')
                        se_ch = int(input('ENTER THE CHOICE |--> '))
                        if se_ch == 1:
                            w =input('Enter the item_no: ')
                            cur.execute('SELECT * FROM BREAKFAST WHERE item_no = %s', (w,))
                            item= cur.fetchone()
                            if item:
                                h= ['ITEM_NO', 'ITEM_NAME', 'ITEM_PRICE']
                                print(tabulate.tabulate([item], headers=h, tablefmt='psql'))
                                cp=item[2]
                                print('-'*30)
                                print('\tKINDLY NOTE THE PRICE RS.',cp,'/-')
                                cb+=cp
                                dcb+=cp
                                print('-'*30)
                            else:
                                print('ITEM NOT FOUND.PLEASE TRY AGAIN')
                        elif se_ch==2:
                            print('==================')
                            print('    THANK YOU     ')
                            print('==================')
                        M=input('DO YOU WANT MORE FOODS TO BE ORDERED PRESS YES/NO')
                    print('YOUR TOTAL BILL FOR',d[0],'/',d[1],'/',d[2],'IS RS.',dcb+dcb*0.05,'/-')
                elif d[3]<15:
                    cur.execute('select * from lunch')
                    a=cur.fetchall()
                    h=['ITEM_NO','ITEM_NAME','ITEM_PRICE']
                    print(tabulate.tabulate(a,h,tablefmt='psql'))
                    M='YES'
                    while M.lower()=='yes':
                        print('press 1 SELECT ITEM')
                        print('press 2 EXIT')
                        se_ch = int(input('ENTER THE CHOICE |--> '))
                        if se_ch == 1:
                            w =input('Enter the item_no: ')
                            cur.execute('SELECT * FROM LUNCH WHERE item_no = %s', (w,))
                            item= cur.fetchone()
                            if item:
                                 h= ['ITEM_NO', 'ITEM_NAME', 'ITEM_PRICE']
                                 print(tabulate.tabulate([item], headers=h, tablefmt='psql'))
                                 cp=item[2]
                                 print('-'*30)
                                 print('\tKINDLY NOTE THE RS.',cp,'/-')
                                 print('-'*30)
                                 cb+=cp
                                 dcb+=cp
                            else:
                                print('ITEM NOT FOUND.PLEASE TRY AGAIN')
                        else:
                            print('==================')
                            print('    THANK YOU     ')
                            print('==================')
                            break
                        M=input('DOU YOU WANT CONTINUE PRESS YES/NO')
                    print('YOUR TOTAL BILL FOR',d[0],'/',d[1],'/',d[2],'IS RS.',dcb+dcb*0.05,'/-')
                elif d[3]<22:
                    cur.execute('select * from DINNER')
                    a=cur.fetchall()
                    h=['ITEM_NO','ITEM_NAME','ITEM_PRICE']
                    print(tabulate.tabulate(a,h,tablefmt='psql'))
                    M='YES'
                    while M.lower()=='yes':
                        print('press 1 SELECT ITEM')
                        print('press 2 EXIT')
                        se_ch = int(input('ENTER THE CHOICE |--> '))
                        if se_ch == 1:
                            w =input('Enter the item_no: ')
                            cur.execute('SELECT * FROM DINNER WHERE item_no = %s', (w,))
                            item = cur.fetchone()
                            if item:
                                 h= ['ITEM_NO', 'ITEM_NAME', 'ITEM_PRICE']
                                 print(tabulate.tabulate([item], headers=h, tablefmt='psql'))
                                 cp=item[2]
                                 print('-'*30)
                                 print('\tKINDLY NOTE THE RS.',cp,'/-')
                                 print('-'*30)
                                 cb+=cp
                                 dcb+=cp
                            else:
                                print('ITEM NOT FOUND.PLEASE TRY AGAIN')
            
                        else:
                            print('==========================')
                            print('        THANK YOU         ')
                            print('==========================')
                        M=input('DOU YOU WANT CONTINUE PRESS YES/NO')
                    print('YOUR TOTAL BILL FOR',d[0],'/',d[1],'/',d[2],'IS RS.',dcb+dcb*0.05,'/-')
            elif ch==2:
                ncb=0
                n=int(input('ENTER YOUR NURSE ID:'))
                loading()
                print('CHOSSE FROM THE BELOW MENU')
                if d[3]<11:
                    cur.execute('select * from breakfast')
                    a=cur.fetchall()
                    h=['ITEM_NO','ITEM_NAME','ITEM_PRICE']
                    print(tabulate.tabulate(a,h,tablefmt='psql'))
                    M='YES'
                    while M.lower()=='yes':
                        print('press 1 SELECT ITEM')
                        print('press 2 EXIT')
                        se_ch = int(input('ENTER THE CHOICE |--> '))
                        if se_ch == 1:
                            w =input('ENTER THE ITEM_NO: ')
                            cur.execute('SELECT * FROM BREAKFAST WHERE item_no = %s', (w,))
                            item = cur.fetchone()
                            if item:
                                 h= ['ITEM_NO', 'ITEM_NAME', 'ITEM_PRICE']
                                 print(tabulate.tabulate([item], headers=h, tablefmt='psql'))
                                 cp=item[2]
                                 print('-'*30)
                                 print('\tKINDLY NOTE THE RS.',cp,'/-')
                                 print('-'*30)
                                 cb+=cp
                                 ncb+=cp
                            else:
                                print('ITEM NOT FOUND.PLEASE TRY AGAIN')
                        else:
                            print('==================')
                            print('    THANK YOU     ')
                            print('==================')
                        M=input('DOU YOU WANT CONTINUE PRESS YES/NO')
                    print('YOUR TOTAL BILL FOR',d[0],'/',d[1],'/',d[2],'IS RS.',ncb+ncb*0.05,'/-')
                elif d[3]<15:
                    cur.execute('select * from lunch')
                    a=cur.fetchall()
                    h=['ITEM_NO','ITEM_NAME','ITEM_PRICE']
                    print(tabulate.tabulate(a,h,tablefmt='psql'))
                    M='YES'
                    while M.lower()=='yes':
                        print('press 1 SELECT ITEM')
                        print('press 2 EXIT')
                        se_ch = int(input('ENTER THE CHOICE |--> '))
                        if se_ch == 1:
                            w =input('ENTER THE ITEM_NO: ')
                            cur.execute('SELECT * FROM LUNCH WHERE item_no = %s', (w,))
                            item = cur.fetchone()
                            if item:
                                 h= ['ITEM_NO', 'ITEM_NAME', 'ITEM_PRICE']
                                 print(tabulate.tabulate([item], headers=h, tablefmt='psql'))
                                 cp=item[2]
                                 print('-'*30)
                                 print('\tKINDLY NOTE THE RS.',cp,'/-')
                                 print('-'*30)
                                 cb+=cp
                                 ncb+=cp
                            else:
                                print('ITEM NOT FOUND.PLEASE TRY AGAIN')
                        else:
                            print('==================')
                            print('    THANK YOU     ')
                            print('==================')
                        M=input('DOU YOU WANT CONTINUE PRESS YES/NO')
                    print('YOUR TOTAL BILL FOR',d[0],'/',d[1],'/',d[2],'IS RS.',ncb+ncb*0.05,'/-')
                elif d[3]<22:
                    cur.execute('select * from DINNER')
                    a=cur.fetchall()
                    h=['ITEM_NO','ITEM_NAME','ITEM_PRICE']
                    print(tabulate.tabulate(a,h,tablefmt='psql'))
                    M='YES'
                    while M.lower()=='yes':
                        print('press 1 SELECT ITEM')
                        print('press 2 EXIT')
                        se_ch = int(input('ENTER THE CHOICE |--> '))
                        if se_ch == 1:
                            w =input('ENTER THE ITEM_NO: ')
                            cur.execute('SELECT * FROM DINNER WHERE item_no = %s', (w,))
                            item = cur.fetchone()
                            if item:
                                 h= ['ITEM_NO', 'ITEM_NAME', 'ITEM_PRICE']
                                 print(tabulate.tabulate([item], headers=h, tablefmt='psql'))
                                 cp=item[2]
                                 print('-'*30)
                                 print('\tKINDLY NOTE THE RS.',cp,'/-')
                                 print('-'*30)
                                 cb+=cp
                                 ncb+=cp
                            else:
                                print('ITEM NOT FOUND.PLEASE TRY AGAIN')
                        else:
                            print('==========================')
                            print('        THANK YOU         ')
                            print('==========================')
                        M=input('DOU YOU WANT CONTINUE PRESS YES/NO')
                    print('YOUR TOTAL BILL FOR',d[0],'/',d[1],'/',d[2],'IS RS.',ncb+ncb*0.05,'/-')
                else:
                    print('INVALID INPUT')
            else:
                break    
#MAIN PROGRAM   
print('〰'*50)
print('-'*30,'WELCOME TO APJ Hospital','-'*40)
print('〰'*50)
print('                                                 -“Where healing and compassion come together”')
d=t.localtime()
print('----Date-',d[2],'/',d[1],'/',d[0] ,'--------------------------------------','Time-',d[3],':',d[4],':',d[5],'--------------')
bill=0
ti='m'
while ti.lower()=='m':
    print('-'*50)
    print('Kindly select who you are:')
    print('\t','1➟PATIENT')
    print('\t','2➟HOSPITAL STAFF')
    try:
        mpc=int(input('ENTER YOUR CHOICE 1/2:'))
        if mpc==1:
            mi='h'
            while mi=='h':
                print('-'*50)
                print('Kindly select from the following :')
                print('\t','MENU')
                print('\t','1➟Appointment')
                print('\t','2➟View Our top Doctors')
                print('\t','3➟Patient(sign in and up)')
                print('\t','4➟Canteen(order food)')
                print('\t','5➟Rooms (book rooms)')
                print('\t','6➟About APJ Hospital')
                print('\t','7➟Give Feedback')
                print('\t','8➟EXIT')
                print('-'*50)
                yuc=int(input('Enter your  choice 1/2/3/4/5/6/7/8'))
                if yuc==1:
                    ans='y'
                    while ans=='y':
                        print('-'*50)
                        print('\t','Please choose from the below options')
                        print('\t','1➟Book an appointment')
                        print('\t','2➟Delete appointment')
                        print('\t','3➟Go back')
                        print('-'*50)
                        ch=int(input('enter your choice'))
                        print('-'*50)
                        if ch==1:
                            loading()
                            print('Enter all details correctly,Check before proceeding')
                            na=input('Enter patient name')
                            doc=input('Enter doctor name')
                            app=input('Enter appointment date(yyyy/m/dd)')
                            tui=float(input('enter time(hr min)(24hr format)'))
                            if int(app[0:4])>=d[0] and int(app[5:7])>=1 and int(app[5:7])<=12:
                                if int(app[0:4])==d[0]:
                                    if int(app[5:7])>=d[1] and int(app[5:7])<=12:
                                        cur.execute("insert into patient_appointment values('{}','{}','{}',{})".format(na,doc,app,tui))
                                        x.commit() 
                                        print('-'*50)
                                        print('-'*10,'APPOINTMENT BOOKED','-'*11)
                                        print('-'*50)
                                    else:
                                        print('\t','!!!!!Please select a valid monnth!!!!')
                                else:
                                    cur.execute("insert into patient_appointment values('{}','{}','{}',{})".format(na,doc,app,tui))
                                    x.commit() 
                                    print('-'*50)
                                    print('-'*10,'APPOINTMENT BOOKED','-'*11)
                                    print('-'*50)

                            else:
                                print('\t','!!!!please select a year in future!!!!')
                        elif ch==2:
                            try:
                                loading()
                                ena=input('Enter patient name to delete the appointment')
                                cur.execute("delete from patient_appointment where Patient_name='{}'".format(ena))
                                x.commit()
                                print('-'*50)
                                print('-'*10,'Patient appointment deleted','-'*11)
                                print('-'*50)
                            except:
                                print('ENTER CORRECT PATIENT NAME')
                        elif ch==3:
                            break
                        ans=input('press y to go back to menu')
                elif yuc==2:
                    print('\t','Top doctors of APJ hospital')
                    cur.execute('select doctorid,doctor_name,qualification,specialist from doctor_details')
                    adv=cur.fetchall()
                    h=['Doctor id','Doctor Name','Qualification','Specialist in']
                    print(tabulate.tabulate(adv,h,tablefmt='psql'))
                elif yuc==3:
                    loading()
                    pat='p'
                    while pat=='p':
                        print('-'*50)
                        print('\t','Choose:')
                        print('\t','1➟SIGN IN(New patient)')
                        print('\t','2➟SIGN UP(Existing patient)')
                        print('\t','3➟Exit')
                        print('-'*50)
                        choicep=int(input('Enter choice 1/2/3'))
                        print('-'*50)
                        if choicep==1:
                            new_patient()
                        elif choicep==2:
                            lo6='o'
                            while lo6=='o':
                                print('-'*50)
                                print("CHOOSE FROM THE BELOW MENU")
                                print('\t','1➟View my details')
                                print('\t','2➟View my total bill')
                                print('\t','3➟Update my details')
                                print('\t','4➟Exit')
                                print('-'*50)
                                choose=int(input('Select your choice 1/2/3/4'))
                                print('-'*50)
                                if choose==1:
                                    search_patient()
                                elif choose==2:
                                    try:
                                        loading()
                                        pid2=int(input('enter your patient id'))
                                        lo2='q'
                                        while lo2=='q':
                                            print('-'*50)
                                            print('Choose from the below:')
                                            print('\t','1➟VIEW ROOM BILL')
                                            print('\t','2➟VIEW CANTEEN BILL')
                                            print('\t','3➟EXIT')
                                            print('-'*50)
                                            ch3=int(input('Enter your choice'))
                                            print('-'*50)
                                            if ch3==1:
                                                cur.execute('select Room_type,no_of_days,total_price from booked_rooms where patient_id={}'.format(pid2))
                                                a=cur.fetchall()
                                                h=['ROOM TYPE','NO OF DAYS','TOTAL PRICE']
                                                print('〰'*20)
                                                print('-'*10,'APJ Hospital','-'*10)
                                                print('〰'*30)
                                                print('-'*10,'ROOM BILL SUMMARY:','-'*10)
                                                print('PATIENT ID:',pid2)
                                                print('BILL-NO:',random.randint(10,79))
                                                print('BILL DATE:',d[2],'/',d[1],'/',d[0])
                                                print('BILL TIME:',d[3],':',d[4],':',d[5])
                                                print(tabulate.tabulate(a,h,tablefmt='rounded_grid'))
                                                print('\t','\t','TOTAL BILL:',a[0][2])
                                                print('-'*60)
                                            elif ch3==2:
                                                cur.execute("select amount,discount_if_any_or_gst_tax,total_amount,patient_id from bill ifexists where patient_id={} and description='canteen'".format(pid2))
                                                cda=cur.fetchall()
                                                hb=['FOOD PRICE','GST','AMOUNT','PATIENT ID']
                                                print('〰'*20)
                                                print('-'*10,'APJ Hospital','-'*10)
                                                print('〰'*30)
                                                print('-'*10,'CANTEEN BILL SUMMARY:','-'*10)
                                                print('PATIENT ID:',pid2)
                                                print('BILL-NO:',random.randint(10,79))
                                                print('BILL DATE:',d[2],'/',d[1],'/',d[0])
                                                print('BILL TIME:',d[3],':',d[4],':',d[5])
                                                cur.execute("select sum(total_amount) from bill where patient_id={} and description='canteen'".format(pid2))
                                                ep=cur.fetchall()
                                                print(tabulate.tabulate(cda,hb,tablefmt='rounded_grid'))
                                                for i in ep:
                                                    for j in i:
                                                        print('\t','    ','TOTAL PRICE:',str(j))
                                                print('-'*30)
                                            else:
                                                break
                                            lo2=input('press q to continue')
                                    except:
                                        print('please enter correct patient id')
                                elif choose==3:
                                   loading()
                                   pidi=int(input('##KINDLY INPUT YOUR PATIENT ID##'))
                                   loop='l'
                                   while loop=='l':
                                       print('-'*50)
                                       print('Choose which you want to update')
                                       print('\t','[MENU]')
                                       print('\t','1➟Name')
                                       print('\t','2➟Age')
                                       print('\t','3➟Phone number')
                                       print('\t','4➟Address')
                                       print('\t','5➟Exit')
                                       print('-'*50)
                                       ucho=int(input('Enter choice'))
                                       print('-'*50)
                                       if ucho==1:
                                           loading()
                                           nnamp=input('Enter new name')
                                           cur.execute("update patientdetails set patientname='{}' where patientid={}".format(nnamp,pidi))
                                           x.commit()
                                           print('\t','---''Name updated successfully''---')
                                           print('Details of patient',nnamp,'after updation')
                                           cur.execute('select * from patientdetails where patientid={}'.format(pidi))
                                           nada=cur.fetchall()
                                           head=['Patient Name','PatientID','Age','Date of birth','Gender','Address','Father name','Mother name','Contact no','Email','Patient Address','Weight','Height','Body temperature']
                                           print(tabulate.tabulate(nada,head,tablefmt='psql'))
                                       elif ucho==2:
                                           loading()
                                           newage=int(input('enter new age'))
                                           cur.execute('update patientdetails set age={} where patientid={}'.format(newage,pidi))
                                           x.commit()
                                           print('\t','---','Age updated successfully','---')
                                           print('Details of patient after updation:')
                                           cur.execute('select * from patientdetails where patientid={}'.format(pidi))
                                           head=['Patient Name','PatientID','Age','Date of birth','Gender','Address','Father name','Mother name','Contact no','Email','Patient Address','Weight','Height','Body temperature']
                                           fetchdet=cur.fetchall()
                                           print(tabulate.tabulate(fetchdet,head,tablefmt='psql'))
                                       elif ucho==3:
                                           loading()
                                           newno=int(input('Enter new contact number'))
                                           cur.execute("update patientdetails set contactno='{}' where patientid={}".format(newno,pidi))
                                           x.commit()
                                           print('\t','---','Contact number updated successfully','---')
                                           print('Details of patient after updation')
                                           cur.execute('select * from patientdetails where patientid={}'.format(pidi))
                                           head=['Patient Name','PatientID','Age','Date of birth','Gender','Address','Father name','Mother name','Contact no','Email','Patient Address','Weight','Height','Body temperature']
                                           fetchdet=cur.fetchall()
                                           print(tabulate.tabulate(fetchdet,head,tablefmt='psql'))
                                       elif ucho==4:
                                           loading()
                                           newadd=input('enter new address')
                                           cur.execute("update patientdetails set address='{}' where patientid={}".format(newadd,pidi))
                                           x.commit()
                                           print('\t','---','Address updated successfully!!!!!!!!!!','---')
                                           print('Details of patient after updation')
                                           cur.execute('select * from patientdetails where patientid={}'.format(pidi))
                                           head=['Patient Name','PatientID','Age','Date of birth','Gender','Address','Father name','Mother name','Contact no','Email','Patient Address','Weight','Height','Body temperature']
                                           fetchdet=cur.fetchall()
                                           print(tabulate.tabulate(fetchdet,head,tablefmt='psql'))
                                       elif ucho==5:
                                           break
                                elif choose==4:
                                    break
                        break
                elif yuc==4:
                    print('='*98)
                    print('='*40,'WELCOME TO CANTEEN','='*38)
                    print('='*98)
                    d=t.localtime()
                    ans='y'
                    cb=0
                    while ans=='y':
                        print('-'*50)
                        print('PRESS 1 IF YOU ARE A PATIENT')
                        print('PRESS 2 IF YOU ARE A VISTOR')
                        print('PRESS 3 IF YOU WANT TO EXIT')
                        print('-'*50)
                        ch=int(input('ENTER YOUR CHOICE:'))
                        print('-'*50)
                        loading()
                        if ch==1:
                            pcb=0
                            p=int(input('ENTER YOUR PATIENT_ID:'))
                            loading()
                            print('CHOSSE FROM THE BELOW MENU')
                            if d[3]<11:
                                cur.execute('select * from breakfast')
                                a=cur.fetchall()
                                h=['ITEM_NO','ITEM_NAME','ITEM_PRICE']
                                print(tabulate.tabulate(a,h,tablefmt='psql'))
                                M='YES'
                                while M.lower()=='yes':
                                    print('press 1 SELECT ITEM')
                                    print('press 2 EXIT')
                                    se_ch = int(input('ENTER THE CHOICE |--> '))
                                    if se_ch == 1:
                                        w =input('Enter the item_no: ')
                                        cur.execute('SELECT * FROM BREAKFAST WHERE item_no = %s', (w,))
                                        item = cur.fetchone()
                                        if item:
                                             h= ['ITEM_NO', 'ITEM_NAME', 'ITEM_PRICE']
                                             print(tabulate.tabulate([item], headers=h, tablefmt='psql'))
                                             cp=item[2]
                                             print('-'*30)
                                             print('\tKINDLY NOTE THE RS.',cp,'/-')
                                             print('-'*30)
                                             cb+=cp
                                             pcb+=cp
                                        else:
                                            print('ITEM NOT FOUND.PLEASE TRY AGAIN')
                           
                                    else:
                                        print('==================')
                                        print('    THANK YOU     ')
                                        print('==================')
                                    M=input('DO YOU WANT CONTINUE PRESS YES/NO')
                                print('YOUR TOTAL BILL FOR',d[0],'/',d[1],'/',d[2],'IS RS.',pcb+pcb*0.05,'/-')
                            elif d[3]<15:
                                cur.execute('select * from lunch')
                                a=cur.fetchall()
                                h=['ITEM_NO','ITEM_NAME','ITEM_PRICE']
                                print(tabulate.tabulate(a,h,tablefmt='psql'))
                                M='YES'
                                while M.lower()=='yes':
                                    print('press 1 SELECT ITEM')
                                    print('press 2 EXIT')
                                    se_ch = int(input('ENTER THE CHOICE |--> '))
                                    if se_ch == 1:
                                        w =input('Enter the item_no: ')
                                        cur.execute('SELECT * FROM LUNCH WHERE item_no = %s', (w,))
                                        item = cur.fetchone()
                                        if item:
                                             h= ['ITEM_NO', 'ITEM_NAME', 'ITEM_PRICE']
                                             print(tabulate.tabulate([item], headers=h, tablefmt='psql'))
                                             cp=item[2]
                                             print('-'*30)
                                             print('\tKINDLY NOTE THE RS.',cp,'/-')
                                             print('-'*30)
                                             cb+=cp
                                             pcb+=cp
                                             cur.execute("insert into bill values ('Canteen',{},'5%GST',{},{})".format(pcb,pcb+(pcb*0.05),p))
                                             x.commit()
                                        else:
                                            print('ITEM NOT FOUND.PLEASE TRY AGAIN')
                                    else:
                                        print('==================')
                                        print('    THANK YOU     ')
                                        print('==================')
                                    M=input('DOU YOU WANT CONTINUE PRESS YES/NO')
                                print('YOUR TOTAL BILL FOR',d[0],'/',d[1],'/',d[2],'IS RS.',pcb+pcb*0.05,'/-')
                            elif d[3]<22:
                                cur.execute('select * from DINNER')
                                a=cur.fetchall()
                                h=['ITEM_NO','ITEM_NAME','ITEM_PRICE']
                                print(tabulate.tabulate(a,h,tablefmt='psql'))
                                M='YES'
                                while M.lower()=='yes':
                                    print('press 1 SELECT ITEM')
                                    print('press 2 EXIT')
                                    se_ch = int(input('ENTER THE CHOICE |--> '))
                                    if se_ch == 1:
                                        w =input('Enter the item_no: ')
                                        cur.execute('SELECT * FROM DINNER WHERE item_no = %s', (w,))
                                        item = cur.fetchone()
                                        if item:
                                             h= ['ITEM_NO', 'ITEM_NAME', 'ITEM_PRICE']
                                             print(tabulate.tabulate([item], headers=h, tablefmt='psql'))
                                             cp=item[2]
                                             print('-'*30)
                                             print('\tKINDLY NOTE THE RS.',cp,'/-')
                                             print('-'*30)
                                             cb+=cp
                                             pcb+=cp
                                             
                                        else:
                                            print('ITEM NOT FOUND.PLEASE TRY AGAIN')
                                    else:
                                        print('==========================')
                                        print('        THANK YOU         ')
                                        print('==========================')
                                    M=input('DOU YOU WANT CONTINUE PRESS YES/NO')
                                print('YOUR TOTAL BILL FOR',d[0],'/',d[1],'/',d[2],'IS RS.',pcb+pcb*0.05,'/-')
                                cur.execute("insert into bill values('Canteen',{},'5%GST',{},{})".format(pcb,pcb+(pcb*0.05),p))
                                x.commit()
                        elif ch==2:
                            vcb=0
                            print('CHOOSE FROM THE BELOW MENU')
                            if d[3]<11:
                                cur.execute('select * from breakfast')
                                a=cur.fetchall()
                                h=['ITEM_NO','ITEM_NAME','ITEM_PRICE']
                                print(tabulate.tabulate(a,h,tablefmt='psql'))
                                M='YES'
                                while M.lower()=='yes':
                                    print('press 1 SELECT ITEM')
                                    print('press 2 EXIT')
                                    se_ch = int(input('ENTER THE CHOICE |--> '))
                                    if se_ch == 1:
                                        w =input('Enter the item_no: ')
                                        cur.execute('SELECT * FROM BREAKFAST WHERE item_no = %s', (w,))
                                        item = cur.fetchone()
                                        if item:
                                             h= ['ITEM_NO', 'ITEM_NAME', 'ITEM_PRICE']
                                             print(tabulate.tabulate([item], headers=h, tablefmt='psql'))
                                             cp=item[2]
                                             print('-'*30)
                                             print('\tKINDLY NOTE THE RS.',cp,'/-')
                                             print('-'*30)
                                             cb+=cp
                                             vcb+=cp
                                        else:
                                            print('ITEM NOT FOUND.PLEASE TRY AGAIN')
                                    else:
                                        print('==================')
                                        print('    THANK YOU     ')
                                        print('==================')
                                    M=input('DOU YOU WANT CONTINUE PRESS YES/NO')
                                print('YOUR TOTAL BILL FOR',d[0],'/',d[1],'/',d[2],'IS RS.',vcb+vcb*0.05,'/-')
                            elif d[3]<15:
                                cur.execute('select * from lunch')
                                a=cur.fetchall()
                                h=['ITEM_NO','ITEM_NAME','ITEM_PRICE']
                                print(tabulate.tabulate(a,h,tablefmt='psql'))
                                M='YES'
                                while M.lower()=='yes':
                                    print('press 1 SELECT ITEM')
                                    print('press 2 EXIT')
                                    se_ch = int(input('ENTER THE CHOICE |--> '))
                                    if se_ch == 1:
                                        w =input('ENTER THE ITEM_NO: ')
                                        cur.execute('SELECT * FROM LUNCH WHERE item_no = %s', (w,))
                                        item = cur.fetchone()
                                        if item:
                                            h= ['ITEM_NO', 'ITEM_NAME', 'ITEM_PRICE']
                                            print(tabulate.tabulate([item], headers=h, tablefmt='psql'))
                                            cp=item[2]
                                            print('-'*30)
                                            print('\tKINDLY NOTE THE RS.',cp,'/-')
                                            print('-'*30)
                                            cb+=cp
                                            vcb+=cp
                                        else:
                                            print('ITEM NOT FOUND.PLEASE TRY AGAIN') 
                                    else:
                                        print('==================')
                                        print('    THANK YOU     ')
                                        print('==================')
                                    M=input('DOU YOU WANT CONTINUE PRESS YES/NO')
                                print('YOUR TOTAL BILL FOR',d[0],'/',d[1],'/',d[2],'IS RS.',vcb+vcb*0.05,'/-')
                            elif d[3]<22:
                                cur.execute('select * from DINNER')
                                a=cur.fetchall()
                                h=['ITEM_NO','ITEM_NAME','ITEM_PRICE']
                                print(tabulate.tabulate(a,h,tablefmt='psql'))
                                M='YES'
                                while M.lower()=='yes':
                                    print('press 1 SELECT ITEM')
                                    print('press 2 EXIT')
                                    se_ch = int(input('ENTER THE CHOICE |--> '))
                                    if se_ch == 1:
                                        w =input('ENTER THE ITEM_NO: ')
                                        cur.execute('SELECT * FROM DINNER WHERE item_no = %s', (w,))
                                        item = cur.fetchone()
                                        if item:
                                             h= ['ITEM_NO', 'ITEM_NAME', 'ITEM_PRICE']
                                             print(tabulate.tabulate([item], headers=h, tablefmt='psql'))
                                             cp=item[2]
                                             print('-'*30)
                                             print('\tKINDLY NOTE THE RS.',cp,'/-')
                                             print('-'*30)
                                             cb+=cp
                                             #bill+=cp
                                             vcb+=cp
                                        else:
                                             print('ITEM NOT FOUND.PLEASE TRY AGAIN')
                                    else:
                                        print('==========================')
                                        print('        THANK YOU         ')
                                        print('==========================')
                                    M=input('DOU YOU WANT CONTINUE PRESS YES/NO')
                                print('YOUR TOTAL BILL FOR',d[0],'/',d[1],'/',d[2],'IS RS.',vcb+vcb*0.05,'/-')
                        elif ch==3:
                            break
                elif yuc==5:
                    rooms()
                elif yuc==6:
                    print('〰'*50)
                    print('-'*30,'Welcome to APJ Hospital','-'*40)
                    print('〰'*50)
                    print('\t','Our patients are our priority, we offer quality medical services with a team of specialists.')
                    print('\t','Our mission is to improve the health of our community by providing high-quality, comprehensive medical care in a welcoming and compassionate environment.')
                    print('➟On behalf of the entire doctors, we would like to welcome you to our clinic. We are pleased to have the opportunity to assist you with your physical therapy care. Our goal is to provide the highest quality and most up-to-date physical therapy treatments available in a professional and caring manner,')
                    print('➟We are committed to helping you attain your rehabilitation goals. It is also our goal to provide you with outstanding service.')
                    print('')
                    print('_'*70)
                    print('\t','Why Choose us?')
                    print('➟Center of Excellence in Advanced Cancer Care')
                    print('➟Center of Excellence in Advanced Surgeries')
                    print('➟Best of Class and Best in Breed Specialists')
                    print('➟State-of-art Operating Theatres, ICU and related infrastructure')
                    print('➟All beds of international make')     
                    print('➟Comfortable waiting and ICU lounges')
                    print('➟Fully Air-Conditioned Wi-Fi enabled Hospital')
                    print('➟Happy to Help service that makes you feel at home, (we move around while you remain seated)')
                    ch=input('Do you want to view more details y/n')
                    if ch=='y':
                       loading()
                       l2='l'
                       while l2=='l':
                          print('-'*50)
                          print('\t','Choose from the below')
                          print('\t','1➟International patient services')
                          print('\t','2➟Highlights')
                          print('\t','3➟Go back')
                          print('-'*50)
                          choi=int(input('Enter your choice 1/2/3'))
                          print('-'*50)
                          if choi==1:
                              loading()
                              print('INTERNATIONAL PATIENT SREVICES:')
                              print('')
                              print('~Pre-travel medical opinions and appointments')
                              print('')
                              print('~Translation services for medical and non-medical communication')
                              print('')
                              print('~Accommodation bookings for patients and their families')
                              print('')
                              print('~Emergency and non-emergency care services')
                              print('')
                              print('~Assistance with flight arrangements and airport transfers')
                              print('')
                              print('~Arrangements for special dietary requirements')
                              print('')
                              print('~Visa application and extension supportVisa application and extension support')
                              print('')
                              print('~Financial counseling and cost estimates for medical treatments')
                          elif choi==2:
                              loading()
                              print('HOSPITAL HIGHLIGHTS :')
                              print('')
                              print('-->State-of-the-Art Planning, Design, Architecture and Infrastructure')
                              print('')
                              print('-->Cutting-Edge Technology, Equipment, and Resources')
                              print('')
                              print('-->High-Quality Care with No Differentiation in Service')
                              print('')
                              print('-->Scalable, Multi-Use In-Patient and Isolation Rooms')
                              print('')
                              print('-->Fully-Digitised, Instant Access to Patient Medical Records')
                              print('')
                              print('-->National and International Green Building Conformance')
                          elif choi==3:
                              loading()
                              break
                          l2=input('Enter l to continue')
                    elif ch=='n':
                       None
                elif yuc==7:
                    loading()
                    print('\t','-----------THANKYOU FOR VISITING APJ HOSPITAL-----------')
                    print('➟GIVE FEEDBACK SO WE COULD IMPROVE OURSELVES')
                    print('\t','Rate:')
                    print('\t','1➟☆☆☆☆★')
                    print('\t','2➟☆☆☆★★')
                    print('\t','3➟☆☆★★★')
                    print('\t','4➟☆★★★★')
                    print('\t','5➟★★★★★')
                    rev=int(input('RATE 1-5'))
                    print('!!RATING SUBMITTED ON:',d[0],'/',d[1],'/',d[2])
                    print('')
                    print('➟WRITE REVIEW')
                    REV2=input('Write Review')
                    print('##THANKYOU FOR REVIEWING OUR HOSPITAL##')
                    print('##WE ARE SORRY FOR THE INCONVENIENCE CAUSED IF ANY WE WILL FIX IT VERY SOON##')
                    print('')
                    print('!!REVIEW SUBMITTED ON:',d[0],'/',d[1],'/',d[2])
                elif yuc==8:
                    break
        elif mpc==2:
            wo3='w'
            while wo3=='w':
                print('-'*50)
                print('Kindly select from the following :')
                print('\t','MENU')
                print('\t','1➟Appointment Management')
                print('\t','2➟Hospital Staff Management')
                print('\t','3➟Pharmacy Management')
                print('\t','4➟Rooms Management')
                print('\t','5➟Ambulance driver Management')
                print('\t','6➟Canteen')
                print('\t','7➟View rating reviews')
                print('\t','8➟EXIT')
                print('-'*50)
                chm2=int(input('Enter your choice 1/2/3/4/5/6/7/8'))
                if chm2==1:
                    ans='y'
                    while ans=='y':
                        print('-'*50)
                        print('\t','Please choose from the below options')
                        print('\t','1➟View existing appointments')
                        print('\t','2➟Delete an appointment')
                        print('\t','3➟Go back')
                        print('-'*50)
                        ch=int(input('enter your choice'))
                        print('-'*50)
                        if ch==1:
                            loading()
                            cur.execute('select * from patient_appointment ifexists')
                            a=cur.fetchall()
                            h=['Patient name','Doctor name','Date','Time']
                            print('EXISTING APPOINTMENTS')
                            print(tabulate.tabulate(a,h,tablefmt='psql'))
                        elif ch==2:
                            try:
                                loading()
                                ena=input('Enter patient name to delete the appointment')
                                cur.execute("delete from patient_appointment where Patient_name='{}'".format(ena))
                                x.commit()
                                print('-'*50)
                                print('-'*10,'Patient appointment deleted','-'*11)
                                print('-'*50)
                            except:
                                print('ENTER CORRECT PATIENT NAME')
                        elif ch==3:
                            break
                        ans=input('enter y to continue')
                elif chm2==2:
                    loading()
                    wor='p'
                    while wor=='p':
                        print('-'*50)
                        print('\t','Choose:')
                        print('\t','1➟Doctor')
                        print('\t','2➟Nurse')
                        print('\t','3➟Exit')
                        print('-'*50)
                        choicep=int(input('Enter choice 1/2/3'))
                        print('-'*50)
                        if choicep==1:
                            lo8='l'
                            while lo8=='l':
                                print('\t','1➟SIGN IN')
                                print('\t','2➟SIGN UP')
                                print('\t','3➟Exit')
                                yuch=int(input('Enter your choice'))
                                if yuch==1:
                                    new_doctor()
                                elif yuch==2:
                                    search_doctor()
                                elif yuch==3:
                                    break
                                lo8=input('Enter l to continue')
                        elif choicep==2:
                            loading()
                            l3='l'
                            while l3.lower()=='l':
                                print('-'*50)
                                print("CHOOSE FROM THE BELOW MENU")
                                print('\t','1➟SIGN IN')
                                print('\t','2➟SIGN UP')
                                print('\t','3➟Exit')
                                print('-'*50)
                                chowa=int(input('Select your choice 1/2/3'))
                                print('-'*50)
                                if chowa==1:
                                    new_nurse()
                                elif chowa==2:
                                    nursignup()
                                elif chowa==3:
                                    break
                        elif choicep==3:
                            break
                elif chm2==3:
                    medicines()
                elif chm2==4:
                    rooms()
                elif chm2==5:
                    ambulance_driver()
                elif chm2==6:
                    worker_canteen()
                elif chm2==7:
                    print('HOSPITAL RATING AND REVIEW')
                    cur.execute('select * from review')
                    h=cur.fetchall()
                    d4=['Rating','Review','Date','Patient Id']
                    print(tabulate.tabulate(h,d4,tablefmt='psql'))
                elif chm2==8:
                    break
    except ValueError:
        print('PLEASE ENTER INTEGER VALUE,TRY AGAIN')
    except IndexError:
        print('#An unknown Error occurred#,Reload the programtwice')
    except SyntaxError:
        print('#An unknown Error occurred#,Reload the programthrice')
    except NameError:
        print('#An unknown Error occurred#,Reload the programfourth')
    except TypeError:
        print('#An Error occurred#,Reload the programquartzth')
    ti=input('PRESS M IF YOU WANT GO BACK TO LOGIN MENU')
print('-'*20,'WHEREVER THE ART OF MEDICINE IS LOVED THERE IS ALWAYS A LOVE OF HUMANITY','-'*20)
print('THANKYOU FOR CHOOSING OUR HOSPITAL,WE HOPE THAT YOU HAD ALL YOUR HEALTH ISSUES CURED!!!!!')                                                                                                                

            
