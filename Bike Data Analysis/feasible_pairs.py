import pandas as pd


def trip_analysis(data):
    # start = time.time()  # record start time

    # convert the time columns to datetime objects
    data['start'] = pd.to_datetime(data['started_at'], format='%d-%m-%Y %H:%M')
    data['end'] = pd.to_datetime(data['ended_at'], format='%d-%m-%Y %H:%M')

    data['start'] = data['start'].dt.strftime('%H:%M')
    data['end'] = data['end'].dt.strftime('%H:%M')

    # Filtering the data
    data = data[(data['start'] >= '06:00') & (data['start'] <= '18:00')]

    # print FEASIBLE PAIRS
    
    starting_lat = list(data['start_lat'])
    starting_long = list(data['start_lng'])
    ending_lat = list(data['end_lat'])
    ending_long = list(data['end_lng'])
    trip_no = list(data['trip_id'])

    feasible_count = 0
    for lat in ending_lat:
        for i in range(len(starting_lat)):
            if lat == starting_lat[i] and ending_long[ending_lat.index(lat)] == starting_long[i] and ending_lat.index(lat) < i and \
                    trip_no[ending_lat.index(lat)] != trip_no[i]:
                feasible_count += 1
    print(f" Feasible pairs: {feasible_count}")


bikes = pd.read_csv('bike_data_new.csv')
trip_analysis(bikes)
