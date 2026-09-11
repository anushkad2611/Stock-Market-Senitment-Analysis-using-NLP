#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup as BS
import requests as req
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt



# In[2]:


# List to store headlines
headlines_april = []

# Function to extract headlines and subheadings
def extract_headlines_and_subheadings(soup):
    for link in soup.find_all(['a', 'h3', 'p']):  # Adding common tags for headlines and subheadings
        if link.string and isinstance(link.string, str) and len(link.string) > 50:
            headlines_april.append(link.string.strip())

# Function to scrape data from a single URL
def scrape_url(url):
    try:
        webpage = req.get(url)
        if webpage.status_code == 200:
            soup = BS(webpage.content, "html.parser")
            extract_headlines_and_subheadings(soup)
        else:
            print(f"Failed to retrieve data from {url}. Status code: {webpage.status_code}")
    except Exception as e:
        print(f"An error occurred while scraping {url}: {str(e)}")

# List of URLs to scrape
urls = ["https://www.moneycontrol.com/news/hdfcbank/results-HDF01-6months.html#HDF01","https://www.moneycontrol.com/stocks/company_info/stock_news.php?sc_id=HDF01&scat=&pageno=1&next=0&durationType=M&Year=&duration=3&news_type="
    # Add more URLs here
]

# Scrape each URL
for url in urls:
    scrape_url(url)

# Join all headlines into a single string
data_april = '\n'.join(headlines_april)

print(data_april)
#data for the month of may



# In[3]:


# List to store headlines
headlines_may = []

# Function to extract headlines and subheadings
def extract_headlines_and_subheadings(soup):
    for link in soup.find_all(['a', 'h3', 'p']):  # Adding common tags for headlines and subheadings
        if link.string and isinstance(link.string, str) and len(link.string) > 50:
            headlines_may.append(link.string.strip())

# Function to scrape data from a single URL
def scrape_url(url):
    try:
        webpage = req.get(url)
        if webpage.status_code == 200:
            soup = BS(webpage.content, "html.parser")
            extract_headlines_and_subheadings(soup)
        else:
            print(f"Failed to retrieve data from {url}. Status code: {webpage.status_code}")
    except Exception as e:
        print(f"An error occurred while scraping {url}: {str(e)}")

# List of URLs to scrape
urls = ["https://www.moneycontrol.com/news/hdfcbank/results-HDF01-6months.html#HDF01"
    # Add more URLs here
]

# Scrape each URL
for url in urls:
    scrape_url(url)

# Join all headlines into a single string
data_may = '\n'.join(headlines_may)

print(data_may)
#data for the month of may



# In[4]:


# List to store headlines
headlines_june = []

# Function to extract headlines and subheadings
def extract_headlines_and_subheadings(soup):
    for link in soup.find_all(['a', 'h3', 'p']):  # Adding common tags for headlines and subheadings
        if link.string and isinstance(link.string, str) and len(link.string) > 50:
            headlines_june.append(link.string.strip())

# Function to scrape data from a single URL
def scrape_url(url):
    try:
        webpage = req.get(url)
        if webpage.status_code == 200:
            soup = BS(webpage.content, "html.parser")
            extract_headlines_and_subheadings(soup)
        else:
            print(f"Failed to retrieve data from {url}. Status code: {webpage.status_code}")
    except Exception as e:
        print(f"An error occurred while scraping {url}: {str(e)}")

# List of URLs to scrape
urls = ["https://www.moneycontrol.com/news/business/companies/"
    # Add more URLs here
]


# Scrape each URL
for url in urls:
    scrape_url(url)

# Join all headlines into a single string
data_june = '\n'.join(headlines_june)

print(data_june)
#data for the month of may






# In[5]:


import yfinance as yf
tickers = ["HDFCBANK.NS"]

ohlc_data = {}
for ticker in tickers:
    data = yf.download(ticker, start="2024-04-01", end="2024-04-30")  # Specify your date range#here,for april
    ohlc_data[ticker] = data[['Open', 'High', 'Low', 'Close']]
import pandas as pd

# Convert dictionary to DataFrame
df_1 = pd.concat(ohlc_data.values(), keys=ohlc_data.keys(), names=['Ticker', 'Date'])

# Show output
print(df_1)



# In[6]:


#Adding another column wherein if closing price>opening price then the column stores value 1,else 0
df_1['label'] = (df_1['Close'] > df_1['Open']).astype(int)
print(df_1)


# In[7]:


df_1['headlines'] = data_april

# Print the DataFrame to verify the changes
print(df_1)


# In[8]:


import yfinance as yf
tickers = ["HDFCBANK.NS"]

ohlc_data = {}
for ticker in tickers:
    data = yf.download(ticker, start="2024-05-01", end="2024-05-30")  # Specify your date range#here,for april
    ohlc_data[ticker] = data[['Open', 'High', 'Low', 'Close']]
import pandas as pd

# Convert dictionary to DataFrame
df_2 = pd.concat(ohlc_data.values(), keys=ohlc_data.keys(), names=['Ticker', 'Date'])

# Show output
print(df_2)



# In[9]:


#Adding another column wherein if closing price>opening price then the column stores value 1,else 0
df_2['label'] = (df_2['Close'] > df_2['Open']).astype(int)
print(df_2)


# In[10]:


df_2['headlines'] = data_may

# Print the DataFrame to verify the changes
print(df_2)


# In[11]:


import yfinance as yf
tickers = ["HDFCBANK.NS"]

ohlc_data = {}
for ticker in tickers:
    data = yf.download(ticker, start="2024-06-01", end="2024-06-13")  # Specify your date range#here,for april
    ohlc_data[ticker] = data[['Open', 'High', 'Low', 'Close']]
import pandas as pd

# Convert dictionary to DataFrame
df_3 = pd.concat(ohlc_data.values(), keys=ohlc_data.keys(), names=['Ticker', 'Date'])

# Show output
print(df_3)



# In[12]:


#Adding another column wherein if closing price>opening price then the column stores value 1,else 0
df_3['label'] = (df_3['Close'] > df_3['Open']).astype(int)
print(df_3)


# In[13]:


df_3['headlines'] = data_june

# Print the DataFrame to verify the changes
print(df_3)


# In[14]:


merged_df = pd.concat([df_1, df_2, df_3], ignore_index=True)

# Print the merged DataFrame
print(merged_df)


# In[15]:


merged_df.shape


# In[16]:


import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob

# Download the VADER lexicon
nltk.download('vader_lexicon')

# Initialize VADER
sid = SentimentIntensityAnalyzer()

# Function to calculate sentiment scores for a given text
def calculate_sentiment_scores(text):
    sentiment_scores = sid.polarity_scores(text)
    return sentiment_scores['pos'], sentiment_scores['neg'], sentiment_scores['neu'], sentiment_scores['compound']

