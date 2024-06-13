# main.py

import pandas as pd
import matplotlib.pyplot as plt


# Exercise 1: Data Reading and Cleaning

# 1.1. Implement a function called read_csv
def read_csv(file_path):
    """
    Reads a CSV file and prints its first five rows and its structure.

    Args:
    file_path (str): Path to the CSV file.

    Returns:
    pd.DataFrame: The loaded dataframe.
    """
    print("\n1.1. Reading CSV file...")
    df = pd.read_csv(file_path)
    print("First five rows of the dataframe:")
    print(df.head())  # Display the first five rows
    print("\nDataframe structure:")
    print(df.info())  # Display the dataframe structure
    return df


# 1.2. Implement a function called clean_csv
def clean_csv(df):
    """
    Cleans the dataframe by retaining only the specified columns.

    Args:
    df (pd.DataFrame): The input dataframe.

    Returns:
    pd.DataFrame: The cleaned dataframe with only relevant columns.
    """
    print("\n1.2. Cleaning CSV file by keeping relevant columns...")
    columns_to_keep = ['month', 'state', 'permit', 'handgun', 'long_gun']
    cleaned_df = df[columns_to_keep]
    print("Columns retained:")
    print(cleaned_df.columns)  # Display the column names
    print("First five rows of the cleaned dataframe:")
    print(cleaned_df.head())
    return cleaned_df


# 1.3. Implement a function called rename_col
def rename_col(df):
    """
    Renames 'longgun' column to 'long_gun' and prints the new column names.

    Args:
    df (pd.DataFrame): The input dataframe.

    Returns:
    pd.DataFrame: The dataframe with renamed columns.
    """
    print("\n1.3. Renaming columns...")
    if 'longgun' in df.columns:
        df.rename(columns={'longgun': 'long_gun'}, inplace=True)
    print("Updated column names:")
    print(df.columns)  # Display the column names
    return df


# Exercise 2: Data Processing

# 2.1. Implement a function called breakdown_date
def breakdown_date(df):
    """
    Splits the 'month' column into 'year' and 'month' columns.

    Args:
    df (pd.DataFrame): The input dataframe.

    Returns:
    pd.DataFrame: The dataframe with separate 'year' and 'month' columns.
    """
    print("\n2.1. Breaking down 'month' column into 'year' and 'month'...")
    df[['year', 'month']] = df['month'].str.split('-', expand=True).astype(int)
    print("First five rows of the dataframe after breaking down the date:")
    print(df.head())  # Display the first five rows
    return df


# 2.2. Implement a function called erase_month
def erase_month(df):
    """
    Removes the 'month' column from the dataframe.

    Args:
    df (pd.DataFrame): The input dataframe.

    Returns:
    pd.DataFrame: The dataframe without the 'month' column.
    """
    print("\n2.2. Removing 'month' column...")
    df = df.drop(columns=['month'])
    print("First five rows of the dataframe after removing 'month' column:")
    print(df.head())  # Display the first five rows
    print("Updated column names:")
    print(df.columns)  # Display the column names
    return df


# Exercise 3: Data Grouping

# 3.1. Implement a function called groupby_state_and_year
def groupby_state_and_year(df):
    """
    Groups the dataframe by 'year' and 'state', summing the numerical columns.

    Args:
    df (pd.DataFrame): The input dataframe.

    Returns:
    pd.DataFrame: The grouped dataframe.
    """
    print("\n3.1. Grouping data by 'state' and 'year'...")
    grouped_df = df.groupby(['year', 'state']).sum().reset_index()
    print("First five rows of the grouped dataframe:")
    print(grouped_df.head())
    return grouped_df


# 3.2. Implement a function called print_biggest_handguns
def print_biggest_handguns(df):
    """
    Prints the state and year with the highest number of handguns.

    Args:
    df (pd.DataFrame): The input dataframe.
    """
    max_handguns = df[df['handgun'] == df['handgun'].max()]
    print("\n3.2. State and year with the highest number of handguns:")
    print(f"Highest number of handguns was in {max_handguns['state'].values[0]} in {max_handguns['year'].values[0]}")


# 3.3. Implement a function called print_biggest_longguns
def print_biggest_longguns(df):
    """
    Prints the state and year with the highest number of long guns.

    Args:
    df (pd.DataFrame): The input dataframe.
    """
    max_longguns = df[df['long_gun'] == df['long_gun'].max()]
    print("\n3.3. State and year with the highest number of long guns:")
    print(f"Highest number of long guns was in {max_longguns['state'].values[0]} in {max_longguns['year'].values[0]}")


# Exercise 4: Temporal Analysis

