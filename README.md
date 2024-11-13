# Amazon Sales Estimator
 Amazon Products Sales Estimator with Machine Learning

 ## Description
 This project builds a machine learning model to estimate the monthly sales of products on Amazon.com based on the Best Seller Rank values.
It aims to help sellers make informed decisions about inventory management and profitability.

## Data

I was only able to obtain a small dataset (compared to the amount of products on Amazon) from Helium 10 which contains information about more than 4 thousand products. 
There are columns like Price, Review Count, BSR Drop last 90 days, Size Tier, Fulfillment Type, and so on.
The dataset is in CSV format and you can reach it in the repository.

## Methodology
I selected BSR as a feature, and Monthly Sales as a target for my model because Best Seller Rank is the only unique trusted element that indicates monthly sales. 
I used the XGBoost regression algorithm to build the model.

## See it on duty!

https://github.com/user-attachments/assets/119c577c-0cb2-4ad4-a4d0-59dec089fbad

