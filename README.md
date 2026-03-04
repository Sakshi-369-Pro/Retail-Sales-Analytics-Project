📊 MySQL Python Data Analytics Project

👩‍💻 Author: Sakshi Singh

🔎 Project Type: Data Analysis | Database Normalization | Business Insights

🌟 Project Overview

This project focuses on analyzing retail sales data by converting raw transactional data into a structured relational database and generating business insights using Python.

The main goal of this project was to understand how real-world business data is stored, processed, and analyzed for decision-making.

🎯 Project Objectives

✔ Convert raw denormalized dataset into normalized relational database
✔ Perform data cleaning and transformation
✔ Analyze sales performance across regions and customer segments
✔ Generate business insights using data visualization
✔ Understand real-world database design and analytics workflow

🗂 Dataset Description

The dataset contains retail store transaction data including:

📦 Order Details – Order ID, order date, shipping information
👤 Customer Information – Customer ID, name, and segment
🛍 Product Information – Category, sub-category, and product details
🌍 Geographic Information – Region, state, and city
💰 Financial Metrics – Sales, profit, quantity, and discount

🧱 Database Design

The raw dataset was normalized into 5 relational tables:

1️⃣ customers – Stores customer details and segment information
2️⃣ locations – Stores geographic data
3️⃣ products – Stores product category and sub-category details
4️⃣ orders – Stores order-level information
5️⃣ order_items – Stores individual product order details

✨ Normalization helped improve data consistency and reduce redundancy.

📈 Analysis Performed
🌍 1. Regional Sales Analysis

✔ Identified high-performing sales regions
✔ Compared profit distribution across regions

👥 2. Customer Segment Analysis

✔ Compared revenue contribution by customer segments
✔ Identified customer behavior patterns

🛒 3. Product Category Analysis

✔ Evaluated sales and profit performance of product categories
✔ Identified high-demand product categories

⏳ 4. Time-Based Sales Analysis

✔ Studied monthly and yearly sales trends
✔ Identified seasonal sales patterns

💡 Key Insights

📌 Certain regions contribute significantly higher revenue
📌 Consumer segment generates major sales volume
📌 Some product categories generate high revenue but lower profit margin
📌 Sales show seasonal trends during specific months

🗃 Project Structure
MySQL-Python-Data-Analytics-Mini-Project
│
├── 📁 data
│   ├── customers.csv
│   ├── orders.csv
│   ├── order_items.csv
│   ├── products.csv
│   └── locations.csv
│
├── 📁 notebooks
│   ├── Region_Segment_Analysis.ipynb
│   ├── Product_Category_Analysis.ipynb
│   └── Time_Series_Analysis.ipynb
│
├── 📁 sql
│   ├── database_schema.sql
│   └── data_insertion.sql
│
├── 📄 README.md
└── 📦 requirements.txt

🛠 Tools & Technologies Used

🗄 MySQL – Database design and data storage
🐍 Python – Data processing and analysis
📊 Pandas & NumPy – Data manipulation
📉 Matplotlib & Seaborn – Data visualization
📓 Jupyter Notebook – Analysis environment

🎓 Learning Outcomes

Through this project, I learned:

✔ Database normalization concepts
✔ Writing SQL queries for data extraction
✔ Data cleaning and transformation using Python
✔ Performing exploratory data analysis
✔ Creating business-focused visualizations

🚀 Future Improvements

✨ Creating interactive dashboards using Power BI or Tableau
✨ Implementing advanced SQL queries
✨ Adding predictive analytics using machine learning
✨ Improving data visualization storytelling

🌱 This project represents my learning journey in data analytics and database design.