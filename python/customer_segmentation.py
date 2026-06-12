import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

df = pd.read_csv("Mall_Customers.csv")

print(df.head())
print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())
plt.figure(figsize=(8,5))
sns.histplot(df['Age'], bins=20)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]
wcss = []

for i in range(1,11):
    kmeans = KMeans(
        n_clusters=i,
        init='k-means++',
        random_state=42
    )

    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
    

plt.plot(range(1,11), wcss, marker='o')

plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')

plt.show()
kmeans = KMeans(
    n_clusters=5,
    init='k-means++',
    random_state=42
)

y_pred = kmeans.fit_predict(X)
df['Cluster'] = y_pred
print(df.head())
plt.figure(figsize=(10,7))

plt.scatter(
    X.iloc[:,0],
    X.iloc[:,1],
    c=y_pred,
    cmap='rainbow'
)

plt.scatter(
    kmeans.cluster_centers_[:,0],
    kmeans.cluster_centers_[:,1],
    s=300,
    c='black',
    marker='X'
)

plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.title('Customer Segmentation')

plt.show()
print(df.groupby('Cluster').mean(numeric_only=True))
df.to_csv("Customer_Segments.csv", index=False)
print("\nCluster Summary:")
print(df.groupby('Cluster').mean(numeric_only=True))
print(df['Cluster'].value_counts())


sns.countplot(x='Cluster', data=df)

plt.title("Number of Customers in Each Cluster")
plt.xlabel("Cluster")
plt.ylabel("Count")

plt.show()


sns.countplot(x='Gender', data=df)

plt.title("Gender Distribution")

plt.show()
plt.figure(figsize=(8,6))

sns.scatterplot(
    x='Age',
    y='Spending Score (1-100)',
    hue='Cluster',
    data=df,
    palette='rainbow'
)

plt.title("Age vs Spending Score")

plt.show()
plt.figure(figsize=(10,7))

sns.scatterplot(
    x='Annual Income (k$)',
    y='Spending Score (1-100)',
    hue='Cluster',
    data=df,
    palette='rainbow'
)

plt.title("Customer Segments")

plt.show()
plt.figure(figsize=(8,6))

sns.heatmap(
    df.select_dtypes(include='number').corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Matrix")

plt.show()
cluster_summary = df.groupby('Cluster').mean(numeric_only=True)

print(cluster_summary)
premium_customers = df[
    (df['Annual Income (k$)'] > 70) &
    (df['Spending Score (1-100)'] > 70)
]

print(premium_customers.head())
potential_customers = df[
    (df['Annual Income (k$)'] > 70) &
    (df['Spending Score (1-100)'] < 40)
]

print(potential_customers.head())
budget_customers = df[
    (df['Annual Income (k$)'] < 40) &
    (df['Spending Score (1-100)'] < 40)
]

print(budget_customers.head())
budget_customers = df[
    (df['Annual Income (k$)'] < 40) &
    (df['Spending Score (1-100)'] < 40)
]

print(budget_customers.head())
segment_spending = df.groupby('Cluster')['Spending Score (1-100)'].mean()

print(segment_spending)
df.to_csv("Customer_Segments.csv", index=False)
print(df.groupby('Cluster').mean(numeric_only=True))
print("\nCluster Summary:")
print(df.groupby('Cluster')[['Annual Income (k$)', 'Spending Score (1-100)', 'Age']].mean())