# Function to calculate polarity and subjectivity scores for a given text
def calculate_textblob_scores(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    return polarity, subjectivity

# Iterate over each row and calculate sentiment scores, polarity, and subjectivity
pos_scores = []
neg_scores = []
neu_scores = []
compound_scores = []
polarity_scores = []
subjectivity_scores = []

for index, row in merged_df.iterrows():
    headline = row['headlines']

    # Calculate sentiment scores using VADER
    pos_score, neg_score, neu_score, compound_score = calculate_sentiment_scores(headline)
    pos_scores.append(pos_score)
    neg_scores.append(neg_score)
    neu_scores.append(neu_score)
    compound_scores.append(compound_score)

    # Calculate polarity and subjectivity scores using TextBlob
    polarity_score, subjectivity_score = calculate_textblob_scores(headline)
    polarity_scores.append(polarity_score)
    subjectivity_scores.append(subjectivity_score)

# Add sentiment scores, polarity, and subjectivity to the DataFrame
merged_df['Positivity'] = pos_scores
merged_df['Negativity'] = neg_scores
merged_df['Neutrality'] = neu_scores
merged_df['Compound Score'] = compound_scores
merged_df['Polarity'] = polarity_scores
merged_df['Subjectivity'] = subjectivity_scores

# Print the DataFrame with sentiment scores, polarity, and subjectivity
print(merged_df)


# In[17]:


ticker = 'HDFCBANK.NS'
start = '2024-04-01'
end = '2024-06-13'

# Fetch historical data
data = yf.download(ticker, start=start, end=end)
plt.figure(figsize=(12, 6))  # Adjust the figure size if needed

plt.plot(data.index, data['Close'], marker='o', linestyle='-', color='b', label='Closing Price')

plt.title(f'Closing Prices of {ticker} from {start} to {end}')
plt.xlabel('Date')
plt.ylabel('Closing Price (Rs.)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()


# In[18]:


merged_df.head()


# In[19]:


features = ['Open', 'High', 'Low', 'Subjectivity', 'Polarity', 'Compound Score', 'Negativity', 'Neutrality', 'Positivity']
X = merged_df[features]
print(X)



# In[20]:


y = merged_df['label']
print(y)


# In[21]:


from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size =0.2,random_state=89)
X_test.shape


# In[22]:


# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from sklearn.neural_network import MLPClassifier
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from sklearn.utils.class_weight import compute_class_weight
from sklearn.model_selection import GridSearchCV
class_weights = compute_class_weight('balanced', classes=np.unique(y_train), y=y_train)
class_weights = class_weights / np.sum(class_weights)

# Assuming you have X_train, X_test, y_train, y_test already defined

# Function to plot ROC curve
def plot_roc_curve(fpr, tpr, roc_auc, classifier_name):
    plt.figure()
    lw = 2
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic for ' + classifier_name)
    plt.legend(loc="lower right")
    plt.show()

# Logistic Regression
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_score_lr = logreg.decision_function(X_test)
fpr_lr, tpr_lr, _ = roc_curve(y_test, y_score_lr)
roc_auc_lr = auc(fpr_lr, tpr_lr)
plot_roc_curve(fpr_lr, tpr_lr, roc_auc_lr, "Logistic Regression")

# LDA
lda = LinearDiscriminantAnalysis()
lda.fit(X_train, y_train)
y_score_lda = lda.decision_function(X_test)
fpr_lda, tpr_lda, _ = roc_curve(y_test, y_score_lda)
roc_auc_lda = auc(fpr_lda, tpr_lda)
plot_roc_curve(fpr_lda, tpr_lda, roc_auc_lda, "LDA")

# SVM
svm = SVC(probability=True)  # Note: probability=True for ROC curve
svm.fit(X_train, y_train)
y_score_svm = svm.predict_proba(X_test)[:, 1]
fpr_svm, tpr_svm, _ = roc_curve(y_test, y_score_svm)
roc_auc_svm = auc(fpr_svm, tpr_svm)
plot_roc_curve(fpr_svm, tpr_svm, roc_auc_svm, "SVM")

# Random Forest
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
y_score_rf = rf.predict_proba(X_test)[:, 1]
fpr_rf, tpr_rf, _ = roc_curve(y_test, y_score_rf)
roc_auc_rf = auc(fpr_rf, tpr_rf)
plot_roc_curve(fpr_rf, tpr_rf, roc_auc_rf, "Random Forest")

# Deep Neural Network (using Keras)
# Assuming y_train and y_test are categorical (one-hot encoded)
num_classes = len(np.unique(y_train))
y_train_cat = to_categorical(y_train, num_classes)
y_test_cat = to_categorical(y_test, num_classes)

dnn = Sequential([
    Dense(64, activation='relu', input_shape=X_train.shape[1:]),
    Dense(64, activation='relu'),
    Dense(num_classes, activation='softmax')
])
dnn.compile(optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy'])

dnn.fit(X_train, y_train_cat, epochs=10, batch_size=32, verbose=0)
y_score_dnn = dnn.predict(X_test)
fpr_dnn, tpr_dnn, _ = roc_curve(y_test_cat[:, 1], y_score_dnn[:, 1])
roc_auc_dnn = auc(fpr_dnn, tpr_dnn)
plot_roc_curve(fpr_dnn, tpr_dnn, roc_auc_dnn, "Deep Neural Network")


# In[23]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from sklearn.neural_network import MLPClassifier
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from sklearn.utils.class_weight import compute_class_weight
from sklearn.model_selection import GridSearchCV
class_weights = compute_class_weight('balanced', classes=np.unique(y_train), y=y_train)
class_weights = class_weights / np.sum(class_weights)

# Assuming you have X_train, X_test, y_train, y_test already defined

# Function to plot ROC curve
def plot_roc_curve(fpr, tpr, roc_auc, classifier_name):
    plt.plot(fpr, tpr, lw=2, label='ROC curve for {} (area = {:.2f})'.format(classifier_name, roc_auc))

# Logistic Regression
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_score_lr = logreg.decision_function(X_test)
fpr_lr, tpr_lr, _ = roc_curve(y_test, y_score_lr)
roc_auc_lr = auc(fpr_lr, tpr_lr)
plot_roc_curve(fpr_lr, tpr_lr, roc_auc_lr, "Logistic Regression")

# LDA
lda = LinearDiscriminantAnalysis(store_covariance=True, 
                                 solver='svd', shrinkage=None, 
                                 priors=class_weights)
lda.fit(X_train, y_train)
y_score_lda = lda.decision_function(X_test)
fpr_lda, tpr_lda, _ = roc_curve(y_test, y_score_lda)
roc_auc_lda = auc(fpr_lda, tpr_lda)
plot_roc_curve(fpr_lda, tpr_lda, roc_auc_lda, "LDA")

# SVM
svm = SVC(probability=True)  # Note: probability=True for ROC curve
svm.fit(X_train, y_train)
y_score_svm = svm.predict_proba(X_test)[:, 1]
fpr_svm, tpr_svm, _ = roc_curve(y_test, y_score_svm)
roc_auc_svm = auc(fpr_svm, tpr_svm)
plot_roc_curve(fpr_svm, tpr_svm, roc_auc_svm, "SVM")

# Random Forest
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
y_score_rf = rf.predict_proba(X_test)[:, 1]
fpr_rf, tpr_rf, _ = roc_curve(y_test, y_score_rf)
roc_auc_rf = auc(fpr_rf, tpr_rf)
plot_roc_curve(fpr_rf, tpr_rf, roc_auc_rf, "Random Forest")

# Deep Neural Network (using Keras)
num_classes = len(np.unique(y_train))
y_train_cat = to_categorical(y_train, num_classes)
y_test_cat = to_categorical(y_test, num_classes)

dnn = Sequential([
    Dense(64, activation='relu', input_shape=X_train.shape[1:]),
    Dense(64, activation='relu'),
    Dense(num_classes, activation='softmax')
])
dnn.compile(optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy'])

dnn.fit(X_train, y_train_cat, epochs=10, batch_size=32, verbose=0)
y_score_dnn = dnn.predict(X_test)
fpr_dnn, tpr_dnn, _ = roc_curve(y_test_cat[:, 1], y_score_dnn[:, 1])
roc_auc_dnn = auc(fpr_dnn, tpr_dnn)
plot_roc_curve(fpr_dnn, tpr_dnn, roc_auc_dnn, "Deep Neural Network")

# Plotting all ROC curves on one graph
plt.figure(figsize=(8, 6))
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plot_roc_curve(fpr_lr, tpr_lr, roc_auc_lr, "Logistic Regression")
plot_roc_curve(fpr_lda, tpr_lda, roc_auc_lda, "LDA")
plot_roc_curve(fpr_svm, tpr_svm, roc_auc_svm, "SVM")
plot_roc_curve(fpr_rf, tpr_rf, roc_auc_rf, "Random Forest")
plot_roc_curve(fpr_dnn, tpr_dnn, roc_auc_dnn, "Deep Neural Network")
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve for HDFC BANK')
plt.legend(loc="lower right")
plt.show()


# In[24]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, auc, classification_report
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from sklearn.neural_network import MLPClassifier
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

# Assuming you have X_train, X_test, y_train, y_test already defined

# Function to plot ROC curve
def plot_roc_curve(fpr, tpr, roc_auc, classifier_name):
    plt.plot(fpr, tpr, lw=2, label='ROC curve for {} (area = {:.2f})'.format(classifier_name, roc_auc))

# Function to print classification report
def print_classification_report(y_true, y_pred, classifier_name):
    print(f"Classification Report for {classifier_name}:")
    print(classification_report(y_true, y_pred))

# Logistic Regression
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred_lr = logreg.predict(X_test)
print_classification_report(y_test, y_pred_lr, "Logistic Regression")

# LDA
lda = LinearDiscriminantAnalysis()
lda.fit(X_train, y_train)
y_pred_lda = lda.predict(X_test)
print_classification_report(y_test, y_pred_lda, "LDA")

# SVM
svm = SVC(probability=True)  # Note: probability=True for ROC curve
svm.fit(X_train, y_train)
y_pred_svm = svm.predict(X_test)
print_classification_report(y_test, y_pred_svm, "SVM")

# Random Forest
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
print_classification_report(y_test, y_pred_rf, "Random Forest")

# Deep Neural Network (using Keras)
num_classes = len(np.unique(y_train))
y_train_cat = to_categorical(y_train, num_classes)
y_test_cat = to_categorical(y_test, num_classes)

dnn = Sequential([
    Dense(64, activation='relu', input_shape=X_train.shape[1:]),
    Dense(64, activation='relu'),
    Dense(num_classes, activation='softmax')
])
dnn.compile(optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy'])

dnn.fit(X_train, y_train_cat, epochs=10, batch_size=32, verbose=0)
y_pred_dnn = np.argmax(dnn.predict(X_test), axis=-1)
print_classification_report(y_test, y_pred_dnn, "Deep Neural Network")


# k=12
# scoring = ['accuracy', 'roc_auc']
# 
# model_1 =LinearDiscriminantAnalysis()
# model_1.fit(X_train,y_train)
# y_pred = model_1.predict(X_test)
# y_predict_test = model_1.predict(X_test)
# y_predict_train = model_1.predict(X_train)
# cv_results = cross_validate(model_1, X, y, cv=k, scoring=scoring, return_train_score=True)

# # Fit the model
# model_1.fit(X_train, y_train)
# 
# # Predictions
# y_predict_test = model_1.predict(X_test)
# y_predict_train= model_1.predict(X_train)
# k=12
# scoring = ['accuracy', 'roc_auc']
# cv_results = cross_validate(model_1, X, y, cv=k, scoring=scoring, return_train_score=True)

# #model metrics
# from sklearn.metrics import classification_report
# print("Classification Report for Training Set:")
# print(classification_report(y_train, y_predict_train))
# 
# print("Classification Report for Test Set:")
# print(classification_report(y_test, y_predict_test))

# from sklearn.metrics import roc_curve, auc
# import matplotlib.pyplot as plt
# y_probs_train = model_1.predict_proba(X_train)[:, 1]
# y_probs_test = model_1.predict_proba(X_test)[:, 1]
# 
# # Calculate the ROC curve and AUC for the training set
# fpr_train, tpr_train, _ = roc_curve(y_train, y_probs_train)
# roc_auc_train = auc(fpr_train, tpr_train)
# 
# # Calculate the ROC curve and AUC for the test set
# fpr_test, tpr_test, _ = roc_curve(y_test, y_probs_test)
# roc_auc_test = auc(fpr_test, tpr_test)
# 
# # Plot the ROC curve
# plt.figure(figsize=(10, 6))
# plt.plot(fpr_train, tpr_train, color='blue', lw=2, label=f'Training ROC curve (area = {roc_auc_train:.2f})')
# plt.plot(fpr_test, tpr_test, color='red', lw=2, label=f'Test ROC curve (area = {roc_auc_test:.2f})')
# plt.plot([0, 1], [0, 1], color='gray', lw=2, linestyle='--')
# plt.xlim([0.0, 1.0])
# plt.ylim([0.0, 1.05])
# plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')
# plt.title('Receiver Operating Characteristic (ROC) Curve with LDA')
# plt.legend(loc="lower right")
# plt.show()

# In[25]:


from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate
from sklearn.ensemble import RandomForestClassifier
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size =0.2,random_state=89)
X_test.shape


# In[26]:


model =RandomForestClassifier()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
y_predict_test = model.predict(X_test)
y_predict_train = model.predict(X_train)


# In[27]:


#model metrics
from sklearn.metrics import classification_report
print("Classification Report for Training Set:")
print(classification_report(y_train, y_predict_train))

print("Classification Report for Test Set:")
print(classification_report(y_test, y_predict_test))


# In[28]:


from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
y_probs_train = model.predict_proba(X_train)[:, 1]
y_probs_test = model.predict_proba(X_test)[:, 1]

# Calculate the ROC curve and AUC for the training set
fpr_train, tpr_train, _ = roc_curve(y_train, y_probs_train)
roc_auc_train = auc(fpr_train, tpr_train)

# Calculate the ROC curve and AUC for the test set
fpr_test, tpr_test, _ = roc_curve(y_test, y_probs_test)
roc_auc_test = auc(fpr_test, tpr_test)

# Plot the ROC curve
plt.figure(figsize=(10, 6))
plt.plot(fpr_train, tpr_train, color='blue', lw=2, label=f'Training ROC curve (area = {roc_auc_train:.2f})')
plt.plot(fpr_test, tpr_test, color='red', lw=2, label=f'Test ROC curve (area = {roc_auc_test:.2f})')
plt.plot([0, 1], [0, 1], color='gray', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve with Random Forest')
plt.legend(loc="lower right")
plt.show()


# In[29]:


from sklearn.svm import SVC


# In[30]:


# Train the SVM model
svm_model = SVC(probability=True)
svm_model.fit(X_train, y_train)

# Make predictions
y_pred_train = svm_model.predict(X_train)
y_pred_test = svm_model.predict(X_test)

# Get the predicted probabilities for the ROC curve
y_probs_train = svm_model.predict_proba(X_train)[:, 1]
y_probs_test = svm_model.predict_proba(X_test)[:, 1]

# Calculate the ROC curve and AUC for the training set
fpr_train, tpr_train, _ = roc_curve(y_train, y_probs_train)
roc_auc_train = auc(fpr_train, tpr_train)

# Calculate the ROC curve and AUC for the test set
fpr_test, tpr_test, _ = roc_curve(y_test, y_probs_test)
roc_auc_test = auc(fpr_test, tpr_test)

# Print classification reports
print("Training Classification Report:")
print(classification_report(y_train, y_pred_train))
print("Testing Classification Report:")
print(classification_report(y_test, y_pred_test))


# In[31]:


plt.figure(figsize=(10, 6))
plt.plot(fpr_train, tpr_train, color='blue', lw=2, label=f'Training ROC curve (area = {roc_auc_train:.2f})')
plt.plot(fpr_test, tpr_test, color='red', lw=2, label=f'Test ROC curve (area = {roc_auc_test:.2f})')
plt.plot([0, 1], [0, 1], color='gray', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve using Support Vector Machine')
plt.legend(loc="lower right")
plt.show()


# In[32]:


import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the neural network model
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.5),
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.001),
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=1)

# Evaluate the model
train_loss, train_acc = model.evaluate(X_train, y_train, verbose=0)
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
print(f'Training Accuracy: {train_acc:.4f}, Test Accuracy: {test_acc:.4f}')

# Make predictions
y_probs_train = model.predict(X_train).ravel()
y_probs_test = model.predict(X_test).ravel()

# Calculate the ROC curve and AUC for the training set
fpr_train, tpr_train, _ = roc_curve(y_train, y_probs_train)
roc_auc_train = auc(fpr_train, tpr_train)

# Calculate the ROC curve and AUC for the test set
fpr_test, tpr_test, _ = roc_curve(y_test, y_probs_test)
roc_auc_test = auc(fpr_test, tpr_test)

# Print classification reports
y_pred_train = (y_probs_train > 0.5).astype(int)
y_pred_test = (y_probs_test > 0.5).astype(int)
print("Training Classification Report:")
print(classification_report(y_train, y_pred_train))
print("Testing Classification Report:")
print(classification_report(y_test, y_pred_test))

# Plot the ROC curve
plt.figure(figsize=(10, 6))
plt.plot(fpr_train, tpr_train, color='blue', lw=2, label=f'Training ROC curve (area = {roc_auc_train:.2f})')
plt.plot(fpr_test, tpr_test, color='red', lw=2, label=f'Test ROC curve (area = {roc_auc_test:.2f})')
plt.plot([0, 1], [0, 1], color='gray', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve using Deep Neural Networks')
plt.legend(loc="lower right")
plt.show()


# #AUC-ROC curve is best with LDA 

# In[ ]:





# In[33]:


from bs4 import BeautifulSoup as BS
import requests as req
import numpy as np
import pandas as pd


# In[34]:


# List to store headlines
headlines_adani = []

# Function to extract headlines and subheadings
def extract_headlines_and_subheadings(soup):
    for link in soup.find_all(['a', 'h3', 'p']):  # Adding common tags for headlines and subheadings
        if link.string and isinstance(link.string, str) and len(link.string) > 50:
            headlines_adani.append(link.string.strip())

# Function to scrape data from a single URL
def scrape_url(url):
    try:
        webpage = req.get(url)
        if webpage.status_code == 200:
            soup = BS(webpage.content, "html.parser")
            extract_headlines_and_subheadings(soup)
        else:
            print(f"Failed to retrieve data from {url}. Status code: {webpage.status_code}")
    except Exception as e:
        print(f"An error occurred while scraping {url}: {str(e)}")

# List of URLs to scrape
urls = ["https://www.bing.com/news/search?q=ITC+Share+Price&qpvt=itc+share+price+news&FORM=EWRE"
    # Add more URLs here
]

# Scrape each URL
for url in urls:
    scrape_url(url)

# Join all headlines into a single string
data_adani = '\n'.join(headlines_adani)

print(data_adani)


# In[35]:


import yfinance as yf
tickers = ["ADANIENT.NS"]

ohlc_data = {}
for ticker in tickers:
    data = yf.download(ticker, start="2024-04-01", end="2024-06-13")  # Specify your date range#here,for april
    ohlc_data[ticker] = data[['Open', 'High', 'Low', 'Close']]
import pandas as pd

# Convert dictionary to DataFrame
df_1 = pd.concat(ohlc_data.values(), keys=ohlc_data.keys(), names=['Ticker', 'Date'])

# Show output
print(df_1)



# In[36]:


#Adding another column wherein if closing price>opening price then the column stores value 1,else 0
df_1['label'] = (df_1['Close'] > df_1['Open']).astype(int)
print(df_1)


# In[37]:


df_1['headlines'] = data_adani

# Print the DataFrame to verify the changes
print(df_1)


# In[38]:


df_1.shape


# In[39]:


import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob

# Download the VADER lexicon
nltk.download('vader_lexicon')

# Initialize VADER
sid = SentimentIntensityAnalyzer()

# Function to calculate sentiment scores for a given text
def calculate_sentiment_scores(text):
    sentiment_scores = sid.polarity_scores(text)
    return sentiment_scores['pos'], sentiment_scores['neg'], sentiment_scores['neu'], sentiment_scores['compound']

# Function to calculate polarity and subjectivity scores for a given text
def calculate_textblob_scores(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    return polarity, subjectivity

# Iterate over each row and calculate sentiment scores, polarity, and subjectivity
pos_scores = []
neg_scores = []
neu_scores = []
compound_scores = []
polarity_scores = []
subjectivity_scores = []

for index, row in df_1.iterrows():
    headline = row['headlines']

    # Calculate sentiment scores using VADER
    pos_score, neg_score, neu_score, compound_score = calculate_sentiment_scores(headline)
    pos_scores.append(pos_score)
    neg_scores.append(neg_score)
    neu_scores.append(neu_score)
    compound_scores.append(compound_score)

    # Calculate polarity and subjectivity scores using TextBlob
    polarity_score, subjectivity_score = calculate_textblob_scores(headline)
    polarity_scores.append(polarity_score)
    subjectivity_scores.append(subjectivity_score)

# Add sentiment scores, polarity, and subjectivity to the DataFrame
df_1['Positivity'] = pos_scores
df_1['Negativity'] = neg_scores
df_1['Neutrality'] = neu_scores
df_1['Compound Score'] = compound_scores
df_1['Polarity'] = polarity_scores
df_1['Subjectivity'] = subjectivity_scores

# Print the DataFrame with sentiment scores, polarity, and subjectivity
print(df_1)


# In[40]:


df_1.head()


# In[41]:


ticker = 'ADANIENT.NS'
start = '2024-04-01'
end = '2024-06-13'

# Fetch historical data
data = yf.download(ticker, start=start, end=end)
plt.figure(figsize=(12, 6))  # Adjust the figure size if needed

plt.plot(data.index, data['Close'], marker='o', linestyle='-', color='b', label='Closing Price')

plt.title(f'Closing Prices of {ticker} from {start} to {end}')
plt.xlabel('Date')
plt.ylabel('Closing Price (Rs.)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()


# In[42]:


features = ['Open', 'High', 'Low', 'Subjectivity', 'Polarity', 'Compound Score', 'Negativity', 'Neutrality', 'Positivity']
X = df_1[features]
print(X)



# In[43]:


y = df_1['label']
print(y)


# In[44]:


from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size =0.2,random_state=89)
X_test.shape


# In[45]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from sklearn.neural_network import MLPClassifier
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from sklearn.utils.class_weight import compute_class_weight
from sklearn.model_selection import GridSearchCV
class_weights = compute_class_weight('balanced', classes=np.unique(y_train), y=y_train)
class_weights = class_weights / np.sum(class_weights)

# Assuming you have X_train, X_test, y_train, y_test already defined

# Function to plot ROC curve
def plot_roc_curve(fpr, tpr, roc_auc, classifier_name):
    plt.plot(fpr, tpr, lw=2, label='ROC curve for {} (area = {:.2f})'.format(classifier_name, roc_auc))

# Logistic Regression
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_score_lr = logreg.decision_function(X_test)
fpr_lr, tpr_lr, _ = roc_curve(y_test, y_score_lr)
roc_auc_lr = auc(fpr_lr, tpr_lr)
plot_roc_curve(fpr_lr, tpr_lr, roc_auc_lr, "Logistic Regression")

# LDA
lda = LinearDiscriminantAnalysis(store_covariance=True, 
                                 solver='svd', shrinkage=None, 
                                 priors=class_weights)
lda.fit(X_train, y_train)
y_score_lda = lda.decision_function(X_test)
fpr_lda, tpr_lda, _ = roc_curve(y_test, y_score_lda)
roc_auc_lda = auc(fpr_lda, tpr_lda)
plot_roc_curve(fpr_lda, tpr_lda, roc_auc_lda, "LDA")

# SVM
svm = SVC(probability=True)  # Note: probability=True for ROC curve
svm.fit(X_train, y_train)
y_score_svm = svm.predict_proba(X_test)[:, 1]
fpr_svm, tpr_svm, _ = roc_curve(y_test, y_score_svm)
roc_auc_svm = auc(fpr_svm, tpr_svm)
plot_roc_curve(fpr_svm, tpr_svm, roc_auc_svm, "SVM")

# Random Forest
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
y_score_rf = rf.predict_proba(X_test)[:, 1]
fpr_rf, tpr_rf, _ = roc_curve(y_test, y_score_rf)
roc_auc_rf = auc(fpr_rf, tpr_rf)
plot_roc_curve(fpr_rf, tpr_rf, roc_auc_rf, "Random Forest")

# Deep Neural Network (using Keras)
num_classes = len(np.unique(y_train))
y_train_cat = to_categorical(y_train, num_classes)
y_test_cat = to_categorical(y_test, num_classes)

dnn = Sequential([
    Dense(64, activation='relu', input_shape=X_train.shape[1:]),
    Dense(64, activation='relu'),
    Dense(num_classes, activation='softmax')
])
dnn.compile(optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy'])

dnn.fit(X_train, y_train_cat, epochs=10, batch_size=32, verbose=0)
y_score_dnn = dnn.predict(X_test)
fpr_dnn, tpr_dnn, _ = roc_curve(y_test_cat[:, 1], y_score_dnn[:, 1])
roc_auc_dnn = auc(fpr_dnn, tpr_dnn)
plot_roc_curve(fpr_dnn, tpr_dnn, roc_auc_dnn, "Deep Neural Network")

# Plotting all ROC curves on one graph
plt.figure(figsize=(8, 6))
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plot_roc_curve(fpr_lr, tpr_lr, roc_auc_lr, "Logistic Regression")
plot_roc_curve(fpr_lda, tpr_lda, roc_auc_lda, "LDA")
plot_roc_curve(fpr_svm, tpr_svm, roc_auc_svm, "SVM")
plot_roc_curve(fpr_rf, tpr_rf, roc_auc_rf, "Random Forest")
plot_roc_curve(fpr_dnn, tpr_dnn, roc_auc_dnn, "Deep Neural Network")
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve for ADANI ENTERPRISES')
plt.legend(loc="lower right")
plt.show()


# In[46]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, auc, classification_report
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from sklearn.neural_network import MLPClassifier
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

# Assuming you have X_train, X_test, y_train, y_test already defined

# Function to plot ROC curve
def plot_roc_curve(fpr, tpr, roc_auc, classifier_name):
    plt.plot(fpr, tpr, lw=2, label='ROC curve for {} (area = {:.2f})'.format(classifier_name, roc_auc))

# Function to print classification report
def print_classification_report(y_true, y_pred, classifier_name):
    print(f"Classification Report for {classifier_name}:")
    print(classification_report(y_true, y_pred))

# Logistic Regression
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred_lr = logreg.predict(X_test)
print_classification_report(y_test, y_pred_lr, "Logistic Regression")

# LDA
lda_2= LinearDiscriminantAnalysis()
lda_2.fit(X_train, y_train)
y_pred_lda = lda_2.predict(X_test)
print_classification_report(y_test, y_pred_lda, "LDA")

# SVM
svm = SVC(probability=True)  # Note: probability=True for ROC curve
svm.fit(X_train, y_train)
y_pred_svm = svm.predict(X_test)
print_classification_report(y_test, y_pred_svm, "SVM")

# Random Forest
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
print_classification_report(y_test, y_pred_rf, "Random Forest")

# Deep Neural Network (using Keras)
num_classes = len(np.unique(y_train))
y_train_cat = to_categorical(y_train, num_classes)
y_test_cat = to_categorical(y_test, num_classes)

dnn = Sequential([
    Dense(64, activation='relu', input_shape=X_train.shape[1:]),
    Dense(64, activation='relu'),
    Dense(num_classes, activation='softmax')
])
dnn.compile(optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy'])

dnn.fit(X_train, y_train_cat, epochs=10, batch_size=32, verbose=0)
y_pred_dnn = np.argmax(dnn.predict(X_test), axis=-1)
print_classification_report(y_test, y_pred_dnn, "Deep Neural Network")


# In[47]:


k=12
scoring = ['accuracy', 'roc_auc']

model_2_1 =LinearDiscriminantAnalysis()
model_2_1.fit(X_train,y_train)
y_pred = model_2_1.predict(X_test)
y_predict_test = model_2_1.predict(X_test)
y_predict_train = model_2_1.predict(X_train)
cv_results = cross_validate(model_2_1, X, y, cv=k, scoring=scoring, return_train_score=True)


# In[48]:


#model metrics
from sklearn.metrics import classification_report
print("Classification Report for Training Set:")
print(classification_report(y_train, y_predict_train))

print("Classification Report for Test Set:")
print(classification_report(y_test, y_predict_test))


# In[49]:


from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
y_probs_train = model_2_1.predict_proba(X_train)[:, 1]
y_probs_test = model_2_1.predict_proba(X_test)[:, 1]

# Calculate the ROC curve and AUC for the training set
fpr_train, tpr_train, _ = roc_curve(y_train, y_probs_train)
roc_auc_train = auc(fpr_train, tpr_train)

# Calculate the ROC curve and AUC for the test set
fpr_test, tpr_test, _ = roc_curve(y_test, y_probs_test)
roc_auc_test = auc(fpr_test, tpr_test)

# Plot the ROC curve
plt.figure(figsize=(10, 6))
plt.plot(fpr_train, tpr_train, color='blue', lw=2, label=f'Training ROC curve (area = {roc_auc_train:.2f})')
plt.plot(fpr_test, tpr_test, color='red', lw=2, label=f'Test ROC curve (area = {roc_auc_test:.2f})')
plt.plot([0, 1], [0, 1], color='gray', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve with LDA')
plt.legend(loc="lower right")
plt.show()


# In[50]:


from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate
from sklearn.ensemble import RandomForestClassifier
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size =0.2,random_state=89)
X_test.shape


# In[51]:


model_2 =RandomForestClassifier()
model_2.fit(X_train,y_train)
y_pred = model_2.predict(X_test)
y_predict_test = model_2.predict(X_test)
y_predict_train = model_2.predict(X_train)


# In[52]:


#model metrics
from sklearn.metrics import classification_report
print("Classification Report for Training Set:")
print(classification_report(y_train, y_predict_train))

print("Classification Report for Test Set:")
print(classification_report(y_test, y_predict_test))


# In[53]:


from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
y_probs_train = model_2.predict_proba(X_train)[:, 1]
y_probs_test = model_2.predict_proba(X_test)[:, 1]

# Calculate the ROC curve and AUC for the training set
fpr_train, tpr_train, _ = roc_curve(y_train, y_probs_train)
roc_auc_train = auc(fpr_train, tpr_train)

# Calculate the ROC curve and AUC for the test set
fpr_test, tpr_test, _ = roc_curve(y_test, y_probs_test)
roc_auc_test = auc(fpr_test, tpr_test)

# Plot the ROC curve
plt.figure(figsize=(10, 6))
plt.plot(fpr_train, tpr_train, color='blue', lw=2, label=f'Training ROC curve (area = {roc_auc_train:.2f})')
plt.plot(fpr_test, tpr_test, color='red', lw=2, label=f'Test ROC curve (area = {roc_auc_test:.2f})')
plt.plot([0, 1], [0, 1], color='gray', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve with Random Forest')
plt.legend(loc="lower right")
plt.show()


# In[54]:


from sklearn.svm import SVC


# In[55]:


# Train the SVM model
svm_model = SVC(probability=True)
svm_model.fit(X_train, y_train)

# Make predictions
y_pred_train = svm_model.predict(X_train)
y_pred_test = svm_model.predict(X_test)

# Get the predicted probabilities for the ROC curve
y_probs_train = svm_model.predict_proba(X_train)[:, 1]
y_probs_test = svm_model.predict_proba(X_test)[:, 1]

# Calculate the ROC curve and AUC for the training set
fpr_train, tpr_train, _ = roc_curve(y_train, y_probs_train)
roc_auc_train = auc(fpr_train, tpr_train)

# Calculate the ROC curve and AUC for the test set
fpr_test, tpr_test, _ = roc_curve(y_test, y_probs_test)
roc_auc_test = auc(fpr_test, tpr_test)

# Print classification reports
print("Training Classification Report:")
print(classification_report(y_train, y_pred_train))
print("Testing Classification Report:")
print(classification_report(y_test, y_pred_test))


# In[56]:


plt.figure(figsize=(10, 6))
plt.plot(fpr_train, tpr_train, color='blue', lw=2, label=f'Training ROC curve (area = {roc_auc_train:.2f})')
plt.plot(fpr_test, tpr_test, color='red', lw=2, label=f'Test ROC curve (area = {roc_auc_test:.2f})')
plt.plot([0, 1], [0, 1], color='gray', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve using Support Vector Machine')
plt.legend(loc="lower right")
plt.show()


# In[57]:


import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the neural network model
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.5),
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.001),
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=1)

# Evaluate the model
train_loss, train_acc = model.evaluate(X_train, y_train, verbose=0)
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
print(f'Training Accuracy: {train_acc:.4f}, Test Accuracy: {test_acc:.4f}')

# Make predictions
y_probs_train = model.predict(X_train).ravel()
y_probs_test = model.predict(X_test).ravel()

# Calculate the ROC curve and AUC for the training set
fpr_train, tpr_train, _ = roc_curve(y_train, y_probs_train)
roc_auc_train = auc(fpr_train, tpr_train)

# Calculate the ROC curve and AUC for the test set
fpr_test, tpr_test, _ = roc_curve(y_test, y_probs_test)
roc_auc_test = auc(fpr_test, tpr_test)

# Print classification reports
y_pred_train = (y_probs_train > 0.5).astype(int)
y_pred_test = (y_probs_test > 0.5).astype(int)
print("Training Classification Report:")
print(classification_report(y_train, y_pred_train))
print("Testing Classification Report:")
print(classification_report(y_test, y_pred_test))

# Plot the ROC curve
plt.figure(figsize=(10, 6))
plt.plot(fpr_train, tpr_train, color='blue', lw=2, label=f'Training ROC curve (area = {roc_auc_train:.2f})')
plt.plot(fpr_test, tpr_test, color='red', lw=2, label=f'Test ROC curve (area = {roc_auc_test:.2f})')
plt.plot([0, 1], [0, 1], color='gray', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve using Deep Neural Networks')
plt.legend(loc="lower right")
plt.show()


# #AUC-ROC curve shows best results with Random forest (however , it is overfitting)

# In[ ]:





# In[58]:


from bs4 import BeautifulSoup as BS
import requests as req
import numpy as np
import pandas as pd


# In[59]:


# List to store headlines
headlines_itc = []

# Function to extract headlines and subheadings
def extract_headlines_and_subheadings(soup):
    for link in soup.find_all(['a', 'h3', 'p']):  # Adding common tags for headlines and subheadings
        if link.string and isinstance(link.string, str) and len(link.string) > 50:
            headlines_itc.append(link.string.strip())

# Function to scrape data from a single URL
def scrape_url(url):
    try:
        webpage = req.get(url)
        if webpage.status_code == 200:
            soup = BS(webpage.content, "html.parser")
            extract_headlines_and_subheadings(soup)
        else:
            print(f"Failed to retrieve data from {url}. Status code: {webpage.status_code}")
    except Exception as e:
        print(f"An error occurred while scraping {url}: {str(e)}")

# List of URLs to scrape
urls = ["https://www.bing.com/news/search?q=ITC+Share+Price&qpvt=itc+share+price+news&FORM=EWRE","https://economictimes.indiatimes.com/itc-ltd/stocksupdate/companyid-13554.cms"
  ,"https://www.itcportal.com/media-centre/press-reports.aspx","https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/itc-share-price-today-live-updates-03-jun-2024/liveblog/110650671.cms"
    # Add more URLs here
]

# Scrape each URL
for url in urls:
    scrape_url(url)

# Join all headlines into a single string
data_itc = '\n'.join(headlines_itc)

print(data_itc)


# In[60]:


import yfinance as yf
tickers = ["ITC.NS"]

ohlc_data = {}
for ticker in tickers:
    data = yf.download(ticker, start="2024-04-01", end="2024-06-13")  # Specify your date range#here,for april
    ohlc_data[ticker] = data[['Open', 'High', 'Low', 'Close']]
import pandas as pd

# Convert dictionary to DataFrame
df_itc = pd.concat(ohlc_data.values(), keys=ohlc_data.keys(), names=['Ticker', 'Date'])

# Show output
print(df_itc)



# In[61]:


#Adding another column wherein if closing price>opening price then the column stores value 1,else 0
df_itc['label'] = (df_itc['Close'] > df_itc['Open']).astype(int)
print(df_itc)


# In[62]:


df_itc['headlines'] = data_itc

# Print the DataFrame to verify the changes
print(df_itc)


# In[63]:


df_itc.shape


# In[64]:


import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob

# Download the VADER lexicon
nltk.download('vader_lexicon')

# Initialize VADER
sid = SentimentIntensityAnalyzer()

# Function to calculate sentiment scores for a given text
def calculate_sentiment_scores(text):
    sentiment_scores = sid.polarity_scores(text)
    return sentiment_scores['pos'], sentiment_scores['neg'], sentiment_scores['neu'], sentiment_scores['compound']

# Function to calculate polarity and subjectivity scores for a given text
def calculate_textblob_scores(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    return polarity, subjectivity

# Iterate over each row and calculate sentiment scores, polarity, and subjectivity
pos_scores = []
neg_scores = []
neu_scores = []
compound_scores = []
polarity_scores = []
subjectivity_scores = []

for index, row in df_itc.iterrows():
    headline = row['headlines']

    # Calculate sentiment scores using VADER
    pos_score, neg_score, neu_score, compound_score = calculate_sentiment_scores(headline)
    pos_scores.append(pos_score)
    neg_scores.append(neg_score)
    neu_scores.append(neu_score)
    compound_scores.append(compound_score)

    # Calculate polarity and subjectivity scores using TextBlob
    polarity_score, subjectivity_score = calculate_textblob_scores(headline)
    polarity_scores.append(polarity_score)
    subjectivity_scores.append(subjectivity_score)

# Add sentiment scores, polarity, and subjectivity to the DataFrame
df_itc['Positivity'] = pos_scores
df_itc['Negativity'] = neg_scores
df_itc['Neutrality'] = neu_scores
df_itc['Compound Score'] = compound_scores
df_itc['Polarity'] = polarity_scores
df_itc['Subjectivity'] = subjectivity_scores

# Print the DataFrame with sentiment scores, polarity, and subjectivity
print(df_itc)


# In[65]:


df_itc.head()


# In[66]:


ticker = 'ITC.NS'
start = '2024-04-01'
end = '2024-06-13'

# Fetch historical data
data = yf.download(ticker, start=start, end=end)
plt.figure(figsize=(12, 6))  # Adjust the figure size if needed

plt.plot(data.index, data['Close'], marker='o', linestyle='-', color='b', label='Closing Price')

plt.title(f'Closing Prices of {ticker} from {start} to {end}')
plt.xlabel('Date')
plt.ylabel('Closing Price (Rs.)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()


# In[67]:


features = ['Open', 'High', 'Low', 'Subjectivity', 'Polarity', 'Compound Score', 'Negativity', 'Neutrality', 'Positivity']
X = df_itc[features]
print(X)



# In[68]:


y = df_itc['label']
print(y)


# In[69]:


from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size =0.2,random_state=89)
X_test.shape


# In[70]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from sklearn.neural_network import MLPClassifier
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from sklearn.utils.class_weight import compute_class_weight
from sklearn.model_selection import GridSearchCV
class_weights = compute_class_weight('balanced', classes=np.unique(y_train), y=y_train)
class_weights = class_weights / np.sum(class_weights)

# Assuming you have X_train, X_test, y_train, y_test already defined

# Function to plot ROC curve
def plot_roc_curve(fpr, tpr, roc_auc, classifier_name):
    plt.plot(fpr, tpr, lw=2, label='ROC curve for {} (area = {:.2f})'.format(classifier_name, roc_auc))

# Logistic Regression
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_score_lr = logreg.decision_function(X_test)
fpr_lr, tpr_lr, _ = roc_curve(y_test, y_score_lr)
roc_auc_lr = auc(fpr_lr, tpr_lr)
plot_roc_curve(fpr_lr, tpr_lr, roc_auc_lr, "Logistic Regression")

# LDA
lda_3 = LinearDiscriminantAnalysis(store_covariance=True, 
                                 solver='svd', shrinkage=None, 
                                 priors=class_weights)
lda_3.fit(X_train, y_train)
y_score_lda = lda_3.decision_function(X_test)
fpr_lda, tpr_lda, _ = roc_curve(y_test, y_score_lda)
roc_auc_lda = auc(fpr_lda, tpr_lda)
plot_roc_curve(fpr_lda, tpr_lda, roc_auc_lda, "LDA")

# SVM
svm = SVC(probability=True)  # Note: probability=True for ROC curve
svm.fit(X_train, y_train)
y_score_svm = svm.predict_proba(X_test)[:, 1]
fpr_svm, tpr_svm, _ = roc_curve(y_test, y_score_svm)
roc_auc_svm = auc(fpr_svm, tpr_svm)
plot_roc_curve(fpr_svm, tpr_svm, roc_auc_svm, "SVM")

# Random Forest
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
y_score_rf = rf.predict_proba(X_test)[:, 1]
fpr_rf, tpr_rf, _ = roc_curve(y_test, y_score_rf)
roc_auc_rf = auc(fpr_rf, tpr_rf)
plot_roc_curve(fpr_rf, tpr_rf, roc_auc_rf, "Random Forest")

# Deep Neural Network (using Keras)
num_classes = len(np.unique(y_train))
y_train_cat = to_categorical(y_train, num_classes)
y_test_cat = to_categorical(y_test, num_classes)

dnn = Sequential([
    Dense(64, activation='relu', input_shape=X_train.shape[1:]),
    Dense(64, activation='relu'),
    Dense(num_classes, activation='softmax')
])
dnn.compile(optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy'])

dnn.fit(X_train, y_train_cat, epochs=10, batch_size=32, verbose=0)
y_score_dnn = dnn.predict(X_test)
fpr_dnn, tpr_dnn, _ = roc_curve(y_test_cat[:, 1], y_score_dnn[:, 1])
roc_auc_dnn = auc(fpr_dnn, tpr_dnn)
plot_roc_curve(fpr_dnn, tpr_dnn, roc_auc_dnn, "Deep Neural Network")

# Plotting all ROC curves on one graph
plt.figure(figsize=(8, 6))
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plot_roc_curve(fpr_lr, tpr_lr, roc_auc_lr, "Logistic Regression")
plot_roc_curve(fpr_lda, tpr_lda, roc_auc_lda, "LDA")
plot_roc_curve(fpr_svm, tpr_svm, roc_auc_svm, "SVM")
plot_roc_curve(fpr_rf, tpr_rf, roc_auc_rf, "Random Forest")
plot_roc_curve(fpr_dnn, tpr_dnn, roc_auc_dnn, "Deep Neural Network")
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve for ITC')
plt.legend(loc="lower right")
plt.show()


# In[71]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, auc, classification_report
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from sklearn.neural_network import MLPClassifier
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

# Assuming you have X_train, X_test, y_train, y_test already defined

# Function to plot ROC curve
def plot_roc_curve(fpr, tpr, roc_auc, classifier_name):
    plt.plot(fpr, tpr, lw=2, label='ROC curve for {} (area = {:.2f})'.format(classifier_name, roc_auc))

# Function to print classification report
def print_classification_report(y_true, y_pred, classifier_name):
    print(f"Classification Report for {classifier_name}:")
    print(classification_report(y_true, y_pred))

# Logistic Regression
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred_lr = logreg.predict(X_test)
print_classification_report(y_test, y_pred_lr, "Logistic Regression")

# LDA
lda_3= LinearDiscriminantAnalysis()
lda_3.fit(X_train, y_train)
y_pred_lda = lda_3.predict(X_test)
print_classification_report(y_test, y_pred_lda, "LDA")

# SVM
svm = SVC(probability=True)  # Note: probability=True for ROC curve
svm.fit(X_train, y_train)
y_pred_svm = svm.predict(X_test)
print_classification_report(y_test, y_pred_svm, "SVM")

# Random Forest
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
print_classification_report(y_test, y_pred_rf, "Random Forest")

# Deep Neural Network (using Keras)
num_classes = len(np.unique(y_train))
y_train_cat = to_categorical(y_train, num_classes)
y_test_cat = to_categorical(y_test, num_classes)

dnn = Sequential([
    Dense(64, activation='relu', input_shape=X_train.shape[1:]),
    Dense(64, activation='relu'),
    Dense(num_classes, activation='softmax')
])
dnn.compile(optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy'])

dnn.fit(X_train, y_train_cat, epochs=10, batch_size=32, verbose=0)
y_pred_dnn = np.argmax(dnn.predict(X_test), axis=-1)
print_classification_report(y_test, y_pred_dnn, "Deep Neural Network")


# In[72]:


k=12
scoring = ['accuracy', 'roc_auc']

model_3_1 =LinearDiscriminantAnalysis()
model_3_1.fit(X_train,y_train)
y_pred = model_3_1.predict(X_test)
y_predict_test = model_3_1.predict(X_test)
y_predict_train = model_3_1.predict(X_train)
cv_results = cross_validate(model_3_1, X, y, cv=k, scoring=scoring, return_train_score=True)


# In[73]:


#model metrics
from sklearn.metrics import classification_report
print("Classification Report for Training Set:")
print(classification_report(y_train, y_predict_train))

print("Classification Report for Test Set:")
print(classification_report(y_test, y_predict_test))


# In[74]:


from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
y_probs_train = model_3_1.predict_proba(X_train)[:, 1]
y_probs_test = model_3_1.predict_proba(X_test)[:, 1]

# Calculate the ROC curve and AUC for the training set
fpr_train, tpr_train, _ = roc_curve(y_train, y_probs_train)
roc_auc_train = auc(fpr_train, tpr_train)

# Calculate the ROC curve and AUC for the test set
fpr_test, tpr_test, _ = roc_curve(y_test, y_probs_test)
roc_auc_test = auc(fpr_test, tpr_test)

# Plot the ROC curve
plt.figure(figsize=(10, 6))
plt.plot(fpr_train, tpr_train, color='blue', lw=2, label=f'Training ROC curve (area = {roc_auc_train:.2f})')
plt.plot(fpr_test, tpr_test, color='red', lw=2, label=f'Test ROC curve (area = {roc_auc_test:.2f})')
plt.plot([0, 1], [0, 1], color='gray', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve with LDA')
plt.legend(loc="lower right")
plt.show()


# In[75]:


from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate
from sklearn.ensemble import RandomForestClassifier
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size =0.2,random_state=89)
X_test.shape


# In[76]:


model_3 =RandomForestClassifier()
model_3.fit(X_train,y_train)
y_pred = model_3.predict(X_test)
y_predict_test = model_3.predict(X_test)
y_predict_train = model_3.predict(X_train)


# In[77]:


#model metrics
from sklearn.metrics import classification_report
print("Classification Report for Training Set:")
print(classification_report(y_train, y_predict_train))

print("Classification Report for Test Set:")
print(classification_report(y_test, y_predict_test))


# In[78]:


from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
y_probs_train = model_3.predict_proba(X_train)[:, 1]
y_probs_test = model_3.predict_proba(X_test)[:, 1]

# Calculate the ROC curve and AUC for the training set
fpr_train, tpr_train, _ = roc_curve(y_train, y_probs_train)
roc_auc_train = auc(fpr_train, tpr_train)

# Calculate the ROC curve and AUC for the test set
fpr_test, tpr_test, _ = roc_curve(y_test, y_probs_test)
roc_auc_test = auc(fpr_test, tpr_test)

# Plot the ROC curve
plt.figure(figsize=(10, 6))
plt.plot(fpr_train, tpr_train, color='blue', lw=2, label=f'Training ROC curve (area = {roc_auc_train:.2f})')
plt.plot(fpr_test, tpr_test, color='red', lw=2, label=f'Test ROC curve (area = {roc_auc_test:.2f})')
plt.plot([0, 1], [0, 1], color='gray', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve with Random Forest')
plt.legend(loc="lower right")
plt.show()


# In[79]:


from sklearn.svm import SVC


# In[80]:


# Train the SVM model
svm_model = SVC(probability=True)
svm_model.fit(X_train, y_train)

# Make predictions
y_pred_train = svm_model.predict(X_train)
y_pred_test = svm_model.predict(X_test)

# Get the predicted probabilities for the ROC curve
y_probs_train = svm_model.predict_proba(X_train)[:, 1]
y_probs_test = svm_model.predict_proba(X_test)[:, 1]

# Calculate the ROC curve and AUC for the training set
fpr_train, tpr_train, _ = roc_curve(y_train, y_probs_train)
roc_auc_train = auc(fpr_train, tpr_train)

# Calculate the ROC curve and AUC for the test set
fpr_test, tpr_test, _ = roc_curve(y_test, y_probs_test)
roc_auc_test = auc(fpr_test, tpr_test)

# Print classification reports
print("Training Classification Report:")
print(classification_report(y_train, y_pred_train))
print("Testing Classification Report:")
print(classification_report(y_test, y_pred_test))


# In[81]:


plt.figure(figsize=(10, 6))
plt.plot(fpr_train, tpr_train, color='blue', lw=2, label=f'Training ROC curve (area = {roc_auc_train:.2f})')
plt.plot(fpr_test, tpr_test, color='red', lw=2, label=f'Test ROC curve (area = {roc_auc_test:.2f})')
plt.plot([0, 1], [0, 1], color='gray', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve using Support Vector Machine')
plt.legend(loc="lower right")
plt.show()


# In[82]:


import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the neural network model
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.5),
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.001),
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=1)

# Evaluate the model
train_loss, train_acc = model.evaluate(X_train, y_train, verbose=0)
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
print(f'Training Accuracy: {train_acc:.4f}, Test Accuracy: {test_acc:.4f}')

# Make predictions
y_probs_train = model.predict(X_train).ravel()
y_probs_test = model.predict(X_test).ravel()

# Calculate the ROC curve and AUC for the training set
fpr_train, tpr_train, _ = roc_curve(y_train, y_probs_train)
roc_auc_train = auc(fpr_train, tpr_train)

# Calculate the ROC curve and AUC for the test set
fpr_test, tpr_test, _ = roc_curve(y_test, y_probs_test)
roc_auc_test = auc(fpr_test, tpr_test)

# Print classification reports
y_pred_train = (y_probs_train > 0.5).astype(int)
y_pred_test = (y_probs_test > 0.5).astype(int)
print("Training Classification Report:")
print(classification_report(y_train, y_pred_train))
print("Testing Classification Report:")
print(classification_report(y_test, y_pred_test))

# Plot the ROC curve
plt.figure(figsize=(10, 6))
plt.plot(fpr_train, tpr_train, color='blue', lw=2, label=f'Training ROC curve (area = {roc_auc_train:.2f})')
plt.plot(fpr_test, tpr_test, color='red', lw=2, label=f'Test ROC curve (area = {roc_auc_test:.2f})')
plt.plot([0, 1], [0, 1], color='gray', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve using Deep Neural Networks')
plt.legend(loc="lower right")
plt.show()


# #AUC-ROC curve shows best results with Random Forest(with slight overfitting)

# #Since we have two random forest classifiers with slight overfitting and a linear Discriminant Analyser,a voting ensemble method would be the best to combine all three models

# In[83]:


from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score


# In[84]:


# Voting classifier with hard voting
voting_clf = VotingClassifier(
    estimators=[('model_1', lda), ('model_2', lda_2), ('model_3', lda_3)],
    voting='hard'  # You can also use 'soft' for soft voting if classifiers support predict_proba
)


# In[85]:


voting_clf.fit(X_train, y_train)

y_pred = voting_clf.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
print(f'Voting Classifier Accuracy: {accuracy:.2f}')


# In[86]:


# Evaluate individual models
lda.fit(X_train, y_train)
lda_pred = lda.predict(X_test)
lda_accuracy = accuracy_score(y_test, lda_pred)
print(f'model_1 Accuracy: {lda_accuracy:.2f}')

lda_2.fit(X_train, y_train)
lda_2_pred = lda_2.predict(X_test)
lda_2_accuracy = accuracy_score(y_test, lda_2_pred)
print(f'model_2 Accuracy: {lda_2_accuracy:.2f}')

lda_3.fit(X_train, y_train)
lda_3_pred = lda_3.predict(X_test)
lda_3_accuracy = accuracy_score(y_test, lda_3_pred)
print(f'model_3 Accuracy: {lda_3_accuracy:.2f}')
print(f'Voting Classifier Accuracy: {accuracy:.2f}')


# Testing the ensemble model

# Retrieving the testing data on Hindustan Uniliver and predicting using the voting classifier ensemble model

# In[87]:


# List to store headlines
headlines_hul = []

# Function to extract headlines and subheadings
def extract_headlines_and_subheadings(soup):
    for link in soup.find_all(['a', 'h3', 'p']):  # Adding common tags for headlines and subheadings
        if link.string and isinstance(link.string, str) and len(link.string) > 50:
            headlines_hul.append(link.string.strip())

# Function to scrape data from a single URL
def scrape_url(url):
    try:
        webpage = req.get(url)
        if webpage.status_code == 200:
            soup = BS(webpage.content, "html.parser")
            extract_headlines_and_subheadings(soup)
        else:
            print(f"Failed to retrieve data from {url}. Status code: {webpage.status_code}")
    except Exception as e:
        print(f"An error occurred while scraping {url}: {str(e)}")

# List of URLs to scrape
urls = ["https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/hindustan-unilever-stocks-live-updates-13-jun-2024/liveblog/110953999.cms",
        "https://www.google.com/finance/quote/HINDUNILVR:NSE","https://finance.yahoo.com/quote/HINDUNILVR.NS/"
]

# Scrape each URL
for url in urls:
    scrape_url(url)

# Join all headlines into a single string
data_hul = '\n'.join(headlines_hul)

print(data_hul)


# In[88]:


import yfinance as yf
tickers = ["HINDUNILVR.NS"]

ohlc_data = {}
for ticker in tickers:
    data = yf.download(ticker, start="2024-06-01", end="2024-06-18")  # Specify your date range#here,for april
    ohlc_data[ticker] = data[['Open', 'High', 'Low', 'Close']]
import pandas as pd

# Convert dictionary to DataFrame
df_1 = pd.concat(ohlc_data.values(), keys=ohlc_data.keys(), names=['Ticker', 'Date'])

# Show output
print(df_1)


# In[89]:


df_1['label'] = (df_1['Close'] > df_1['Open']).astype(int)
print(df_1)


# In[90]:


ticker = 'HINDUNILVR.NS'
start = '2024-06-05'
end = '2024-06-18'

# Fetch historical data
data = yf.download(ticker, start=start, end=end)
plt.figure(figsize=(12, 6))  # Adjust the figure size if needed

plt.plot(data.index, data['Close'], marker='o', linestyle='-', color='b', label='Closing Price')

plt.title(f'Closing Prices of {ticker} from {start} to {end}')
plt.xlabel('Date')
plt.ylabel('Closing Price (Rs.)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()


# In[91]:


df_1['headlines'] = data_hul

# Print the DataFrame to verify the changes
print(df_1)


# In[92]:


import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob

# Download the VADER lexicon
nltk.download('vader_lexicon')

# Initialize VADER
sid = SentimentIntensityAnalyzer()

# Function to calculate sentiment scores for a given text
def calculate_sentiment_scores(text):
    sentiment_scores = sid.polarity_scores(text)
    return sentiment_scores['pos'], sentiment_scores['neg'], sentiment_scores['neu'], sentiment_scores['compound']

# Function to calculate polarity and subjectivity scores for a given text
def calculate_textblob_scores(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    return polarity, subjectivity

# Iterate over each row and calculate sentiment scores, polarity, and subjectivity
pos_scores = []
neg_scores = []
neu_scores = []
compound_scores = []
polarity_scores = []
subjectivity_scores = []

for index, row in df_1.iterrows():
    headline = row['headlines']

    # Calculate sentiment scores using VADER
    pos_score, neg_score, neu_score, compound_score = calculate_sentiment_scores(headline)
    pos_scores.append(pos_score)
    neg_scores.append(neg_score)
    neu_scores.append(neu_score)
    compound_scores.append(compound_score)

    # Calculate polarity and subjectivity scores using TextBlob
    polarity_score, subjectivity_score = calculate_textblob_scores(headline)
    polarity_scores.append(polarity_score)
    subjectivity_scores.append(subjectivity_score)

# Add sentiment scores, polarity, and subjectivity to the DataFrame
df_1['Positivity'] = pos_scores
df_1['Negativity'] = neg_scores
df_1['Neutrality'] = neu_scores
df_1['Compound Score'] = compound_scores
df_1['Polarity'] = polarity_scores
df_1['Subjectivity'] = subjectivity_scores

# Print the DataFrame with sentiment scores, polarity, and subjectivity
print(df_1)


# In[93]:


df_1.head()


# In[94]:


features = ['Open','High','Low','Subjectivity', 'Polarity', 'Compound Score', 'Negativity', 'Neutrality', 'Positivity']
X = df_1[features]
print(X)


# In[95]:


y_predict =voting_clf.predict(X)


# In[96]:


y_predict


# In[97]:


y_actual =df_1['label']
print(y_actual)


# In[98]:


accuracy = accuracy_score(y_actual,y_predict)
print(f'Accuracy: {accuracy:.2f}')


# Testing on another stock

# In[99]:


# List to store headlines
headlines_test = []

# Function to extract headlines and subheadings
def extract_headlines_and_subheadings(soup):
    for link in soup.find_all(['a', 'h3', 'p']):  # Adding common tags for headlines and subheadings
        if link.string and isinstance(link.string, str) and len(link.string) > 50:
            headlines_test.append(link.string.strip())

# Function to scrape data from a single URL
def scrape_url(url):
    try:
        webpage = req.get(url)
        if webpage.status_code == 200:
            soup = BS(webpage.content, "html.parser")
            extract_headlines_and_subheadings(soup)
        else:
            print(f"Failed to retrieve data from {url}. Status code: {webpage.status_code}")
    except Exception as e:
        print(f"An error occurred while scraping {url}: {str(e)}")

# List of URLs to scrape
urls = ["https://finance.yahoo.com/quote/INFY/","https://finance.yahoo.com/quote/INFY/news/","https://economictimes.indiatimes.com/infosys-ltd/stocksupdate/companyid-10960.cms",
       "https://www.msn.com/en-in/money/topstories/infosys-wins-100-million-ikea-deal/ar-BB1ofxc6?ocid=BingNewsSerp",
        "https://www.livemint.com/market/stock-market-news/infosys-board-meeting-to-be-held-on-july-18-to-consider-q1fy25-quarterly-results-11718378856120.html",
        "https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/infosys-share-price-live-updates-05-jun-2024/liveblog/110718620.cms"


]

# Scrape each URL
for url in urls:
    scrape_url(url)

# Join all headlines into a single string
data_test = '\n'.join(headlines_test)

print(data_test)


# In[100]:


import yfinance as yf
tickers = ["INFY.NS"]

ohlc_data = {}
for ticker in tickers:
    data = yf.download(ticker, start="2024-06-01", end="2024-06-14")  # Specify your date range#here,for april
    ohlc_data[ticker] = data[['Open', 'High', 'Low', 'Close']]
import pandas as pd

# Convert dictionary to DataFrame
df_1 = pd.concat(ohlc_data.values(), keys=ohlc_data.keys(), names=['Ticker', 'Date'])

# Show output
print(df_1)


# In[101]:


df_1['label'] = (df_1['Close'] > df_1['Open']).astype(int)
print(df_1)


# In[102]:


df_1['headlines'] = data_test

# Print the DataFrame to verify the changes
print(df_1)


# In[103]:


import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob

# Download the VADER lexicon
nltk.download('vader_lexicon')

# Initialize VADER
sid = SentimentIntensityAnalyzer()

# Function to calculate sentiment scores for a given text
def calculate_sentiment_scores(text):
    sentiment_scores = sid.polarity_scores(text)
    return sentiment_scores['pos'], sentiment_scores['neg'], sentiment_scores['neu'], sentiment_scores['compound']

# Function to calculate polarity and subjectivity scores for a given text
def calculate_textblob_scores(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    return polarity, subjectivity

# Iterate over each row and calculate sentiment scores, polarity, and subjectivity
pos_scores = []
neg_scores = []
neu_scores = []
compound_scores = []
polarity_scores = []
subjectivity_scores = []

for index, row in df_1.iterrows():
    headline = row['headlines']

    # Calculate sentiment scores using VADER
    pos_score, neg_score, neu_score, compound_score = calculate_sentiment_scores(headline)
    pos_scores.append(pos_score)
    neg_scores.append(neg_score)
    neu_scores.append(neu_score)
    compound_scores.append(compound_score)

    # Calculate polarity and subjectivity scores using TextBlob
    polarity_score, subjectivity_score = calculate_textblob_scores(headline)
    polarity_scores.append(polarity_score)
    subjectivity_scores.append(subjectivity_score)

# Add sentiment scores, polarity, and subjectivity to the DataFrame
df_1['Positivity'] = pos_scores
df_1['Negativity'] = neg_scores
df_1['Neutrality'] = neu_scores
df_1['Compound Score'] = compound_scores
df_1['Polarity'] = polarity_scores
df_1['Subjectivity'] = subjectivity_scores

# Print the DataFrame with sentiment scores, polarity, and subjectivity
print(df_1)


# In[104]:


df_1.head()


# In[105]:


features = ['Open','High','Low','Subjectivity', 'Polarity', 'Compound Score', 'Negativity', 'Neutrality', 'Positivity']
X = df_1[features]
print(X)


# In[106]:


y_predict =voting_clf.predict(X)


# In[107]:


y_predict


# In[108]:


y_actual =df_1['label']
print(y_actual)


# In[109]:


accuracy = accuracy_score(y_actual,y_predict)
print(f'Accuracy: {accuracy:.2f}')


# In[110]:


# List to store headlines
headlines_test = []

# Function to extract headlines and subheadings
def extract_headlines_and_subheadings(soup):
    for link in soup.find_all(['a', 'h3', 'p']):  # Adding common tags for headlines and subheadings
        if link.string and isinstance(link.string, str) and len(link.string) > 50:
            headlines_test.append(link.string.strip())

# Function to scrape data from a single URL
def scrape_url(url):
    try:
        webpage = req.get(url)
        if webpage.status_code == 200:
            soup = BS(webpage.content, "html.parser")
            extract_headlines_and_subheadings(soup)
        else:
            print(f"Failed to retrieve data from {url}. Status code: {webpage.status_code}")
    except Exception as e:
        print(f"An error occurred while scraping {url}: {str(e)}")

# List of URLs to scrape
urls = ["https://www.livemint.com/biocon/news/companyid-s0003121","https://economictimes.indiatimes.com/biocon-ltd/stocksupdate/companyid-2082.cms"
   ,"https://www.moneycontrol.com/news/business/markets/trade-spotlight-how-should-you-trade-tata-steel-biocon-apollo-tyres-wipro-rallis-india-and-others-on-monday-12744477.html",
        "https://www.moneycontrol.com/stocks/stock_market/sector_announcements.php","https://www.moneycontrol.com/stocks/sectors/pharmaceuticals.html",
    ]

# Scrape each URL
for url in urls:
    scrape_url(url)

# Join all headlines into a single string
data_test = '\n'.join(headlines_test)

print(data_test)


# In[111]:


import yfinance as yf
tickers = ["BIOCON.NS"]

ohlc_data = {}
for ticker in tickers:
    data = yf.download(ticker, start="2024-05-27", end="2024-06-09")  # Specify your date range#here,for april
    ohlc_data[ticker] = data[['Open', 'High', 'Low', 'Close']]
import pandas as pd

# Convert dictionary to DataFrame
df_1 = pd.concat(ohlc_data.values(), keys=ohlc_data.keys(), names=['Ticker', 'Date'])

# Show output
print(df_1)


# In[112]:


df_1['label'] = (df_1['Close'] > df_1['Open']).astype(int)
print(df_1)


# In[113]:


df_1['headlines'] = data_test

# Print the DataFrame to verify the changes
print(df_1)


# In[114]:


import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob

# Download the VADER lexicon
nltk.download('vader_lexicon')

# Initialize VADER
sid = SentimentIntensityAnalyzer()

# Function to calculate sentiment scores for a given text
def calculate_sentiment_scores(text):
    sentiment_scores = sid.polarity_scores(text)
    return sentiment_scores['pos'], sentiment_scores['neg'], sentiment_scores['neu'], sentiment_scores['compound']

# Function to calculate polarity and subjectivity scores for a given text
def calculate_textblob_scores(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    return polarity, subjectivity

# Iterate over each row and calculate sentiment scores, polarity, and subjectivity
pos_scores = []
neg_scores = []
neu_scores = []
compound_scores = []
polarity_scores = []
subjectivity_scores = []

for index, row in df_1.iterrows():
    headline = row['headlines']

    # Calculate sentiment scores using VADER
    pos_score, neg_score, neu_score, compound_score = calculate_sentiment_scores(headline)
    pos_scores.append(pos_score)
    neg_scores.append(neg_score)
    neu_scores.append(neu_score)
    compound_scores.append(compound_score)

    # Calculate polarity and subjectivity scores using TextBlob
    polarity_score, subjectivity_score = calculate_textblob_scores(headline)
    polarity_scores.append(polarity_score)
    subjectivity_scores.append(subjectivity_score)

# Add sentiment scores, polarity, and subjectivity to the DataFrame
df_1['Positivity'] = pos_scores
df_1['Negativity'] = neg_scores
df_1['Neutrality'] = neu_scores
df_1['Compound Score'] = compound_scores
df_1['Polarity'] = polarity_scores
df_1['Subjectivity'] = subjectivity_scores

# Print the DataFrame with sentiment scores, polarity, and subjectivity
print(df_1)


# In[115]:


df_1.head()


# In[116]:


features = ['Open','High','Low','Subjectivity', 'Polarity', 'Compound Score', 'Negativity', 'Neutrality', 'Positivity']
X = df_1[features]
print(X)


# In[117]:


y_predict =voting_clf.predict(X)


# In[118]:


y_predict


# In[119]:


y_actual =df_1['label']
print(y_actual)


# In[120]:


accuracy = accuracy_score(y_actual,y_predict)
print(f'Accuracy: {accuracy:.2f}')


# In[ ]:





# In[121]:


# List to store headlines
headlines_test = []

# Function to extract headlines and subheadings
def extract_headlines_and_subheadings(soup):
    for link in soup.find_all(['a', 'h3', 'p']):  # Adding common tags for headlines and subheadings
        if link.string and isinstance(link.string, str) and len(link.string) > 50:
            headlines_test.append(link.string.strip())

# Function to scrape data from a single URL
def scrape_url(url):
    try:
        webpage = req.get(url)
        if webpage.status_code == 200:
            soup = BS(webpage.content, "html.parser")
            extract_headlines_and_subheadings(soup)
        else:
            print(f"Failed to retrieve data from {url}. Status code: {webpage.status_code}")
    except Exception as e:
        print(f"An error occurred while scraping {url}: {str(e)}")

# List of URLs to scrape
urls = ["https://www.bing.com/news/search?q=Nvidia+Stocks&qpvt=nvdia+stocks+news&FORM=EWRE","https://finance.yahoo.com/quote/NVDA/news/",
        "https://www.google.com/finance/quote/NVDA:NASDAQ","https://finance.yahoo.com/quote/NVDA/news/",
        "https://www.moneycontrol.com/news/business/markets/nvidia-10-for-1-stock-split-goes-into-effect-after-stock-price-for-the-chipmaker-doubled-this-year-12745226.html",
        "https://www.msn.com/en-us/money/markets/after-2-trillion-gain-nvidia-is-still-irresistible-to-many/ar-BB1nFr9H?ocid=BingNewsSerp",
        "https://www.bloomberg.com/news/articles/2023-08-23/nvidia-gives-rosy-outlook-in-sign-ai-spending-remains-insatiable",
        "https://stockanalysis.com/stocks/nvda/"


]

# Scrape each UR
for url in urls:
    scrape_url(url)

# Join all headlines into a single string
data_test = '\n'.join(headlines_test)

print(data_test)


# In[122]:


import yfinance as yf
tickers = ["NVDA"]

ohlc_data = {}
for ticker in tickers:
    data = yf.download(ticker, start="2024-05-21", end="2024-06-18")  # Specify your date range#here,for april
    ohlc_data[ticker] = data[['Open', 'High', 'Low', 'Close']]
import pandas as pd

# Convert dictionary to DataFrame
df_1 = pd.concat(ohlc_data.values(), keys=ohlc_data.keys(), names=['Ticker', 'Date'])

# Show output
print(df_1)


# In[123]:


df_1['label'] = (df_1['Close'] > df_1['Open']).astype(int)
print(df_1)


# In[124]:


df_1['headlines'] = data_test

# Print the DataFrame to verify the changes
print(df_1)


# In[125]:


import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob

# Download the VADER lexicon
nltk.download('vader_lexicon')

# Initialize VADER
sid = SentimentIntensityAnalyzer()

# Function to calculate sentiment scores for a given text
def calculate_sentiment_scores(text):
    sentiment_scores = sid.polarity_scores(text)
    return sentiment_scores['pos'], sentiment_scores['neg'], sentiment_scores['neu'], sentiment_scores['compound']

# Function to calculate polarity and subjectivity scores for a given text
def calculate_textblob_scores(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    return polarity, subjectivity

# Iterate over each row and calculate sentiment scores, polarity, and subjectivity
pos_scores = []
neg_scores = []
neu_scores = []
compound_scores = []
polarity_scores = []
subjectivity_scores = []

for index, row in df_1.iterrows():
    headline = row['headlines']

    # Calculate sentiment scores using VADER
    pos_score, neg_score, neu_score, compound_score = calculate_sentiment_scores(headline)
    pos_scores.append(pos_score)
    neg_scores.append(neg_score)
    neu_scores.append(neu_score)
    compound_scores.append(compound_score)

    # Calculate polarity and subjectivity scores using TextBlob
    polarity_score, subjectivity_score = calculate_textblob_scores(headline)
    polarity_scores.append(polarity_score)
    subjectivity_scores.append(subjectivity_score)

# Add sentiment scores, polarity, and subjectivity to the DataFrame
df_1['Positivity'] = pos_scores
df_1['Negativity'] = neg_scores
df_1['Neutrality'] = neu_scores
df_1['Compound Score'] = compound_scores
df_1['Polarity'] = polarity_scores
df_1['Subjectivity'] = subjectivity_scores

# Print the DataFrame with sentiment scores, polarity, and subjectivity
print(df_1)


# In[126]:


df_1.head()


# In[127]:


features = ['Open','High','Low','Subjectivity', 'Polarity', 'Compound Score', 'Negativity', 'Neutrality', 'Positivity']
X = df_1[features]
print(X)


# In[128]:


y_predict =voting_clf.predict(X)


# In[129]:


y_predict


# In[130]:


y_actual =df_1['label']
print(y_actual)


# In[131]:


accuracy = accuracy_score(y_actual,y_predict)
print(f'Accuracy: {accuracy:.2f}')


# In[132]:


ticker = 'NVDA'
start = '2024-05-21'
end = '2024-06-18'

# Fetch historical data
data = yf.download(ticker, start=start, end=end)
plt.figure(figsize=(12, 6))  # Adjust the figure size if needed

plt.plot(data.index, data['Close'], marker='o', linestyle='-', color='b', label='Closing Price')

plt.title(f'Closing Prices of {ticker} from {start} to {end}')
plt.xlabel('Date')
plt.ylabel('Closing Price (Rs.)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()


# In[133]:


import yfinance as yf
import numpy as np
#since we are not dealing with government bonds and the study of the stocks have been for over past 3 months only ,we have assumed the risk free rate to be 0%

def calculate_sharpe_ratio(returns, risk_free_rate=0):
    # Calculate average daily return and standard deviation of daily returns
    avg_return = np.mean(returns)
    std_dev = np.std(returns)

    # Calculate annualized Sharpe ratio (252 trading days)
    sharpe_ratio = (avg_return - risk_free_rate) / std_dev * np.sqrt(252)

    return sharpe_ratio

def calculate_maximum_drawdown(prices):
    # Calculate daily returns
    returns = np.diff(prices) / prices[:-1]

    # Calculate cumulative returns
    cumulative_returns = np.cumprod(1 + returns) - 1

    # Calculate maximum drawdown
    max_drawdown = np.max(np.abs(np.maximum.accumulate(cumulative_returns) - cumulative_returns))

    return max_drawdown

def calculate_number_of_trades(returns):
    # Number of trades is simply the count of non-zero returns
    num_trades = np.count_nonzero(returns)

    return num_trades

def calculate_win_ratio(returns):
    # Calculate win ratio (percentage of positive returns) for long position
    win_ratio = np.sum(returns > 0) / len(returns)


    return win_ratio

# Example usage
ticker = 'NVDA'  # Example ticker symbol
start_date = '2024-05-21'
end_date = '2024-06-17'

# Fetch historical data from Yahoo Finance
data = yf.download(ticker, start=start_date, end=end_date)

# Calculate daily returns
data['Daily Return'] = data['Adj Close'].pct_change()

# Remove NaN values (first row)
returns = data['Daily Return'].dropna().values

# Calculate Sharpe ratio
sharpe_ratio = calculate_sharpe_ratio(returns)
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")

# Calculate maximum drawdown
prices = data['Adj Close'].values
max_drawdown = calculate_maximum_drawdown(prices)
print(f"Maximum Drawdown: {max_drawdown:.2%}")

# Calculate number of trades executed (non-zero returns)
num_trades = calculate_number_of_trades(returns)
print(f"Number of Trades Executed: {num_trades}")

# Calculate win ratio
win_ratio = calculate_win_ratio(returns)
print(f"Win Ratio: {win_ratio:.2%}")


# In[134]:


import yfinance as yf
import numpy as np

def calculate_sharpe_ratio(returns, risk_free_rate=0):
    # Calculate average daily return and standard deviation of daily returns
    avg_return = np.mean(returns)
    std_dev = np.std(returns)

    # Calculate annualized Sharpe ratio (252 trading days)
    sharpe_ratio = (avg_return - risk_free_rate) / std_dev * np.sqrt(252)

    return sharpe_ratio

def calculate_maximum_drawdown(prices):
    # Calculate daily returns
    returns = np.diff(prices) / prices[:-1]

    # Calculate cumulative returns
    cumulative_returns = np.cumprod(1 + returns) - 1

    # Calculate maximum drawdown
    max_drawdown = np.max(np.abs(np.maximum.accumulate(cumulative_returns) - cumulative_returns))

    return max_drawdown

def calculate_number_of_trades(returns):
    # Number of trades is simply the count of non-zero returns
    num_trades = np.count_nonzero(returns)

    return num_trades

def calculate_win_ratio(returns):
    # Calculate win ratio (percentage of time the short position was profitable)
    win_ratio = np.sum(returns < 0) / len(returns)

    return win_ratio

# Example usage
ticker = 'HINDUNILVR.NS'  # Example ticker symbol
start_date = '2024-06-07'
end_date = '2024-06-14' # End date for shorting period

# Fetch historical data from Yahoo Finance
data = yf.download(ticker, start=start_date, end=end_date)

# Calculate daily returns
data['Daily Return'] = data['Adj Close'].pct_change()

# Remove NaN values (first row)
data.dropna(inplace=True)

# Calculate cumulative returns for shorting over the period
data['Cumulative Return'] = np.cumprod(1 - data['Daily Return']) - 1

# Extract metrics
returns = data['Cumulative Return'].values
sharpe_ratio = calculate_sharpe_ratio(returns)
max_drawdown = calculate_maximum_drawdown(data['Adj Close'].values)
num_trades = calculate_number_of_trades(data['Daily Return'].values)
win_ratio = calculate_win_ratio(data['Daily Return'].values)

# Print metrics
print(f"Sharpe Ratio: {sharpe_ratio:.4f}")
print(f"Maximum Drawdown: {max_drawdown:.4f}")
print(f"Number of Trades Executed: {num_trades}")
print(f"Win Ratio: {win_ratio:.2%}")


# In[135]:


import yfinance as yf
import matplotlib.pyplot as plt

# Define the ticker symbol and timeframe
ticker_symbol = 'HINDUNILVR.NS'
start_date = '2024-01-01'
end_date = '2024-06-15'

# Fetch the data
stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Extract the closing prices
closing_prices = stock_data['Close']

# Plotting the closing prices
plt.figure(figsize=(12, 6))
plt.plot(closing_prices.index, closing_prices, label='Closing Prices', color='blue')

# Marking the sell point (7th June) and buy point (14th June)
sell_point = '2024-06-07'
buy_point = '2024-06-14'
plt.scatter([sell_point], closing_prices[sell_point], color='red', label='Sell Point', zorder=5)
plt.scatter([buy_point], closing_prices[buy_point], color='green', label='Buy Point', zorder=5)

# Adding labels and title
plt.title(f'{ticker_symbol} Closing Prices with Buy/Sell Points')
plt.xlabel('Date')
plt.ylabel('Closing Price ($)')
plt.legend()

# Display plot
plt.grid(True)
plt.tight_layout()
plt.show()


# In[143]:


import yfinance as yf
import matplotlib.pyplot as plt

# Define the ticker symbol and timeframe
import yfinance as yf
import pandas as pd
import numpy as np

# Define the ticker symbol and timeframe
ticker_symbol = 'NVDA'
start_date = '2024-05-21'
end_date = '2024-06-18'

# Fetch the data
stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Calculate daily returns
stock_data['Daily Return'] = stock_data['Close'].pct_change()

# Calculate Sharpe ratio (assuming risk-free rate of 0% for simplicity)
risk_free_rate = 0
sharpe_ratio = np.sqrt(252) * (stock_data['Daily Return'].mean() - risk_free_rate) / stock_data['Daily Return'].std()

# Calculate number of trades executed per day (using a simple proxy for illustration)
# For demonstration, let's assume a random number of trades between 0 and 10 per day
np.random.seed(0)  # For reproducibility
stock_data['Number of Trades'] = np.random.randint(0, 11, size=len(stock_data))

# Extract necessary columns
table_data = stock_data[['Open', 'High', 'Low', 'Close', 'Number of Trades']]

# Add Sharpe ratio as a row
table_data.loc['Sharpe Ratio'] = [np.nan] * 4 + [sharpe_ratio]

# Display the table
print(f"Stock Data Table for {ticker_symbol} from {start_date} to {end_date}:")
print(table_data)


# Fetch the data
stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Extract the closing prices
closing_prices = stock_data['Close']
nvda = f"{ticker_symbol}_stock_data_{start_date}_to_{end_date}.xlsx"
table_data.to_excel(nvda)

print(f"Stock data saved to {nvda}")


# In[151]:


import yfinance as yf
import matplotlib.pyplot as plt

# Define the ticker symbol and timeframe
import yfinance as yf
import pandas as pd
import numpy as np

# Define the ticker symbol and timeframe
ticker = 'HINDUNILVR.NS'
start = '2024-06-05'
end = '2024-06-18'

# Fetch the data
stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Calculate daily returns
stock_data['Daily Return'] = stock_data['Close'].pct_change()

# Calculate Sharpe ratio (assuming risk-free rate of 0% for simplicity)
risk_free_rate = 0
sharpe_ratio = np.sqrt(252) * (stock_data['Daily Return'].mean() - risk_free_rate) / stock_data['Daily Return'].std()

# Calculate number of trades executed per day (using a simple proxy for illustration)
# For demonstration, let's assume a random number of trades between 0 and 10 per day
np.random.seed(0)  # For reproducibility
stock_data['Number of Trades'] = np.random.randint(0, 11, size=len(stock_data))

# Extract necessary columns
table_data = stock_data[['Open', 'High', 'Low', 'Close', 'Number of Trades']]

# Add Sharpe ratio as a row
table_data.loc['Sharpe Ratio'] = [np.nan] * 4 + [sharpe_ratio]

# Display the table
print(f"Stock Data Table for {ticker_symbol} from {start_date} to {end_date}:")
print(table_data)


# Fetch the data
stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Extract the closing prices
closing_prices = stock_data['Close']
nvda = f"{ticker_symbol}_stock_data_{start_date}_to_{end_date}.xlsx"
table_data.to_excel(hul)

print(f"Stock data saved to {hul}")


# In[146]:


import yfinance as yf
import pandas as pd
import numpy as np

# Define the ticker symbol and timeframe
ticker_symbol = 'NVDA'
start_date = '2024-05-21'
end_date = '2024-06-18'


# Fetch the data
stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Calculate daily returns
stock_data['Daily Return'] = stock_data['Close'].pct_change()

# Calculate Sharpe ratio (assuming risk-free rate of 0% for simplicity)
risk_free_rate = 0
sharpe_ratio = np.sqrt(252) * (stock_data['Daily Return'].mean() - risk_free_rate) / stock_data['Daily Return'].std()

# Calculate number of trades executed per day (using a simple proxy for illustration)
# For demonstration, let's assume a random number of trades between 0 and 10 per day
np.random.seed(0)  # For reproducibility
stock_data['Number of Trades'] = np.random.randint(0, 11, size=len(stock_data))

# Extract necessary columns
table_data = stock_data[['Open', 'High', 'Low', 'Close', 'Number of Trades']]

# Add Sharpe ratio as a row
table_data.loc['Sharpe Ratio'] = [np.nan] * 4 + [sharpe_ratio]

# Specify the path where you want to save the Excel file
excel_file_path = "C:/Users/prish/Downloads/nvda.xlsx"

# Save table_data to the specified Excel file path
table_data.to_excel(excel_file_path)

print(f"Stock data saved to {excel_file_path}")


# In[150]:


import yfinance as yf
import pandas as pd
import numpy as np

# Define the ticker symbol and timeframe
ticker = 'HINDUNILVR.NS'
start = '2024-06-05'
end = '2024-06-18'

# Fetch the data
stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Calculate daily returns
stock_data['Daily Return'] = stock_data['Close'].pct_change()

# Calculate Sharpe ratio (assuming risk-free rate of 0% for simplicity)
risk_free_rate = 0
sharpe_ratio = np.sqrt(252) * (stock_data['Daily Return'].mean() - risk_free_rate) / stock_data['Daily Return'].std()

# Calculate number of trades executed per day (using a simple proxy for illustration)
# For demonstration, let's assume a random number of trades between 0 and 10 per day
np.random.seed(0)  # For reproducibility
stock_data['Number of Trades'] = np.random.randint(0, 11, size=len(stock_data))

# Extract necessary columns
table_data = stock_data[['Open', 'High', 'Low', 'Close', 'Number of Trades']]

# Add Sharpe ratio as a row
table_data.loc['Sharpe Ratio'] = [np.nan] * 4 + [sharpe_ratio]

# Specify the path where you want to save the Excel file
excel_file_path = "C:/Users/prish/Downloads/hul.xlsx"
# Save table_data to the specified Excel file path
table_data.to_excel(excel_file_path)

print(f"Stock data saved to {excel_file_path}")


# In[ ]:





# In[ ]:




