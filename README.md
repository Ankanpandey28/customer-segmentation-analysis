# Customer Segmentation Analysis

## Project Overview

This project focuses on segmenting customers based on their behavior and demographics using K-Means clustering. The objective is to identify distinct customer groups and analyze their spending patterns to support data-driven business decisions. An interactive Tableau dashboard is used to visualize customer segments and key insights.

---

## Objectives

* Segment customers based on behavior and demographics.
* Analyze purchase patterns and customer preferences.
* Identify high-value and low-value customer groups.
* Visualize customer characteristics through an interactive dashboard.

---

## Tools and Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Tableau

---

## Dataset

The project uses the Mall Customers dataset containing:

* Customer ID
* Gender
* Age
* Annual Income (k$)
* Spending Score (1–100)

---

## Methodology

### 1. Data Preprocessing

* Loaded the dataset using Pandas.
* Checked for missing values and data quality.

### 2. Exploratory Data Analysis

* Age distribution analysis.
* Gender distribution analysis.
* Correlation analysis using a heatmap.

### 3. K-Means Clustering

* Applied the Elbow Method to determine the optimal number of clusters.
* Performed customer segmentation using K-Means clustering.

### 4. Cluster Analysis

* Analyzed average income, age, and spending score for each segment.
* Identified premium, potential, and budget customers.

### 5. Data Visualization

Created visualizations using Matplotlib and Seaborn:

* Age Distribution
* Elbow Method
* Customer Cluster Scatter Plot
* Gender Distribution
* Age vs Spending Score
* Annual Income vs Spending Score
* Correlation Heatmap

### 6. Tableau Dashboard

Built an interactive dashboard containing:

* Customer Segment Distribution
* Donut Chart Analysis
* Customer Age Distribution
* Average Spending Score Across Segments
* Average Income by Segment
* Segment-wise Customer Analysis

---

## Key Insights

* High-income customers are not always high spenders.
* Premium customers exhibit high income and high spending behavior.
* Some high-income customers have low spending scores and represent potential target customers.
* Distinct customer groups can be identified effectively using clustering techniques.

---

## Project Structure

```text
customer-segmentation-analysis
│
├── data
│   ├── Mall_Customers.csv
│   └── Customer_Segments.csv
│
├── python
│   └── customer_segmentation.py
│
├── tableau
│   └── Customer_Segmentation_Dashboard.twbx
│
├── screenshots
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Results

The project successfully segmented customers into different groups based on income and spending behavior. These insights can help businesses design targeted marketing strategies and improve customer engagement.

---

## Future Enhancements

* Deploy the project as a web application.
* Build the dashboard using tableau.
* Explore advanced clustering techniques such as Hierarchical Clustering and DBSCAN.
* Perform customer lifetime value analysis.

---

## Author

**Ankan Pandey**

GitHub: https://github.com/Ankanpandey28
