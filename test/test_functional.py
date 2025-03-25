import pytest
from datetime import datetime
from date_time_processor import (
    convert_string_to_datetime,
    format_datetime,
    calculate_date_difference,
    add_time_duration,
    get_day_of_week,
    convert_timezone
)
from test.TestUtils import TestUtils


class TestFunctional:
    """Test cases for date time processor functionality."""
    
    def test_convert_string_to_datetime(self):
        """Test string to datetime conversion functionality."""
        try:
            # Test date only format
            date_only = convert_string_to_datetime("2025-03-19")
            assert date_only.year == 2025, "Should extract correct year"
            assert date_only.month == 3, "Should extract correct month"
            assert date_only.day == 19, "Should extract correct day"
            assert date_only.hour == 0, "Should set hour to 0 for date-only input"
            
            # Test date and time format
            date_time = convert_string_to_datetime("2025-03-19 14:30:00")
            assert date_time.year == 2025, "Should extract correct year"
            assert date_time.month == 3, "Should extract correct month"
            assert date_time.day == 19, "Should extract correct day"
            assert date_time.hour == 14, "Should extract correct hour"
            assert date_time.minute == 30, "Should extract correct minute"
            
            # Test parsing order (specific test for the subtle bug)
            date_time_specific = convert_string_to_datetime("2025-03-19 00:00:00")
            assert date_time_specific.hour == 0, "Should preserve zero hours from input"
            assert date_time_specific.minute == 0, "Should preserve zero minutes from input"
            
            TestUtils.yakshaAssert("test_convert_string_to_datetime", True, "functional")
        except Exception as e:
            TestUtils.yakshaAssert("test_convert_string_to_datetime", False, "functional")
            raise e
    
    def test_format_datetime(self):
        """Test datetime formatting functionality."""
        try:
            dt = datetime(2025, 3, 19, 14, 30)
            
            # Test default format
            default_format = format_datetime(dt)
            assert default_format == "2025-03-19 14:30:00", "Should format with default pattern"
            
            # Test custom format
            custom_format = format_datetime(dt, "%B %d, %Y at %I:%M %p")
            assert custom_format == "March 19, 2025 at 02:30 PM", "Should format with custom pattern"
            
            # Test date only format
            date_only = format_datetime(dt, "%Y-%m-%d")
            assert date_only == "2025-03-19", "Should format date only"
            
            # Test time only format
            time_only = format_datetime(dt, "%H:%M:%S")
            assert time_only == "14:30:00", "Should format time only"
            
            TestUtils.yakshaAssert("test_format_datetime", True, "functional")
        except Exception as e:
            TestUtils.yakshaAssert("test_format_datetime", False, "functional")
            raise e
    
    def test_calculate_date_difference(self):
        """Test date difference calculation functionality."""
        try:
            # Test with datetime objects
            start = datetime(2025, 3, 19)
            end = datetime(2025, 3, 26)
            diff = calculate_date_difference(start, end)
            assert diff["days"] == 7, "Should calculate correct days"
            assert diff["hours"] == 168, "Should calculate correct hours (days * 24)"
            assert diff["minutes"] == 10080, "Should calculate correct minutes (hours * 60)"
            assert diff["total_seconds"] == 604800, "Should calculate correct seconds"
            
            # Test with string dates
            diff_str = calculate_date_difference("2025-03-19", "2025-03-26")
            assert diff_str["days"] == 7, "Should calculate with string inputs"
            
            # Test with different times
            start_time = datetime(2025, 3, 19, 10, 0)
            end_time = datetime(2025, 3, 19, 15, 30)
            diff_time = calculate_date_difference(start_time, end_time)
            assert diff_time["days"] == 0, "Should calculate partial day"
            assert diff_time["hours"] == 5, "Should calculate correct hour difference"
            assert diff_time["minutes"] == 330, "Should calculate correct minute difference (5.5 * 60)"
            
            # Test negative date difference
            reverse_diff = calculate_date_difference(end, start)
            assert reverse_diff["days"] == -7, "Should handle negative days correctly"
            assert reverse_diff["hours"] == -168, "Should handle negative hours correctly"
            
            TestUtils.yakshaAssert("test_calculate_date_difference", True, "functional")
        except Exception as e:
            TestUtils.yakshaAssert("test_calculate_date_difference", False, "functional")
            raise e
    
    def test_add_time_duration(self):
        """Test time duration addition functionality."""
        try:
            dt = datetime(2025, 3, 19, 10, 0)
            
            # Test adding days
            days_added = add_time_duration(dt, days=2)
            assert days_added.year == 2025, "Should maintain year"
            assert days_added.month == 3, "Should maintain month"
            assert days_added.day == 21, "Should add days correctly"
            
            # Test adding hours
            hours_added = add_time_duration(dt, hours=5)
            assert hours_added.day == 19, "Should maintain day"
            assert hours_added.hour == 15, "Should add hours correctly"
            
            # Test adding minutes
            minutes_added = add_time_duration(dt, minutes=45)
            assert minutes_added.hour == 10, "Should maintain hour"
            assert minutes_added.minute == 45, "Should add minutes correctly"
            
            # Test adding combination
            combined = add_time_duration(dt, days=2, hours=5, minutes=30)
            assert combined.day == 21, "Should add days in combination"
            assert combined.hour == 15, "Should add hours in combination"
            assert combined.minute == 30, "Should add minutes in combination"
            
            # Test with string input
            string_result = add_time_duration("2025-03-19 10:00:00", days=2, hours=5)
            assert string_result.day == 21, "Should work with string input"
            assert string_result.hour == 15, "Should work with string input"
            
            # Test with crossing day boundary
            cross_day = add_time_duration(dt, hours=15)
            assert cross_day.day == 20, "Should handle crossing day boundary"
            assert cross_day.hour == 1, "Should calculate correct hour when crossing day boundary"
            
            # Test input validation (non-integer inputs)
            try:
                add_time_duration(dt, days="2")
                assert False, "Should raise TypeError for non-integer inputs"
            except TypeError:
                pass  # Expected behavior
            
            TestUtils.yakshaAssert("test_add_time_duration", True, "functional")
        except Exception as e:
            TestUtils.yakshaAssert("test_add_time_duration", False, "functional")
            raise e
    
    def test_get_day_of_week(self):
        """Test day of week determination functionality."""
        try:
            # Test with datetime object
            dt = datetime(2025, 3, 19)
            day_name = get_day_of_week(dt)
            assert day_name == "Wednesday", "Should return correct day name"
            
            # Test with string date
            day_name_str = get_day_of_week("2025-03-19")
            assert day_name_str == "Wednesday", "Should work with string input"
            
            # Test with different days
            monday = get_day_of_week("2025-03-17")
            assert monday == "Monday", "Should identify Monday"
            
            sunday = get_day_of_week("2025-03-23")
            assert sunday == "Sunday", "Should identify Sunday"
            
            # Test implementation method (must use strftime)
            # We can test this by checking the return type rather than the internal implementation
            future_date = datetime(2025, 12, 31)
            day_name_future = get_day_of_week(future_date)
            assert isinstance(day_name_future, str), "Should return a string"
            
            TestUtils.yakshaAssert("test_get_day_of_week", True, "functional")
        except Exception as e:
            TestUtils.yakshaAssert("test_get_day_of_week", False, "functional")
            raise e
    
    def test_convert_timezone(self):
        """Test timezone conversion functionality."""
        try:
            # Test timezone conversion (Eastern to Pacific)
            dt = datetime(2025, 3, 19, 14, 0)
            pacific_time = convert_timezone(dt, -5, -8)
            assert pacific_time.hour == 11, "Should shift hours correctly"
            assert pacific_time.day == 19, "Should maintain day for small shifts"
            
            # Test day boundary crossing (evening conversion)
            evening = datetime(2025, 3, 19, 23, 0)
            next_day = convert_timezone(evening, -5, 0)  # EST to UTC
            assert next_day.day == 20, "Should change day when crossing boundary"
            assert next_day.hour == 4, "Should calculate correct hour across day boundary"
            
            # Test with string input
            string_result = convert_timezone("2025-03-19 14:00:00", -5, -8)
            assert string_result.hour == 11, "Should work with string input"
            
            # Test shifting forward
            forward_shift = convert_timezone(dt, -8, -5)  # Pacific to Eastern
            assert forward_shift.hour == 17, "Should shift forward correctly"
            
            # Test the direction of conversion
            central_to_eastern = convert_timezone(dt, -6, -5)  # Central to Eastern
            eastern_to_central = convert_timezone(dt, -5, -6)  # Eastern to Central
            assert central_to_eastern.hour == 15, "Should add an hour going east"
            assert eastern_to_central.hour == 13, "Should subtract an hour going west"
            
            TestUtils.yakshaAssert("test_convert_timezone", True, "functional")
        except Exception as e:
            TestUtils.yakshaAssert("test_convert_timezone", False, "functional")
            raise e