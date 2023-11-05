# User Guide: SuperPy
## An Inventory Management Application

This user guide provides an overview of the SuperPy Python Inventory Management Application and explains how to perform various tasks within the application. Users can reference this guide for instructions and troubleshooting information.

# Table of Contents: 
# User Guide: SuperPy
  ## An Inventory Management Application
# 1. Introduction
  ## 1.1 Overview
  ## 1.2 Purpose
  ## 1.3 System Requirements
# 2. Getting Started
  ## 2.1 Installation
   ### 2.1.1 Python
   ### 2.1.2 Required Python Packages
# 3. Inventory Management
  ## 3.1 Buying a Product
   #### Example:
  ## 3.2 Selling a Product
   #### Example:
# 4 Generating Reports
  ## 4.1 Viewing Inventory Report
   #### Example:
  ## 4.2 Year or Month Revenue and Profit Report
   #### Example:
  ## 4.3 Bought Item Report
   #### Example:
# 5. Time Travelling
  ## 5.1 Advancing time
   #### Example:
  ## 5.2 Checking the Current Date
   #### Example:
  ## 5.3 Resetting the Current Date
   #### Example:
# 6. Help Section
  ## 6.1 Categories in Help
   1. **ACTIONS**:
   2. **REPORTS**:
   3. **TIME ACTIONS**:
   4. **HELP**:
# 7. Troubleshooting and Support
  ## 7.1 Common Issues
   **1. Application Not Launching:**
   **2. Invalid Date Format:**
   **3. Data Loss:**
   **4. Unexpected Behavior:**
   **5. Missing CSV Files:**
   **6. Terminal Errors:**
  ## 7.2 Getting Help and Support
# 8. Appendix
  ## 8.1 Glossary
  ## 8.2 License


