import unittest
import sys
import os
import importlib
from datetime import datetime, timedelta
from test.TestUtils import TestUtils

def safely_import_module(module_name):
    """Safely import a module, returning None if import fails."""
    try:
        return importlib.import_module(module_name)
    except ImportError:
        return None

def check_function_exists(module, function_name):
    """Check if a function exists in a module."""
    return hasattr(module, function_name) and callable(getattr(module, function_name))

def safely_call_function(module, function_name, *args, **kwargs):
    """Safely call a function, returning None if it fails."""
    if not check_function_exists(module, function_name):
        return None
    try:
        return getattr(module, function_name)(*args, **kwargs)
    except Exception:
        return None

def load_module_dynamically():
    """Load the student's module for testing"""
    module_obj = safely_import_module("date_time_processor")
    if module_obj is None:
        module_obj = safely_import_module("solution")
    return module_obj

class TestFunctionalDateTime(unittest.TestCase):
    def setUp(self):
        """Standard setup for all test methods"""
        self.test_obj = TestUtils()
        self.module_obj = load_module_dynamically()

    def test_convert_string_to_datetime_functionality(self):
        """Test string to datetime conversion functionality comprehensively"""
        try:
            if self.module_obj is None:
                self.test_obj.yakshaAssert("TestConvertStringToDatetimeFunctionality", False, "functional")
                print("TestConvertStringToDatetimeFunctionality = Failed")
                return

            # Check if function exists
            if not check_function_exists(self.module_obj, "convert_string_to_datetime"):
                self.test_obj.yakshaAssert("TestConvertStringToDatetimeFunctionality", False, "functional")
                print("TestConvertStringToDatetimeFunctionality = Failed")
                return

            # Test date only format
            date_only = safely_call_function(self.module_obj, "convert_string_to_datetime", "2025-03-19")
            if date_only is None or not isinstance(date_only, datetime):
                self.test_obj.yakshaAssert("TestConvertStringToDatetimeFunctionality", False, "functional")
                print("TestConvertStringToDatetimeFunctionality = Failed")
                return
            if date_only.year != 2025 or date_only.month != 3 or date_only.day != 19:
                self.test_obj.yakshaAssert("TestConvertStringToDatetimeFunctionality", False, "functional")
                print("TestConvertStringToDatetimeFunctionality = Failed")
                return
            if date_only.hour != 0 or date_only.minute != 0:
                self.test_obj.yakshaAssert("TestConvertStringToDatetimeFunctionality", False, "functional")
                print("TestConvertStringToDatetimeFunctionality = Failed")
                return

            # Test date and time format
            date_time = safely_call_function(self.module_obj, "convert_string_to_datetime", "2025-03-19 14:30:00")
            if date_time is None or not isinstance(date_time, datetime):
                self.test_obj.yakshaAssert("TestConvertStringToDatetimeFunctionality", False, "functional")
                print("TestConvertStringToDatetimeFunctionality = Failed")
                return
            if (date_time.year != 2025 or date_time.month != 3 or date_time.day != 19 or 
                date_time.hour != 14 or date_time.minute != 30 or date_time.second != 0):
                self.test_obj.yakshaAssert("TestConvertStringToDatetimeFunctionality", False, "functional")
                print("TestConvertStringToDatetimeFunctionality = Failed")
                return

            # Test parsing order (specific test for zero values)
            date_time_specific = safely_call_function(self.module_obj, "convert_string_to_datetime", "2025-03-19 00:00:00")
            if date_time_specific is None or not isinstance(date_time_specific, datetime):
                self.test_obj.yakshaAssert("TestConvertStringToDatetimeFunctionality", False, "functional")
                print("TestConvertStringToDatetimeFunctionality = Failed")
                return
            if (date_time_specific.hour != 0 or date_time_specific.minute != 0 or 
                date_time_specific.second != 0):
                self.test_obj.yakshaAssert("TestConvertStringToDatetimeFunctionality", False, "functional")
                print("TestConvertStringToDatetimeFunctionality = Failed")
                return

            # Test edge cases
            edge_cases = [
                ("2024-02-29", "leap year date"),
                ("2025-01-01", "first day of year"),
                ("2025-12-31", "last day of year"),
                ("2025-03-19 23:59:59", "end of day time")
            ]
            
            for date_str, description in edge_cases:
                result = safely_call_function(self.module_obj, "convert_string_to_datetime", date_str)
                if result is None or not isinstance(result, datetime):
                    self.test_obj.yakshaAssert("TestConvertStringToDatetimeFunctionality", False, "functional")
                    print("TestConvertStringToDatetimeFunctionality = Failed")
                    return

            # All tests passed
            self.test_obj.yakshaAssert("TestConvertStringToDatetimeFunctionality", True, "functional")
            print("TestConvertStringToDatetimeFunctionality = Passed")

        except Exception as e:
            self.test_obj.yakshaAssert("TestConvertStringToDatetimeFunctionality", False, "functional")
            print("TestConvertStringToDatetimeFunctionality = Failed")

    def test_format_datetime_functionality(self):
        """Test datetime formatting functionality comprehensively"""
        try:
            if self.module_obj is None:
                self.test_obj.yakshaAssert("TestFormatDatetimeFunctionality", False, "functional")
                print("TestFormatDatetimeFunctionality = Failed")
                return

            # Check if function exists
            if not check_function_exists(self.module_obj, "format_datetime"):
                self.test_obj.yakshaAssert("TestFormatDatetimeFunctionality", False, "functional")
                print("TestFormatDatetimeFunctionality = Failed")
                return

            dt = datetime(2025, 3, 19, 14, 30, 45)

            # Test default format
            default_format = safely_call_function(self.module_obj, "format_datetime", dt)
            if default_format is None or not isinstance(default_format, str):
                self.test_obj.yakshaAssert("TestFormatDatetimeFunctionality", False, "functional")
                print("TestFormatDatetimeFunctionality = Failed")
                return
            if default_format != "2025-03-19 14:30:45":
                # Allow some flexibility in default format
                if "2025" not in default_format or "03" not in default_format or "19" not in default_format:
                    self.test_obj.yakshaAssert("TestFormatDatetimeFunctionality", False, "functional")
                    print("TestFormatDatetimeFunctionality = Failed")
                    return

            # Test custom format
            custom_format = safely_call_function(self.module_obj, "format_datetime", dt, "%B %d, %Y at %I:%M %p")
            if custom_format is None or not isinstance(custom_format, str):
                self.test_obj.yakshaAssert("TestFormatDatetimeFunctionality", False, "functional")
                print("TestFormatDatetimeFunctionality = Failed")
                return
            if custom_format != "March 19, 2025 at 02:30 PM":
                self.test_obj.yakshaAssert("TestFormatDatetimeFunctionality", False, "functional")
                print("TestFormatDatetimeFunctionality = Failed")
                return

            # Test date only format
            date_only = safely_call_function(self.module_obj, "format_datetime", dt, "%Y-%m-%d")
            if date_only is None or not isinstance(date_only, str) or date_only != "2025-03-19":
                self.test_obj.yakshaAssert("TestFormatDatetimeFunctionality", False, "functional")
                print("TestFormatDatetimeFunctionality = Failed")
                return

            # Test time only format
            time_only = safely_call_function(self.module_obj, "format_datetime", dt, "%H:%M:%S")
            if time_only is None or not isinstance(time_only, str) or time_only != "14:30:45":
                self.test_obj.yakshaAssert("TestFormatDatetimeFunctionality", False, "functional")
                print("TestFormatDatetimeFunctionality = Failed")
                return

            # Test various format patterns
            format_tests = [
                ("%A", "weekday name"),
                ("%B", "month name"),
                ("%Y", "4-digit year"),
                ("%m", "2-digit month"),
                ("%d", "2-digit day"),
                ("%H", "24-hour hour"),
                ("%I", "12-hour hour"),
                ("%M", "minute"),
                ("%S", "second"),
                ("%p", "AM/PM")
            ]
            
            for pattern, description in format_tests:
                result = safely_call_function(self.module_obj, "format_datetime", dt, pattern)
                if result is None or not isinstance(result, str) or len(result) == 0:
                    self.test_obj.yakshaAssert("TestFormatDatetimeFunctionality", False, "functional")
                    print("TestFormatDatetimeFunctionality = Failed")
                    return

            # Test edge dates
            edge_dt = datetime(1, 1, 1, 0, 0, 0)
            edge_result = safely_call_function(self.module_obj, "format_datetime", edge_dt, "%Y-%m-%d")
            if edge_result is None or not isinstance(edge_result, str):
                self.test_obj.yakshaAssert("TestFormatDatetimeFunctionality", False, "functional")
                print("TestFormatDatetimeFunctionality = Failed")
                return

            # All tests passed
            self.test_obj.yakshaAssert("TestFormatDatetimeFunctionality", True, "functional")
            print("TestFormatDatetimeFunctionality = Passed")

        except Exception as e:
            self.test_obj.yakshaAssert("TestFormatDatetimeFunctionality", False, "functional")
            print("TestFormatDatetimeFunctionality = Failed")

    def test_calculate_date_difference_functionality(self):
        """Test date difference calculation functionality comprehensively"""
        try:
            if self.module_obj is None:
                self.test_obj.yakshaAssert("TestCalculateDateDifferenceFunctionality", False, "functional")
                print("TestCalculateDateDifferenceFunctionality = Failed")
                return

            # Check if function exists
            if not check_function_exists(self.module_obj, "calculate_date_difference"):
                self.test_obj.yakshaAssert("TestCalculateDateDifferenceFunctionality", False, "functional")
                print("TestCalculateDateDifferenceFunctionality = Failed")
                return

            # Test with datetime objects
            start = datetime(2025, 3, 19)
            end = datetime(2025, 3, 26)
            diff = safely_call_function(self.module_obj, "calculate_date_difference", start, end)
            if diff is None or not isinstance(diff, dict):
                self.test_obj.yakshaAssert("TestCalculateDateDifferenceFunctionality", False, "functional")
                print("TestCalculateDateDifferenceFunctionality = Failed")
                return
            if (diff.get("days") != 7 or diff.get("hours") != 168 or 
                diff.get("minutes") != 10080 or diff.get("total_seconds") != 604800):
                self.test_obj.yakshaAssert("TestCalculateDateDifferenceFunctionality", False, "functional")
                print("TestCalculateDateDifferenceFunctionality = Failed")
                return

            # Test with string dates
            diff_str = safely_call_function(self.module_obj, "calculate_date_difference", "2025-03-19", "2025-03-26")
            if diff_str is None or not isinstance(diff_str, dict) or diff_str.get("days") != 7:
                self.test_obj.yakshaAssert("TestCalculateDateDifferenceFunctionality", False, "functional")
                print("TestCalculateDateDifferenceFunctionality = Failed")
                return

            # Test with different times
            start_time = datetime(2025, 3, 19, 10, 0)
            end_time = datetime(2025, 3, 19, 15, 30)
            diff_time = safely_call_function(self.module_obj, "calculate_date_difference", start_time, end_time)
            if diff_time is None or not isinstance(diff_time, dict):
                self.test_obj.yakshaAssert("TestCalculateDateDifferenceFunctionality", False, "functional")
                print("TestCalculateDateDifferenceFunctionality = Failed")
                return
            if (diff_time.get("days") != 0 or diff_time.get("hours") != 5 or 
                diff_time.get("minutes") != 330):
                self.test_obj.yakshaAssert("TestCalculateDateDifferenceFunctionality", False, "functional")
                print("TestCalculateDateDifferenceFunctionality = Failed")
                return

            # Test negative date difference
            reverse_diff = safely_call_function(self.module_obj, "calculate_date_difference", end, start)
            if reverse_diff is None or not isinstance(reverse_diff, dict):
                self.test_obj.yakshaAssert("TestCalculateDateDifferenceFunctionality", False, "functional")
                print("TestCalculateDateDifferenceFunctionality = Failed")
                return
            if reverse_diff.get("days") != -7 or reverse_diff.get("hours") != -168:
                self.test_obj.yakshaAssert("TestCalculateDateDifferenceFunctionality", False, "functional")
                print("TestCalculateDateDifferenceFunctionality = Failed")
                return

            # Test mixed input types
            mixed_diff = safely_call_function(self.module_obj, "calculate_date_difference", "2025-03-19", end)
            if mixed_diff is None or not isinstance(mixed_diff, dict):
                self.test_obj.yakshaAssert("TestCalculateDateDifferenceFunctionality", False, "functional")
                print("TestCalculateDateDifferenceFunctionality = Failed")
                return

            # Test same date
            same_diff = safely_call_function(self.module_obj, "calculate_date_difference", start, start)
            if same_diff is None or not isinstance(same_diff, dict):
                self.test_obj.yakshaAssert("TestCalculateDateDifferenceFunctionality", False, "functional")
                print("TestCalculateDateDifferenceFunctionality = Failed")
                return
            if same_diff.get("days") != 0 or same_diff.get("total_seconds") != 0:
                self.test_obj.yakshaAssert("TestCalculateDateDifferenceFunctionality", False, "functional")
                print("TestCalculateDateDifferenceFunctionality = Failed")
                return

            # Test required dictionary keys
            required_keys = ["days", "hours", "minutes", "total_seconds"]
            if diff is not None and isinstance(diff, dict):
                for key in required_keys:
                    if key not in diff:
                        self.test_obj.yakshaAssert("TestCalculateDateDifferenceFunctionality", False, "functional")
                        print("TestCalculateDateDifferenceFunctionality = Failed")
                        return

            # All tests passed
            self.test_obj.yakshaAssert("TestCalculateDateDifferenceFunctionality", True, "functional")
            print("TestCalculateDateDifferenceFunctionality = Passed")

        except Exception as e:
            self.test_obj.yakshaAssert("TestCalculateDateDifferenceFunctionality", False, "functional")
            print("TestCalculateDateDifferenceFunctionality = Failed")

    def test_add_time_duration_functionality(self):
        """Test time duration addition functionality comprehensively"""
        try:
            if self.module_obj is None:
                self.test_obj.yakshaAssert("TestAddTimeDurationFunctionality", False, "functional")
                print("TestAddTimeDurationFunctionality = Failed")
                return

            # Check if function exists
            if not check_function_exists(self.module_obj, "add_time_duration"):
                self.test_obj.yakshaAssert("TestAddTimeDurationFunctionality", False, "functional")
                print("TestAddTimeDurationFunctionality = Failed")
                return

            dt = datetime(2025, 3, 19, 10, 0)

            # Test adding days
            days_added = safely_call_function(self.module_obj, "add_time_duration", dt, days=2)
            if days_added is None or not isinstance(days_added, datetime):
                self.test_obj.yakshaAssert("TestAddTimeDurationFunctionality", False, "functional")
                print("TestAddTimeDurationFunctionality = Failed")
                return
            if (days_added.year != 2025 or days_added.month != 3 or days_added.day != 21 or 
                days_added.hour != 10):
                self.test_obj.yakshaAssert("TestAddTimeDurationFunctionality", False, "functional")
                print("TestAddTimeDurationFunctionality = Failed")
                return

            # Test adding hours
            hours_added = safely_call_function(self.module_obj, "add_time_duration", dt, hours=5)
            if hours_added is None or not isinstance(hours_added, datetime):
                self.test_obj.yakshaAssert("TestAddTimeDurationFunctionality", False, "functional")
                print("TestAddTimeDurationFunctionality = Failed")
                return
            if hours_added.day != 19 or hours_added.hour != 15:
                self.test_obj.yakshaAssert("TestAddTimeDurationFunctionality", False, "functional")
                print("TestAddTimeDurationFunctionality = Failed")
                return

            # Test adding minutes
            minutes_added = safely_call_function(self.module_obj, "add_time_duration", dt, minutes=45)
            if minutes_added is None or not isinstance(minutes_added, datetime):
                self.test_obj.yakshaAssert("TestAddTimeDurationFunctionality", False, "functional")
                print("TestAddTimeDurationFunctionality = Failed")
                return
            if minutes_added.hour != 10 or minutes_added.minute != 45:
                self.test_obj.yakshaAssert("TestAddTimeDurationFunctionality", False, "functional")
                print("TestAddTimeDurationFunctionality = Failed")
                return

            # Test adding combination
            combined = safely_call_function(self.module_obj, "add_time_duration", dt, days=2, hours=5, minutes=30)
            if combined is None or not isinstance(combined, datetime):
                self.test_obj.yakshaAssert("TestAddTimeDurationFunctionality", False, "functional")
                print("TestAddTimeDurationFunctionality = Failed")
                return
            if combined.day != 21 or combined.hour != 15 or combined.minute != 30:
                self.test_obj.yakshaAssert("TestAddTimeDurationFunctionality", False, "functional")
                print("TestAddTimeDurationFunctionality = Failed")
                return

            # Test with string input
            string_result = safely_call_function(self.module_obj, "add_time_duration", "2025-03-19 10:00:00", days=2, hours=5)
            if string_result is None or not isinstance(string_result, datetime):
                self.test_obj.yakshaAssert("TestAddTimeDurationFunctionality", False, "functional")
                print("TestAddTimeDurationFunctionality = Failed")
                return
            if string_result.day != 21 or string_result.hour != 15:
                self.test_obj.yakshaAssert("TestAddTimeDurationFunctionality", False, "functional")
                print("TestAddTimeDurationFunctionality = Failed")
                return

            # Test with crossing day boundary
            cross_day = safely_call_function(self.module_obj, "add_time_duration", dt, hours=15)
            if cross_day is None or not isinstance(cross_day, datetime):
                self.test_obj.yakshaAssert("TestAddTimeDurationFunctionality", False, "functional")
                print("TestAddTimeDurationFunctionality = Failed")
                return
            if cross_day.day != 20 or cross_day.hour != 1:
                self.test_obj.yakshaAssert("TestAddTimeDurationFunctionality", False, "functional")
                print("TestAddTimeDurationFunctionality = Failed")
                return

            # Test negative durations
            negative_result = safely_call_function(self.module_obj, "add_time_duration", dt, days=-1, hours=-2, minutes=-30)
            if negative_result is None or not isinstance(negative_result, datetime):
                self.test_obj.yakshaAssert("TestAddTimeDurationFunctionality", False, "functional")
                print("TestAddTimeDurationFunctionality = Failed")
                return
            expected = datetime(2025, 3, 18, 7, 30)
            if negative_result != expected:
                self.test_obj.yakshaAssert("TestAddTimeDurationFunctionality", False, "functional")
                print("TestAddTimeDurationFunctionality = Failed")
                return

            # Test zero duration
            zero_result = safely_call_function(self.module_obj, "add_time_duration", dt, days=0, hours=0, minutes=0)
            if zero_result is None or not isinstance(zero_result, datetime) or zero_result != dt:
                self.test_obj.yakshaAssert("TestAddTimeDurationFunctionality", False, "functional")
                print("TestAddTimeDurationFunctionality = Failed")
                return

            # Test default parameters
            default_test = safely_call_function(self.module_obj, "add_time_duration", dt, days=1)
            if default_test is None or not isinstance(default_test, datetime):
                self.test_obj.yakshaAssert("TestAddTimeDurationFunctionality", False, "functional")
                print("TestAddTimeDurationFunctionality = Failed")
                return

            # All tests passed
            self.test_obj.yakshaAssert("TestAddTimeDurationFunctionality", True, "functional")
            print("TestAddTimeDurationFunctionality = Passed")

        except Exception as e:
            self.test_obj.yakshaAssert("TestAddTimeDurationFunctionality", False, "functional")
            print("TestAddTimeDurationFunctionality = Failed")

    def test_get_day_of_week_functionality(self):
        """Test day of week determination functionality comprehensively"""
        try:
            if self.module_obj is None:
                self.test_obj.yakshaAssert("TestGetDayOfWeekFunctionality", False, "functional")
                print("TestGetDayOfWeekFunctionality = Failed")
                return

            # Check if function exists
            if not check_function_exists(self.module_obj, "get_day_of_week"):
                self.test_obj.yakshaAssert("TestGetDayOfWeekFunctionality", False, "functional")
                print("TestGetDayOfWeekFunctionality = Failed")
                return

            # Test with datetime object
            dt = datetime(2025, 3, 19)  # Known to be Wednesday
            day_name = safely_call_function(self.module_obj, "get_day_of_week", dt)
            if day_name is None or not isinstance(day_name, str) or day_name != "Wednesday":
                self.test_obj.yakshaAssert("TestGetDayOfWeekFunctionality", False, "functional")
                print("TestGetDayOfWeekFunctionality = Failed")
                return

            # Test with string date
            day_name_str = safely_call_function(self.module_obj, "get_day_of_week", "2025-03-19")
            if day_name_str is None or not isinstance(day_name_str, str) or day_name_str != "Wednesday":
                self.test_obj.yakshaAssert("TestGetDayOfWeekFunctionality", False, "functional")
                print("TestGetDayOfWeekFunctionality = Failed")
                return

            # Test with different known days
            known_days = [
                ("2025-03-17", "Monday"),
                ("2025-03-18", "Tuesday"),
                ("2025-03-19", "Wednesday"),
                ("2025-03-20", "Thursday"),
                ("2025-03-21", "Friday"),
                ("2025-03-22", "Saturday"),
                ("2025-03-23", "Sunday")
            ]
            
            for date_str, expected_day in known_days:
                result = safely_call_function(self.module_obj, "get_day_of_week", date_str)
                if result is None or not isinstance(result, str) or result != expected_day:
                    self.test_obj.yakshaAssert("TestGetDayOfWeekFunctionality", False, "functional")
                    print("TestGetDayOfWeekFunctionality = Failed")
                    return

            # Test edge dates
            edge_dates = [
                ("2025-01-01", "first day of year"),
                ("2025-12-31", "last day of year"),
                ("2024-02-29", "leap year date"),
                ("2000-01-01", "Y2K date")
            ]
            
            for date_str, description in edge_dates:
                result = safely_call_function(self.module_obj, "get_day_of_week", date_str)
                if result is None or not isinstance(result, str) or len(result) == 0:
                    self.test_obj.yakshaAssert("TestGetDayOfWeekFunctionality", False, "functional")
                    print("TestGetDayOfWeekFunctionality = Failed")
                    return

            # Test with datetime that has time component
            dt_with_time = datetime(2025, 3, 19, 14, 30, 45)
            day_with_time = safely_call_function(self.module_obj, "get_day_of_week", dt_with_time)
            if day_with_time is None or not isinstance(day_with_time, str) or day_with_time != "Wednesday":
                self.test_obj.yakshaAssert("TestGetDayOfWeekFunctionality", False, "functional")
                print("TestGetDayOfWeekFunctionality = Failed")
                return

            # Test that function returns full weekday names
            valid_weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            test_result = safely_call_function(self.module_obj, "get_day_of_week", "2025-03-19")
            if test_result is not None and test_result not in valid_weekdays:
                self.test_obj.yakshaAssert("TestGetDayOfWeekFunctionality", False, "functional")
                print("TestGetDayOfWeekFunctionality = Failed")
                return

            # All tests passed
            self.test_obj.yakshaAssert("TestGetDayOfWeekFunctionality", True, "functional")
            print("TestGetDayOfWeekFunctionality = Passed")

        except Exception as e:
            self.test_obj.yakshaAssert("TestGetDayOfWeekFunctionality", False, "functional")
            print("TestGetDayOfWeekFunctionality = Failed")

    def test_convert_timezone_functionality(self):
        """Test timezone conversion functionality comprehensively"""
        try:
            if self.module_obj is None:
                self.test_obj.yakshaAssert("TestConvertTimezoneFunctionality", False, "functional")
                print("TestConvertTimezoneFunctionality = Failed")
                return

            # Check if function exists
            if not check_function_exists(self.module_obj, "convert_timezone"):
                self.test_obj.yakshaAssert("TestConvertTimezoneFunctionality", False, "functional")
                print("TestConvertTimezoneFunctionality = Failed")
                return

            # Test timezone conversion (Eastern to Pacific)
            dt = datetime(2025, 3, 19, 14, 0)
            pacific_time = safely_call_function(self.module_obj, "convert_timezone", dt, -5, -8)
            if pacific_time is None or not isinstance(pacific_time, datetime):
                self.test_obj.yakshaAssert("TestConvertTimezoneFunctionality", False, "functional")
                print("TestConvertTimezoneFunctionality = Failed")
                return
            if (pacific_time.hour != 11 or pacific_time.day != 19 or 
                pacific_time.year != 2025 or pacific_time.month != 3):
                self.test_obj.yakshaAssert("TestConvertTimezoneFunctionality", False, "functional")
                print("TestConvertTimezoneFunctionality = Failed")
                return

            # Test day boundary crossing
            evening = datetime(2025, 3, 19, 23, 0)
            next_day = safely_call_function(self.module_obj, "convert_timezone", evening, -5, 0)
            if next_day is None or not isinstance(next_day, datetime):
                self.test_obj.yakshaAssert("TestConvertTimezoneFunctionality", False, "functional")
                print("TestConvertTimezoneFunctionality = Failed")
                return
            if next_day.day != 20 or next_day.hour != 4:
                self.test_obj.yakshaAssert("TestConvertTimezoneFunctionality", False, "functional")
                print("TestConvertTimezoneFunctionality = Failed")
                return

            # Test with string input
            string_result = safely_call_function(self.module_obj, "convert_timezone", "2025-03-19 14:00:00", -5, -8)
            if string_result is None or not isinstance(string_result, datetime) or string_result.hour != 11:
                self.test_obj.yakshaAssert("TestConvertTimezoneFunctionality", False, "functional")
                print("TestConvertTimezoneFunctionality = Failed")
                return

            # Test shifting forward and backward
            forward_shift = safely_call_function(self.module_obj, "convert_timezone", dt, -8, -5)
            if forward_shift is None or not isinstance(forward_shift, datetime) or forward_shift.hour != 17:
                self.test_obj.yakshaAssert("TestConvertTimezoneFunctionality", False, "functional")
                print("TestConvertTimezoneFunctionality = Failed")
                return

            # Test the direction of conversion
            central_to_eastern = safely_call_function(self.module_obj, "convert_timezone", dt, -6, -5)
            eastern_to_central = safely_call_function(self.module_obj, "convert_timezone", dt, -5, -6)
            
            if central_to_eastern is None or central_to_eastern.hour != 15:
                self.test_obj.yakshaAssert("TestConvertTimezoneFunctionality", False, "functional")
                print("TestConvertTimezoneFunctionality = Failed")
                return
            
            if eastern_to_central is None or eastern_to_central.hour != 13:
                self.test_obj.yakshaAssert("TestConvertTimezoneFunctionality", False, "functional")
                print("TestConvertTimezoneFunctionality = Failed")
                return

            # Test same timezone conversion
            same_tz = safely_call_function(self.module_obj, "convert_timezone", dt, -5, -5)
            if same_tz is None or not isinstance(same_tz, datetime) or same_tz != dt:
                self.test_obj.yakshaAssert("TestConvertTimezoneFunctionality", False, "functional")
                print("TestConvertTimezoneFunctionality = Failed")
                return

            # Test maximum timezone differences
            max_east = safely_call_function(self.module_obj, "convert_timezone", dt, -12, 14)
            if max_east is None or not isinstance(max_east, datetime):
                self.test_obj.yakshaAssert("TestConvertTimezoneFunctionality", False, "functional")
                print("TestConvertTimezoneFunctionality = Failed")
                return
            if max_east.day != 20 or max_east.hour != 16:
                self.test_obj.yakshaAssert("TestConvertTimezoneFunctionality", False, "functional")
                print("TestConvertTimezoneFunctionality = Failed")
                return

            max_west = safely_call_function(self.module_obj, "convert_timezone", dt, 14, -12)
            if max_west is None or not isinstance(max_west, datetime) or max_west.day != 18:
                self.test_obj.yakshaAssert("TestConvertTimezoneFunctionality", False, "functional")
                print("TestConvertTimezoneFunctionality = Failed")
                return

            # Test crossing year boundary
            year_end = datetime(2025, 12, 31, 23, 30)
            cross_year = safely_call_function(self.module_obj, "convert_timezone", year_end, -8, 3)
            if cross_year is None or not isinstance(cross_year, datetime):
                self.test_obj.yakshaAssert("TestConvertTimezoneFunctionality", False, "functional")
                print("TestConvertTimezoneFunctionality = Failed")
                return
            if cross_year.year != 2026 or cross_year.month != 1 or cross_year.day != 1:
                self.test_obj.yakshaAssert("TestConvertTimezoneFunctionality", False, "functional")
                print("TestConvertTimezoneFunctionality = Failed")
                return

            # Test minute and second preservation
            precise_dt = datetime(2025, 3, 19, 14, 45, 30)
            precise_result = safely_call_function(self.module_obj, "convert_timezone", precise_dt, -5, -8)
            if precise_result is None or not isinstance(precise_result, datetime):
                self.test_obj.yakshaAssert("TestConvertTimezoneFunctionality", False, "functional")
                print("TestConvertTimezoneFunctionality = Failed")
                return
            if precise_result.minute != 45 or precise_result.second != 30:
                self.test_obj.yakshaAssert("TestConvertTimezoneFunctionality", False, "functional")
                print("TestConvertTimezoneFunctionality = Failed")
                return

            # Test edge timezone offsets
            edge_offsets = [
                (-12, -11, "minimum source to near minimum target"),
                (13, 14, "near maximum source to maximum target"),
                (0, 0, "UTC to UTC"),
                (-1, 1, "negative to positive")
            ]
            
            for source, target, description in edge_offsets:
                result = safely_call_function(self.module_obj, "convert_timezone", dt, source, target)
                if result is None or not isinstance(result, datetime):
                    self.test_obj.yakshaAssert("TestConvertTimezoneFunctionality", False, "functional")
                    print("TestConvertTimezoneFunctionality = Failed")
                    return

            # All tests passed
            self.test_obj.yakshaAssert("TestConvertTimezoneFunctionality", True, "functional")
            print("TestConvertTimezoneFunctionality = Passed")

        except Exception as e:
            self.test_obj.yakshaAssert("TestConvertTimezoneFunctionality", False, "functional")
            print("TestConvertTimezoneFunctionality = Failed")

    def test_datetime_module_implementation_techniques(self):
        """Test that datetime module techniques are implemented correctly"""
        try:
            if self.module_obj is None:
                self.test_obj.yakshaAssert("TestDatetimeModuleImplementationTechniques", False, "functional")
                print("TestDatetimeModuleImplementationTechniques = Failed")
                return

            # Check that datetime module is imported
            try:
                import inspect
                source = inspect.getsource(self.module_obj)
                if "import datetime" not in source and "from datetime import" not in source:
                    self.test_obj.yakshaAssert("TestDatetimeModuleImplementationTechniques", False, "functional")
                    print("TestDatetimeModuleImplementationTechniques = Failed")
                    return
            except Exception:
                # If we can't check source, continue with functional tests
                pass

            # Test that functions handle both string and datetime inputs appropriately
            test_dt = datetime(2025, 3, 19, 14, 30)
            test_str = "2025-03-19 14:30:00"

            # Functions that should accept both string and datetime
            dual_input_functions = [
                "calculate_date_difference",
                "add_time_duration",
                "get_day_of_week",
                "convert_timezone"
            ]

            for func_name in dual_input_functions:
                if check_function_exists(self.module_obj, func_name):
                    # Test with datetime input
                    if func_name == "calculate_date_difference":
                        dt_result = safely_call_function(self.module_obj, func_name, test_dt, test_dt)
                        str_result = safely_call_function(self.module_obj, func_name, test_str, test_str)
                    elif func_name == "add_time_duration":
                        dt_result = safely_call_function(self.module_obj, func_name, test_dt, days=1)
                        str_result = safely_call_function(self.module_obj, func_name, test_str, days=1)
                    elif func_name == "get_day_of_week":
                        dt_result = safely_call_function(self.module_obj, func_name, test_dt)
                        str_result = safely_call_function(self.module_obj, func_name, test_str)
                    elif func_name == "convert_timezone":
                        dt_result = safely_call_function(self.module_obj, func_name, test_dt, -5, -8)
                        str_result = safely_call_function(self.module_obj, func_name, test_str, -5, -8)

                    if dt_result is None or str_result is None:
                        self.test_obj.yakshaAssert("TestDatetimeModuleImplementationTechniques", False, "functional")
                        print("TestDatetimeModuleImplementationTechniques = Failed")
                        return

                    # Results should be equivalent for get_day_of_week
                    if (func_name == "get_day_of_week" and dt_result != str_result):
                        self.test_obj.yakshaAssert("TestDatetimeModuleImplementationTechniques", False, "functional")
                        print("TestDatetimeModuleImplementationTechniques = Failed")
                        return

            # Test that format_datetime uses strftime
            if check_function_exists(self.module_obj, "format_datetime"):
                test_patterns = [
                    ("%Y", "year"),
                    ("%m", "month"),
                    ("%d", "day"),
                    ("%H", "hour"),
                    ("%M", "minute"),
                    ("%S", "second"),
                    ("%A", "weekday name")
                ]

                for pattern, description in test_patterns:
                    result = safely_call_function(self.module_obj, "format_datetime", test_dt, pattern)
                    if result is None or not isinstance(result, str):
                        self.test_obj.yakshaAssert("TestDatetimeModuleImplementationTechniques", False, "functional")
                        print("TestDatetimeModuleImplementationTechniques = Failed")
                        return

            # Test that timedelta is used for duration operations
            if check_function_exists(self.module_obj, "add_time_duration"):
                large_duration = safely_call_function(self.module_obj, "add_time_duration", test_dt, days=365)
                if large_duration is None or not isinstance(large_duration, datetime) or large_duration.year != 2026:
                    self.test_obj.yakshaAssert("TestDatetimeModuleImplementationTechniques", False, "functional")
                    print("TestDatetimeModuleImplementationTechniques = Failed")
                    return

            # Test that date arithmetic works correctly
            if check_function_exists(self.module_obj, "calculate_date_difference"):
                start_precise = datetime(2025, 3, 19, 12, 0, 0)
                end_precise = datetime(2025, 3, 19, 12, 0, 30)
                precise_diff = safely_call_function(self.module_obj, "calculate_date_difference", start_precise, end_precise)
                if precise_diff is None or precise_diff.get("total_seconds") != 30:
                    self.test_obj.yakshaAssert("TestDatetimeModuleImplementationTechniques", False, "functional")
                    print("TestDatetimeModuleImplementationTechniques = Failed")
                    return

            # Test that datetime objects preserve all components
            if check_function_exists(self.module_obj, "convert_string_to_datetime"):
                full_datetime = safely_call_function(self.module_obj, "convert_string_to_datetime", "2025-03-19 14:30:45")
                if full_datetime is None or not isinstance(full_datetime, datetime):
                    self.test_obj.yakshaAssert("TestDatetimeModuleImplementationTechniques", False, "functional")
                    print("TestDatetimeModuleImplementationTechniques = Failed")
                    return

                components = [
                    (full_datetime.year, 2025, "year"),
                    (full_datetime.month, 3, "month"),
                    (full_datetime.day, 19, "day"),
                    (full_datetime.hour, 14, "hour"),
                    (full_datetime.minute, 30, "minute"),
                    (full_datetime.second, 45, "second")
                ]

                for actual, expected, component in components:
                    if actual != expected:
                        self.test_obj.yakshaAssert("TestDatetimeModuleImplementationTechniques", False, "functional")
                        print("TestDatetimeModuleImplementationTechniques = Failed")
                        return

            # All tests passed
            self.test_obj.yakshaAssert("TestDatetimeModuleImplementationTechniques", True, "functional")
            print("TestDatetimeModuleImplementationTechniques = Passed")

        except Exception as e:
            self.test_obj.yakshaAssert("TestDatetimeModuleImplementationTechniques", False, "functional")
            print("TestDatetimeModuleImplementationTechniques = Failed")

if __name__ == '__main__':
    unittest.main()