import calendar
import csv
from datetime import datetime
from rich import print
from rich.console import Console
from rich.table import Table
from rich.style import Style
from rich.text import Text
from modules.csv_utils import read_csv_data
from modules.date_utils import read_current_date, check_expiry_status

console = Console()


# Function to generate and print reports
def generate_and_print_reports(month, year, revenue, profit):
  """
  Generates and prints a summary report for revenue and profit.

  Args:
      month (int or None): The month (1-12) or None for annual report.
      year (int): The year for the report.
      revenue (float): Total revenue.
      profit (float): Total profit.
  """
  if month is not None:
    title = f"Revenue and Profit for {calendar.month_name[month]} {year}"
  else:
    title = f"Yearly Revenue and Profit for {year}"
  print(title)

  # Create a table to display the report
  table = Table(title="Overall Summary")
  table.add_column("Report", style="white")
  table.add_column("Amount", style="bold")

  # Define the styles for positive and negative values in the "Amount" column
  positive_style = Style(color="green")
  negative_style = Style(color="red")

  # Add Total Revenue to the table with styling
  total_revenue_text = Text("Total Revenue:", style="white")
  total_revenue_amount = Text(f"${revenue:.2f}")
  total_revenue_amount.stylize(
      positive_style if revenue >= 0 else negative_style)
  table.add_row(total_revenue_text, total_revenue_amount)

  # Add Total Profit to the table with styling
  total_profit_text = Text("Total Profit:", style="white")
  total_profit_amount = Text(f"${profit:.2f}")
  total_profit_amount.stylize(
      positive_style if profit >= 0 else negative_style)
  table.add_row(total_profit_text, total_profit_amount)

  # Print the table
  console.print(table)


# Function to generate reports
def generate_reports(month, year, bought_file, sold_file):
  """
  Generates a summary report of revenue and profit from sold and bought data.

  Args:
      month (int or None): The month (1-12) or None for annual report.
      year (int): The year for the report.
      bought_file (str): The path to the CSV file with bought data.
      sold_file (str): The path to the CSV file with sold data.
  """
  # Read data from CSV files
  bought_data = read_csv_data(bought_file)
  sold_data = read_csv_data(sold_file)

  if not bought_data or not sold_data:
    console.print('No data found in either bought.csv or sold.csv.')
    return

  # Initialize dictionaries to track revenue and profit per product
  product_revenue = {}
  product_profit = {}

  # Iterate through sold data
  for sale in sold_data[1:]:
    product_id, product_name, quantity_sold, sell_date, buy_date, price_bought, price_sold, expiry_date, expired = sale
    sell_date = datetime.strptime(sell_date, '%Y-%m-%d')

    # Check if the sale date matches the specified month and year
    if (month is None
        or (sell_date.month == month and sell_date.year == year)):
      # Track revenue per product
      if product_name not in product_revenue:
        product_revenue[product_name] = 0.0
        product_profit[product_name] = 0.0

      product_revenue[product_name] += float(price_sold) * float(quantity_sold)

      # Calculate profit for the product
      for purchase in bought_data[1:]:
        if purchase[0] == product_id:
          buy_price = float(purchase[4])
          product_profit[product_name] += (float(price_sold) -
                                           buy_price) * float(quantity_sold)
          break

  # Calculate the total revenue and profit
  total_revenue = sum(product_revenue.values())
  total_profit = sum(product_profit.values())

  # Generate and print reports
  generate_and_print_reports(month, year, total_revenue, total_profit)


  # Function to generate product profit and loss report
def generate_product_PL_report(sold_file, bought_file):
  """
  Generates a report of product profit and revenue.

  Args:
      sold_file (str): The path to the CSV file with sold data.
      bought_file (str): The path to the CSV file with bought data.
  """
  sold_data = read_csv_data(sold_file)
  bought_data = read_csv_data(bought_file)

  if not sold_data or len(sold_data) <= 1:
    console.print('No sales data available.')
    return

  if not bought_data or len(bought_data) <= 1:
    console.print('No purchase data available.')
    return

  # Prompt the user to choose per year or per month
  report_period = input(
      'Do you want the report per year (Y) or per month (M)? ').strip().lower(
      )

  if report_period == 'y':
    # Report per year, prompt for the year
    year = int(input('Enter the year (e.g., 2023): '))
    month = None  # No month needed for annual report
  elif report_period == 'm':
    # Report per month, prompt for the year and month
    year = int(input('Enter the year (e.g., 2023): '))
    month = int(input('Enter the month (1-12): '))
  else:
    console.print(
        'Invalid choice. Please choose Y for per year or M for per month.')
    return

  product_revenue = {}
  product_profit = {}

  for sale in sold_data[1:]:
    product_id, product_name, quantity_sold, sell_date, buy_date, price_bought, price_sold, expiry_date, expired = sale
    sell_year = int(sell_date.split('-')[0])
    sell_month = int(sell_date.split('-')[1])

    if report_period == 'y':
      if sell_year != year:
        continue
    elif report_period == 'm':
      if sell_year != year or sell_month != month:
        continue

    if product_name not in product_revenue:
      product_revenue[product_name] = 0.0
      product_profit[product_name] = 0.0

    product_revenue[product_name] += float(price_sold) * float(quantity_sold)

    for purchase in bought_data[1:]:
      if purchase[0] == product_id:
        buy_price = float(purchase[4])
        product_profit[product_name] += (float(price_sold) -
                                         buy_price) * float(quantity_sold)
        break

  table = Table(title=f"Product Profit and Revenue Report")
  table.add_column("Product Name", style="bold")
  table.add_column("Revenue", style="green")
  table.add_column("Profit", style="red")

  total_revenue = 0.0
  total_profit = 0.0

  for product_name in product_revenue.keys():
    revenue = product_revenue[product_name]
    profit = product_profit[product_name]
    table.add_row(product_name, f"${revenue:.2f}", f"${profit:.2f}")
    total_revenue += revenue
    total_profit += profit

  # Add totals to the footer
  table.add_row("Total", f"${total_revenue:.2f}", f"${total_profit:.2f}")

  # Customize the border style for the last row
  table.rows[-1].style = "bold blue"

  console.print(table)


