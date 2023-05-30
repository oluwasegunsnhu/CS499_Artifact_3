import sqlite3

class InventoryDatabase:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, quantity INTEGER)")
    
    def __del__(self):
        self.cursor.close()
        self.connection.close()
    
    def add_product(self, name, quantity):
        self.cursor.execute("INSERT INTO products (name, quantity) VALUES (?, ?)", (name, quantity))
        self.connection.commit()
        print("Product added successfully!")
    
    def display_products(self):
        self.cursor.execute("SELECT * FROM products")
        products = self.cursor.fetchall()

        if len(products) > 0:
            print("Product List:")
            for product in products:
                print(f"ID: {product[0]}, Name: {product[1]}, Quantity: {product[2]}")
        else:
            print("No products found.")
    
    def update_quantity(self, product_id, new_quantity):
        self.cursor.execute("UPDATE products SET quantity=? WHERE id=?", (new_quantity, product_id))
        self.connection.commit()
        print("Quantity updated successfully!")
    
    def search_product(self, name):
        self.cursor.execute("SELECT * FROM products WHERE name LIKE ?", ('%' + name + '%',))
        products = self.cursor.fetchall()

        if len(products) > 0:
            print("Search Results:")
            for product in products:
                print(f"ID: {product[0]}, Name: {product[1]}, Quantity: {product[2]}")
        else:
            print("No products found matching the search.")

# Example usage:

# Create an instance of the inventory database
inventory_db = InventoryDatabase("inventory.db")

# Add a product
inventory_db.add_product("Product 1", 10)

# Display the product list
inventory_db.display_products()

# Update the quantity of a product
inventory_db.update_quantity(1, 15)

# Search for products by name
inventory_db.search_product("Product")
