# Importing libraries
import pyautogui as notification
import schedule
import time
import os
from colorama import Fore, Style, init

# Initialization for the colorama lib
init(autoreset=True)


def script():
	# Defining the alert function
	def alert(message):
		# Printing text on screen
		print(Fore.GREEN + Style.BRIGHT + "[+] Notification Sent")
		# Sending the notification 
		notification.alert(text=message, title="Notification System by Arshan")

	# Defining main function
	def main():
		# Loops as long as "False" isn't returned
		while True:
			# Runs any scheduled tasks
			schedule.run_pending()
			# Interval
			time.sleep(1)

	# Storing user input as variable
	messageToShow = input(Fore.YELLOW + Style.BRIGHT + "[?] Notification Message: ")

	# If variable is empty then exit the script with a message
	if messageToShow == "":
		print(Fore.RED + Style.BRIGHT + "[-] Please enter a valid value")
		exit()
	elif messageToShow == " ":
		print(Fore.RED + Style.BRIGHT + "[-] Please enter a valid value")
		exit()

	amountOfTimeToWait = input(Fore.YELLOW + Style.BRIGHT + "[?] Run every: ")
	if amountOfTimeToWait == "":
		print(Fore.RED + Style.BRIGHT + "[-] Please enter a valid value")
		exit()
	elif amountOfTimeToWait == " ":
		print(Fore.RED + Style.BRIGHT + "[-] Please enter a valid value")
		exit()
	# Clear screen, tries to run the 'cls' command and if it fails it runs the 'clear' command
	# 'cls' clears the screen on windows computers while 'clear' works on unix based systems such as linux
	os.system("cls;clear")

	# Checking if string is in variable
	if "second" in amountOfTimeToWait:
		# Fetches any numbers inside string
		time1 = int(''.join(char for char in amountOfTimeToWait if char.isdigit()))
		# Takes the number in string and converts it to a integer and then runs the scheduler
		schedule.every(int(time1)).seconds.do(alert, messageToShow)
		# Prints message
		print(Fore.MAGENTA + Style.BRIGHT + "[!] Every " + amountOfTimeToWait + " the message '" + messageToShow + "' will be displayed")
		# Runs main function
		main()
	elif "minute" in amountOfTimeToWait:
		time2 = int(''.join(char for char in amountOfTimeToWait if char.isdigit()))
		schedule.every(int(time2)).minutes.do(alert, messageToShow)
		print(Fore.MAGENTA + Style.BRIGHT + "[!] Every " + amountOfTimeToWait + " the message '" + messageToShow + "' will be displayed")
		main()
	elif "hour" in amountOfTimeToWait:
		time3 = int(''.join(char for char in amountOfTimeToWait if char.isdigit()))
		schedule.every(int(time3)).hours.do(alert, messageToShow)
		print(Fore.MAGENTA + Style.BRIGHT + "[!] Every " + amountOfTimeToWait + " the message '" + messageToShow + "' will be displayed")
		main()
	else:
		print(Fore.RED + Style.BRIGHT + "[-] Please enter a valid time")
		exit()

if __name__ == '__main__':
    try:
        script()
    except KeyboardInterrupt:
        os.system("cls;clear")
        print(Fore.RED + Style.BRIGHT + "[!] Exiting")
