# This is a converter for shift work.
# The tool was created as I started to travel more internationally and had to keep the same working hours for my original timezone.
# Created by Kristopher Sandoval. Claude and https://www.online-python.com used for testing and iteration. Caveat emptor.

import datetime
import pytz
import re
import sys

class RestartException(Exception):
    """Custom exception to handle program restart."""
    pass

def check_for_restart(input_str):
    """Check if the user wants to restart the program."""
    if input_str.lower() in ['restart', 'r', '/restart']:
        print("\n=== Restarting the program ===\n")
        raise RestartException()
    return input_str

def get_time_input(prompt):
    """Get a time input from the user in HH:MM (24-hour) format."""
    while True:
        time_str = input(prompt)
        
        # Check for restart command
        check_for_restart(time_str)
        
        # Check if the input matches the HH:MM format
        if re.match(r"^\d{1,2}:\d{2}$", time_str):
            try:
                hours, minutes = map(int, time_str.split(':'))
                if 0 <= hours < 24 and 0 <= minutes < 60:
                    return datetime.time(hours, minutes)
                else:
                    print("Invalid time. Hours must be 0-23 and minutes 0-59.")
            except ValueError:
                print("Invalid time format. Please use HH:MM (24-hour format).")
        else:
            print("Invalid time format. Please use HH:MM (24-hour format).")

def get_date_input(prompt="Enter date (YYYY-MM-DD), or press Enter for today: "):
    """Get a date input from the user, defaulting to today."""
    while True:
        date_str = input(prompt)
        
        # Check for restart command
        check_for_restart(date_str)
        
        if not date_str:  # User pressed Enter for today
            return datetime.date.today()
        
        # Check if the input matches the YYYY-MM-DD format
        if re.match(r"^\d{4}-\d{2}-\d{2}$", date_str):
            try:
                year, month, day = map(int, date_str.split('-'))
                return datetime.date(year, month, day)
            except ValueError:
                print("Invalid date. Please check the values and try again.")
        else:
            print("Invalid date format. Please use YYYY-MM-DD.")

def display_popular_cities():
    """Display a list of popular cities for time zone selection."""
    popular_cities = [
        "New York", "Los Angeles", "Chicago", "Toronto", "Mexico City",
        "London", "Paris", "Berlin", "Rome", "Moscow",
        "Dubai", "Mumbai", "New Delhi", "Shanghai", "Beijing", "Tokyo",
        "Sydney", "Melbourne", "Auckland", "Honolulu"
    ]
    
    print("\nPopular cities for time zone selection:")
    for i, city in enumerate(popular_cities, 1):
        print(f"{i}. {city}")
    print("\nYou can enter one of these cities or any other major city.")

def get_timezone_by_city():
    """Get a timezone based on city name input."""
    display_popular_cities()
    
    while True:
        city = input("\nEnter a city name for the target time zone: ").strip()
        
        # Check for restart command
        check_for_restart(city)
        
        # Create a list of all timezone names containing the city (case insensitive)
        matching_timezones = []
        for tz in pytz.all_timezones:
            # Extract just the city name from the timezone
            tz_parts = tz.split('/')
            if len(tz_parts) > 1:
                tz_city = tz_parts[-1].replace('_', ' ')
                if city.lower() in tz_city.lower():
                    matching_timezones.append(tz)
        
        if matching_timezones:
            if len(matching_timezones) > 1:
                print(f"\nMultiple time zones found for '{city}':")
                for i, tz in enumerate(matching_timezones, 1):
                    print(f"{i}. {tz}")
                
                while True:
                    try:
                        selection_str = input("\nSelect a time zone number: ")
                        # Check for restart command
                        check_for_restart(selection_str)
                        
                        selection = int(selection_str)
                        if 1 <= selection <= len(matching_timezones):
                            return pytz.timezone(matching_timezones[selection-1])
                        else:
                            print(f"Please enter a number between 1 and {len(matching_timezones)}")
                    except ValueError:
                        print("Please enter a valid number")
            else:
                return pytz.timezone(matching_timezones[0])
        else:
            # If no match found, try common substitutions
            common_cities = {
                "new york": "America/New_York",
                "los angeles": "America/Los_Angeles",
                "london": "Europe/London",
                "paris": "Europe/Paris",
                "berlin": "Europe/Berlin",
                "tokyo": "Asia/Tokyo",
                "sydney": "Australia/Sydney",
                "beijing": "Asia/Shanghai",
                "dubai": "Asia/Dubai",
                "moscow": "Europe/Moscow",
                "chicago": "America/Chicago",
                "toronto": "America/Toronto",
                "mexico city": "America/Mexico_City",
                "rome": "Europe/Rome",
                "mumbai": "Asia/Kolkata",
                "new delhi": "Asia/Kolkata",
                "shanghai": "Asia/Shanghai",
                "melbourne": "Australia/Melbourne",
                "auckland": "Pacific/Auckland",
                "honolulu": "Pacific/Honolulu"
            }
            
            city_lower = city.lower()
            if city_lower in common_cities:
                return pytz.timezone(common_cities[city_lower])
            
            print(f"No time zone found for '{city}'. Please try another city.")

