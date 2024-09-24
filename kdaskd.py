import csv
from pwinput import pwinput
from prettytable import PrettyTable
from datetime import datetime


class CoffeeShop:
    def __init__(self):
        self.menu = {}
        self.stock = {}
        self.customer_orders = {}
        self.order_records = {}
        self.users = self.load_users()

    def load_users(self):
        users = []
        with open('users.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                users.append(row)
        return users

    # Function untuk menyimpan data pengguna ke file CSV.
    def save_users(self):
        with open('users.csv', mode='w', newline='') as file:
            fieldnames = ['Username', 'Password', 'Role', 'Balance']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for customer in self.users:
                writer.writerow(customer)

    # Function pendaftaran pengguna baru.
    def register_user(self):
        username = input("Enter a new username: ")
        if not username:
            print("Username cannot be empty. Please choose a valid username.")
            return

        if username in {'-1', '0', '-2', '-3', '-4', '-5', '-6', '-7'}:
            print("Username cannot be '-1, -2 , -3, -4, -5 , -6, -7 ' or '0' . Please choose a different username.")
            return

        existing_users = self.load_users()
        for customer in existing_users:
            if customer['Username'] == username:
                print("Username already exists. Please choose a different username.")
                return

        password = pwinput(prompt="Enter a password:")
        if not password:
            print("Password cannot be empty. Please enter a valid password.")
            return

        if password in {'-1', '0', '-2', '-3', '-4', '-5', '-6', '-7'}:
            print("Password cannot be '-1, -2, -3, -4, -5, -6, -7 ' or '0'. Please choose a different password.")
            return

        role = input("Enter the customer role (cashier, manager, customer): ")
        if role not in ["cashier", "manager", "customer"]:
            print("Invalid role. Please choose from 'cashier', 'manager', or 'customer'.")
            return

        try:
            balance = int(input("Enter the initial E-money balance: "))
            if balance <= 0:
                print("Balance cannot be zero or negative. Please enter a positive balance.")
                return
        except ValueError:
            print("Invalid balance. Please enter a valid numeric balance.")
            return

        new_user = {'Username': username, 'Password': password, 'Role': role, 'Balance': balance}
        self.users.append(new_user)
        self.save_users()
        print("User registered successfully.")

    # Function untuk memuat data stok barang dari file CSV.
    def load_stock(self):
        stock = {}
        with open('stock.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                stock[row['Item']] = int(row['Quantity'])
        return stock

    # Function untuk menyimpan data stok barang ke file CSV.
    def save_stock(self):
        with open('stock.csv', mode='w', newline='') as file:
            fieldnames = ['Item', 'Quantity']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for item, quantity in self.stock.items():
                writer.writerow({'Item': item, 'Quantity': quantity})

    # Function untuk memuat data pengguna dari file CSV.
    def load_menu(self):
        menu = {}
        with open('menu.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                menu[row['Item']] = int(row['Price'])
        return menu

    # Function untuk menyimpan menu ke file CSV.
    def save_menu(self):
        with open('menu.csv', mode='w', newline='') as file:
            fieldnames = ['Item', 'Price']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for item, price in self.menu.items():
                writer.writerow({'Item': item, 'Price': price})

    # Function untuk menampilkan menu dengan harga dan stok.
    def display_menu(self):
        table = PrettyTable(["Menu", "Price", "Stock"])
        for item, price in self.menu.items():
            stock_quantity = self.stock.get(item, 0)
            table.add_row([item, price, stock_quantity])
        print("Coffee Shop Menu")
        print(table)

    # Function untuk antarmuka pelanggan.
    def customer_interface(self):
        pass

    # Function untuk menampilkan catatan pesanan.
    def display_orders(self):
        pass

    # Function untuk menambahkan kopi baru ke menu.
    def add_new_coffee(self):
        pass

    # Function untuk mengupdate stok barang.
    def update_stock(self):
        pass

    # Function untuk menandai pesanan sebagai sudah dibayar.
    def search_order(self):
        pass

    # Function untuk memilih peran setelah login
    def role_selection(self):
        pass

    # Function untuk antarmuka kasir.
    def cashier_interface(self):
        pass

    # Function untuk antarmuka manager.
    def manager_interface(self):
        pass

    # Function untuk menampilkan catatan total pesanan.
    def display_total_orders(self):
        pass

    # Function untuk menampilkan total stok barang.
    def display_total_stock(self):
        pass

    # Function untuk mengupdate pesanan pelanggan.
    def update_orders(self):
        pass

    # Function utama program.
    def main_menu(self):
        pass


if __name__ == '__main__':
    coffee_shop = CoffeeShop()
    coffee_shop.main_menu()
