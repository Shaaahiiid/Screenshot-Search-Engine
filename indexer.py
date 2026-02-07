import os
import sqlite3
from PIL import Image
import pytesseract

SCREENSHOTS_DIR = "screenshots"
DB_PATH = "ocr_index.db"
SUPPORTED_EXTENSIONS = (".png",".jpg",".jpeg")

def get_db_connection():
    return sqlite3.connect(DB_PATH)

def image_already_indexed(cursor,image_path):
    cursor.execute(
        "SELECT 1 FROM screenshots WHERE image_path = ?",
        (image_path,)
    )
    return cursor.fetchone() is not None

def ocr_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img, lang="eng")
    return text.strip().lower()

def index_screenshots():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    for filename in os.listdir(SCREENSHOTS_DIR):
        if not filename.lower().endswith(SUPPORTED_EXTENSIONS):
            continue
        image_path = os.path.join(SCREENSHOTS_DIR, filename)
        
        if image_already_indexed(cursor, image_path):
            print(f"Skip : {filename}")
            continue
        print(f"OCR processing: {filename}")
        text = ocr_image(image_path)
        
        cursor.execute(
            "INSERT INTO screenshots (image_path, extracted_text) VALUES(?,?)",
            (image_path,text)
        )
        
        conn.commit()
    conn.close()
    print("Indexing complete.")
    
if __name__ == "__main__":
    index_screenshots()