# 1. Introduction
## 1.1 Overview
The Python Inventory Management Application is a command-line tool that allows users to manage product inventory, track purchases and sales, generate reports, and maintain product data.
## 1.2 Purpose
The purpose of this application is to provide businesses and individuals with a simple and efficient way to manage their inventory and gain insights into their operations.
## 1.3 System Requirements
- Python 3.x
- Required Python packages (see "Installation" section)
# 2. Getting Started
Before you start using the SuperPy Python Inventory Management Application, you need to make sure you have the required software and packages installed on your system.
## 2.1 Installation
### 2.1.1 Python
First, ensure that you have Python 3.x installed on your system. You can download Python from the official website (https://www.python.org/downloads/) and follow the installation instructions for your specific operating system.
### 2.1.2 Required Python Packages
In addition to Python, you will need to install several Python packages that are essential for the SuperPy application to run smoothly. Open your terminal or command prompt and run the following commands to install these packages one by one:

```bash
pip install tabulate
pip install prompt_toolkit
pip install rich
```

Each of these packages serves a specific purpose in the application, and installing them individually ensures that you have all the necessary components to run SuperPy effectively.

Once you have installed Python and the required packages, you are ready to launch and use the SuperPy application. You can proceed to the next section to learn how to launch the application and get started.
# 3. Inventory Management
The management of the inventory is done automatically by the program by simply registering the buying and selling of products. Below an explanation and examples of how this is done. 
## 3.1 Buying a Product
To buy a product use type the command: 
```bash
python main.py buy
```
This will start a prompt guiding you through the information that is required to buy a product and add it to the bought.csv and inventory.csv file. 
#### Example:
Let's say you want to buy 100 apples that cost $0.50 each, and they expire on 2023-12-31. Here's how you would buy a product:

1. type python main.py buy ( press enter).
2. Enter the product details as prompted:

   - Product Name: apples
   - Quantity: 100
   - Price: 0.50
   - Expiry Date: 2023-12-31

3. The product will be added to your inventory with a unique ID, and you will see a confirmation message.

## 3.2 Selling a Product
To sell a product use type the command: 
```bash
python main.py sell
```
This will start a prompt guiding you through the information that is required to sell a product and add it to the sold.csv and change the remainder of the product in the  inventory.csv file.
#### Example:
You have 20 lemons in your inventory, and you sold 10 of them for $1.00 each. Here's how you would sell a product:

1. type python main.py sell (press enter).
2. When typing the first letter of a product, an autocomplete list of products starting with that letter will pop up to assist in choosing the right product. Choose the product name from the auto-completed list (e.g., "lemons").
3. Enter the quantity sold: 10.
4. Enter the selling price: 1.00.
5. The product will be changed in the inventory, the sale will be recorded, and you will see a confirmation message.
# 4 Generating Reports
Of course you will want to know when and what you have bought and sold. You can generate various types of reports to track your inventory and financial data. Here are the different types of reports you can create:
## 4.1 Viewing Inventory Report
To view a report in the inventory type the command: 
```bash
python main.py inventory-report
```
This will show you an overview of the current inventory as below: 

#### Example:
To view your current inventory, follow these steps:

1. Type python main.py inventory-report (press enter).
2. You will see a list of products, their quantities, and their expiry status, like this:

```
id 	Product Name   Quantity   buy_date buy_price Expirtion_date Expired
----------------------------------------------------------------------------------------------------------
1	apples               100       2023-11-04     0.60        2023-11-24  Not Expired
2	lemons              10          2023-11-04    5.00        2023-12-02  Not Expired
3	oranges             30         2023-11-05    3.00         2023-12-15 Not Expired
```
Because of the use of Rich module - the overview is more clear in the program than in this example because of the use of a table layout and coloring on the expiry status column. 
## 4.2 Year or Month Revenue and Profit Report
To view a report on Revenue and profit type the command: 
```bash
python main.py report-PL
```
This will show you an report on revenue and profit as below: : 
#### Example:
You want to see the PL report for November 2023. 
Type 
```bash
python main.py report-PL
```
This will prompt you to specify what time the report should show:
Do you want the report per year (Y) or per month (M)? - type either Y or M. Other input is automatically ignored. 
if you choose Year you will be asked to type the year you want to see the report for. 
Enter the year (e.g., 2023): 2023
if you choose Month you will first have to type the year, and then the number of the month you want to see. 
  Enter the year (e.g., 2023): 2023
Enter the month (1-12): 11

## 4.3 Bought Item Report
The bought item report provides details of the products you have purchased, such as buy date and price as well as the expiration dates. These are colored green if not expired and red if expired. 

To view a report on items bought type: 
```bash
python main.py bought-report
```
This will show you an report on bought items as below:

#### Example:
To generate a bought item report, type the following command in the terminal:

```
python main.py bought_report
```

# 5. Time Travelling
Working with products that have expiration dates you will need to always think about the future. You need to know which products will soon expire that have not sold yet, so you can create a good deal for the customer to sell the items before they expire. To help in this proactive mindset Superpy allows you to travel ahead in time! 

## 5.1 Advancing time
You need to check which product will be expired in the next 2 weeks to set up promotions in your shop. Simply look at your calender, pick the right date and type: 
```bash
python main.py advance-time
```
This will then ask you which date to time travel to, and you can print you report to see clearly what items you need to sell before that date!
#### Example:
You want to set the current date to February 15, 2023. Here's how you would do it:

1. Type: python main.py advance-time ( Press Enter)
2. Enter the desired date: 2023-02-15.

The current date will be updated to February 15, 2023.

## 5.2 Checking the Current Date

You can check the current date that the CLI is currently working with using the "Check Date" command. This feature is helpful if you want to verify or ensure that the CLI is operating with the correct date.
#### Example:

To check the current date, simply run the following command:

```bash
python main.py check-date
```
This will than reply with the date currently in use:: 

## 5.3 Resetting the Current Date
Of course you will need to go back to the real world time as well. 
#### Example:
You've set the current date to a specific date and want to reset it to the actual real world date. Here's how you would reset the current date:

```bash
python main.py reset-date
```
This will reset the date. To make sure it worked you can use the check-date command again: 





# 6. Help Section
In SuperPy we've included a 'help' section to provide you with a quick reference to all available actions, reports, and time-related commands. To access this helpful guide, simply type the following command:

```bash
python main.py help
```

Upon executing this command, the CLI will display an organized list of available actions and their descriptions. This guide is designed to assist you in understanding how to use the CLI effectively.




## 6.1 Categories in Help
The 'help' section categorizes actions into several categories to help you navigate through the available options:
1. **ACTIONS**: 
These are basic actions that allow you to interact with the CLI.

    - **Buy**: Buys items.
        ```bash
        buy
        ```

    - **Sell**: Sells items.
        ```bash
        sell
        ```
2. **REPORTS**:
 This category includes actions related to generating various reports.

    - **Profit and Revenue Report (report-PL)**: Generate a year or month Profit and Revenue overview.
        ```bash
        report-PL
        ```

    - **Inventory Report (inventory-report)**: Print a report on the current inventory.
        ```bash
        inventory-report
        ```

    - **Bought Report (bought-report)**: Get an overview of 'bought.csv' with styling on expiration date.
        ```bash
        bought-report
        ```
3. **TIME ACTIONS**:
 If you need to manage the current date, this category covers actions like advancing time and checking the current date.

    - **Advance Time (advance-time)**: Advance the current date to certain date to perform actions.
        ```bash
        advance-time 
        ```

    - **Get Current Date (get-current-date)**: Show the date that the CLI is currently working with.
        ```bash
        get-current-date
        ```

    - **Reset Date (reset-date)**: Reset the current date to the actual date when advanced.
        ```bash
        reset-date
        ```
4. **HELP**:
 Finally, the 'help' action allows you to access this guide at any time.

    - **Help**: Access the help section for actions.
        ```bash
        help
        ```

The 'help' section is a valuable resource that can enhance your experience with the CLI, making it easier to perform various tasks and generate reports.

# 7. Troubleshooting and Support
In this section you will find some helpfull information when things don’t go as planned. 
## 7.1 Common Issues
Encountering challenges while using software is a common occurrence. This section provides solutions to common issues you might face while working with the SuperPy Python Inventory Management Application. Here are some fictional common problems and their suggested solutions:

**1. Application Not Launching:**

   - *Issue*: You're unable to launch the application.
   - *Solution*: Ensure you have Python 3.x installed. Also, confirm that you've installed the required Python packages mentioned in the "Installation" section. If the problem persists, check for any error messages and consult the SuperPy community for assistance.

**2. Invalid Date Format:**

   - *Issue*: The application is rejecting your date input.
   - *Solution*: Make sure you're using the correct date format (YYYY-MM-DD) and that the date is valid (e.g., February 30 is not a valid date). Double-check your input to avoid formatting errors.

**3. Data Loss:**

   - *Issue*: Data in your inventory or transaction files is missing or corrupted.
   - *Solution*: Regularly back up your data files, and consider using version control or data recovery tools. In the event of data loss, refer to your backups.

**4. Unexpected Behavior:**

   - *Issue*: The application is behaving unexpectedly or producing incorrect results.
   - *Solution*: Check the commands you've used, the data you've entered, and the current date. Confirm that you've followed the instructions correctly. If you still encounter issues, contact SuperPy's support channels for further assistance.

**5. Missing CSV Files:**

   - *Issue*: You can't find the required CSV files.
   - *Solution*: Ensure that you've placed the CSV files in the correct directory as instructed. If you've inadvertently moved or deleted them, restore the CSV files from your backups.

**6. Terminal Errors:**

   - *Issue*: You're encountering errors in the terminal.
   - *Solution*: Carefully review the error message, as it often provides clues to the issue. Search for the error message online or consult the SuperPy community for possible solutions.



## 7.2 Getting Help and Support
- If you encounter issues not covered reach out to 
*mijnietbellen@noonecares.com*

# 8. Appendix
Some more useful information
## 8.1 Glossary
Defines terms used in the application.

**1. Inventory:** A list of products and their relevant details, including quantity, purchase price, and expiration date, which is managed by the application.

**2. Product:** A specific item that is part of the inventory. Products have attributes such as name, quantity, purchase price, and expiration date.

**3. Buy:** An action that involves adding products to the inventory. It requires specifying the product's name, quantity, purchase price, and expiration date.

**4. Sell:** An action that involves removing products from the inventory due to a sale. It requires specifying the product's name and the quantity sold.

**5. Inventory Report:** A report that provides an overview of the current state of the inventory, including product names, quantities, and expiration statuses.

**6. Product Profit and Loss Report:** A report that breaks down the revenue and profit generated by individual products, helping analyze their performance.

**7. Current Date:** The date the application is currently using for all actions and calculations, which can be set or advanced using specific commands.

**8. Advance Time:** An action that allows you to move the current date forward by a specified number of days to simulate future actions.

**9. Reset Date:** An action that resets the current date to the actual system date after it has been advanced or set to a different date.

**10. Expiry Status:** Indicates whether a product has expired or not based on its expiration date.

**11. CSV Files:** Comma-separated value files used to store data such as product information and transactions.

**12. Revenue:** The total income generated from selling products.

**13. Profit:** The amount of money earned from selling products, calculated as revenue minus the cost of purchasing those products.

This glossary provides definitions for key terms used in the application, helping users understand the terminology and concepts related to inventory management and reporting.
## 8.2 License

The SuperPy Python Inventory Management Application is released under the "SuperPy Open Source License," a permissive open-source license designed to promote the free use, modification, and distribution of the software. This license encourages collaboration, innovation, and transparency. Key points of the license include:

**1. Open Source:** The SuperPy application is open source, meaning its source code is freely accessible and can be modified and redistributed by users.

**2. Permissive Usage:** Users are granted the freedom to use the application for any purpose, including personal, educational, or commercial use.

**3. Modification:** You have the right to modify the application's source code to tailor it to your specific needs.

**4. Distribution:** Users can distribute the modified or unmodified application to others without restrictions.

**5. Attribution:** While not mandatory, we appreciate attribution to the SuperPy project when using or distributing the software.

**Please note that this is a fictional licensing description.**
The SuperPy application should use an appropriate real-world open-source license, such as the MIT License, Apache License, or another license that suits the project's goals and requirements. Users should always refer to the actual license provided with the software for accurate licensing information.


