import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Read in the data
data = pd.read_csv('responses.csv')

# Remove duplicates and incomplete entries
data.drop_duplicates(inplace=True)
data.dropna(inplace=True)

# Convert data to numerical form
data['Communication Skills'] = pd.to_numeric(data['Communication Skills'])
data['Teaching Style'] = pd.to_numeric(data['Teaching Style'])
data['Clarity of Explanation'] = pd.to_numeric(data['Clarity of Explanation'])
data['Engagement Level'] = pd.to_numeric(data['Engagement Level'])
data['Availability for Help'] = pd.to_numeric(data['Availability for Help'])
data['Overall Rating'] = pd.to_numeric(data['Overall Rating'])

# Split the data into training and testing sets
X = data[['Communication Skills', 'Teaching Style', 'Clarity of Explanation', 'Engagement Level', 'Availability for Help']]
y = data['Overall Rating']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Apply linear regression to the training data
reg = LinearRegression()
reg.fit(X_train, y_train)

# Use the model to predict the overall rating for a new input
new_data = {'Communication Skills': 8, 'Teaching Style': 7, 'Clarity of Explanation': 9, 'Engagement Level': 8, 'Availability for Help': 7}
new_df = pd.DataFrame(new_data, index=[0])
predicted_rating = reg.predict(new_df)
print(predicted_rating[0])
