import numpy as np
import pandas as pd

# load the dataset
cities = pd.read_csv('data/cities.csv')
providers = pd.read_csv('data/providers.csv')
stations = pd.read_csv('data/stations.csv')
ticket_data = pd.read_csv('data/ticket_data.csv')

dataset = {'cities': cities, 'providers': providers, 'stations': stations, 'ticket_data': ticket_data}

print('_________________________________________________________')
print('Price statistics')
print('_________________________________________________________')
print('number of NAN values in price_in_cents =', ticket_data['price_in_cents'].isna().sum())
print('min price =', round(ticket_data['price_in_cents'].min()/100, 2), '€')
print('max price =', round(ticket_data['price_in_cents'].max()/100, 2), '€')
print('median price =', round(ticket_data['price_in_cents'].median()/100, 2), '€')
print('mean price =', round(ticket_data['price_in_cents'].mean()/100, 2), '€')
print('most trips have a price =', round(ticket_data['price_in_cents'].value_counts().idxmax()/100, 2), '€')
print('_________________________________________________________')

print('_________________________________________________________')
print('Duration statistics')
print('_________________________________________________________')
print('number of NAN values in departure_ts =', ticket_data['departure_ts'].isna().sum())
print('number of NAN values in arrival_ts =', ticket_data['arrival_ts'].isna().sum())
# add duration column in hours
fmt = '%Y-%m-%d %H:%M:%S+%f'
ticket_data['departure_ts'] = pd.to_datetime(ticket_data['departure_ts'], format=fmt)
ticket_data['arrival_ts'] = pd.to_datetime(ticket_data['arrival_ts'], format=fmt)
ticket_data['duration'] = ticket_data['arrival_ts'] - ticket_data['departure_ts']
ticket_data['duration'] = round(ticket_data['duration'].dt.seconds / 3600, 2)

print('min duration =', round(ticket_data['duration'].min(), 2), 'hours')
print('max duration =', round(ticket_data['duration'].max(), 2), 'hours')
print('median duration =', round(ticket_data['duration'].median(), 2), 'hours')
print('mean duration =', round(ticket_data['duration'].mean(), 2), 'hours')
print('most trips have a duration =', round(ticket_data['duration'].value_counts().idxmax(), 2), 'hours')
print('_________________________________________________________')

from modules.Geo import Geo
from modules.Manager import Manager

print(Manager.transportTypesOfTicket(6795025, ticket_data, providers))
print(Geo.getLatLongStation(2, stations))
print(Geo.distanceOfTicket(6795027, ticket_data, stations), 'km')

# print(ticket_data.head())
# fill NAN values with the mode (value with max occurences)
ticket_data['price_in_cents'] = ticket_data['price_in_cents'].fillna(ticket_data['price_in_cents'].value_counts().idxmax())
# for d in dataset.values():
#     for c in d.columns:
#         d[c] = d[c].fillna(d[c].value_counts().idxmax())
# print(ticket_data.head())