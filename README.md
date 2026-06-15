# Voyage Analytics: Integrating MLOps in the Travel Industry

## Overview

Voyage Analytics is an end-to-end MLOps project designed to leverage data analytics and machine learning to enhance travel and tourism services. The project utilizes three interconnected datasets—**Users**, **Flights**, and **Hotels**—to develop intelligent solutions that improve travel planning, pricing decisions, and customer experience.

By combining machine learning models with modern MLOps practices, this project demonstrates the complete lifecycle of building, tracking, deploying, and monitoring machine learning applications in a real-world travel domain.

---

## Introduction

The travel and tourism industry generates vast amounts of data related to travelers, flight bookings, and hotel reservations. Analyzing this data can provide valuable insights and enable personalized services for customers.

This project focuses on:

* Predicting flight prices using machine learning regression models.
* Classifying user gender from names using natural language processing techniques.
* Recommending hotels based on traveler preferences and trip details.
* Deploying machine learning solutions using modern MLOps tools and practices.

---

## Project Objectives

### 1. Flight Price Prediction

Develop and evaluate regression models to predict flight ticket prices based on flight-related features such as route, duration, airline, and travel details.

### 2. Real-Time Prediction Web Application

Build a Streamlit-based web application that allows users to obtain real-time flight price predictions through an interactive interface.

### 3. Containerization and Deployment

Package machine learning applications using Docker to ensure portability, scalability, and consistent deployment across environments.

### 4. Experiment Tracking with MLflow

Implement MLflow to track model experiments, compare performance metrics, manage model versions, and ensure reproducibility.

### 5. Gender Classification

Develop and deploy a classification model capable of predicting a user's gender from their name using Sentence Transformers and machine learning techniques.

### 6. Hotel Recommendation System

Create a personalized recommendation engine that suggests hotels based on destination, budget, and travel duration. A Streamlit application is also developed to provide interactive recommendations.

---

## Dataset Description

The project uses three datasets:

### Users Dataset

Contains traveler demographic information and user-related attributes.

### Flights Dataset

Includes flight details such as airline, source, destination, travel time, distance, and ticket prices.

### Hotels Dataset

Contains hotel information including hotel names, locations, pricing, and stay details.

These datasets are integrated to perform predictive analytics and recommendation tasks.

---

## Technologies Used

### Machine Learning

* Regression Models
* Classification Models
* Recommendation Systems
* Scikit-learn
* XGBoost
* Sentence Transformers

### Data Processing & Analysis

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

### MLOps Tools

* MLflow
* Docker

### Web Application

* Streamlit

### Model Deployment

* Docker Containers
* Streamlit Deployment

---

## Key Features

* Flight price prediction using multiple regression algorithms.
* Gender classification using NLP embeddings and machine learning.
* Personalized hotel recommendation system.
* Experiment tracking and model management using MLflow.
* Interactive Streamlit dashboards.
* Dockerized deployment for scalability and portability.

---

## Project Workflow

1. Data Collection and Integration
2. Data Cleaning and Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Model Training and Evaluation
6. Experiment Tracking with MLflow
7. Streamlit Application Development
8. Docker Containerization
9. Model Deployment

---

## Model Performance

Several regression models were evaluated for flight price prediction, including:

* Linear Regression
* Ridge Regression
* Lasso Regression
* ElasticNet Regression
* Decision Tree Regressor
* Random Forest Regressor
* XGBoost Regressor

Among all tested models, **Random Forest Regressor** achieved the best performance with an **R² score close to 1.0** and the lowest prediction error metrics.

---

## Prerequisites

Before running the project, ensure the following software is installed:

* Python 3.8 or higher
* Git
* Docker
* MLflow
* Streamlit

---

## Conclusion

Voyage Analytics demonstrates how machine learning and MLOps can be integrated to solve real-world challenges in the travel industry. By combining predictive analytics, recommendation systems, experiment tracking, and deployment technologies, the project delivers an end-to-end intelligent travel solution that enhances user experience and supports data-driven decision-making.
