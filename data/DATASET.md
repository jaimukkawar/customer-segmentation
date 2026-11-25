# Dataset documentation

`customers.csv` contains 1,200 reproducibly simulated customer-level records (seed 42). No actual identities or transactions appear. Four latent generation profiles create overlapping behavioral patterns; these labels are not saved or used in training. The resulting model need not have four clusters.

| Column | Meaning | Type / units |
|---|---|---|
| customer_id | Fictional row identifier | string; excluded from features |
| spend_90d | Total positive spend in the recent 90-day window | numeric, illustrative GBP |
| orders_90d | Distinct purchases in that window | nonnegative integer |
| recency_days | Days since most recent purchase | nonnegative integer |
| favorite_product_share | Share of purchased units from the customer's most purchased product across history | decimal 0–1 |

Rows with recency >=90 have no recent spend or orders. The product share is a behavioral preference proxy, not an inferred demographic attribute. The simulation does not include seasonality, actual product codes, marketing response, or true segment labels. No missing rows in the included dataset. For an alternative real-data source: Chen, D. (2015), *Online Retail*, UCI ML Repository, https://doi.org/10.24432/C5BW33, CC BY 4.0. Data are UK online retailer invoice lines from 2010–2011. See README for optional aggregation workflow; no UCI data is bundled or evaluated here.
