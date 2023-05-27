import sqlite3

# Create a connection to the database
connection = sqlite3.connect("inventory.db")
cursor = connection.cursor()

# Create a table for products
cursor.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER)")

def add_product(name, quantity):
    # Insert a new product into the database
    cursor.execute("INSERT INTO products (name, quantity) VALUES (?, ?)", (name, quantity))
    connection.commit()
    print("Product added successfully!")

def display_products():
    # Retrieve all products from the database
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    # Print the retrieved products
    if len(products) > 0:
        print("Product List:")
        for product in products:
            print(f"ID: {product[0]}, Name: {product[1]}, Quantity: {product[2]}")
    else:
        print("No products found.")

def update_quantity(product_id, new_quantity):
    # Update the quantity of a product in the database
    cursor.execute("UPDATE products SET quantity=? WHERE id=?", (new_quantity, product_id))
    connection.commit()
    print("Quantity updated successfully!")

def search_product(name):
    # Search for a product by name in the database
    cursor.execute("SELECT * FROM products WHERE name LIKE ?", ('%' + name + '%',))
    products = cursor.fetchall()

    # Print the search results
    if len(products) > 0:
        print("Search Results:")
        for product in products:
            print(f"ID: {product[0]}, Name: {product[1]}, Quantity: {product[2]}")
    else:
        print("No products found matching the search.")

# Example usage:

# Add a product
add_product("Product 1", 10)

# Display the product list
display_products()

# Update the quantity of a product
update_quantity(1, 15)

# Search for products by name
search_product("Product")

# Close the database connection
cursor.close()
connection.close()
