import time
import winsound
def myalarm():
    try:
        mytime=list(map(int,input("Enter time in hour minute second\n").split()))
        if(len(mytime)==3):
            total_seconds=mytime[0]*60*60+mytime[1]*60+mytime[2]
            time.sleep(total_seconds)
            frequebcy=2500 #25
            duration=1000 # 1000ms=1s
            winsound.Beep(frequebcy,duration)
        else:
            print("Enter time in correct format as mentioned\n")
            myalarm()
    except Exception as e:
        print("this is the exception\n",e,"So! please eneter correct details\n")
        myalarm()
myalarm()
