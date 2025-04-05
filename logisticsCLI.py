from mylib.logistics import distance_between_cities, find_coordinates, calc_total_distance
import click

#build a click group
@click.group()
def cli():
    """Logistics tool"""

#create a list of cities with coordinates

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

@cli.command("total-distance")
def total_distance():
    """Calculate the total distance between two points"""
    total_distance = calc_total_distance(cities)
    click.echo(f"Total distance: {total_distance} miles")


def print_cities():
    """Print the list of cities"""
    for city in cities:
        print("Hiya")
        #click.echo(city[0])
        #print(city[0])

#print_cities()

