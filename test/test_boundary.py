import pytest
from datetime import datetime
from date_time_processor import convert_string_to_datetime, calculate_date_difference, add_time_duration, get_day_of_week, convert_timezone
from test.TestUtils import TestUtils

class TestBoundary:
    """Test cases for boundary conditions in the date time processor."""
    
    def test_boundary_conditions(self):
        """Test all boundary conditions for the date time processor."""
        try:
            # Test minimum and maximum dates
            min_date = convert_string_to_datetime("0001-01-01")
            assert min_date.year == 1 and min_date.month == 1 and min_date.day == 1, "Should handle minimum date"
            
            future_date = convert_string_to_datetime("9999-12-31")
            assert future_date.year == 9999 and future_date.month == 12 and future_date.day == 31, "Should handle maximum date"
            
            # Test same date difference
            same_date = datetime(2025, 3, 19, 12, 0)
            diff = calculate_date_difference(same_date, same_date)
            assert diff["days"] == 0 and diff["hours"] == 0 and diff["minutes"] == 0, "Should return zero difference for same dates"
            
            # Test negative date difference
            start = datetime(2025, 3, 19)
            end = datetime(2025, 3, 18)
            diff = calculate_date_difference(start, end)
            assert diff["days"] == -1 and diff["hours"] == -24, "Should handle negative date differences"
            
            # Test zero duration
            dt = datetime(2025, 3, 19, 12, 0)
            new_dt = add_time_duration(dt, days=0, hours=0, minutes=0)
            assert new_dt == dt, "Should return same datetime with zero duration"
            
            # Test negative duration
            negative_dt = add_time_duration(dt, days=-1, hours=-2, minutes=-30)
            expected = datetime(2025, 3, 18, 9, 30)
            assert negative_dt == expected, "Should handle negative durations correctly"
            
            # Test weekday detection at boundaries
            jan1 = get_day_of_week("2025-01-01")
            dec31 = get_day_of_week("2025-12-31")
            assert isinstance(jan1, str) and len(jan1) > 0, "Should return weekday name for January 1st"
            assert isinstance(dec31, str) and len(dec31) > 0, "Should return weekday name for December 31st"
            
            # Test timezone same offsets
            dt = datetime(2025, 3, 19, 12, 0)
            same_tz = convert_timezone(dt, -5, -5)
            assert same_tz == dt, "Should return same time when source and target timezone are identical"
            
            # Test timezone maximum difference
            max_diff = convert_timezone(dt, -12, 14)  # From UTC-12 to UTC+14 (26 hours difference)
            expected = datetime(2025, 3, 20, 14, 0)
            assert max_diff == expected, "Should handle maximum timezone difference correctly"
            
            TestUtils.yakshaAssert("test_boundary_conditions", True, "boundary")
        except Exception as e:
            TestUtils.yakshaAssert("test_boundary_conditions", False, "boundary")
            raise e