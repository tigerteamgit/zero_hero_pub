from mylib.logistics import distance_between_two_points, get_coordinates, cities_list
import click


# build a click group
@click.group()
def cli():
    """Logistics tool"""


@cli.command("cities")
def list_cities():
    """List all cities"""
    click.echo("List of cities:")
    for city in cities_list():
        click.echo(city[0])


@cli.command("distance")
@click.argument("city1")
@click.argument("city2")
def distance(city1, city2):
    """Calculate the distance between two cities"""

    click.echo(click.style(f"Distance between two cities", fg="green"))
    click.echo(
        f"Distance between {city1} and {city2}: {get_coordinates((city1, city2))} miles"
    )


# invoke the click command
if __name__ == "__main__":
    cli()


# estimate the travel time between two cities by car


def travel_time(city1, city2, speed=60):
    """Estimate the travel time between two cities by car"""
    assert (
        distance_between_two_points((cities_list[0][1], cities_list[1][1]))
        == 2450.950344683375
    )


def test_print_cities():
    """Test the print_cities function"""
    assert "Dallas" in cities_list()