def get_local_timezone():
    """Get the user's local timezone."""
    print("\nPlease select your local timezone:")
    return get_timezone_by_city()

def main():
    while True:
        try:
            print("=== Work Shift Time Zone Converter ===\n")
            print("Type 'restart' at any prompt to restart the program.\n")
            
            # Get the user's local timezone
            print("First, let's determine your current time zone.")
            local_tz = get_local_timezone()
            print(f"Your local time zone: {local_tz}")
            
            # Get the shift date
            shift_date = get_date_input("\nEnter shift date (YYYY-MM-DD), or press Enter for today: ")
            
            # Get the shift start and end times
            print("\nEnter times in 24-hour format (HH:MM):")
            start_time = get_time_input("Enter shift start time: ")
            end_time = get_time_input("Enter shift end time: ")
            
            # Create datetime objects for the start and end times
            start_dt = datetime.datetime.combine(shift_date, start_time)
            end_dt = datetime.datetime.combine(shift_date, end_time)
            
            # If end time is earlier than start time, assume the shift ends on the next day
            if end_dt < start_dt:
                end_dt += datetime.timedelta(days=1)
            
            # Localize the datetime objects to the local timezone
            local_start = local_tz.localize(start_dt)
            local_end = local_tz.localize(end_dt)
            
            # Get the target timezone
            print("\nNow, let's select the time zone you want to convert to.")
            target_tz = get_timezone_by_city()
            print(f"Target time zone: {target_tz}")
            
            # Convert the times to the target timezone
            target_start = local_start.astimezone(target_tz)
            target_end = local_end.astimezone(target_tz)
            
            # Display the results
            print("\n=== Conversion Results ===")
            print(f"Shift in {local_tz}:")
            print(f"  Start: {local_start.strftime('%Y-%m-%d %H:%M')} ({local_tz})")
            print(f"  End:   {local_end.strftime('%Y-%m-%d %H:%M')} ({local_tz})")
            print(f"\nShift converted to {target_tz}:")
            print(f"  Start: {target_start.strftime('%Y-%m-%d %H:%M')} ({target_tz})")
            print(f"  End:   {target_end.strftime('%Y-%m-%d %H:%M')} ({target_tz})")
            
            # Show the duration of the shift
            duration = end_dt - start_dt
            hours, remainder = divmod(duration.seconds, 3600)
            minutes = remainder // 60
            print(f"\nShift duration: {hours} hours and {minutes} minutes")
            
            # Ask if the user wants to perform another conversion
            while True:
                another = input("\nDo you want to perform another conversion? (yes/no): ").lower()
                check_for_restart(another)
                if another in ['yes', 'y']:
                    print("\n" + "="*50 + "\n")
                    break
                elif another in ['no', 'n']:
                    print("\nThank you for using the Shift Time Converter!")
                    return
                else:
                    print("Please enter 'yes' or 'no'.")
        
        except RestartException:
            # The program will restart from the beginning
            continue
        except KeyboardInterrupt:
            print("\n\nProgram terminated by user.")
            sys.exit(0)
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            print("The program will restart. If this keeps happening, please check your inputs.")
            continue

if __name__ == "__main__":
    main()
