'''
INSTRUCTIONS:

Write a function named "add_time" that takes in two required parameters and one optional parameter:

- a start time in the 12-hour clock format (ending in AM or PM)
- a duration time that indicates the number of hours and minutes
- (optional) a starting day of the week, case insensitive

The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show "(next day)" after the time. If the result will be more than one day later,
it should show "(n days later)" after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result.
The day of the week in the output should appear after the time and before the number of days later.

Below are some examples of different cases the function should handle. Pay close attention to the spacing and punctuation of the results.

add_time("3:00 PM", "3:10")
Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
Returns: 12:03 PM

add_time("10:10 PM", "3:30")
Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
Returns: 7:42 AM (9 days later)

Do not import any Python libraries. Assume that the start times are valid times.
The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.
'''

def add_time(start, duration, start_day_week=None):
    '''
    Description:
        This function takes in start and duration times, adds them together and returns the result.
        Optionally, it could receive a third parameter indicating the starting day of the week.
    
    Args:
        - start: a start time in the 12-hour clock format (ending in AM or PM)
        - duration: a duration time that indicates the number of hours and minutes
        - start_day_week [optional]: the starting day of the week, case insensitive
    
    Returns:
        Returns the result of adding the duration to the start time
    '''

    # Split time and AM/PM from start time
    start_split = start.split(' ')

    # Take hours, mins and AM/PM
    start_hh = int(start_split[0].split(':')[0])
    start_mm = int(start_split[0].split(':')[1])
    start_am_pm = start_split[1]

    # Take hours and mins from duration time
    duration_hh = int(duration.split(':')[0])
    duration_mm = int(duration.split(':')[1])

    # Handle minutes
    # Add start and duration minutes together and calculate the remainder of the division by 60
    sum_mm = start_mm + duration_mm
    result_mm = sum_mm % 60
    # Convert to string (if remainder consists of a single digit add a 0 before it)
    if result_mm < 10:
        result_mm = "0" + str(result_mm)
    else:
        result_mm = str(result_mm)
    
    # If the sum of minutes is greater than 60, add a carryover by 1 to the hours (the max value of the sum
    # will never be greater than 118 because the maximum value of minutes is 59, so carryover will not be greater than 1)
    carry_to_hh = 0
    if sum_mm > 60:
        carry_to_hh = 1
    
    # Handle hours
    # Add start and duration hours together considering carryover too and calculate the remainder of the division by 12
    sum_hh = start_hh + duration_hh + carry_to_hh
    result_hh = sum_hh % 12
    # Convert to string (if remainder = 0, set it to 12)
    if result_hh == 0:
        result_hh = "12"
    else:
        result_hh = str(result_hh)
    
    # Handle AM/PM
    # Find number of clock revolutions dividing the sum of the hours by 12 and keeping only the whole part of the result
    clock_rounds = sum_hh // 12
    # If number of clock revolutions is even confirm AM/PM indicated in start time, else change it
    if clock_rounds % 2:
        if start_am_pm == 'AM':
            result_am_pm = 'PM'
        else:
            result_am_pm = 'AM'
    else:
        result_am_pm = start_am_pm

    # Handle number of subsequent days
    # If there have been no complete clock revolutions the day doesn't change
    if clock_rounds == 0:
        next_days = 0
    # Else, obtain the number of days to add, dividing number of clock revolutions by 2 and keeping only the whole part of the result
    else:
        next_days = clock_rounds // 2
        # If PM, add 1 day to the result
        if start_am_pm == 'PM':
            next_days += 1
    # Create string to return
    if next_days == 0:
        result_next_days = ""
    elif next_days == 1:
        result_next_days = " (next day)"
    else:
        result_next_days = " ("+ str(next_days) + " days later)"
    
    # Handle weekday (if argument is passed)
    if not start_day_week is None:
        start_day_week = start_day_week.capitalize()
        
        # Create a tuple containing all the weekdays
        days_of_week = (('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'))
        
        # Look for the day passed as an argument and extract its position in the tuple
        start_day_week_pos = days_of_week.index(start_day_week)

        # Add the position to the number of subsequent days calculated previously
        # and find the index in the tuple keeping the remainder of the division by 7
        final_day_week_pos = (start_day_week_pos + next_days) % 7

        # Extract the day of the week from the tuple
        result_day_of_week = days_of_week[final_day_week_pos]

    # Set the final string:
    # - without weekday
    if start_day_week is None:
        new_time = result_hh + ":" + result_mm + " " + result_am_pm + result_next_days
    # with weekday
    else:
        new_time = result_hh + ":" + result_mm + " " + result_am_pm + ", " + result_day_of_week + result_next_days
    
    # Return final string
    return new_time
