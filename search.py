import sqlite3

DB_PATH = "ocr_index.db"

def search_screenshots(query):
    words = query.lower().split()
    if not words:
        return []

    conditions = []
    values = []

    for word in words:
        conditions.append("extracted_text LIKE ?")
        values.append(f"%{word}%")
    
    where_clause = " OR ".join(conditions)
    
    query = f"""
    SELECT image_path FROM screenshots
    WHERE {where_clause}
    """
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(query, values)
    results = cursor.fetchall()
    
    conn.close()

    return [row[0] for row in results]
        
