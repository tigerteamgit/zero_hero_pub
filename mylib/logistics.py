"""

THis module deals with logistics and calculates distances between two points

"""

from geopy import distance

CITIES = (
    ("Newport", (41.49008, -71.312796)),
    ("Cleveland", (41.499498, -81.695391)),
    ("Seattle", (47.6062, -122.3321)),
    ("San Francisco", (37.7749, -122.4194)),
    ("Los Angeles", (34.0522, -118.2437)),
    ("Chicago", (41.8781, -87.6298)),
    ("Boston", (42.3601, -71.0589)),
    ("Miami", (25.7617, -80.1918)),
    ("Houston", (29.7604, -95.3698)),
    ("Dallas", (32.7767, -96.7970)),
    ("Denver", (39.7392, -104.9903)),
    ("Phoenix", (33.4484, -112.0740)),
    ("Atlanta", (33.7490, -84.3880)),
    ("Philadelphia", (39.9526, -75.1652)),
    ("Washington", (38.9072, -77.0369)),
    ("New York", (40.7128, -74.0060)),
    ("Boston", (42.3601, -71.0589)),
    ("Baltimore", (39.2904, -76.6122)),
    ("Charlotte", (35.2271, -80.8431)),
    ("Orlando", (28.5383, -81.3792)),
    ("Tampa", (27.9506, -82.4572)),
    ("San Diego", (32.7157, -117.1611)),
    ("Portland", (45.5155, -122.6793)),
    ("Las Vegas", (36.1699, -115.1398)),
    ("Salt Lake City", (40.7608, -111.8910)),
    ("Kansas City", (39.0997, -94.5786)),
    ("St. Louis", (38.6270, -90.1994)),
)


# build a function to calculate the distance between two points
def calc_distance(point1, point2):
    """Calculate the distance between two points"""
    return distance.distance(point1, point2).miles


# build a function that finds the coordinates of a city
def find_coordinates(city):
    """Find the coordinates of a city"""
    return city.latitude, city.longitude


# calculate the total distance between a list of cities
def distance_between_two_points(point1, point2):
    """Calculate the total distance between two cities"""
    return distance.distance(point1, point2).miles


# return the tuple of a city
def get_coordinates(city):
    """Get the tuple of a city"""
    for city_name, coordinates in CITIES:
        if city_name == city:
            return coordinates


# print cities
def cities_list():
    """Peturn the list of cities"""

    return [city[0] for city in CITIES]


# print(distance_from_cities(cities[0]))
