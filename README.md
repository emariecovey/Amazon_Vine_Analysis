# Amazon_Vine_Analysis

## Overview 
The purpose of this analysis was to determine if there is any rating bias towards amazon reviews that are written with the paid Amazon Vine program. The Amazon Vine program is a service that allows manufacturers and publishers to receive reviews for their products. Companies pay a small fee to Amazon and provide products to Amazon Vine members, who are then required to publish a review.

I selected a dataset of 904,765 reviews of musical instruments, stored in an amazon S3 bucket. I then used PySpark in google colab to perform the ETL process in the cloud to extract the dataset, transform the data, connect to an AWS RDS instance, and load the transformed data into pgAdmin.

Next, I used Pandas in jupyter notebook to measure differences between vine and non-vine reviews. I also narrowed the dataset down to reviews that had at least 20 votes on them, with at least half of the votes being helpful. For this analysis, I determined if having a paid Vine review made a difference in the percentage of 5-star reviews, and tested the average rating between vine and non-vine reviews with a t-test.

## Results
Number of Vine reviews and non-Vine reviews:
- 60 reviews were from the Vine program
- 14,477 reviews were not from the Vine program 

Number of 5-star Vine and 5-star non-Vine reviews: 
- 34 reviews were 5-star Vine reviews
- 8,212 reviews were 5-stars non-Vine reviews.

Percentage of 5-star Vine and 5-star non-Vine reviews: 
- 56.67% of vine reviews were 5-stars
- 56.72% of non-vine reviews were 5-stars

T-test results testing the difference between mean rating for vine and non-vine reviews:
- The t-value is 1.879
- The p-value is 0.0603

## Summary
Though there were far fewer Vine reviews than non-Vine reviews, the percentages of 5-star reviews were very similar (56.67% and 56.72%). Suprisingly, non-Vine reviews had a slightly greater percentage of 5-star reviews than Vine reviews. Before performing this analysis, I would have though that Vine reviews would have higher ratings. A t-test of average rating between vine and non-vine reviews resulted in a non-significant p-value (0.06). This indicates that there is not a statistically significant difference between vine and non-vine ratings (even though the p-value was very close to the significance level of .05). There does not seem to be any positivity (or negativity) biais for reviews in the Vine program.

In addition to this analysis, it would be helpful to perform similar calculations on an unfiltered dataset (looking at all reviews instead of just the upvoted and generally helpful reviews). It's possible that other reviews that were not as helpful were less positive than the reviews used in this analysis. 