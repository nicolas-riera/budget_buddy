# Budget Buddy

![pythonversion](https://img.shields.io/badge/python-3.7+-blue)
![ctk](https://img.shields.io/badge/customtkinter-required-yellow)

![screenshot_general](/docs/screenshots/screenshot_general.png)

Budget Buddy is a personal budgeting application designed to help you track your income, expenses, and financial habits in a simple and effective way. It provides a sleek interface to manage your finances every day.

## Features

- 💼 User account management
- 📊 Transaction tracking
- 📈 Expense visualization
- 🔐 Secure login & registration
- 🧠 Modern and intuitive GUI
- 🧰 MySQL database for data storage

## Prerequisites

Make sure you have installed :

- Python 3.7+
- MySQL
- dependencies in `requirements.txt` -> `python -m pip install -r requirements.txt`

### Clone

Clone the repository :

```
git clone https://github.com/nicolas-riera/budget_buddy.git
cd budget_buddy 
```

Don't forget to install the dependencies.

### Prepare database

In MySQL, create a database named "buddget_buddy" :

```SQL
CREATE DATABASE budget_buddy;
```

Then, import budget_buddy.sql in MySQL :

```bash
mysql -u {user} -p budget_buddy < {path_to_budget_buddy.sql}
```

Finally, in the root of the project, create a `.env` file and fill it like this:

```
DB_HOST = {ip adress, should be localhost}
DB_USER = {user}
DB_PASSWORD = {password}
DB_NAME = budget_buddy
```

Now, you can start the program :

```bash
python main.py
```

## Screenshots

![screenshot_login](/docs/screenshots/screenshot_login.png)
![screenshot_history](/docs/screenshots/screenshot_history.png)
![screenshot_accounts](/docs/screenshots/screenshot_accounts.png)

## Physical Data Model (PDM)

![PDM](/docs/db/PDM.png)

## Authors

This project has been realised by [Nicolas](https://github.com/nicolas-riera), [Hugo](https://github.com/hugo-belaloui) and [Hykoo13](https://github.com/Hykoo13)

