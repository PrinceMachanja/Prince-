def classify_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Repeatedly prompt the user until a valid integer is entered
while True:
    user_input = input("Enter an integer: ")
    try:
        number = int(user_input)
        result = classify_number(number)
        print(f"The number is {result}.")
        break  # Exit the loop after a valid input
    except ValueError:
        print("That's not a valid integer. Please try again.")

#QUESTION 2
def calculate_average(*args):
    """
    Calculate the average of a variable number of numeric arguments.

    Parameters:
    *args (float or int): A sequence of numbers to average.

    Returns:
    float: The average of the input numbers.
           Returns 0.0 if no arguments are provided.

    Example:
    >>> calculate_average(10, 20, 30)
    20.0
    """
    if not args:
        return 0.0
    return sum(args) / len(args)

#QUESTION 3
while True:
    try:
        user_input = input("Please enter a number: ")
        number = float(user_input)  # You can use int() if you want only integers
        print(f"Thank you! You entered the number: {number}")
        break  # Exit the loop once a valid number is entered
    except ValueError:
        print("Oops! That wasn't a valid number. Please try again.")

#Question4
# List of names to write
names = ["Pincho", "Baller", "Choppa", "Diana", "Ethan"]

# Write names to names.txt, each on a new line
with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

# Read and print each name from names.txt
with open("names.txt", "r") as file:
    for line in file:
        print(line.strip())  # .strip() removes the newline character

#Question5
# Sample list of temperatures in Celsius
celsius_temps = [0, 10, 20, 30, 37, 100]

# Convert to Fahrenheit using lambda and map
fahrenheit_temps = list(map(lambda c: c * 9/5 + 32, celsius_temps))

# Print the converted list
print("Celsius temperatures:", celsius_temps)
print("Fahrenheit temperatures:", fahrenheit_temps)

#QUESTION6
def divide_numbers(numerator, denominator):
    """
    Divides the numerator by the denominator and handles exceptions.

    Parameters:
    numerator (int or float): The number to be divided.
    denominator (int or float): The number to divide by.

    Returns:
    float: The result of the division if successful.
    None: If an exception occurs.

    Exceptions Handled:
    - ZeroDivisionError: If denominator is zero.
    - TypeError: If inputs are not numbers.
    """
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Both inputs must be numbers.")

# Example usage
print(divide_numbers(10, 2))     # ➞ 5.0
print(divide_numbers(10, 0))     # ➞ Error message
print(divide_numbers("10", 2))   # ➞ Error message

#QUESTION 7
# Define the custom exception
class NegativeNumberError(Exception):
    """Exception raised when a negative number is encountered."""
    def __init__(self, value):
        super().__init__(f"Negative number error: {value} is not allowed.")
        self.value = value

# Function that checks if a number is positive
def check_positive(number):
    """
    Raises NegativeNumberError if the input number is negative.

    Parameters:
    number (int or float): The number to check.

    Returns:
    str: Confirmation message if the number is non-negative.
    """
    if number < 0:
        raise NegativeNumberError(number)
    return f"{number} is a positive number."

# Demonstration using a try block
try:
    num = -5  # You can change this to test other values
    message = check_positive(num)
    print(message)
except NegativeNumberError as e:
    print(e)

#QUESTION 8
import random

def generate_random_numbers(count, start=1, end=100):
    """Generate a list of random integers within a specified range."""
    return [random.randint(start, end) for _ in range(count)]

def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

# Generate the list
random_numbers = generate_random_numbers(10)

# Calculate the average
average = calculate_average(random_numbers)

# Display the results
print("Generated numbers:", random_numbers)
print(f"Average: {average:.2f}")

#QUESTION9
import re

# I. Extract all email addresses from a given text
def extract_emails(text):
    """
    Extracts all email addresses from the input text.
    """
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(email_pattern, text)

# II. Validate a date in the format "YYYY-MM-DD"
def is_valid_date(date_str):
    """
    Validates if the input string matches the YYYY-MM-DD format.
    """
    date_pattern = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$'
    return bool(re.match(date_pattern, date_str))

# III. Replace all occurrences of a word with another word
def replace_word(text, old_word, new_word):
    """
    Replaces all whole-word occurrences of old_word with new_word.
    """
    return re.sub(rf'\b{re.escape(old_word)}\b', new_word, text)

# IV. Split a string by all non-alphanumeric characters
def split_by_non_alphanum(text):
    """
    Splits the input string by any non-alphanumeric character.
    """
    return re.split(r'\W+', text)

# Sample usage
if __name__ == "__main__":
    sample_text = "Contact us at support@example.com, sales@shop.co.uk or admin@domain.org."
    print("📧 Extracted Emails:", extract_emails(sample_text))

    date_input = "2025-09-16"
    print("📅 Date Valid:", is_valid_date(date_input))

    original_text = "The quick brown fox jumps over the lazy dog. The dog was not amused."
    replaced_text = replace_word(original_text, "dog", "cat")
    print("🔄 Replaced Text:", replaced_text)

    messy_string = "Hello! How's everything? Great, I hope."
    split_result = split_by_non_alphanum(messy_string)
    print("🔍 Split Result:", split_result)

#QUESTION 10
import socket

def start_server(host='127.0.0.1', port=65432):
    """
    Starts a TCP server that sends a greeting message to the client.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((host, port))
            server_socket.listen()
            print(f"Server listening on {host}:{port}...")

            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                message = "Hello from server!"
                conn.sendall(message.encode('utf-8'))
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    start_server()

    import socket


    def connect_to_server(host='127.0.0.1', port=65432):
        """
        Connects to the server and receives a message.
        """
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect((host, port))
                data = client_socket.recv(1024)
                print("Received from server:", data.decode('utf-8'))
        except ConnectionRefusedError:
            print("Connection failed: Server may not be running.")
        except socket.error as e:
            print(f"Socket error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


    if __name__ == "__main__":
        connect_to_server()

#QUESTION 11
import requests

def get_github_api():
    url = "https://api.github.com"  # Public API endpoint
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()  # Convert JSON response to Python dictionary
            print("✅ API Response:")
            print(data)
        else:
            print(f"❌ Failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Request error: {e}")

get_github_api()