# 4.1. Implement a function called time_evolution
def time_evolution(df):
    """
    Plots the time evolution of permits, handguns, and long guns.

    Args:
    df (pd.DataFrame): The input dataframe.
    """
    print("\n4.1. Plotting time evolution of firearm background checks...")
    yearly_data = df.groupby('year').sum().reset_index()
    plt.figure()
    plt.plot(yearly_data['year'], yearly_data['permit'], label='Permits')
    plt.plot(yearly_data['year'], yearly_data['handgun'], label='Handguns')
    plt.plot(yearly_data['year'], yearly_data['long_gun'], label='Long Guns')
    plt.xlabel('Year')
    plt.ylabel('Count')
    plt.legend()
    plt.title('Time Evolution of Firearm Background Checks')
    plt.show()


# Exercise 5: Analysis of the States

# 5.1. Implement a function called groupby_state
def groupby_state(df):
    """
    Groups the dataframe by 'state', summing the numerical columns.

    Args:
    df (pd.DataFrame): The input dataframe.

    Returns:
    pd.DataFrame: The grouped dataframe by state.
    """
    print("\n5.1. Grouping data by 'state'...")
    state_grouped_df = df.groupby('state').sum().reset_index()
    print("First five rows of the state-grouped dataframe:")
    print(state_grouped_df.head())
    return state_grouped_df


# 5.2. Implement a function called clean_states
def clean_states(df):
    """
    Removes specified states from the dataframe.

    Args:
    df (pd.DataFrame): The input dataframe.

    Returns:
    pd.DataFrame: The cleaned dataframe.
    """
    print("\n5.2. Cleaning state data by removing specific states...")
    states_to_remove = ['Guam', 'Mariana Islands', 'Puerto Rico', 'Virgin Islands']
    df = df[~df['state'].isin(states_to_remove)]
    print("Number of unique states after cleaning:")
    print(len(df['state'].unique()))  # Display the number of unique states
    return df


# 5.3. Implement a function called merge_datasets
def merge_datasets(firearm_df, population_df):
    """
    Merges the firearm dataframe with the population dataframe.

    Args:
    firearm_df (pd.DataFrame): The firearm data.
    population_df (pd.DataFrame): The population data.

    Returns:
    pd.DataFrame: The merged dataframe.
    """
    print("\n5.3. Merging firearm and population datasets...")
    merged_df = pd.merge(firearm_df, population_df, on='state')
    print("First five rows of the merged dataframe:")
    print(merged_df.head())  # Display the first 5 rows
    return merged_df


# 5.4. Implement a function called calculate_relative_values
def calculate_relative_values(df):
    """
    Calculates relative values for permits, handguns, and long guns.

    Args:
    df (pd.DataFrame): The input dataframe.

    Returns:
    pd.DataFrame: The dataframe with relative values.
    """
    print("\n5.4. Calculating relative values...")
    df['permit_perc'] = (df['permit'] * 100) / df['pop_2014']
    df['longgun_perc'] = (df['long_gun'] * 100) / df['pop_2014']
    df['handgun_perc'] = (df['handgun'] * 100) / df['pop_2014']
    print("First five rows of the dataframe with relative values:")
    print(df.head())
    return df


# 5.5. Handling Outliers
def handle_outliers(df):
    """
    Adjusts outliers and recalculates averages.

    Args:
    df (pd.DataFrame): The input dataframe.

    Returns:
    pd.DataFrame: The dataframe with adjusted values.
    """
    print("\n5.5. Handling outliers...")
    kentucky_data = df[df['state'] == 'Kentucky']
    avg_permit_perc = round(df['permit_perc'].mean(), 2)
    print(f"Average permit percentage before adjusting Kentucky: {avg_permit_perc}")
    print("Kentucky Data:")
    print(kentucky_data)

    df.loc[df['state'] == 'Kentucky', 'permit_perc'] = avg_permit_perc
    new_avg_permit_perc = round(df['permit_perc'].mean(), 2)
    print(f"New average permit percentage after adjusting Kentucky: {new_avg_permit_perc}")

    print("First five rows after handling outliers:")
    print(df.head())
    return df


# Main execution
if __name__ == "__main__":
    print("Starting data analysis...")

    # Read data
    firearm_data = read_csv('nics-firearm-background-checks.csv')
    population_data = read_csv('us-state-populations.csv')

    # Clean data
    firearm_data_cleaned = clean_csv(firearm_data)
    firearm_data_renamed = rename_col(firearm_data_cleaned)

    # Process data
    firearm_data_broken = breakdown_date(firearm_data_renamed)
    firearm_data_no_month = erase_month(firearm_data_broken)

    # Group data
    firearm_data_grouped = groupby_state_and_year(firearm_data_no_month)

    # Print biggest values
    print_biggest_handguns(firearm_data_grouped)
    print_biggest_longguns(firearm_data_grouped)

    # Temporal analysis
    time_evolution(firearm_data_grouped)

    # Analysis of states
    state_grouped_data = groupby_state(firearm_data_grouped)
    cleaned_state_data = clean_states(state_grouped_data)
    merged_data = merge_datasets(cleaned_state_data, population_data)
    relative_values_data = calculate_relative_values(merged_data)
    outliers_handled_data = handle_outliers(relative_values_data)

    print("Data analysis completed.")
