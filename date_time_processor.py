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
    if not isinstance(date_string, str):
        raise TypeError("Date input must be a string")
    
    try:
        # Try parsing with time
        try:
            return datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            # Try parsing date only
            return datetime.datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Date must be in format 'YYYY-MM-DD' or 'YYYY-MM-DD HH:MM:SS'")

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
    if not isinstance(dt, datetime.datetime):
        raise TypeError("Input must be a datetime object")
    
    return dt.strftime(format_string)

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
    # Convert string dates to datetime objects if needed
    if isinstance(start_date, str):
        start_date = convert_string_to_datetime(start_date)
    if isinstance(end_date, str):
        end_date = convert_string_to_datetime(end_date)
    
    if not isinstance(start_date, datetime.datetime) or not isinstance(end_date, datetime.datetime):
        raise TypeError("Dates must be datetime objects or date strings")
    
    # Calculate difference
    difference = end_date - start_date
    
    total_seconds = difference.total_seconds()
    days = difference.days
    hours = int(total_seconds // 3600)
    minutes = int(total_seconds // 60)
    
    return {
        "days": days,
        "hours": hours,
        "minutes": minutes,
        "total_seconds": int(total_seconds)
    }

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
    # Convert string date to datetime object if needed
    if isinstance(dt, str):
        dt = convert_string_to_datetime(dt)
    
    if not isinstance(dt, datetime.datetime):
        raise TypeError("Date must be a datetime object or date string")
    
    # Validate inputs
    if not all(isinstance(val, int) for val in [days, hours, minutes]):
        raise TypeError("Duration values must be integers")
    
    # Calculate new datetime
    delta = timedelta(days=days, hours=hours, minutes=minutes)
    return dt + delta

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
    # Convert string date to datetime object if needed
    if isinstance(date_string, str):
        dt = convert_string_to_datetime(date_string)
    else:
        dt = date_string
    
    if not isinstance(dt, datetime.datetime):
        raise TypeError("Date must be a datetime object or date string")
    
    # Get weekday name
    return dt.strftime("%A")

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
    # Convert string date to datetime object if needed
    if isinstance(dt, str):
        dt = convert_string_to_datetime(dt)
    
    if not isinstance(dt, datetime.datetime):
        raise TypeError("Date must be a datetime object or date string")
    
    # Validate timezone offsets
    if not isinstance(source_offset, int) or not isinstance(target_offset, int):
        raise TypeError("Timezone offsets must be integers")
        
    if source_offset < -12 or source_offset > 14 or target_offset < -12 or target_offset > 14:
        raise ValueError("Timezone offsets must be between -12 and +14")
    
    # Calculate the time difference between timezones
    hours_diff = target_offset - source_offset
    
    # Add the difference to get the time in the target timezone
    return dt + timedelta(hours=hours_diff)

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
    dt_appointment = convert_string_to_datetime(appointment_date)
    print(f"  - Original string: {appointment_date}")
    print(f"  - Converted datetime: {dt_appointment}")
    
    # 2. Format datetime
    print("\n2. Datetime Formatting:")
    formatted_date = format_datetime(dt_appointment, "%A, %B %d, %Y at %I:%M %p")
    print(f"  - Formatted appointment: {formatted_date}")
    
    # 3. Calculate date difference
    print("\n3. Date Difference Calculation:")
    diff = calculate_date_difference(appointment_date, surgery_date)
    print(f"  - Time between appointment and surgery:")
    print(f"  - Days: {diff['days']}")
    print(f"  - Hours: {diff['hours']}")
    print(f"  - Minutes: {diff['minutes']}")
    
    # 4. Add time duration
    print("\n4. Time Duration Addition:")
    follow_up = add_time_duration(dt_appointment, days=7, hours=1, minutes=30)
    print(f"  - Original appointment: {appointment_date}")
    print(f"  - Follow-up appointment: {format_datetime(follow_up)}")
    
    # 5. Get day of week
    print("\n5. Day of Week Determination:")
    weekday = get_day_of_week(appointment_date)
    surgery_weekday = get_day_of_week(surgery_date)
    print(f"  - Appointment day: {weekday}")
    print(f"  - Surgery day: {surgery_weekday}")
    
    # 6. Timezone conversion
    print("\n6. Timezone Conversion:")
    local_time = convert_string_to_datetime(staff_shift_start)
    remote_time = convert_timezone(local_time, -5, -8)  # Eastern to Pacific
    print(f"  - Staff shift start (Eastern, UTC-5): {format_datetime(local_time)}")
    print(f"  - Staff shift start (Pacific, UTC-8): {format_datetime(remote_time)}")
    
    print("\n===== DATE AND TIME PROCESSING COMPLETE =====")

if __name__ == "__main__":
    main()