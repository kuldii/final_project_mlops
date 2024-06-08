import joblib
import pandas as pd

from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer


df = pd.read_csv('data/cleaned_dataset.csv')

X_train = df['cleaned']
y_train = df['sentiment']


# Define the pipeline with TfidfVectorizer and RandomForestClassifier
pipeline = make_pipeline(
    TfidfVectorizer(),
    RandomForestClassifier(random_state=42)
)

# Define the parameter grid
param_grid = {
    'randomforestclassifier__n_estimators': [100, 200, 300],
    'randomforestclassifier__max_features': ['sqrt', 'log2'],
    'randomforestclassifier__max_depth': [10, 20, 30],
}

# Set up the GridSearchCV
grid_search = GridSearchCV(estimator=pipeline,
                           param_grid=param_grid,
                           cv=5, n_jobs=-1, verbose=2)

# Fit the grid search to the data
grid_search.fit(X_train, y_train)

# Get the best parameters and the best score
best_params = grid_search.best_params_
best_score = grid_search.best_score_

print("Best parameters found: ", best_params)
print("Best cross-validation score: ", best_score)

# Save the fitted grid search model using joblib
joblib_file = 'model/random_forest_model.pkl'
joblib.dump(grid_search, joblib_file)

print(f"Model saved to {joblib_file}")
