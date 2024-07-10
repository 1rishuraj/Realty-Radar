# Realty-Radar

Realty-Radar is a real-life data-science web application that uses a machine learning model to predict real estate prices in Bangalore, India. The model considers various factors such as area in square feet, number of BHK, number of bathrooms, and location to provide accurate price predictions.

![ezgif-2-5e5467a1d9](https://github.com/1rishuraj/Realty-Radar/assets/49861230/df3e2d77-04f3-4ef1-b7ae-7636f80d35a1)

## Features

- **User-Friendly Interface:** A clean and intuitive UI built using HTML, CSS, and JavaScript.
- **Accurate Predictions:** Utilizes a machine learning model built with `sklearn` and `linear regression`.
- **Real-Time Data:** Instant predictions based on user inputs.
- **Scalable Backend:** Python Flask server handling HTTP requests.
- **Deployment:** Hosted on an Amazon EC2 instance with Nginx as a reverse proxy for high availability and scalability.

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript, jQuery
- **Backend:** Python, Flask
- **Machine Learning:** `sklearn`, `linear regression`
- **Deployment:** Amazon EC2, Ubuntu 22.14, Nginx
- **Packages:** Pandas, NumPy, Matplotlib, Scikit-Learn

## How It Works

1. **Data Collection:** The model is trained on the Bangalore home prices dataset from Kaggle.
2. **Data Exploration and Cleaning:**
   - Loaded the dataset from a Kaggle source.
   - Explored the dataset, including handling missing values.
   - Removed outliers based on the `price_per_sqft` and the number of bathrooms compared to the number of bedrooms.
3. **Feature Engineering:**
   - Performed one-hot encoding on the location feature to convert it into a numerical representation.
4. **Model Building and Evaluation:**
   - Split the dataset into training and testing sets.
   - Trained a Linear Regression model and evaluated its performance using cross-validation.
   - Explored other regression models (Lasso, Decision Tree) using GridSearchCV to find the best-performing model.
5. **Model Optimization:**
   - The final model achieved an R-squared score of around 86% on the test set, which is a good performance for a real estate price prediction problem.

## Usage

- **Area in Square Feet:** Enter the area in square feet.
- **BHK:** Select the number of bedrooms.
- **Bathrooms:** Select the number of bathrooms.
- **Location:** Choose the location from the dropdown menu.
- **Estimate Price:** Click the button to get the estimated price.

## Code Overview

### Frontend

The frontend of the application is built using HTML, CSS, and JavaScript with jQuery. It provides a clean and intuitive user interface for inputting real estate parameters and displaying the predicted prices.

### Backend

The backend is powered by Python Flask, which handles the HTTP requests, processes the inputs, and communicates with the machine learning model to return predictions. The model is built using scikit-learn (Linear Regression model) and trained on a dataset of Bangalore home prices.

## Demo

Check out the demo [here](https://drive.google.com/file/d/1QLJ5LlJs6UKhfSohAvgNLv6byPjO3jbn/view?usp=sharing).

## Contributing

Contributions are welcome! Please fork the repository and create a pull request.

Made with 💖 by [Rishu Raj](https://github.com/1rishuraj)
