"""

THis module deals with logistics and calculates distances between two points

"""

from geopy import distance

newport_ri = (41.49008, -71.312796)
cleveland_oh = (41.499498, -81.695391)
print(distance.distance(newport_ri, cleveland_oh).miles)

cities = (
    ("Newport, RI", (41.49008, -71.312796)),
    ("Cleveland, OH", (41.499498, -81.695391)),
    ("Seattle, WA", (47.6062, -122.3321)),
    ("San Francisco, CA", (37.7749, -122.4194)),
    ("Los Angeles, CA", (34.0522, -118.2437)),
    ("Chicago, IL", (41.8781, -87.6298)),
    ("Boston, MA", (42.3601, -71.0589)),
    ("Miami, FL", (25.7617, -80.1918)),
    ("Houston, TX", (29.7604, -95.3698)),
    ("Dallas, TX", (32.7767, -96.7970)),
    ("Denver, CO", (39.7392, -104.9903)),
    ("Phoenix, AZ", (33.4484, -112.0740)),
    ("Atlanta, GA", (33.7490, -84.3880)),
    ("Philadelphia, PA", (39.9526, -75.1652)),
    ("Washington, DC", (38.9072, -77.0369)),
    ("New York, NY", (40.7128, -74.0060)),
    ("Boston, MA", (42.3601, -71.0589)),
    ("Baltimore, MD", (39.2904, -76.6122)),
    ("Charlotte, NC", (35.2271, -80.8431)),
    ("Orlando, FL", (28.5383, -81.3792)),
    ("Tampa, FL", (27.9506, -82.4572)),
    ("San Diego, CA", (32.7157, -117.1611)),
    ("Portland, OR", (45.5155, -122.6793)),
    ("Las Vegas, NV", (36.1699, -115.1398)),
    ("Salt Lake City, UT", (40.7608, -111.8910)),
    ("Kansas City, MO", (39.0997, -94.5786)),
    ("St. Louis, MO", (38.6270, -90.1994)),
)

#build a function to calculate the distance between two points
def calc_distance(point1, point2):
    """Calculate the distance between two points"""
    return distance.distance(point1, point2).miles

#build a function that finds the coordinates of a city
def find_coordinates(city):
    """Find the coordinates of a city"""
    return city.latitude, city.longitude

#calculate the total distance between a list of cities
def distance_from_cities(cities):
    """Calculate the total distance between two cities"""
    return distance.distance(cities[0][1], cities[1][1]).miles
   
#print cities
def print_cities():
    """Print the list of cities"""
    for city in cities:
        print(city[0])
    return [city[0] for city in cities]

print(distance_from_cities(cities[0]))