# 📸 Screenshot Search Engine (OCR-Based)

A local web application that lets you **search your screenshots by the text inside them**.  
It uses **OCR (Optical Character Recognition)** to extract text from images, indexes it using **SQLite**, and provides a **Flask web interface** to instantly retrieve matching screenshots.

---

## 🚀 Problem Statement

We take hundreds of screenshots—WiFi passwords, receipts, code snippets, quotes—but later **cannot find them**.

Traditional file search does not look **inside images**.

👉 This project solves that by:
- Reading text inside screenshots using OCR
- Storing the extracted text in a database
- Allowing keyword-based search to retrieve the exact screenshots

---

## 🧠 How It Works

### 1️⃣ Indexing Phase
- Screenshots are stored in a folder
- OCR is run **once per image**
- Extracted text is saved in an SQLite database

### 2️⃣ Search Phase
- User enters keywords in a web UI
- SQLite searches through OCR text
- Matching screenshots are returned instantly

---

## 🛠 Tech Stack

- **Python**
- **Tesseract OCR**
- **pytesseract**
- **SQLite**
- **Flask**
- **HTML & CSS**
