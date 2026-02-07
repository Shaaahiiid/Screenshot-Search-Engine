import sqlite3

conn = sqlite3.connect("ocr_index.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS screenshots (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    image_path TEXT UNIQUE,
    extracted_text TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  
)
""")

conn.commit()
conn.close()

print("Database and table created successfully.")
