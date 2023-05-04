import pandas as pd
import time


def trip_analysis(data):
    start = time.time()  # record start time

    # convert the time columns to datetime objects
    data['start'] = pd.to_datetime(data['started_at'], format='%d-%m-%Y %H:%M')
    data['end'] = pd.to_datetime(data['ended_at'], format='%d-%m-%Y %H:%M')

    # calculate the travel time for each bike
    data['duration'] = data['end'] - data['start']

    # calculate the travel time in minutes
    data['duration_minutes'] = data['duration'].dt.total_seconds() / 60.0

    # filter out trips of duration 0 minutes
    data = data[data['duration_minutes'] != 0]

    # calculate the statistics on the remaining trips
    max_dur = data['duration_minutes'].max()
    min_dur = data['duration_minutes'].min()
    num_min_dur_trips = len(data[data['duration_minutes'] == min_dur])

    # print the statistics
    print(f"Max duration: {max_dur} minutes")
    print(f"Min duration: {min_dur} minutes")
    print(f"Number of trips with min duration: {num_min_dur_trips}")

    # Filter the DataFrame to include only circular trips
    circular = data[(data['start_lat'] == data['end_lat']) & (data['start_lng'] == data['end_lng'])]

    # Calculate the percentage of total circular trips
    total_trips = len(data)
    total_circular = len(circular)
    print(total_circular)
    percentage_circular = total_circular / total_trips * 100

    # Print the percentage of total circular trips
    print(f"Percentage of total circular trips: {percentage_circular:.2f}%")

    # calculate and print the runtime
    end = time.time()
    runtime = end - start
    print(f"runtime: {runtime} secs")


bike = pd.read_csv('bike_data_new.csv')
trip_analysis(bike)
