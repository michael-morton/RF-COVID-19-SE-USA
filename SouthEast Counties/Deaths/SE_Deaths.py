import pandas as pd
import numpy as np

df = pd.read_csv("SE_Counties.csv")
#print(df.head())
#print(df.dtypes)
print(df.describe())

df = df.select_dtypes(exclude=['object'])
#df = df.fillna(df.mean())

X = df.drop('deaths',axis=1)
y = df['deaths']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

test = X_test
#test.to_csv('test.csv', index = False)

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 1000, random_state = 42)
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
df = pd.DataFrame({'actual deaths':y_test, 'predicted deaths':y_pred})

importance = regressor.feature_importances_

print()
for i,v in enumerate(importance):
	print('Feature: %0d, Score: %.5f' % (i,v))

results = df
#results.to_csv('results_deaths.csv', index = False)

concat_results = pd.concat([test, results], axis = 1)
concat_results.to_csv('results_deaths.csv', index = False)

from sklearn import metrics

print()
print('Explained Variance Score:' , metrics.explained_variance_score(y_test, y_pred))
print('R^2 Score:' , metrics.r2_score(y_test, y_pred))

# Calculate the absolute errors
errors = abs(y_pred - y_test)
# Print out the mean absolute error (mae)
print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')
print()