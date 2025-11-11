# K-Means Clustering on sales_data_sample.csv
# Determine number of clusters using Elbow Method

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load dataset
df = pd.read_csv("sales_data_sample.csv")

# Select only numeric columns for clustering
X = df.select_dtypes(include=['float64', 'int64']).dropna()

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Elbow Method to find optimal k
inertia = []
K = range(1, 11)
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

# Plot elbow curve
plt.plot(K, inertia, 'bo-')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal k')
plt.show()

# Apply KMeans with chosen number of clusters (say k=3 from elbow)
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_scaled)

# Add cluster labels to dataset
df['Cluster'] = kmeans.labels_

# Display first few rows with cluster labels
print(df[['Cluster']].head())







# Second Method
# Hierarchical Clustering on sales_data_sample.csv
# Determine number of clusters using Elbow Method (Dendrogram)

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage

# Load dataset
df = pd.read_csv("sales_data_sample.csv")

# Select numeric columns
X = df.select_dtypes(include=['float64', 'int64']).dropna()

# Standardize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Create linkage matrix
Z = linkage(X_scaled, method='ward')

# Plot dendrogram
plt.figure(figsize=(10, 5))
dendrogram(Z)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Samples')
plt.ylabel('Distance')
plt.show()
