# import datetime as dt
# total_count = 0 #total number of people = out_count
# counter = 0
# time1 = dt.datetime.now()
# time2 = time1 + dt.timedelta(minutes = 2)
# time_diff = (time2 - time1).total_seconds()
#
#
# def display_time(people_in_queue,avg_time):
#     print(people_in_queue*avg_time)
#
# def find_avg(prev_avg, new_time, person_count):
#     return (prev_avg*(person_count-1) + new_time)/(person_count))
#
# display_time(total_count,new_avg_time)

######################################
import statistics
import datetime as dt
# time11 = dt.datetime.now()
# time12 = time11 + dt.timedelta(minutes = 2)
# time21 = time11 + dt.timedelta(minutes = 1)
# time22 = time21 + dt.timedelta(minutes = 5)
# data = [[time11,time12],[time21,time22]]
# [print(my_time[0].minute,my_time[1].minute) for my_time in data]
# print(data)

def find_avg(sensor_time, count=1):
    '''
    Calculates the average time based on the in and out time.
    Also taking into consideration count i.e size od data set
    '''
    time_per_person = []
    while count > 0:
        time_per_person.append((sensor_time[count-1][1] - sensor_time[count-1][0]).total_seconds())
        count -= 1
    print(time_per_person)
    avg_time = statistics.mean(time_per_person)
    return avg_time/60


def display_time(people_in_queue,avg_time):
    '''
    Display time required to clear the queue;
    Calculates based on: people_in_queue * avg_time
    '''
    return (people_in_queue*avg_time)

count = 2  #counter value; no.of people inside queue
people_count = 6    # no. of people that have already completed billing
with open('time_stamp','r') as f:   #fetching data from text file with data in the format of in-time;out-time
    file_data = [time_data.strip().split(';') for time_data in f]
# Converting data in datetime object 
time_stamp = [[dt.datetime.strptime(times[0],"%Y-%m-%d %H:%M:%S"),dt.datetime.strptime(times[1],"%Y-%m-%d %H:%M:%S")] for times in file_data ]

avg_time_per_person = find_avg(time_stamp,people_count)
print(avg_time_per_person,display_time(count,avg_time_per_person))
