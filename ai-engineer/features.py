import pandas as pd

# Load the titanic dataset 
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

# Display the first few rows of the dataset
print(df.head())

# Display the dataset information 
# print(df.info())

# Separate the features and target variable
categorical_features = df.select_dtypes(include=['str']).columns.tolist()
numerical_features = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

print ("Categorical Features:", categorical_features)
print ("Numerical Features:", numerical_features)

# Print the summary of categorical features
for feature in categorical_features:
    print(f"\nSummary of {feature}:")
    print(df[feature].value_counts())   


# Print the summary of numerical features
for feature in numerical_features:
    print(f"\nSummary of {feature}:")
    print(df[feature].describe())

