import time
import csv
import datetime as dt
import os
import serial
import threading
import micropyGPS as mpG

PATH = ['/home','/pi','/GPS_DATAs','/GPS_DATA_',[],'.csv']

#path_day = 0
day = 0
gps = mpG.MicropyGPS(9,'dd')

def rungps():
    s = serial.Serial('/dev/serial0',9600,timeout=10)
    s.readline()
    while(1):
        sentence = s.readline().decode('utf-8')
        if sentence[0] != '$':
            continue
        for x in sentence:
            gps.update(x)


gpsthread = threading.Thread(target=rungps,args=())
gpsthread.daemon = True
gpsthread.start()

def create_path(PATH):
    path = ''
    for i in range(PATH):
        path = path + PATH[i]
    return path

if __name__ == '__main__':
    print('HELLO')
    
    while(1):
        #path_day = dt.date.today()
        day = dt.tatetime.now().day
        #print(day)
        ymd = str(dt.datetime.now().year)+'-'+str(dt.datetime.now().month)+'-'+str(day)
        #print(ymd)
        PATH[4] = ymd
        #print(PATH)
        path = create_path(PATH)
        print('path =',path)
        
        if os.path.isfile(path) == True:
            print('Found the file specified by the path')
            f = open(path,'w',encoding='utf-8')
        elif os.path.isfile(path) =- False:
            print('Could not find the file specified by the path')
            f = open(path,'x',encoding='utf-8')
        else:
            print('An unknown ERROR occurred')
            exit(-1)
        
        writer = csv.writer(f)
        writer.writerow(['hello user.',dt.datetime.now()])
        
        while(1):
            time.sleep(1.0)
            f.write('%2.8f' % gps.latitude[0])
            f.write(',')
            f.write('%2.8f' % gps.longitude[0])
            f.write(',')
            f.write('%f' % gps.altitude)
            f.write('\n')
            #print('%2.8f,%2.8f,%f'%(gps.latitude[0],gps.longitude[0],gps.altitude))
            if (dt.datetime.now().day != day and(dt.datetime.now().second == 0 or de.datetime.now().second == 1)):
                writer.writerow(['Good_bye user.',dt.datetime.now()])
                time.sleep()
                break
        f.close()
        #break
    #print('test compleat')

'''
Python3
動作環境
Raspberry Pi3 --Linux(Raspbian)--
'''