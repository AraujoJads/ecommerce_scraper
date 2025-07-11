import sqlite3

def init_db():
    conn = sqlite3.connect("data/products.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price TEXT,
            availability TEXT,
            rating TEXT,
            image_url TEXT,
            product_page TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_products(products):
    conn = sqlite3.connect("data/products.db")
    cursor = conn.cursor()
    for product in products:
        cursor.execute("""
            INSERT INTO products (title, price, availability, rating, image_url, product_page)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            product["title"],
            product["price"],
            product["availability"],
            product["rating"],
            product["image_url"],
            product["product_page"]
        ))
    conn.commit()
    conn.close()

def get_products():
    conn = sqlite3.connect("data/products.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    conn.close()
    return [
        {
            "id": row[0],
            "title": row[1],
            "price": row[2],
            "availability": row[3],
            "rating": row[4],
            "image_url": row[5],
            "product_page": row[6]
        }
        for row in rows
    ]
