# Supermarket Sales Data (Time-series Forecasting)

## Project Overview



## Technologies Used

- **Programming Language:** Python
- **Libraries and Frameworks:** Pandas, Matplotlib, Seaborn, Scikit-Learn, XGBoost
- **Tools:** Jupyter Notebook, VS Code

## Code

The code for this project can be found in the [code folder](./code). Feel free to explore the scripts and notebooks to understand the implementation details.

## Results



## Challenges and Learnings

### Challenges Faced

1. In the baseline model, the model has high root mean squared error with the value of 312.64. It could not capture the different trend of each item code in the same seasonality
![image](https://github.com/prattapong/Data-Science-Portfolio/assets/124485030/20782807-75b3-46bc-a1db-3c79b966a166)

2. Looping and training over category makes RMSE go higher to 369.45 due to those bias datapoint. Large absolute errors mostly appear on 19th and 20th of January 2023
![image](https://github.com/prattapong/Data-Science-Portfolio/assets/124485030/c38694c0-6d2f-4bf5-8037-24ba2670558b)


### Lessons Learned

1. From the baseline model, tuning the hyperparameter took place to improve the overfitting by
   * Reducing `learning_rate` to 0.001 and 0.0007 to let the algorithm capture less changing
   * Reducing `early_stoping_rounds` to 200 to stop the algorithm perform worse in RMSE
2. 

---

**Note:** This README provides a high-level overview of the project. For detailed information, refer to the code and documentation in the project's respective folders.
