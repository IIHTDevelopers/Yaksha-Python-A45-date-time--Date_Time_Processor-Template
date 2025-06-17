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
    module_obj = safely_import_module("skeleton")
    if module_obj is None:
        module_obj = safely_import_module("solution")
    return module_obj

class TestBoundaryConditions(unittest.TestCase):
    def setUp(self):
        """Standard setup for all test methods"""
        self.test_obj = TestUtils()
        self.module_obj = load_module_dynamically()

    def test_boundary_conditions_comprehensive(self):
        """Comprehensive test for all boundary conditions and edge cases"""
        try:
            if self.module_obj is None:
                self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                print("TestBoundaryConditionsComprehensive = Failed")
                return

            # Check all required functions exist
            required_functions = [
                "convert_string_to_datetime",
                "format_datetime",
                "calculate_date_difference",
                "add_time_duration",
                "get_day_of_week",
                "convert_timezone"
            ]
            
            missing_functions = []
            for func_name in required_functions:
                if not check_function_exists(self.module_obj, func_name):
                    missing_functions.append(func_name)
            
            if missing_functions:
                self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                print("TestBoundaryConditionsComprehensive = Failed")
                return

            # SECTION 1: DATE STRING CONVERSION BOUNDARY TESTS
            if check_function_exists(self.module_obj, "convert_string_to_datetime"):
                # Test minimum and maximum dates
                min_date = safely_call_function(self.module_obj, "convert_string_to_datetime", "0001-01-01")
                if min_date is None or not isinstance(min_date, datetime):
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return
                if min_date.year != 1 or min_date.month != 1 or min_date.day != 1:
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return

                future_date = safely_call_function(self.module_obj, "convert_string_to_datetime", "9999-12-31")
                if future_date is None or not isinstance(future_date, datetime):
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return
                if future_date.year != 9999 or future_date.month != 12 or future_date.day != 31:
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return

                # Test leap year boundary
                leap_date = safely_call_function(self.module_obj, "convert_string_to_datetime", "2024-02-29")
                if leap_date is None or not isinstance(leap_date, datetime):
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return
                if leap_date.year != 2024 or leap_date.month != 2 or leap_date.day != 29:
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return

                # Test date with time
                datetime_string = safely_call_function(self.module_obj, "convert_string_to_datetime", "2025-03-19 14:30:00")
                if datetime_string is None or not isinstance(datetime_string, datetime):
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return
                if (datetime_string.year != 2025 or datetime_string.month != 3 or 
                    datetime_string.day != 19 or datetime_string.hour != 14 or datetime_string.minute != 30):
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return

            # SECTION 2: DATE DIFFERENCE CALCULATION BOUNDARY TESTS
            if check_function_exists(self.module_obj, "calculate_date_difference"):
                # Test same date difference
                same_date = datetime(2025, 3, 19, 12, 0)
                diff = safely_call_function(self.module_obj, "calculate_date_difference", same_date, same_date)
                if diff is None or not isinstance(diff, dict):
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return
                if diff.get("days") != 0 or diff.get("hours") != 0 or diff.get("minutes") != 0:
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return

                # Test negative date difference
                start = datetime(2025, 3, 19)
                end = datetime(2025, 3, 18)
                diff = safely_call_function(self.module_obj, "calculate_date_difference", start, end)
                if diff is None or not isinstance(diff, dict):
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return
                if diff.get("days") != -1:
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return

                # Test string input handling
                string_diff = safely_call_function(self.module_obj, "calculate_date_difference", "2025-03-19", "2025-03-26")
                if string_diff is None or not isinstance(string_diff, dict):
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return
                if string_diff.get("days") != 7:
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return

                # Test large date difference
                large_start = datetime(2000, 1, 1)
                large_end = datetime(2025, 12, 31)
                large_diff = safely_call_function(self.module_obj, "calculate_date_difference", large_start, large_end)
                if large_diff is None or not isinstance(large_diff, dict):
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return
                if large_diff.get("days") <= 0:
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return

            # SECTION 3: TIME DURATION ADDITION BOUNDARY TESTS
            if check_function_exists(self.module_obj, "add_time_duration"):
                # Test zero duration
                dt = datetime(2025, 3, 19, 12, 0)
                new_dt = safely_call_function(self.module_obj, "add_time_duration", dt, days=0, hours=0, minutes=0)
                if new_dt is None or not isinstance(new_dt, datetime) or new_dt != dt:
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return

                # Test negative duration
                negative_dt = safely_call_function(self.module_obj, "add_time_duration", dt, days=-1, hours=-2, minutes=-30)
                if negative_dt is None or not isinstance(negative_dt, datetime):
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return
                expected = datetime(2025, 3, 18, 9, 30)
                if negative_dt != expected:
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return

                # Test string input handling
                string_dt = safely_call_function(self.module_obj, "add_time_duration", "2025-03-19 12:00:00", days=1, hours=2)
                if string_dt is None or not isinstance(string_dt, datetime):
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return
                expected = datetime(2025, 3, 20, 14, 0)
                if string_dt != expected:
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return

                # Test large duration
                large_dt = safely_call_function(self.module_obj, "add_time_duration", dt, days=365, hours=24, minutes=60)
                if large_dt is None or not isinstance(large_dt, datetime) or large_dt.year != 2026:
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return

                # Test month/year boundary crossing
                boundary_dt = safely_call_function(self.module_obj, "add_time_duration", "2025-01-31", days=31)
                if boundary_dt is None or not isinstance(boundary_dt, datetime):
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return
                if boundary_dt.month != 3 or boundary_dt.year != 2025:
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return

            # SECTION 4: DAY OF WEEK BOUNDARY TESTS
            if check_function_exists(self.module_obj, "get_day_of_week"):
                # Test weekday detection at year boundaries
                jan1 = safely_call_function(self.module_obj, "get_day_of_week", "2025-01-01")
                if jan1 is None or not isinstance(jan1, str) or len(jan1) == 0:
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return

                dec31 = safely_call_function(self.module_obj, "get_day_of_week", "2025-12-31")
                if dec31 is None or not isinstance(dec31, str) or len(dec31) == 0:
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return

                # Test datetime object input
                dt_input = datetime(2025, 3, 19)
                weekday_dt = safely_call_function(self.module_obj, "get_day_of_week", dt_input)
                if weekday_dt is None or not isinstance(weekday_dt, str) or len(weekday_dt) == 0:
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return

                # Test leap year date
                leap_weekday = safely_call_function(self.module_obj, "get_day_of_week", "2024-02-29")
                if leap_weekday is None or not isinstance(leap_weekday, str):
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return

                # Test known weekday
                known_date = safely_call_function(self.module_obj, "get_day_of_week", "2025-03-19")
                if known_date is None or not isinstance(known_date, str) or known_date != "Wednesday":
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return

            # SECTION 5: TIMEZONE CONVERSION BOUNDARY TESTS
            if check_function_exists(self.module_obj, "convert_timezone"):
                # Test same offsets
                dt = datetime(2025, 3, 19, 12, 0)
                same_tz = safely_call_function(self.module_obj, "convert_timezone", dt, -5, -5)
                if same_tz is None or not isinstance(same_tz, datetime) or same_tz != dt:
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return

                # Test maximum timezone difference
                max_diff = safely_call_function(self.module_obj, "convert_timezone", dt, -12, 14)
                if max_diff is None or not isinstance(max_diff, datetime):
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return
                expected = datetime(2025, 3, 20, 14, 0)
                if max_diff != expected:
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return

                # Test string input handling
                string_tz = safely_call_function(self.module_obj, "convert_timezone", "2025-03-19 12:00:00", -5, -8)
                if string_tz is None or not isinstance(string_tz, datetime):
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return
                expected = datetime(2025, 3, 19, 9, 0)
                if string_tz != expected:
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return

                # Test crossing date boundary
                late_time = datetime(2025, 3, 19, 23, 30)
                cross_date = safely_call_function(self.module_obj, "convert_timezone", late_time, -8, 3)
                if cross_date is None or not isinstance(cross_date, datetime) or cross_date.day != 20:
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return

            # SECTION 6: FORMAT DATETIME BOUNDARY TESTS
            if check_function_exists(self.module_obj, "format_datetime"):
                # Test default format
                dt = datetime(2025, 3, 19, 14, 30, 45)
                default_format = safely_call_function(self.module_obj, "format_datetime", dt)
                if default_format is None or not isinstance(default_format, str) or len(default_format) == 0:
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return

                # Test custom format
                custom_format = safely_call_function(self.module_obj, "format_datetime", dt, "%B %d, %Y at %I:%M %p")
                if custom_format is None or not isinstance(custom_format, str) or "March" not in custom_format:
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return

                # Test edge date formatting
                edge_date = datetime(1, 1, 1, 0, 0, 0)
                edge_format = safely_call_function(self.module_obj, "format_datetime", edge_date, "%Y-%m-%d")
                if edge_format is None or not isinstance(edge_format, str) or edge_format != "0001-01-01":
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return

            # SECTION 7: ADDITIONAL EDGE CASES
            if check_function_exists(self.module_obj, "convert_string_to_datetime"):
                # Test century and millennium boundaries
                century_boundary = safely_call_function(self.module_obj, "convert_string_to_datetime", "2000-01-01")
                if century_boundary is None or century_boundary.year != 2000:
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return

                millennium_boundary = safely_call_function(self.module_obj, "convert_string_to_datetime", "1000-01-01")
                if millennium_boundary is None or millennium_boundary.year != 1000:
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return

            # Test time precision boundaries
            if check_function_exists(self.module_obj, "calculate_date_difference"):
                precise_start = datetime(2025, 3, 19, 12, 0, 0)
                precise_end = datetime(2025, 3, 19, 12, 0, 1)
                precise_diff = safely_call_function(self.module_obj, "calculate_date_difference", precise_start, precise_end)
                if precise_diff is None or precise_diff.get("total_seconds") != 1:
                    self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
                    print("TestBoundaryConditionsComprehensive = Failed")
                    return

            # All tests passed
            self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", True, "boundary")
            print("TestBoundaryConditionsComprehensive = Passed")

        except Exception as e:
            self.test_obj.yakshaAssert("TestBoundaryConditionsComprehensive", False, "boundary")
            print("TestBoundaryConditionsComprehensive = Failed")

if __name__ == '__main__':
    unittest.main()