# 🌾 Crop Recommendation Tool using Python & Pandas

This project was developed as part of my efforts to enhance my data science and programming skills. It is a **Python-based crop recommendation system** designed to assist farmers in selecting the most suitable crops based on their available resources and constraints.

---

## 📌 Project Overview

The tool analyzes crop data stored in a CSV file and allows users to filter recommendations using one of three criteria:

- ✅ **Type of Crop** (e.g., Fruit, Vegetable, Legume, etc.)
- ✅ **Available Fertilizers** (Nitrogen, Phosphorus, or Potassium-based)
- ✅ **Time Duration** available for crop growth (in days)

It then returns a list of crops that match the selected condition, along with additional details like crop category, recommended fertilizer, and estimated growth time.

---

## 🧠 Key Features

- Data filtering and recommendation based on user input
- Real-world agricultural relevance
- Clear command-line interface for interaction
- Flexible input: crop type, fertilizer availability, or growing time
- CSV-based data source for scalability

---

## 🛠️ Technologies Used

- **Python**
- **Pandas** (for data manipulation)
- **CSV** (crop data source)
- Command-line interface (CLI)

---

## 📂 Project Structure

```plaintext
├── crop_recommendation.py       # Main Python script
├── data/
│   └── crop_information.csv     # Dataset containing crop information
├── README.md                    # Project documentation