# Function to generate an inventory report
def generate_inventory_report(inventory_file):
  """
  Generates an inventory report with expiry status.

  Args:
      inventory_file (str): The path to the CSV file with inventory data.
  """
  with open(inventory_file, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    inventory_data = list(reader)

  if not inventory_data or len(inventory_data) == 1:
    console.print('No inventory data available.')
    return

  headers = inventory_data[0]
  data = inventory_data[1:]

  # Find the index of the "expired" column
  expired_index = headers.index("expired")

  table = Table(title="Inventory Report")

  for header in headers:
    table.add_column(header)

# Get the current date
  current_date = read_current_date()

  for row in data:
    # Find the expiration date and calculate the expiry status
    expiration_date = row[headers.index("expiration_date")]
    expired_status = check_expiry_status(expiration_date)

    # Create a style based on the expiry status
    if expired_status == 'Expired':
      expired_style = Style(color="red")
    else:
      expired_style = Style(color="green")

    # Create a Text object with the style
    expired_text = Text(expired_status, style=expired_style)

    # Update the data with the styled text
    row[expired_index] = expired_text

    table.add_row(*row)  # Append the row to the existing table

  return table


# Function to generate a report for bought items
def generate_bought_report(bought_file):
  """
  Generates a report for bought items with expiry status.

  Args:
      bought_file (str): The path to the CSV file with bought data.
  """
  with open(bought_file, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    bought_data = list(reader)

  if not bought_data or len(bought_data) == 1:
    console.print('No bought data available.')
    return

  headers = bought_data[0]
  data = bought_data[1:]

  # Create a table to display the report with all text in white
  table = Table(title="Bought Report")
  for header in headers:
    table.add_column(header, style="white")

  # Find the index of the "expiration_date" column
  expired_index = headers.index("expiration_date")

  for row in data:
    # Get the expiration date from the row
    expiration_date = row[expired_index]

    # Calculate the expiry status
    expired_status = check_expiry_status(expiration_date)

    # Create a style based on the expiry status
    if expired_status == 'Expired':
      expired_style = Style(color="red")
    else:
      expired_style = Style(color="green")

    # Create a Text object with the style
    expiration_date_text = Text(expiration_date, style=expired_style)

    # Update the data with the styled expiration date text
    row[expired_index] = expiration_date_text

    # Add the row to the table with all text in white
    table.add_row(*row)

  # Print the table without styling for the last row
  console.print(table)


# Function to generate a yearly profit and loss report
def generate_year_profit_and_loss_report(year, sold_file):
  """
  Generates a yearly profit and loss report for products.

  Args:
      year (int): The year for the report.
      sold_file (str): The path to the CSV file with sold data.
  """
  # Read data from the sold.csv file
  sold_data = read_csv_data(sold_file)

  if not sold_data or len(sold_data) <= 1:
    console.print('No sales data available.')
    return

  # Initialize dictionaries to track revenue and profit per product for the given year
  product_revenue = {}
  product_profit = {}

  # Iterate through sold data
  for sale in sold_data[1:]:
    product_id, product_name, quantity_sold, sell_date, buy_date, price_bought, price_sold, expiry_date, expired = sale
    sell_date = datetime.strptime(sell_date, '%Y-%m-%d')

    # Check if the sale date matches the specified year
    if sell_date.year == year:
      # Track revenue per product
      if product_name not in product_revenue:
        product_revenue[product_name] = 0.0
        product_profit[product_name] = 0.0

      product_revenue[product_name] += float(price_sold) * float(quantity_sold)

      # Calculate profit for the product
      for purchase in bought_data[1:]:
        if purchase[0] == product_id:
          buy_price = float(purchase[4])
          product_profit[product_name] += (float(price_sold) -
                                           buy_price) * float(quantity_sold)
          break

  # Create and print the 'year P&L' report
  title = f"Yearly Profit and Loss Report for {year}"
  print(title)

  # Create a table to display the report
  table = Table(title="Product Summary")
  table.add_column("Product Name", style="white")
  table.add_column("Revenue", style="bold")
  table.add_column("Profit", style="bold")

  # Define the styles for positive and negative values in the "Revenue" and "Profit" columns
  positive_style = Style(color="green")
  negative_style = Style(color="red")

  # Add product revenue and profit to the table with styling
  for product_name, revenue in product_revenue.items():
    profit = product_profit.get(product_name, 0.0)
    revenue_text = Text(f"${revenue:.2f}")
    profit_text = Text(f"${profit:.2f}")
    revenue_text.stylize(positive_style if revenue >= 0 else negative_style)
    profit_text.stylize(positive_style if profit >= 0 else negative_style)
    table.add_row(product_name, revenue_text, profit_text)

  # Print the table
  console.print(table)


# Main code block
if __name__ == "__main__":
  # Example usage:
  generate_reports(10, 2023, 'bought.csv', 'sold.csv')
  generate_inventory_report('inventory.csv')
  generate_bought_report('bought.csv')
  generate_and_print_reports(10, 2023, 7.7, 3.9)
  generate_year_profit_and_loss_report(2023, 'sold.csv')
  generate_product_PL_report('sold.csv', 'bought.csv')
