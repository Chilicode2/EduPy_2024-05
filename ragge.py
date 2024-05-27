# erik_budisavljevic erik.budisavljevic.itsak23@edu.edugrade.se 
import sys

error_count = 0
notice_count = 0

def process_logfile(filepath, action):
    try:
        # Open the log file
        with open(filepath, 'r') as log:
            # Read all lines from the log file
            logs = log.readlines()

            if action == 'statistics':  # Check the action provided
                process_statistics(logs)
            elif action == 'notices':
                process_line(logs)  # Call function to process notices
            elif action == 'errors':
                process_line(logs)  # Call function to process errors
            else:
                print("Invalid action. Please choose 'statistics', 'notices', or 'errors'.")
    except FileNotFoundError:
        print("File not found. Please provide a valid filepath.")

def process_statistics(logs):
    global error_count, notice_count
    for line in logs:
        if 'error' in line.lower():
            error_count += 1
        elif 'notice' in line.lower():
            notice_count += 1
    print(f"errors: {error_count}\nnotice: {notice_count}")

def process_line(logs):
    for line in logs:
        if action == 'notices': # if 3rd argument == notices
            if "[notice]" in line:
                split_line = line.split() # split that from whitespaces
                split_line.remove("[notice]")
                print(*split_line)# * prints all of Xx_line_xX instead of compartmentalising each word/strings. <- Ugly asf
        elif action == 'errors':
            if "[error]" in line:
                split_line = line.split()
                split_line.remove("[error]")
                print(*split_line)
        else:
            print("Invalid action. Please choose 'statistics', 'notices', or 'errors'.")

if __name__ == "__main__":  # Check if the script is being run directly
    # Check if enough arguments are provided
    if len(sys.argv) < 3:
        print("Usage: python script_name.py <filepath> <action>")
    else:
        filepath = str(sys.argv[1])
        action = str(sys.argv[2])
        process_logfile(filepath, action)