import time
import datetime
import schedule
def fun():
	print("Inside fun at :",datetime.datetime.now())
def main():
	print("Inside automation script at:",datetime.datetime.now())
	schedule.every(20).seconds.do(fun)

	while True:
		schedule.run_pending()#Run pending tasks
		time.sleep(1)#Without sleep(1), the while loop would execute continuously and consume unnecessary CPU resources

		

	
if __name__ == "__main__":
	main()