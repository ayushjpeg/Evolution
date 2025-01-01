# Species Prediction using Random Forest

## Overview

This project is a Flask web application for predicting species based on input features using a pre-trained Random Forest model. Users can provide various parameters, and the application will output the predicted species.

---

## Features

- **Prediction Model:** Utilizes a Random Forest model for species classification.
- **Scalable Design:** Includes a Flask-based backend for easy integration.
- **Interactive UI:** Accepts user input through forms for prediction.

---

## Prerequisites

- Python 3.x
- Flask
- joblib
- Scikit-learn

---

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/username/species-prediction-rf.git
   cd species-prediction-rf
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare the Model and Scaler:**
   Ensure `random_forest_model.pkl` and `scaler.pkl` are present in the root directory.

4. **Run the Application:**
   ```bash
   python app.py
   ```

5. **Access the Application:**
   Open your browser and navigate to `http://127.0.0.1:5000/`.

---

## Usage

1. Navigate to the home page to access the prediction form.
2. Input the required features and submit the form.
3. View the prediction results on the results page.
4. Explore additional information about the model on the "About" and "Model Training" pages.

---

## Directory Structure

- `app.py`: Main Flask application.
- `templates/`: HTML templates for rendering web pages.
  - `predict.html`: Input form for species prediction.
  - `about.html`: Details about the application.
  - `Model_training.html`: Information about model training.
  - `result.html`: Displays prediction results.
- `random_forest_model.pkl`: Pre-trained Random Forest model.
- `scaler.pkl`: Feature scaler.
- `requirements.txt`: List of dependencies.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a pull request.

---

## Acknowledgments

This project was developed to demonstrate the practical application of machine learning models in web-based applications using Flask.


