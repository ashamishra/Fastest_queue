#! python3
# data set collection for queue

import time
import statistics

# Instructions.
print('Press ENTER to begin. Afterwards, press ENTER to end the stopwatch.Press Ctrl-C to quit.')

custNum = 0		# Customer count
count = 0		# to check if customer has started billing(count=1)
custList = []		#list of Customer time data

# To track customer time.
try:
  while True:
         input()                     # press Enter to begin
         count = 1
         print('In...',end='')
         startTime = time.time()    # In time
         custNum += 1

         if count:
           input()
           print('Out.')
           lastTime = time.time()	# Out Time
           lapTime = round(lastTime - startTime, 2)	#Out Time - In Time
           custList.append(lapTime)
           avgTime = round(statistics.mean(custList),2)	#Average time per person
           print('Customer #%s: %s (Avg Time per person: %s)' % (custNum, lapTime, avgTime))
       	   
       	   count -= 1
except KeyboardInterrupt:
       # Handle the Ctrl-C exception to keep its error message from displaying.
       print('\nDone.')
