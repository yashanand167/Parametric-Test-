import test

if __name__ == "__main__":
    # File name
    file_name = 'Untitled_from.csv'
    # Required columns
    satisfaction_columns = [
        'How satisfied are you with your academic experience in your department?',
        'How satisfied are you with the resources available (labs, libraries, online resources, etc.) in your department',
        'How satisfied are you with the academic workload and its balance in your department? ',
        'How satisfied are you with the support provided by faculty and staff?',
        'How satisfied are you with the opportunities for student engagement and extracurricular activities in your department?'
    ]

    try:
        # Reading the dataset
        df = test.read_data(file_name)

        # Validating the columns
        test.validate_columns(df, satisfaction_columns + ['Department'])

        # Calculating the satisfaction score
        df = test.calculate_satisfaction_score(df, satisfaction_columns)

        # Performing the t-test
        t_stat, p_value = test.perform_ttest(df)
        print("T-statistic:", t_stat)
        print("P-value:", p_value)

        # Interpreting the result
        alpha = 0.05  # Significance level
        if p_value < alpha:
            print("Reject the null hypothesis: Significant difference between the departments.")
        else:
            print("Fail to reject the null hypothesis: No significant difference.")

        # Printing the descriptive statistics
        print("\nDescriptive Statistics:")
        print(test.descriptive_statistics(df))

    except Exception as e:
        print(f"An error occurred: {e}")
