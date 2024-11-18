import pandas as pd
from scipy.stats import ttest_ind

def read_data(file_name):
    """Reading the CSV file."""
    try:
        df = pd.read_csv(file_name)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_name}' not found. Please check the file name and location.")

def validate_columns(df, required_columns):
    """Validating if required columns exist in the dataset."""
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")

def calculate_satisfaction_score(df, satisfaction_columns):
    """Creating a Satisfaction Score column."""
    df['Satisfaction_Score'] = df[satisfaction_columns].mean(axis=1)
    return df

def perform_ttest(df):
    """Performing the independent t-test and returns the results."""
    ctis_scores = df[df['Department'].str.contains('CTMA|CTIS', na=False, case=False)]['Satisfaction_Score']
    aiml_scores = df[df['Department'].str.contains('AIML', na=False, case=False)]['Satisfaction_Score']
    t_stat, p_value = ttest_ind(ctis_scores, aiml_scores, nan_policy='omit')
    return t_stat, p_value

def descriptive_statistics(df):
    """Printing the descriptive statistics grouped by department."""
    return df.groupby('Department')['Satisfaction_Score'].describe()
