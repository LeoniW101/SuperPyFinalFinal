# Imports
import argparse
from rich.console import Console
from rich.table import Table
from inventory import buy_product, sell_product
from modules.date_utils import advance_time, read_current_date, reset_current_date
from modules.reports import (
    generate_inventory_report,
    generate_bought_report,
    generate_product_PL_report,
)
from modules.csv_utils import read_csv_data, get_inventory_file_path
from prompt_toolkit import prompt

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"
# Your code below this line.

# Define path constants
SOLD_FILE = "inventory_data/sold.csv"
BOUGHT_FILE = "inventory_data/bought.csv"

console = Console()


def main():
  # Create a command-line argument parser
  parser = argparse.ArgumentParser(description="Inventory Management CLI")
  parser.add_argument(
      "action",
      choices=[
          "buy",
          "sell",
          "report-PL",
          "advance-time",
          "inventory-report",
          "bought-report",
          "check-date",
          "reset-date",
          "help",
      ],
      help="Action to perform",
  )
  # Parse the command-line arguments
  args = parser.parse_args()

  if args.action == "buy":
    # Prompt the user to enter product details and buy the product
    product_name = prompt("Enter Product Name: ")
    quantity = float(prompt("Enter Quantity: "))
    price = None
    while price is None:
      try:
        price = float(prompt("Enter Price: "))
        price = f"{price:.2f}"  # Format price as "0.00"
      except ValueError:
        print("Error: Please enter a valid numeric price.")

    expiry_date = prompt("Enter Expiry Date (YYYY-MM-DD): ")
    buy_product(product_name, quantity, price, expiry_date)

  elif args.action == "sell":
    # Perform the "sell" action
    sell_product()

  elif args.action == "report-PL":
    # Generate and print the Profit and Loss report
    sold_file = SOLD_FILE
    bought_file = BOUGHT_FILE
    generate_product_PL_report(sold_file, bought_file)

  elif args.action == "advance-time":
    # Prompt the user to enter the date to advance time to
    target_date = prompt("Enter the date to advance time to (YYYY-MM-DD): ")
    advance_time(target_date)

  elif args.action == "inventory-report":
    # Generate and display the inventory report
    inventory_file = get_inventory_file_path()
    table = generate_inventory_report(inventory_file)
    console.print(table)

  elif args.action == "bought-report":
    # Generate and print the Bought report
    generate_bought_report("inventory_data/bought.csv")

  elif args.action == "check-date":
    # Display the current date
    console.print(read_current_date())

  elif args.action == "reset-date":
    # Reset the current date
    reset_current_date()

  elif args.action == "help":
    # Display help message directly here
    border_style = "blue"

    table = Table(title="Actions", title_style=border_style)
    table.add_column("Action", style="bold", header_style=border_style)
    table.add_column("Description", style="italic")

    sections = [
        ("ACTIONS:", [("buy,", "buys items"), ("sell,", "sells items")]),
        ("REPORTS:",
         [("report-PL", "prints year or month Profit and Revenue overview"),
          ("inventory-report", "prints report on current inventory"),
          ("bought-report",
           "prints overview of bought.csv with styling on expiration date")]),
        ("TIME ACTIONS:",
         [("advance-time",
           "advance time by X number of days to perform actions"),
          ("get-current-date",
           "shows date that the CLI is currently working with"),
          ("reset-date", "reset current date to the actual date when advanced")
          ]), ("HELP:", [("help", "help section for actions")])
    ]

    for section_title, actions in sections:
      table.add_row(f"[bold]{section_title}", style=border_style)
      for action, description in actions:
        table.add_row(action, description)

    console.print(table)


if __name__ == "__main__":
  main()
