import time

# Countdown Timer Function
def countdown_timer(seconds):
    while seconds:  # Keep going as long as seconds are left
        mins, secs = divmod(seconds, 60)  # Convert total seconds into minutes and seconds
        hours, mins = divmod(mins, 60)  # Convert minutes into hours and remaining minutes
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)  # Show time in hh:mm:ss format
        print(timer, end="\r")  # Print the time on the same line (replacing the old one)
        time.sleep(1)  # Wait for 1 second before doing the next step
        seconds -= 1  # Subtract 1 second from the time
    
    print("Time's up! 🚨")  # When it reaches zero, show this message

# Main Function
def main():
    print("Welcome to the Countdown Timer!")
    
    # Initialize total_seconds to zero
    total_seconds = 0

    # Ask the user what they want to enter
    hours_input = input("Do you want to enter hours? (yes/no): ").strip().lower()
    if hours_input == 'yes':
        hours = int(input("Enter the number of hours: "))
        total_seconds += hours * 3600  # Convert hours to seconds

    minutes_input = input("Do you want to enter minutes? (yes/no): ").strip().lower()
    if minutes_input == 'yes':
        minutes = int(input("Enter the number of minutes: "))
        total_seconds += minutes * 60  # Convert minutes to seconds

    seconds_input = input("Do you want to enter seconds? (yes/no): ").strip().lower()
    if seconds_input == 'yes':
        seconds = int(input("Enter the number of seconds: "))
        total_seconds += seconds  # Add seconds directly to total seconds

    if total_seconds <= 0:
        print("Please enter a positive number for the time.")
    else:
        countdown_timer(total_seconds)

# Run the program
if __name__ == "__main__":
    main()
