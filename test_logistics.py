from mylib.logistics import cities, distance_from_cities, print_cities

#estimate the travel time between two cities by car

def travel_time(city1, city2, speed=60):
    """Estimate the travel time between two cities by car"""
    assert distance_from_cities((cities[0][1], cities[1][1])) == 2450.950344683375

def test_print_cities():
    """Test the print_cities function"""
    assert "Dallas" in print_cities()