import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Get user input for city (chicago, new york city, washington).
    while True:
        try:
            city = input("Would you like to see data for chicago, new york city or washington? \n").lower()
            if city == "chicago" or city == "new york city" or city == "washington":
                break;
            else:
                print("city should either be chigago,new york city or washington")
        except:
            continue
 
    # Get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("Would you like to filter by month? enter month \n").lower()
            if month == "all"or month == "january"or month == "february"or month == "march"or month == "april"or month == "may"or month ==                           "june":
                break;
            else:
                print("month should either be all,january,february,march,april,may or june")
        except:
            continue
       
    # Get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("Would you like to filter by day of week? enter day \n").lower()
            if day == "all"or day == "monday"or day == "tuesday"or day == "wednesday"or day == "thursday"or day == "friday"or day == "saturday"or day == "sunday":
                break;
            else:
                print("day should either be all,monday,tuesday,wednesday,thursday,friday,saturday or sunday")
        except:
            continue
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    # Display 5 rows of raw data
    view_data = input('\nWould you like to view 5 rows of raw data? Enter yes or no\n').lower()
    start_loc = 0
    while True:
        if view_data == "yes":
            print(df.iloc[start_loc:start_loc + 5])
            start_loc += 5
        view_display = input("Do you wish to continue?: Enter yes or no\n").lower()
        if view_display != "yes":
            break
# convert the Start Time column to datetime 
    df['Start Time'] = pd.to_datetime(df['Start Time']) 
# extract month and day of week from Start Time to create new columns 
    df['month'] = df['Start Time'].dt.month 
    df['day_of_week'] = df['Start Time'].dt.weekday_name 
    # filter by month if applicable 
    if month != 'all': 
        # use the index of the months list to get the corresponding int 
        months = ['january', 'february', 'march', 'april', 'may', 'june'] 
        month = months.index(month) + 1 
        # filter by month to create the new dataframe 
        df = df[df['month'] == month] 
        # filter by day of week if applicable 
    if day != 'all': 
        # filter by day of week to create the new dataframe 
        df = df[df['day_of_week'] == day.title()] 

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month of Travel is:', most_common_month)
    # Display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of week of Travel is:', most_common_day_of_week)
    # Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print('The most common start hour of Travel is:', most_common_start_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    most_commonly_used_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is:', most_commonly_used_start_station)

    # Display most commonly used end station
    most_commonly_used_end_station = df['End Station'].mode()[0]
    print('The most common used end station is:', most_commonly_used_end_station)

    # Display most frequent combination of start station and end station trip
    most_frequent_combination_of_start_and_end_station = df['Start Station' and 'End Station'].mode()[0]
    print('The most frequent combination of start station and end station is:', most_frequent_combination_of_start_and_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is:', total_travel_time)

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print('What is the breakdown of user type?\n', counts_of_user_types)

    # Display counts of gender
    if "Gender" in df.columns:
        counts_of_gender = df['Gender'].value_counts()
        print('What is the breakdown of gender?\n', counts_of_gender)
    else:
        print('No data for Gender')

    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        earliest_year_of_birth = df['Birth Year'].min()
        print('The earliest year of birth is:', earliest_year_of_birth)
        most_recent_year_of_birth = df['Birth Year'].max()
        print('The most recent year of birth is:', most_recent_year_of_birth)
        most_common_year_of_birth = df['Birth Year'].mode()
        print('The most common year of birth is:', most_common_year_of_birth)
    else:
        print('No data for Birth Year')
            
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
