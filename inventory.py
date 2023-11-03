import csv
from datetime import date
from tabulate import tabulate

from modules.date_utils import read_current_date, advance_time
from modules.csv_utils import generate_unique_id, add_to_inventory

# Define path constants for files
bought_file = 'inventory_data/bought.csv'
inventory_file = 'inventory_data/inventory.csv'
sold_file = 'inventory_data/sold.csv'


# Function to buy a product and add it to inventory
def buy_product(product_name, quantity, price, expiry_date):
  '''
  Buy a product and add it to the inventory.

  Args:
      product_name (str): The name of the product.
      quantity (float): The quantity of the product bought.
      price (str): The price of the product.
      expiry_date (str): The expiry date of the product in 'YYYY-MM-DD' format.

  Returns:
      None
  '''
  # Convert product name to lowercase for consistency
  product_name = product_name.lower()

  # Generate a unique product ID
  product_id = generate_unique_id(bought_file)

  # Add the product to the bought and inventory files
  add_to_inventory(bought_file, product_id, product_name, quantity,
                   date.today().strftime('%Y-%m-%d'), price, expiry_date)
  add_to_inventory(inventory_file, product_id, product_name, quantity,
                   date.today().strftime('%Y-%m-%d'), price, expiry_date)

  # Calculate if the product has expired
  sale_date = date.today()
  expiration_date = date.fromisoformat(expiry_date)
  expired = 'yes' if sale_date > expiration_date else 'no'

  # Update the inventory file with the expiration status
  with open(inventory_file, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    inventory = list(reader)

  for index, row in enumerate(inventory):
    if row and row[0] == product_id:
      inventory[index].append(expired)

  with open(inventory_file, 'w', newline='') as csvfile:
    csv.writer(csvfile).writerows(inventory)

  print(f'Product with ID {product_id} bought successfully!')


  # Function to sell a product
def sell_product():
  '''
  Sell a product from the inventory.

  Prompts the user for the product name, quantity sold, 
  and the price at which it's sold.
  Updates the inventory and sold files accordingly.

  Returns:
      None
  '''
  product_name = input('Enter the product name you want to sell: ').lower()
  inventory = []

  with open(inventory_file, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    inventory = list(reader)

  product_found = False
  quantity = None
  price_bought = None

  # Find the price at which the product was bought
  with open(bought_file, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      if row[1].lower() == product_name:
        price_bought = row[4]
        break

  for index, row in enumerate(inventory):
    if len(row) >= 6 and row[1].lower() == product_name:
      product_id = row[0]
      quantity = float(row[2])
      expiry_date = row[5]

  # Prompt the user for quantity sold and price
  if quantity is not None and price_bought is not None:
    quantity_sold = None
    while quantity_sold is None:
      try:
        quantity_sold = float(
            input(f'Enter the quantity of {product_name} sold: '))
      except ValueError:
        print('Error: Please enter a valid numeric quantity.')

    # Check if there is enough quantity in inventory to sell
    price_sold = None
    while price_sold is None:
      try:
        price_sold = float(
            input(
                f'Enter the price at which {product_name} was sold (with 2 decimal places): '
            ))
        price_sold = round(price_sold, 2)
      except ValueError:
        print(
            'Error: Please enter a valid numeric price with 2 decimal places.')

    if quantity_sold <= quantity:
      inventory[index][2] = str(quantity - quantity_sold)

      sale_date = date.today()
      expiration_date = date.fromisoformat(expiry_date)
      expired = 'yes' if sale_date > expiration_date else 'no'

      if len(inventory[index]) >= 6:
        inventory[index][6] = expired

      # Update the inventory file
      with open(inventory_file, 'w', newline='') as csvfile:
        csv.writer(csvfile).writerows(inventory)

      # Generate a unique ID for the sold product and add it to the sold file
      sold_id = generate_unique_id(sold_file)
      data = [
          sold_id, product_name, quantity_sold,
          date.today().strftime('%Y-%m-%d'),
          date.today().strftime('%Y-%m-%d'), price_bought, price_sold,
          expiry_date, expired
      ]
      add_to_inventory(sold_file, *data)

      print(f'{quantity_sold} units of {product_name} sold successfully!')

      product_found = True
    else:
      print('Error: Insufficient quantity in inventory to sell.')

  if not product_found:
    print(f'Error: {product_name} not found in inventory.')
