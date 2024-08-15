#alarm time 

import time

alarm_time = int(input("Enter alarm time (HH:MM): "))
while True:
    current_time = time.strftime("%H:%M")
    if current_time == alarm_time:
      print("Alarm!")
      break 
    time.sleep(1)