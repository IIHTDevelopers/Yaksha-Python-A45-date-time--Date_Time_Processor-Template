"""
Date and Time Processor - Working with Python's datetime Module

This program demonstrates essential date and time processing capabilities using Python's
datetime module to manage scheduling operations for healthcare applications.
"""

import datetime
from datetime import timedelta, timezone

def convert_string_to_datetime(date_string):
    """
    Convert a string date to a datetime object.
    
    Parameters:
    date_string (str): Date string in format 'YYYY-MM-DD' or 'YYYY-MM-DD HH:MM:SS'
    
    Returns:
    datetime: Datetime object representing the input date
    
    Example:
    >>> convert_string_to_datetime("2025-03-19")
    datetime.datetime(2025, 3, 19, 0, 0)
    >>> convert_string_to_datetime("2025-03-19 14:30:00")
    datetime.datetime(2025, 3, 19, 14, 30)
    """
    # TODO: Implement this function
    # Hint: Use datetime.strptime() with appropriate format strings
    # Remember to validate input type and handle format variations
    pass

def format_datetime(dt, format_string="%Y-%m-%d %H:%M:%S"):
    """
    Format a datetime object to a specified string pattern.
    
    Parameters:
    dt (datetime): Datetime object to format
    format_string (str): Format pattern (default: "%Y-%m-%d %H:%M:%S")
    
    Returns:
    str: Formatted date string
    
    Example:
    >>> format_datetime(datetime.datetime(2025, 3, 19, 14, 30), "%B %d, %Y at %I:%M %p")
    'March 19, 2025 at 02:30 PM'
    """
    # TODO: Implement this function
    # Hint: Validate input type and use datetime.strftime() with the provided format string
    pass

def calculate_date_difference(start_date, end_date):
    """
    Calculate the difference between two dates.
    
    Parameters:
    start_date (datetime or str): Start date (datetime object or string)
    end_date (datetime or str): End date (datetime object or string)
    
    Returns:
    dict: Dictionary with time difference in days, hours, minutes and total_seconds
    
    Example:
    >>> calculate_date_difference("2025-03-19", "2025-03-26")
    {'days': 7, 'hours': 168, 'minutes': 10080, 'total_seconds': 604800}
    """
    # TODO: Implement this function
    # Hint: Convert string inputs to datetime objects if needed, then calculate difference
    # Return a dictionary with different time units
    pass

def add_time_duration(dt, days=0, hours=0, minutes=0):
    """
    Add a specified time duration to a datetime.
    
    Parameters:
    dt (datetime or str): Original datetime
    days (int): Number of days to add
    hours (int): Number of hours to add
    minutes (int): Number of minutes to add
    
    Returns:
    datetime: New datetime with duration added
    
    Example:
    >>> add_time_duration(datetime.datetime(2025, 3, 19), days=2, hours=5)
    datetime.datetime(2025, 3, 21, 5, 0)
    """
    # TODO: Implement this function
    # Hint: Convert string input to datetime if needed
    # Validate input types and use timedelta to create a duration
    pass

def get_day_of_week(date_string):
    """
    Get the weekday name for a given date.
    
    Parameters:
    date_string (str or datetime): Date to find day of week
    
    Returns:
    str: Name of the weekday (e.g., 'Monday', 'Tuesday')
    
    Example:
    >>> get_day_of_week("2025-03-19")
    'Wednesday'
    """
    # TODO: Implement this function
    # Hint: Convert input to datetime if needed, then use strftime with %A format
    pass

def convert_timezone(dt, source_offset, target_offset):
    """
    Convert a datetime from one timezone offset to another.
    
    Parameters:
    dt (datetime or str): Datetime to convert
    source_offset (int): Source timezone offset in hours (-12 to +14)
    target_offset (int): Target timezone offset in hours (-12 to +14)
    
    Returns:
    datetime: Datetime adjusted to target timezone
    
    Example:
    >>> convert_timezone("2025-03-19 14:30:00", -5, -8)  # Eastern to Pacific
    datetime.datetime(2025, 3, 19, 11, 30)
    """
    # TODO: Implement this function
    # Hint: Validate input types and timezone offset ranges
    # Calculate time difference between timezones and add it to the datetime
    pass

def main():
    """
    Main function to demonstrate the functionality of the Date and Time Processor.
    """
    print("===== DATE AND TIME PROCESSOR =====")
    
    # Sample date and time data
    appointment_date = "2025-03-19 14:30:00"
    surgery_date = "2025-04-02 09:00:00"
    staff_shift_start = "2025-03-19 08:00:00"
    
    # 1. Convert string to datetime
    print("\n1. String to Datetime Conversion:")
    # TODO: Add code to convert appointment_date string to datetime object and display result
    
    # 2. Format datetime
    print("\n2. Datetime Formatting:")
    # TODO: Add code to format a datetime object with a custom format
    
    # 3. Calculate date difference
    print("\n3. Date Difference Calculation:")
    # TODO: Add code to calculate and display time between appointment and surgery
    
    # 4. Add time duration
    print("\n4. Time Duration Addition:")
    # TODO: Add code to calculate a follow-up appointment by adding days, hours, minutes
    
    # 5. Get day of week
    print("\n5. Day of Week Determination:")
    # TODO: Add code to get and display weekday names for appointments
    
    # 6. Timezone conversion
    print("\n6. Timezone Conversion:")
    # TODO: Add code to convert time between Eastern and Pacific timezones
    
    print("\n===== DATE AND TIME PROCESSING COMPLETE =====")

if __name__ == "__main__":
    main()