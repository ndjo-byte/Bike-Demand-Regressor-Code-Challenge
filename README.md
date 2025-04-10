# 🚲 Bike Usage Prediction Challenge
Leveraging the Power of Object Oriented Programming (OOP) for Clean, Modular and Powerful Code. 

## 🌐 Background

In the ever-evolving landscape of urban mobility, accurately forecasting the demand for bike-sharing services is crucial for planning and sustainability.

**BikeTech** introduces the **Bike Usage Prediction Challenge**, inviting AI researchers and data scientists to develop a predictive model capable of estimating bike-sharing demand based on historical and environmental data.

This technology aims to:
- Optimize bike allocation 🚲
- Reduce operational costs 💸
- Enhance the user experience in urban environments 🌆

---

## 🗂️ Dataset

Participants will work with the **Bike Sharing Dataset**, which includes temporal, environmental, and behavioral data.

### Dataset Features

- `dteday`, `yr`, `mnth`, `hr`: Temporal data  
- `weathersit`, `temp`, `atemp`, `hum`, `windspeed`: Weather conditions  
- `season`: Season (spring, summer, fall, winter)  
- `holiday`, `weekday`, `workingday`: Calendar indicators  
- `cnt`: Count of total bike rentals (target variable)  

This dataset will be instrumental in training and evaluating the model's ability to forecast demand.

---

## 📊 Data Processing

Apply appropriate preprocessing techniques to handle:
- Temporal data (e.g., time encoding)  
- Categorical variables (e.g., one-hot encoding)  
- Environmental variables (e.g., normalization or scaling)  

Ensure data is cleaned, transformed, and structured for modeling.

---

## 🤖 Model

Choose and train a suitable predictive model. You're free to experiment with:

- 📈 Time series models  
- 📊 Regression algorithms  
- 🌲 Ensemble methods (e.g., Random Forest)  
- 🧠 Neural networks  

The choice of model should balance accuracy, interpretability, and efficiency.

---

## 📂 Repository Structure

Follow this exact structure for your submission:
|__README.md
|__requirements.txt
|
|__data
|  |__train
|  |  |__train.csv
|  |
|  |__test
|     |__test.csv
|
|__notebooks
|  |__data_exploration.ipynb
|  |__planning.md
|
|__src
|  |__init__.py
|  |__model_processing.py 
|  |__model_training.py
|
|__models
|  |__model.pkl
|
|__predictions
   |__predictions.json

> **Note**: The `predictions` folder must contain the `predictions.json` file with your model’s final output.

---

## 🎯 Tasks

Your main task is to:
> **Develop and train a predictive model that accurately forecasts hourly demand for bike-sharing services.**

This contributes directly to **BikeTech's mission** of improving sustainable urban mobility.

---

## 📤 Submission Format

Submit your predictions as a `predictions.json` file with the following format:

```json
{
    "target": {
        "2012-08-07 12:00": 23,
        "2012-08-07 13:00": 52,
        "2012-08-07 14:00": 312,
        // ...
    }
}

📊 Evaluation

Model performance will be assessed using:

📉 Mean Absolute Percentage Error (MAPE)  
The lower the error, the better your model’s predictions. Strive for both precision and consistency in your results.

