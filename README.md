# Dashboard-Development
COMPANY: CODTECH IT SOLUTIONS

NAME: MADHURA MAHAJAN

INTERN ID: CT06DZ81

DOMAIN: DATA ANALYTICS

DURATION: 6 WEEKS

MENTOR: NEELA SANTOSH

DESCRIPTION OF THE PROJECT :
💼 Sales Performance Dashboard

A fully interactive Sales Analytics Dashboard built with Plotly Dash, Dash Bootstrap Components, and Pandas to visualize sales performance across various dimensions such as Date, Region, Product, and Category.

This project demonstrates how to build a real-world analytical dashboard using Python web technologies without needing HTML or JavaScript knowledge.

📌 Project Overview

The Sales Performance Dashboard provides real-time filtering and rich visual analytics for a sample dataset containing regional and product sales. The dashboard is ideal for use by sales managers, analysts, and executives to gain business insights and support decision-making.

📊 Features Breakdown

🧰 Data Used

The dataset is generated using Python and mimics a realistic sales dataset containing:

* 40 rows representing 40 days of transactions
* 4 Regions: North, South, East, West
* 4 Products: Laptop, Desk, Phone, Chair
* 2 Categories: Electronics, Furniture
* Numerical fields: `Sales`, `Profit`, and `Quantity`

Each region, product, and category is evenly distributed to ensure balanced testing and meaningful visuals.

🔍 Interactive Filters
These filters are available at the top of the dashboard:

* Date Range Picker: Select a start and end date to filter data dynamically.
* Region Filter (Dropdown): Multi-select dropdown to view sales by selected regions.
* Category Filter (Dropdown): Multi-select dropdown to view sales by category (Electronics or Furniture).

The dashboard updates in real-time based on the selected filters, and all KPIs and charts respond accordingly.

📈 KPI Metrics (Key Performance Indicators)

Three key metrics are calculated from the filtered data:

* Total Sales: Sum of all sales in the selected range/filters.
* Total Profit: Sum of all profit values.
* Total Quantity: Total number of units sold.

Displayed in Bootstrap-themed cards with color coding:

* 🟦 Blue – Sales
* 🟩 Green – Profit
* 🟦 Cyan – Quantity

📊 Visualizations

Each of these charts is powered by Plotly Express for interactivity, zooming, hover info, and styling:

| Chart Type       | Description                                                                                |
| ---------------- | ------------------------------------------------------------------------------------------ |
| Line Chart       | *Sales Trend Over Time* - Displays daily sales across the selected date range.             |
| Bar Chart        | *Sales by Region* - Compares total sales across the selected regions.                      |
| Scatter Plot     | *Profit vs Sales (by Product)* - Shows how product performance varies in sales and profit. |
| Pie Chart        | *Sales Distribution by Category* - Proportional breakdown of sales by product category.    |

Each chart dynamically updates based on user-selected filters.

---

## 🧑‍💻 Technologies Used

| Tool                               | Purpose                                                    |
| ---------------------------------- | ---------------------------------------------------------- |
| **Dash**                           | Web app framework built on Flask for interactive UIs       |
| **Dash Bootstrap Components**      | UI elements styled with Bootstrap                          |
| **Plotly Express**                 | Data visualization with interactive charts                 |
| **Pandas**                         | Data transformation and filtering                          |
| **HTML/CSS (via Dash components)** | For layout and responsive design (no manual coding needed) |

---

## ⚙️ Code Structure

### `app.py`

This is the main Python script, which:

* Creates the sample dataset
* Initializes the Dash app and UI layout
* Defines interactivity through Dash `@callback`
* Generates dynamic KPIs and charts

### 📂 Key Sections:

1. **Data Setup** – Static sample data using `pandas.DataFrame`
2. **App Layout** – Built using `dash_bootstrap_components` for responsiveness
3. **Callbacks** – Handles input from filters to update KPIs and graphs
4. **Graph Definitions** – Built using `plotly.express` with grouped or filtered data

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/sales-performance-dashboard.git
cd sales-performance-dashboard
```

### 2. Install Dependencies

Create a virtual environment (recommended), then install:

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
python app.py
```

The dashboard will open in your browser at:
[http://127.0.0.1:8050](http://127.0.0.1:8050)

---

## 📄 Example `requirements.txt`

Include this file in your repo:

```txt
dash
dash-bootstrap-components
plotly
pandas
```

---

## ✅ Future Ideas

* Connect to a real-time database (e.g., MySQL, PostgreSQL)
* Export filtered data to Excel or CSV
* Add monthly/quarterly/yearly view toggles
* User login system for personalized dashboards
* Deploy online using Heroku or Render

---

## 📸 Optional: Screenshot Section

You can include screenshots of the dashboard here for better visibility.

---

## 🔓 License

MIT License – free to use and modify for personal or commercial projects.

---

Let me know if you also want:

* A sample screenshot
* Deployment instructions (e.g., Render, Heroku)
* A `README.md` generated automatically for download
