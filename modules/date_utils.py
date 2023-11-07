from datetime import date, datetime, timedelta
import os


# Read the current date from a file or return today's date
def read_current_date():
  current_date_file = 'current_date.txt'
  if not os.path.exists(current_date_file):
    return date.today()

  with open(current_date_file, 'r') as file:
    return datetime.strptime(file.read(), '%Y-%m-%d').date()


# Advance the current date to a specified target date
def advance_time(target_date):
  try:
    target_date = datetime.strptime(target_date, '%Y-%m-%d').date()
    write_current_date(target_date)  # Update the current date in the file
    return True
  except ValueError:
    return False


# Write the new current date to a file
def write_current_date(new_date):
  with open('current_date.txt', 'w') as file:
    file.write(new_date.strftime('%Y-%m-%d'))


# Reset the current date by removing the date file
def reset_current_date():
  current_date_file = 'current_date.txt'
  if os.path.exists(current_date_file):
    os.remove(current_date_file)


# Check the expiry status of a product based on the current date
def check_expiry_status(expiry_date):
  current_date = read_current_date()  # Get the current date
  expiry_date = datetime.strptime(expiry_date,
                                  '%Y-%m-%d').date()  # Parse the expiry date

  if current_date > expiry_date:
    return 'Expired'
  else:
    return 'Not Expired'


# Function to time travel by a specified number of days
def time_travel(days):
  current_date = read_current_date()  # Get the current date
  new_date = current_date + timedelta(days=days)  # Calculate the new date

  # Update the current date in the file
  write_current_date(new_date)
  return new_date
