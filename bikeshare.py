import time
import pandas as pd
import numpy as np

# put the csv files in dictionary to create dataFrame from it
CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello, Let's explore some US bikeshare data!")
    # TO DO: get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    invalid_input = "No... No... No... This is invalid input"

    while True:
        city = input("Enter the city you want to explore the data about it? (Chicago, New York city, Washington)").lower()
        if city in ["chicago", "new york city", "washington"]:
            break
        else:
            print(f"{invalid_input}, Please enter a name of city from them: (Chicago, New York city, Washington)")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Enter the month -From the first six month- you want view it\'s data?... type "all" if you want '
                      'data for all exist month').lower()
        if month in ["all", "january", "february", "march", "april", "may", "june"]:
            break
        else:
            print(f"{invalid_input}, Please select a month from this list: (January, February, March, April, "
                  f"May, June or All))")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter the day which you want data about? ... type "all" if you want the full week').lower()
        if day in ["all", "saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]:
            break
        else:
            print(f"{invalid_input}, Please select a day of the week or type all if you want thr full week")

    print('-'*40)
    return city, month, day


def load_data(city: str, month: str, day: str) -> pd.DataFrame:
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data of the city into a dataframe.
    df = pd.read_csv(CITY_DATA[city])

    # Create datetime from the Start Time.
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # create columns for month and day.
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name

    # filter by month.
    if month != 'all':
        month = ['january', 'february', 'march', 'april', 'may', 'june']
        month = month.index(month) + 1

        # create new dataframe by the selected month.
        df = df[df['month'] == month]

    # filter by day of week.
    if day != 'all':
        # create new dataframe... when the user didn't want all day of week.
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df) -> None:
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    # -----df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print(f'The common month is {common_month}')

    # TO DO: display the most common day of week
    # ----df['day_of_week'] = df['Start Time'].dt.day_name
    common_day = df['day_of_week'].mode()[0]
    print(f'The common day is {common_day}')

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print(f'The common start hour is {common_start_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df) -> None:
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f'The most common start station is {common_start_station}')

    # TO DO: display most commonly used end station
    common_end_station = df["End Station"].mode()[0]
    print(f"The most common end station is {common_end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " " + df['End Station']
    most_frequent_station = df['combination']
    print(most_frequent_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"The total travel time = {total_travel_time}")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f'The average travel time = {mean_travel_time}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df) -> None:
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    number_user_types = df['User Type'].value_counts()
    print(f"The number of user types = {number_user_types}")

    # TO DO: Display counts of gender
    # Because Washington didn't have data about 'Gender'... so we will handle the input to avoid error:
    try:
        number_gender = df['Gender'].value_counts()
        print(f"The number of gender of the user = {number_gender}")
    except:
        print("Washington city didn't have data about gender")

    # TO DO: Display earliest, most recent, and most common year of birth
    # We will handle the data here also... for washington:
    try:
        earliest_year_of_birth = int(df['Birth Year'].min())
        print(f"The earliest year of birth is: {earliest_year_of_birth}")

        most_recent_year_of_birth = int(df['Birth Year'].max())
        print(f"The earliest year of birth is: {most_recent_year_of_birth}")

        most_common_year_of_birth = int(df['Birth Year'].mode()[0])
        print(f"The earliest year of birth is: {most_common_year_of_birth}")
    except:
        print("Washington city didn't have Birth Year data")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
