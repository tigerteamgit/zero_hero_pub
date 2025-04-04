#!/usr/bin/env python3

from mylib.calc import add, sub, mul, div, pow
import click

@click.group()
def cli():
    """A simple calculator CLI"""

@cli.command("add")
@click.argument('x', type=float)
@click.argument('y', type=float)
def add_cmd(x, y):
    """Add two numbers

    Example:
    ./calCLI.py add 1 2
    """

    #Use colored output to print the result
    click.echo(f"{x} + {y} = {add(x, y)}")

@cli.command("sub")
@click.argument('x', type=float)
@click.argument('y', type=float)
def sub_cmd(x, y):
    """Subtract two numbers

    Example:
    ./calCLI.py sub 2 1
    """
    click.echo(f"{x} - {y} = {sub(x, y)}")

@cli.command("mul")
@click.argument('x', type=float)
@click.argument('y', type=float)
def mul_cmd(x, y):
    """Multiply two numbers

    Example:
    ./calCLI.py mul 2 3
    """
    click.echo(f"{x} * {y} = {mul(x, y)}")

@cli.command("div")
@click.argument('x', type=float)
@click.argument('y', type=float)
def div_cmd(x, y):
    """Divide two numbers

    Example:
    ./calCLI.py div 6 3
    """
    click.echo(f"{x} / {y} = {div(x, y)}")

@cli.command("pow")
@click.argument('x', type=float)
@click.argument('y', type=float)
def power_cmd(x, y):
    """Calculate the power of a number

    Example:
    ./calCLI.py power 2 3
    """
    click.echo(f"{x} ^ {y} = {pow(x, y)}")

if __name__ == "__main__":
    cli()

