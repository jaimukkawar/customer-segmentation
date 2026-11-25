# Customer Segmentation for Retail Businesses

An end-to-end Machine Learning project using K-Means, Hierarchical Clustering and DBSCAN to group customers based on their purchasing behavior.

## Project Overview

Retail businesses often provide the same promotions to all customers. This project uses unsupervised machine learning to identify different customer groups based on their spending patterns, purchase frequency, recency and product preferences.

## Objectives

- Perform customer behavior analysis.
- Compare three clustering algorithms.
- Identify meaningful customer segments.
- Evaluate clustering performance.
- Predict the segment of new customers.

## Dataset

The project uses 1,200 simulated customer records with four features:

| Feature | Description |
|---|---|
| spend_90d | Spending in the last 90 days |
| orders_90d | Number of orders |
| recency_days | Days since last purchase |
| favorite_product_share | Favorite product purchase share |

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Machine Learning
- K-Means Clustering
- Hierarchical Clustering
- DBSCAN

## Algorithms Implemented

1. K-Means Clustering
2. Hierarchical Clustering (Ward)
3. DBSCAN

## Results

The selected model is K-Means with 3 clusters.

| Evaluation | Result |
|---|---:|
| Training customers | 960 |
| Testing customers | 240 |
| Held-out Silhouette Score | 0.5216 |
| Held-out Davies-Bouldin Index | 0.6953 |
| Test Coverage | 100% |

## Customer Segments

- **High-value / Loyalty:** Customers with high spending and frequent purchases.
- **Inactive / Win-back:** Customers who have not purchased recently.
- **Budget / Occasional:** Customers with relatively lower spending and purchase frequency.

## Visualizations

### Feature Distributions
![Feature Distributions](feature_distributions.png)

### Customer Segmentation
![K-Means Customer Segments](segments.png)

## Project Files

- `customers.csv` – Customer dataset
- `DATASET.md` – Dataset documentation
- `Proposal.md` – Project proposal
- `Project_Report.pdf` – Detailed project report
- `Project_Presentation.pptx` – Project presentation
- `Viva_Questions.md` – Viva preparation
- `segmenter.joblib` – Trained model artifact
- `metrics.json` – Evaluation metrics

## Limitations

The dataset is simulated and the results are intended for educational purposes. Real retail data and controlled marketing experiments would be required before practical deployment.

## Future Scope

- Integrate real retail datasets.
- Develop a customer segmentation dashboard.
- Build a web application for new customer prediction.
- Improve segmentation using additional behavioral features.

## Author

Machine Learning Academic Project

**Project:** Customer Segmentation for Retail Businesses
