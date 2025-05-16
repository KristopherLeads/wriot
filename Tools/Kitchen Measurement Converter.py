# This is a converter for kitchen measurements.
# The following tool was created for a specific edge case: I only had a 1/4 Tsp measurement, and I needed to measure out 1 Cup + 1/4 Tbsp.
# And yes, my scale was dead, otherwise I'd have done this by weight.
# Created by Kristopher Sandoval. Claude and https://www.online-python.com used for testing and iteration. Caveat emptor.

#!/usr/bin/env python3

import re
from fractions import Fraction

# Standard conversion rates
CONVERSIONS = {
    'cup': {'cup': 1, 'tbsp': 16, 'tsp': 48},
    'tbsp': {'cup': 1/16, 'tbsp': 1, 'tsp': 3},
    'tsp': {'cup': 1/48, 'tbsp': 1/3, 'tsp': 1}
}

def parse_measurement(input_str):
    """Parse a measurement string into quantity and unit."""
    input_str = input_str.strip().lower()
    
    # Match patterns like "1/2 cup", "2.5 tbsp", "3 tsp"
    pattern = r'^([\d./]+)\s*(cup|cups|tbsp|tablespoon|tablespoons|tsp|teaspoon|teaspoons)$'
    match = re.match(pattern, input_str)
    
    if not match:
        return None, None
    
    quantity_str, unit = match.groups()
    
    # Convert unit aliases to standard form
    if unit in ['cups', 'cup']:
        unit = 'cup'
    elif unit in ['tbsp', 'tablespoon', 'tablespoons']:
        unit = 'tbsp'
    elif unit in ['tsp', 'teaspoon', 'teaspoons']:
        unit = 'tsp'
    
    # Convert the quantity to a float
    try:
        if '/' in quantity_str:
            if ' ' in quantity_str:  # Handle mixed fractions like "1 1/2"
                whole, frac = quantity_str.split(' ', 1)
                quantity = float(whole) + float(Fraction(frac))
            else:
                quantity = float(Fraction(quantity_str))
        else:
            quantity = float(quantity_str)
    except ValueError:
        return None, None
    
    return quantity, unit

def convert_measurement(from_quantity, from_unit, to_unit):
    """Convert a measurement from one unit to another."""
    if from_unit not in CONVERSIONS or to_unit not in CONVERSIONS:
        return None
    
    # Calculate the equivalent in the base unit (tsp)
    base_amount = from_quantity * CONVERSIONS[from_unit]['tsp']
    
    # Convert from base unit to target unit
    to_quantity = base_amount / CONVERSIONS[to_unit]['tsp']
    
    return to_quantity

def format_output(quantity):
    """Format the quantity for display, using fractions for common values."""
    if quantity == int(quantity):
        return str(int(quantity))
    
    # Try to represent as a simple fraction
    fraction = Fraction(quantity).limit_denominator(16)
    if fraction.numerator == 0:
        return "0"
    elif fraction.denominator == 1:
        return str(fraction.numerator)
    elif quantity > 1:
        whole = int(quantity)
        frac = Fraction(quantity - whole).limit_denominator(16)
        if frac.numerator == 0:
            return str(whole)
        return f"{whole} {frac.numerator}/{frac.denominator}"
    else:
        return f"{fraction.numerator}/{fraction.denominator}"

def display_conversions(from_quantity, from_unit):
    """Display all possible conversions for a given measurement."""
    print(f"\nConversions for {format_output(from_quantity)} {from_unit}:")
    print("-" * 40)
    
    for to_unit in CONVERSIONS:
        if to_unit == from_unit:
            continue
        
        to_quantity = convert_measurement(from_quantity, from_unit, to_unit)
        formatted_quantity = format_output(to_quantity)
        print(f"{formatted_quantity} {to_unit}")

def custom_measurement_conversion(from_quantity, from_unit, to_quantity, to_unit):
    """Calculate how many of a specific measure equals another specific measure."""
    # Convert both to a common unit (tsp)
    from_in_tsp = from_quantity * CONVERSIONS[from_unit]['tsp']
    to_in_tsp = to_quantity * CONVERSIONS[to_unit]['tsp']
    
    # Calculate the ratio
    ratio = from_in_tsp / to_in_tsp
    
    return ratio

def main():
    print("Kitchen Measurement Converter")
    print("=" * 40)
    print("This tool converts between common kitchen measurements.")
    print("You can: ")
    print("1. Convert a measurement to all other units")
    print("2. Calculate how many of one measure equals another")
    
    while True:
        print("\nChoose an option:")
        print("1. Convert a measurement to all equivalents")
        print("2. Calculate specific measurement conversion")
        print("3. Quit")
        
        choice = input("> ")
        
        if choice == "1":
            measurement = input("\nEnter a measurement (e.g., '2 tbsp', '1/4 cup'): ")
            quantity, unit = parse_measurement(measurement)
            
            if quantity is None or unit is None:
                print("Invalid input. Please try again.")
                continue
            
            display_conversions(quantity, unit)
            
        elif choice == "2":
            print("\nYou have a recipe that calls for:")
            measure1 = input("Enter measurement needed (e.g., '2 tbsp'): ")
            from_quantity, from_unit = parse_measurement(measure1)
            
            if from_quantity is None or from_unit is None:
                print("Invalid input. Please try again.")
                continue
            
            print("\nBut you only have:")
            measure2 = input("Enter your available measuring tool (e.g., '1/3 tsp'): ")
            to_quantity, to_unit = parse_measurement(measure2)
            
            if to_quantity is None or to_unit is None:
                print("Invalid input. Please try again.")
                continue
            
            ratio = custom_measurement_conversion(from_quantity, from_unit, to_quantity, to_unit)
            
            print(f"\nResult: You need {format_output(ratio)} of your {format_output(to_quantity)} {to_unit} measure(s)")
            
        elif choice == "3":
            print("\nThank you for using the Kitchen Measurement Converter!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
