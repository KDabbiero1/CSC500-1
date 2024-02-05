def get_current_time_and_hours():
    currentTime = int(input("What is the current time in hours (0-24):"))
    hours = int(input("How many hours till the alarm goes off:"))
    return currentTime, hours

def calc_start_24_hour_time(currentTime):
    if currentTime == 0:
        start_time = 12
        start_am_pm = 'am'
    elif currentTime < 12:
        start_time = currentTime
        start_am_pm = 'am'
    elif currentTime == 12:
        start_time = currentTime
        start_am_pm = 'pm'
    else:
        start_time = currentTime - 12
        start_am_pm = 'pm'
    return start_time, start_am_pm
    
def calc_end_24_hour_time(currentTime, hours):
    total_time = currentTime + hours
    mod = total_time % 24
    if mod == 0:
        end_time = 12
        end_am_pm = 'am'
    elif mod < 12:
        end_time = mod
        end_am_pm = 'am'
    elif mod == 12:
        end_time = mod
        end_am_pm = 'pm'
    else:
        end_time = mod - 12
        end_am_pm = 'pm'
    return end_time, end_am_pm

def main():
    currentTime, hours = get_current_time_and_hours()
    start_time, start_am_pm = calc_start_24_hour_time(currentTime)
    end_time, end_am_pm = calc_end_24_hour_time(currentTime, hours)
    print(f"Current time:{start_time} {start_am_pm} + {hours} hours\nAlarm Time: {end_time} {end_am_pm} ")

main()
