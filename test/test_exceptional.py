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

def check_raises(func, args, expected_exception=Exception):
    """Check if a function raises an expected exception."""
    try:
        func(*args)
        return False
    except expected_exception:
        return True
    except Exception:
        return False

def load_module_dynamically():
    """Load the student's module for testing"""
    module_obj = safely_import_module("skeleton")
    if module_obj is None:
        module_obj = safely_import_module("solution")
    return module_obj

class TestExceptionHandling(unittest.TestCase):
    def setUp(self):
        """Standard setup for all test methods"""
        self.test_obj = TestUtils()
        self.module_obj = load_module_dynamically()

    def test_exception_handling_comprehensive(self):
        """Comprehensive test for all exception handling scenarios"""
        try:
            if self.module_obj is None:
                self.test_obj.yakshaAssert("TestExceptionHandlingComprehensive", False, "exception")
                print("TestExceptionHandlingComprehensive = Failed")
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
                self.test_obj.yakshaAssert("TestExceptionHandlingComprehensive", False, "exception")
                print("TestExceptionHandlingComprehensive = Failed")
                return

            # SECTION 1: TYPE VALIDATION TESTS
            
            # Test convert_string_to_datetime with invalid types
            if check_function_exists(self.module_obj, "convert_string_to_datetime"):
                invalid_inputs = [None, 20250319, 123, [], {}, True, datetime.now()]
                for invalid_input in invalid_inputs:
                    result = check_raises(
                        self.module_obj.convert_string_to_datetime, 
                        [invalid_input], 
                        (TypeError, ValueError)
                    )
                    if not result:
                        self.test_obj.yakshaAssert("TestExceptionHandlingComprehensive", False, "exception")
                        print("TestExceptionHandlingComprehensive = Failed")
                        return

            # Test format_datetime with invalid types
            if check_function_exists(self.module_obj, "format_datetime"):
                invalid_inputs = ["2025-03-19", None, 123, [], {}, True]
                for invalid_input in invalid_inputs:
                    result = check_raises(
                        self.module_obj.format_datetime, 
                        [invalid_input], 
                        (TypeError, ValueError)
                    )
                    if not result:
                        self.test_obj.yakshaAssert("TestExceptionHandlingComprehensive", False, "exception")
                        print("TestExceptionHandlingComprehensive = Failed")
                        return
                
                # Test with invalid format strings
                valid_dt = datetime(2025, 3, 19)
                invalid_formats = [None, 123, [], {}]
                for invalid_format in invalid_formats:
                    result = check_raises(
                        self.module_obj.format_datetime, 
                        [valid_dt, invalid_format], 
                        (TypeError, ValueError)
                    )
                    if not result:
                        self.test_obj.yakshaAssert("TestExceptionHandlingComprehensive", False, "exception")
                        print("TestExceptionHandlingComprehensive = Failed")
                        return

            # Test calculate_date_difference with invalid types
            if check_function_exists(self.module_obj, "calculate_date_difference"):
                invalid_pairs = [
                    (123, "2025-03-19"),
                    ("2025-03-19", 123),
                    (None, datetime(2025, 3, 19)),
                    (datetime(2025, 3, 19), None),
                    ([], "2025-03-19"),
                    ({}, datetime(2025, 3, 19))
                ]
                
                for start, end in invalid_pairs:
                    result = check_raises(
                        self.module_obj.calculate_date_difference, 
                        [start, end], 
                        (TypeError, ValueError)
                    )
                    if not result:
                        self.test_obj.yakshaAssert("TestExceptionHandlingComprehensive", False, "exception")
                        print("TestExceptionHandlingComprehensive = Failed")
                        return

            # Test add_time_duration with invalid types
            if check_function_exists(self.module_obj, "add_time_duration"):
                # Invalid datetime input
                invalid_dt_inputs = [None, "invalid", 123, [], {}]
                for invalid_dt in invalid_dt_inputs:
                    result = check_raises(
                        self.module_obj.add_time_duration, 
                        [invalid_dt, 1, 1, 1], 
                        (TypeError, ValueError)
                    )
                    if not result:
                        self.test_obj.yakshaAssert("TestExceptionHandlingComprehensive", False, "exception")
                        print("TestExceptionHandlingComprehensive = Failed")
                        return
                
                # Invalid duration inputs
                valid_dt = datetime(2025, 3, 19)
                invalid_duration_sets = [
                    ("2", 5, 10),  # String days
                    (5, "2", 10),  # String hours
                    (5, 5, "10"),  # String minutes
                    (1.5, 5, 10),  # Float days
                    (5, 2.5, 10),  # Float hours
                    (5, 5, 1.5),   # Float minutes
                    ([], 5, 10),   # List days
                    (5, {}, 10),   # Dict hours
                    (5, 5, None)   # None minutes
                ]
                
                for days, hours, minutes in invalid_duration_sets:
                    result = check_raises(
                        self.module_obj.add_time_duration, 
                        [valid_dt, days, hours, minutes], 
                        (TypeError, ValueError)
                    )
                    if not result:
                        self.test_obj.yakshaAssert("TestExceptionHandlingComprehensive", False, "exception")
                        print("TestExceptionHandlingComprehensive = Failed")
                        return

            # Test get_day_of_week with invalid types
            if check_function_exists(self.module_obj, "get_day_of_week"):
                invalid_inputs = [123, None, [], {}, True]
                for invalid_input in invalid_inputs:
                    result = check_raises(
                        self.module_obj.get_day_of_week, 
                        [invalid_input], 
                        (TypeError, ValueError)
                    )
                    if not result:
                        self.test_obj.yakshaAssert("TestExceptionHandlingComprehensive", False, "exception")
                        print("TestExceptionHandlingComprehensive = Failed")
                        return

            # Test convert_timezone with invalid types
            if check_function_exists(self.module_obj, "convert_timezone"):
                # Invalid datetime input
                invalid_dt_inputs = [None, "invalid", 123, [], {}]
                for invalid_dt in invalid_dt_inputs:
                    result = check_raises(
                        self.module_obj.convert_timezone, 
                        [invalid_dt, -5, -8], 
                        (TypeError, ValueError)
                    )
                    if not result:
                        self.test_obj.yakshaAssert("TestExceptionHandlingComprehensive", False, "exception")
                        print("TestExceptionHandlingComprehensive = Failed")
                        return
                
                # Invalid timezone offset types
                valid_dt = datetime(2025, 3, 19)
                invalid_offset_sets = [
                    ("EST", -8),    # String source offset
                    (-5, "PST"),    # String target offset
                    (1.5, -8),      # Float source offset
                    (-5, 2.5),      # Float target offset
                    ([], -8),       # List source offset
                    (-5, {}),       # Dict target offset
                    (None, -8),     # None source offset
                    (-5, None)      # None target offset
                ]
                
                for source, target in invalid_offset_sets:
                    result = check_raises(
                        self.module_obj.convert_timezone, 
                        [valid_dt, source, target], 
                        (TypeError, ValueError)
                    )
                    if not result:
                        self.test_obj.yakshaAssert("TestExceptionHandlingComprehensive", False, "exception")
                        print("TestExceptionHandlingComprehensive = Failed")
                        return

            # SECTION 2: FORMAT VALIDATION TESTS
            
            # Test convert_string_to_datetime with invalid date formats
            if check_function_exists(self.module_obj, "convert_string_to_datetime"):
                definitely_invalid_formats = [
                    "03-19-2025",         # MM-DD-YYYY format
                    "19/03/2025",         # DD/MM/YYYY format
                    "March 19, 2025",     # Text format
                    "2025-13-19",         # Invalid month
                    "2025-03-32",         # Invalid day
                    "2025-02-30",         # Invalid day for February
                    "2024-02-30",         # Invalid day for leap year February
                    "25-03-19",           # 2-digit year
                    "2025/03/19",         # Slash separators
                    "2025.03.19",         # Dot separators
                    "",                   # Empty string
                    "invalid date",       # Completely invalid
                    "2025-03-19 25:00:00", # Invalid hour
                    "2025-03-19 14:60:00", # Invalid minute
                    "2025-03-19 14:30:60"  # Invalid second
                ]
                
                for invalid_format in definitely_invalid_formats:
                    result = check_raises(
                        self.module_obj.convert_string_to_datetime, 
                        [invalid_format], 
                        (ValueError, TypeError)
                    )
                    if not result:
                        self.test_obj.yakshaAssert("TestExceptionHandlingComprehensive", False, "exception")
                        print("TestExceptionHandlingComprehensive = Failed")
                        return

            # Test convert_timezone with invalid offset ranges
            if check_function_exists(self.module_obj, "convert_timezone"):
                valid_dt = datetime(2025, 3, 19)
                invalid_offset_ranges = [
                    (-15, 8),    # Source offset too negative
                    (8, -15),    # Target offset too negative
                    (15, 8),     # Source offset too positive
                    (8, 15),     # Target offset too positive
                    (-20, 5),    # Way out of range negative
                    (5, 20),     # Way out of range positive
                    (-13, 0),    # Just outside lower bound
                    (0, 15)      # Just outside upper bound
                ]
                
                for source, target in invalid_offset_ranges:
                    result = check_raises(
                        self.module_obj.convert_timezone, 
                        [valid_dt, source, target], 
                        (ValueError, TypeError)
                    )
                    if not result:
                        self.test_obj.yakshaAssert("TestExceptionHandlingComprehensive", False, "exception")
                        print("TestExceptionHandlingComprehensive = Failed")
                        return

            # SECTION 3: EXTREME VALUE HANDLING
            
            # Test add_time_duration with extreme values
            if check_function_exists(self.module_obj, "add_time_duration"):
                dt = datetime(2025, 3, 19)
                
                # Test moderately large values first (should work)
                moderate_values = [
                    (365, 0, 0),        # One year
                    (0, 8760, 0),       # One year in hours
                    (0, 0, 525600),     # One year in minutes
                    (-365, 0, 0),       # Negative one year
                    (10000, 0, 0),      # Large but manageable days
                    (-10000, 0, 0)      # Large negative days
                ]
                
                for days, hours, minutes in moderate_values:
                    result = safely_call_function(self.module_obj, "add_time_duration", dt, days=days, hours=hours, minutes=minutes)
                    if result is None:
                        self.test_obj.yakshaAssert("TestExceptionHandlingComprehensive", False, "exception")
                        print("TestExceptionHandlingComprehensive = Failed")
                        return
                    if not isinstance(result, datetime):
                        self.test_obj.yakshaAssert("TestExceptionHandlingComprehensive", False, "exception")
                        print("TestExceptionHandlingComprehensive = Failed")
                        return

            # SECTION 4: STRING INPUT VALIDATION FOR FUNCTIONS THAT ACCEPT BOTH
            
            # Test functions that accept both string and datetime inputs
            mixed_input_functions = [
                ("calculate_date_difference", ["invalid_date", "2025-03-19"]),
                ("calculate_date_difference", ["2025-03-19", "invalid_date"]),
                ("add_time_duration", ["invalid_date", 1, 1, 1]),
                ("get_day_of_week", ["invalid_date"]),
                ("convert_timezone", ["invalid_date", -5, -8])
            ]
            
            for func_name, args in mixed_input_functions:
                if check_function_exists(self.module_obj, func_name):
                    result = check_raises(
                        getattr(self.module_obj, func_name), 
                        args, 
                        (ValueError, TypeError)
                    )
                    if not result:
                        self.test_obj.yakshaAssert("TestExceptionHandlingComprehensive", False, "exception")
                        print("TestExceptionHandlingComprehensive = Failed")
                        return

            # SECTION 5: EDGE CASES AND CONSISTENCY CHECKS
            
            # Test that functions handle edge dates consistently
            if (check_function_exists(self.module_obj, "convert_string_to_datetime") and 
                check_function_exists(self.module_obj, "format_datetime")):
                
                edge_dates = [
                    "0001-01-01",
                    "9999-12-31",
                    "2000-01-01",  # Y2K
                    "2024-02-29"   # Leap year
                ]
                
                for date_str in edge_dates:
                    dt = safely_call_function(self.module_obj, "convert_string_to_datetime", date_str)
                    if dt is not None:
                        formatted = safely_call_function(self.module_obj, "format_datetime", dt, "%Y-%m-%d")
                        if formatted is None:
                            self.test_obj.yakshaAssert("TestExceptionHandlingComprehensive", False, "exception")
                            print("TestExceptionHandlingComprehensive = Failed")
                            return
                        if formatted != date_str:
                            self.test_obj.yakshaAssert("TestExceptionHandlingComprehensive", False, "exception")
                            print("TestExceptionHandlingComprehensive = Failed")
                            return

            # SECTION 6: RETURN TYPE CONSISTENCY
            
            # Test that all functions return appropriate types for valid inputs
            test_dt = datetime(2025, 3, 19, 14, 30)
            
            type_check_functions = [
                ("convert_string_to_datetime", ["2025-03-19"], datetime),
                ("format_datetime", [test_dt], str),
                ("calculate_date_difference", [test_dt, test_dt], dict),
                ("add_time_duration", [test_dt, 1, 1, 1], datetime),
                ("get_day_of_week", [test_dt], str),
                ("convert_timezone", [test_dt, -5, -8], datetime)
            ]
            
            for func_name, args, expected_type in type_check_functions:
                if check_function_exists(self.module_obj, func_name):
                    result = safely_call_function(self.module_obj, func_name, *args)
                    if result is None:
                        self.test_obj.yakshaAssert("TestExceptionHandlingComprehensive", False, "exception")
                        print("TestExceptionHandlingComprehensive = Failed")
                        return
                    if not isinstance(result, expected_type):
                        self.test_obj.yakshaAssert("TestExceptionHandlingComprehensive", False, "exception")
                        print("TestExceptionHandlingComprehensive = Failed")
                        return

            # All tests passed
            self.test_obj.yakshaAssert("TestExceptionHandlingComprehensive", True, "exception")
            print("TestExceptionHandlingComprehensive = Passed")

        except Exception as e:
            self.test_obj.yakshaAssert("TestExceptionHandlingComprehensive", False, "exception")
            print("TestExceptionHandlingComprehensive = Failed")

if __name__ == '__main__':
    unittest.main()