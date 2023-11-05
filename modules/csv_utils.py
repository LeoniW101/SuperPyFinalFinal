import csv
import os

# Constants
DATA_DIR = 'inventory_data'
BOUGHT_FILE = os.path.join(DATA_DIR, 'bought.csv')
INVENTORY_FILE = os.path.join(DATA_DIR, 'inventory.csv')
SOLD_FILE = os.path.join(DATA_DIR, 'sold.csv')

# Create data directory if it doesn't exist
if not os.path.exists(DATA_DIR):
  os.makedirs(DATA_DIR)

# Check if CSV files exist; if not, create them
for file_path, header in [
    (BOUGHT_FILE, [
        'id', 'product_name', 'quantity', 'buy_date', 'buy_price',
        'expiration_date'
    ]),
    (INVENTORY_FILE, [
        'id', 'product_name', 'quantity', 'buy_date', 'buy_price',
        'expiration_date', 'expired'
    ]),
    (SOLD_FILE,
     ['id', 'product_id', 'sell_date', 'sell_price', 'quantity_sold'])
]:
  if not os.path.exists(file_path):
    with open(file_path, 'w', newline='') as csvfile:
      csv.writer(csvfile).writerow(header)


def read_csv_data(file_path):
  with open(file_path, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    return list(reader)


def generate_unique_id(file_path):
  with open(file_path, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    ids = []
    for row in reader:
      if len(row) > 0:
        try:
          ids.append(int(row[0]))
        except (ValueError, TypeError):
          pass  
  if ids:
    new_id = max(ids) + 1
  else:
    new_id = 1  
  return str(new_id)


def add_to_inventory(file_path, *data):
  with open(file_path, 'a', newline='') as csvfile:
    csv.writer(csvfile).writerow(data)


def get_inventory_file_path():
  if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

  return INVENTORY_FILE
