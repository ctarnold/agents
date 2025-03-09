# https://www.geeksforgeeks.org/python-read-csv-using-pandas-read_csv/
# https://remarkablemark.org/blog/2020/08/26/python-iterate-csv-rows/
import pandas as pd

path = r"C:\Users\chris\OneDrive\Desktop\SeniorThesisCode\travelplanner\validation.csv"
# Forms of 1, 2, and 3 cities
# 1 city, len(line) = 9
# 2 city, len(line) = 15
# 3 city, len(line) = 21
# Need to see what form the prompt is in to extract the data

""""
CITY 1
ATTRACTIONS
RESTAURANTS
ACCOMODATIONS

FLIGHT ORG TO DEST
SELF-DRIVING ORG TO DEST
TAXI ORG TO DEST

FLIGHT DEST TO ORG
SELF DRIVING DEST TO ORG
TAXI DEST TO ORG
"""

""""
CITY 1
ATTRACTIONS
RESTAURANTS
ACCOMODATIONS

CITY 2
ATTRACTIONS
RESTAURANTS
ACCOMODATIONS

CITY 1
FLIGHT
SELF-DRIVING
TAXI

CITY 1 TO CITY 2
FLIGHT
SELF DRIVING
TAXI

CITY 2 TO ORG
FLIGHT
SELF DRIVING
TAXI

"""


""""
CITY 1

ATTRACTIONS
RESTAURANTS
ACCOMODATIONS

CITY 2

ATTRACTIONS
RESTAURANTS
ACCOMODATIONS

CITY 3

ATTRACTIONS
RESTAURANTS
ACCOMODATIONS

ORG TO CITY 1

FLIGHT
DRIVE
TAXI

CITY 1 TO 2

FLIGHT
DRIVE 
TAXI

CITY 2 TO 3

FLIGHT
DRIVE 
TAXI

CITY 3 TO ORG

FLIGHT
DRIVE
TAXI

"""


df = pd.read_csv(path)
for index, row in df.iterrows():
    if index == 50:
        line = eval(row['reference_information'])
        print(len(line))
        print(type(line))
        for item in line:
            print(item['Description'])

def get_raw_data():
    """"
    TODO
    """

def get_flights_case_1():
    """
    This tool returns flights for a one city trip. Before
    calling this function, validate that you are making a one city
    trip.

    Args:
        TODO
    Returns:
        A string of information containing flight data

    """
    return 