# Countdown Timer

A simple and flexible **Python Countdown Timer** that allows the user to enter hours, minutes, and seconds, then counts down the time in **hh:mm:ss** format. The timer updates every second and notifies the user when the time is up.

## Features

- Allows user to input hours, minutes, and seconds separately.
- Displays time in **hh:mm:ss** format.
- Flexible input: you can choose to only input hours, minutes, or seconds based on your needs.
- Counts down one second at a time and prints the updated time in real-time.
- When the timer reaches zero, the program will display "Time's up! 🚨".

## How to Use

1. **Clone the repository** to your local machine.
   
(https://github.com/kavitsheth/Countdown-Timer.git)

markdown
Copy

2. **Navigate to the project directory**:

cd Countdown-Timer

markdown
Copy

3. **Run the program**:

python main.py

markdown
Copy

4. **Follow the prompts**:
 - Enter if you want to input **hours**, **minutes**, or **seconds**.
 - The program will then display the countdown in **hh:mm:ss** format.

## Example Usage

When you run the program, it will ask:
Welcome to the Countdown Timer! Do you want to enter hours? (yes/no): yes Enter the number of hours: 2 Do you want to enter minutes? (yes/no): no Do you want to enter seconds? (yes/no): yes Enter the number of seconds: 45

sql
Copy

The program will then calculate the total time (2 hours and 45 seconds) and begin the countdown:
02:00:45 02:00:44 02:00:43 ... Time's up! 🚨

pgsql
Copy

## Code Explanation

- **`countdown_timer()`**: This function takes the total time in seconds and counts down. It uses `divmod()` to convert total seconds into hours, minutes, and seconds, and then formats the countdown in **hh:mm:ss** format. The timer updates every second using `time.sleep(1)`.
  
- **`main()`**: This function asks the user what units of time they want to input (hours, minutes, and/or seconds). It then calls `countdown_timer()` with the calculated total seconds.
  
## Requirements

- Python 3.x
- No additional libraries or dependencies are required beyond Python's built-in libraries.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
