from data_prep import *

taxi_trip = pd.read_csv('/Users/Tian/3sigma/trip_data_12.csv') # Import taxi_trip data
taxi_trip.columns = [i.strip() for i in taxi_trip.columns]
taxi_trip = taxi_trip.drop(['medallion','hack_license','vendor_id','rate_code','store_and_fwd_flag','passenger_count','trip_time_in_secs'] ,1)

subway_gps = pd.read_csv('/Users/Tian/3sigma/code/3Sigma/subways.csv')

for i in range(len(subway_gps)):
    subway_gps.STATION[i] = subway_gps.STATION[i].strip()

sub_dict = {}

for i in range(len(subway_gps)):
    sub_dict[subway_gps.STATION[i]] = [subway_gps.LAT[i], subway_gps.LON[i]]


def apply_nn(taxi_trip):
    return subway_nearest_neighbor(sub_dict, [taxi_trip.pickup_latitude, taxi_trip.pickup_longitude])
