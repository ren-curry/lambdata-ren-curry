"""This contains the functions for Module 1 assignment. A number of basic helper functions to practice on."""

def null_count(df):
    """Check a dataframe for nulls and return the number of missing values."""
    return df.isnull().sum().sum()

def train_test_split(df, frac):
    """A Train/Test split function for a dataframe that returns both the Training and Testing sets. Frac refers to the percent of data you would like to set aside for Training."""
    df = df.copy()

    # Retrieve the length of the dataframe and calculate the length of the 'frac' for Training data (train_length)
    df_length =  len(df)
    train_length = round(df_length * frac, 0)

    # Split the dataframe into Train and Test based on the train_length
    df_train = df.iloc[:train_length]
    df_test = df.iloc[train_length:]

    return df_train, df_test

def randomize(df):
    """Randomization function that randomizes all of a dataframes cells then returns that randomized dataframe."""
    # TODO - Implement
    return 'randomize'

def addy_split(add_series): 
    """Splits addresses into three columns (df['city'], df['state'], and df['zip'])"""
    # TODO - Implement
    return 'addy_split'

def abbr_2_st(state_series, abbr_2_state=True):
    """Return a new column with the full name from a State abbreviation column -> An input of FL would return Florida. 
    This function should also take a boolean (abbr_2_state) and when False takes full state names and return state abbreviations. 
    -> An input of Florida would return Fl.
    """
    # TODO - Implement
    return 'abbr_2_st'

def list_2_series(list_2_series, df):
    """Single function to take a list and dataframe then turn the list into a series and add it to the inputted dataframe as a new column."""
    # TODO - Implement
    return 'list_2_series'

def rm_outlier(df):
    """A 1.5*Interquartile range outlier detection/removal function that gets rid of outlying rows and returns that outlier cleaned dataframe."""
    # TODO - Implement
    return 'rm_outlier'

def split_dates(date_series):
    """Function to split dates of format "MM/DD/YYYY" into multiple columns (df['month'], df['day'], df['year']) 
    and then return the same dataframe with those additional columns.
    """
    # TODO - Implement
    return 'split_dates'