from data_prep import *

taxi_trip = pd.read_csv('/Users/Tian/3sigma/trip_data_12.csv') # Import taxi_trip data
taxi_trip.columns = [i.strip() for i in taxi_trip.columns]
taxi_trip = taxi_trip.drop(['medallion','hack_license','vendor_id','rate_code','store_and_fwd_flag','passenger_count','trip_time_in_secs'] ,1)
taxi_trip.pickup_datetime = pd.to_datetime(taxi_trip.pickup_datetime)
taxi_trip.dropoff_datetime = pd.to_datetime(taxi_trip.dropoff_datetime)
mon_trip = taxi_trip[taxi_trip.pickup_datetime <= pd.datetime(2013, 12, 3)][taxi_trip.pickup_datetime >= pd.datetime(2013,12,2)] # data from 2013/12/01-2013/12/07
mon_trip.append(taxi_trip[taxi_trip.pickup_datetime <= pd.datetime(2013, 12, 10)][taxi_trip.pickup_datetime >= pd.datetime(2013,12,9)])
mon_trip.append(taxi_trip[taxi_trip.pickup_datetime <= pd.datetime(2013, 12, 10)][taxi_trip.pickup_datetime >= pd.datetime(2013,12,9)])

subway_gps = pd.read_csv('/Users/Tian/3sigma/code/3Sigma/subways.csv')
subway_gps = subway_gps.drop('Unnamed: 0', 1)

sub_dict = {}

for i in range(len(subway_gps)):
    sub_dict[subway_gps.STATION[i]] = [subway_gps.LAT[i], subway_gps.LON[i]]

dict_sub = pd.DataFrame(sub_dict).transpose()
dict_sub.index = [i.strip() for i in dict_sub.index]

for i in range(len(subway_gps)):
    subway_gps.STATION[i] = subway_gps.STATION[i].strip()


def apply_nn(taxi_trip):
    return subway_nearest_neighbor(sub_dict, [taxi_trip.pickup_latitude, taxi_trip.pickup_longitude])

def apply_nnoff(taxi_trip):
    return subway_nearest_neighbor(sub_dict, [taxi_trip.dropoff_latitude, taxi_trip.dropoff_longitude])

def date_groupby(start_date, end_date, taxi_trip, sample_size):
    mask1 = taxi_trip.pickup_datetime >= start_date
    mask2 = taxi_trip.pickup_datetime <= end_date
    trip_day = taxi_trip[mask1][mask2]
    random_sample = np.random.permutation(len(trip_day))[:sample_size]
    return trip_day.iloc[random_sample]

