import pytz
from datetime import datetime

def transform(input_dt_str, out_time):

    input_dt_format = '%Y-%m-%d %H:%M:%S'

    try:
            
        # Create a datetime object from the input string
        input_dt = datetime.strptime(input_dt_str, input_dt_format)

        # Define the time zone to convert to
        if out_time=='MST':
            target_tz = pytz.timezone('US/Mountain')
        elif out_time=='EST':
            target_tz = pytz.timezone('US/Eastern')
        #elif out_time=='CDT':
        #    target_tz = pytz.timezone('US/Central')
        elif out_time=='PST':    
            target_tz = pytz.timezone('US/Pacific')
        else:
            return False

        # Convert the datetime object to the target time zone
        target_dt = input_dt.astimezone(target_tz)

        return target_dt.strftime('%m/%d/%Y %I:%M %p %Z')
    except Exception as e:
        return False


if __name__ == "__main__":
    # Define the input datetime string and its format
    print('NOTE: Input timezone is always CDT!!')
    input_dt_str = input('Enter datetime in following format (yyyy-mm-dd hh:mm:ss): ')

    out_time = input('Enter an output US Timezone (EST/MST/PST):').upper()


    target_dt = transform(input_dt_str, out_time)
    if target_dt:
        # Print the result in different formats
        #print(target_dt.strftime('%Y-%m-%d %H:%M:%S %Z%z')) # YYYY-MM-DD HH:MM:SS Timezone+-offset
        print(target_dt) # YYYY-MM-DD HH:MM:SS Timezone
    else:
        print("Please enter a valid Timezone!!!")