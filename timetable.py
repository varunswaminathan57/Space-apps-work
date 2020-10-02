
# --------------------------------------INPUTS CONSIDERED----------------------------------
# DATES[MM//DD/YYYY] - LAUNCH START,DOCK
# TRAVEL - SOURCE , DESTINATION , TIME PERIOD 
# PERSONAL - WORK SCHEDULE , PREFERRED TIME OF SLEEP , NO OF HOURS OF SLEEP  
#
#--------------------------------------REQUIRED OUTPUT------------------------------------------
# SLEEP TIMETABLE, EXCERCISE TIME TABLE , MEAL TIME TABLE [BFAST,LUNCH,DINNER,SNACK{maybe}]
import datetime as dt


no_of_days_completed = 0

def find_no_of_days(launch_date,launch_time,land_date,land_time,dock_date,dock_time,undock_date,undock_time):

    #varun gonna give this function
    
    #return values - integer  = no of days starting from launch to dock in space and dock,undock in iss 
    #rocketday = launch-dock in hours
    #issday = dock-undoc in hours
    #landday = undoc-land in hours
    rocketday_datesec = (launch_date - dock_date).totalseconds()
    rocketday_timesec = (launch_time - dock_time).totalseconds() 
    rocketday = (rocketday_datesec*3600) + (rocketday_timesec*3600)
    issday_datesec = (dock_date - undock_date).totalseconds()
    issday_timesec = (dock_time - undock_time).totalseconds()
    issday = (issday_datesec*3600) + (issday_timesec*3600)
    landday_datesec = (undock_date - land_date).totalseconds()
    landday_timesec = (undock_time - undock_time).totalseconds()
    landday = (landday_datesec*3600) + (landday_timesec*3600)
              
              
def get_daily_timetable(no_of_sleep_hours,no_of_work_hours,sleep_preferred):

    timetable_total=[]
    #PARAMETERS
    #SLEEP HOURS - INT
    #WORK HOURS - INT
    #SLEEP PREFERED - INT (PREFERRED TIME OF SLEEP)

    next_wakeup = sleep_preferred+no_of_sleep_hours
    
    if next_wakeup>=24:
        next_wakeup-=24

    #if already in ISS
    
    #issday is the no of days the pilot stays in the international space station
    #timetable for the number of days astronaut stays in the ISS

    while(no_of_days_completed>issday):
        #timetable for one day
        timetable_oneday = []
        #says what day is the upcoming timetable is for
        timetable_oneday.append("Day "+str(no_of_days_completed))
        
        wakeup_time = next_wakeup  #hardcoded
        if(wakeup_time>=24):
            wakeup_time-=24
        
        breakfast_time = wakeuptime+1
        if breakfast_time>=24:
            breakfast_time-=24
        
        breakfast_end = breakfast_time+1
        if breakfast_end>=24:
            breakfast_end-=24

        workout_time =breakfast_end+0.5 
        if workout_time>=24:
            workout_time-=24

        work_time = workout_time+2
            if work_time>=24:
                work_time-=24 

        lunch_time = work_time+(no_of_work_hours/2)
            if lunch_time>=24:
                    lunch_time-=24 

        work_resume = lunch_time+1
            if work_resume>=24:
                    work_resume-=24  

        work_finish = work_resume+(no_of_work_hours/2)
            if work_finish>=24:
                    work_finish-=24 

        dinner_start = work_finish+1
        if dinner_start>=24:
            dinner_start-=24
            issday-=1
        
        dinner_end = dinner_start+1
        if dinner_end>=24:
            dinner_end-=24
            issday-=1
       
        sleep_time = dinner_end+1
        if sleep_time>=24:
            sleep_time-=24
            issday-=1
        
        next_wakeup = sleep_time+no_of_sleep_hours
        
        timetable_oneday.append("Wake up and freshen up: "+str(wakeup_time)+":00 - "+str(breakfast_time)+":00")
        timetable_oneday.append("Breakfast: "+str(breakfast_time)+":00 - "+str(workout_time)+":00")
        timetable_oneday.append("Workout: "+str(workout_time)+":00 - "+str(work_time)+":00")
        timetable_oneday.append("Start Work: "+str(work_time)+":00 - "+str(lunch_time)+":00")
        timetable_oneday.append("Lunch: "+str(lunch_time)+":00 - "+str(work_resume)+":00")
        timetable_oneday.append("Resume Work: "+str(work_resume)+":00 - "+str(dinner_start)+":00")
        timetable_oneday.append("Dinner time: "+str(dinner_start)+":00 - "+str(dinner_end)+":00")
        timetable_oneday.append("Sleep Time: "+str(sleep_time)+":00 - "+str(next_wakeup)+":00")

        #end of one day
        no_of_days_completed+=1
        #one day timetable appeneded to master timetable
        timetable_total.append(timetable_oneday)

            

            
#for getting inputs
def solve():
    
    S1 = input("Enter launch date in DD MM YYYY format")
    launch_date = datetime.datetime.strptime(S1, "%d %b %Y")
    S2 = input("Enter launch time in hrs:min:sec")
    launch_time = datetime.datetime.strptime(S2, "%H:%M:%S")
    S3 = input("Enter Landing date in DD MM YYYY format")
    land_date = datetime.datetime.strptime(S3, "%d %b %Y")
    S4 = input("Enter land time in hrs:min:sec")
    land_time = datetime.datetime.strptime(S4, "%H:%M:%S")
    S5 = input("Enter dock date DD MM YYYY format")
    dock_date = = datetime.datetime.strptime(S5, "%d %b %Y")
    S6 = input("Enter dock time in hrs:min:sec")
    dock_time = datetime.datetime.strptime(S6, "%H:%M:%S")
    S7 = input("Enter undock date in DD MM YYYY format")
    undock_date = datetime.datetime.strptime(S7, "%d %b %Y")
    S8 = input("Enter undock time in hrs:min:sec")
    undock_time = datetime.datetime.strptime(S8, "%H:%M:%S")

    no_of_rocketdays,no_of_issdays = find_no_of_days(launch_date,dock_date,undock_date)

    sleep_hours = int(input("Enter number of sleep hours"))
    sleep_preferred = int(intput("Entered preffered time to sleep [in 24 hour format]"))
    work_hours = int(input("Enter number of work hours"))

    get_daily_timetable(sleep_hours,work_hours,sleep_preferred)



solve()
