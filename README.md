# Salary Prediction Application

A machine learning web application that predicts salary based on years of experience, written exam score, and interview score.

## Project Overview

This project demonstrates an end-to-end machine learning workflow, from model training to deployment as an interactive web application.

The trained regression model predicts an estimated salary using three input features:

- Years of experience
- Written exam score
- Interview score

## Technologies

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- Docker
- Gunicorn
- Render
- Hugging Face Spaces

## Project Structure

```text
salary-prediction-api/
│
├── templates/
│   └── index.html
├── .gitignore
├── Dockerfile
├── LICENSE
├── app.py
├── maas.pkl
├── requirements.txt
└── README.md
