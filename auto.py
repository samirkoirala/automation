import pywhatkit as kit
import pandas as pd
import time

# Load CSV file correctly
try:
    df = pd.read_csv("abc.csv", dtype={"number": str})  # Ensure numbers are read as strings
except FileNotFoundError:
    print("Error: abc.csv file not found!")
    exit()

# Iterate through rows in the CSV
for index, row in df.iterrows():
    number = str(row["number"]).strip().replace("-", "").replace(" ", "")  # Clean the number
    message = str(row["message"]).strip()

    # Debug: Print the number and its length
    print(f"Processing number: {number} (Length: {len(number)})")

    # Ensure number starts with '+977' and has the correct length
    if not number.startswith("+977"):
        print(f"Skipping invalid number (prefix): {number}")
        continue
    if len(number) != 14:
        print(f"Skipping invalid number (length): {number} (Expected 13, got {len(number)})")
        continue

    try:
        print(f"Sending message to {number}...")
        kit.sendwhatmsg_instantly(number, message, wait_time=10)  # Send message instantly
        print(f"Message sent to {number}")
        time.sleep(10)  # Add delay to prevent rate limiting (10 seconds recommended)
    except Exception as e:
        print(f"Failed to send message to {number}: {e}")