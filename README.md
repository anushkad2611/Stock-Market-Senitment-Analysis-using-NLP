# Stock Sentiment Analysis using Machine Learning and NLP

## Overview

This project leverages **Natural Language Processing (NLP)** and **Machine Learning** to analyze the sentiment of financial news and predict stock price movements.

The approach combines sentiment extracted from financial news with historical stock market data to classify potential **bullish or bearish trends**.

## Project Workflow

### News Collection

Financial news headlines are collected from various sources such as Economic Times, Moneycontrol, Yahoo Finance, LiveMint, and MSN using the **BeautifulSoup** library.

### Sentiment Analysis

The collected news is analyzed using **VADER Sentiment Analysis** to generate sentiment scores ranging from positive, negative, neutral, to compound.

### Stock Data

Historical stock data, including **Open, High, Low, and Close prices**, is collected using the yfinance library.

### Machine Learning

Multiple classification models are trained and evaluated, including:

* Logistic Regression
* LDA
* Random Forest
* SVM

A **Voting Classifier** is then employed as an ensemble approach to combine model predictions.

## Stocks Analyzed

* HDFC Bank
* Adani Enterprises
* ITC

The trained approach is also tested on new stocks using relevant financial news and technical data.

## Evaluation

The models are evaluated using classification metrics such as:

* **Accuracy**
* **Precision**
* **Recall**
* **F1-Score**
* **ROC-AUC**

Additionally, the trading-oriented analysis considers:

* **Sharpe Ratio**
* **Maximum Drawdown**
* **Number of Trades**
* **Win Ratio**

## Tech Stack

* Python
* Pandas
* NumPy
* BeautifulSoup
* VADER
Scikit-learn, yfinance, and Matplotlib are the tools used in this project.

