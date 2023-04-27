from datetime import datetime
import pytz

# function to perfom the date-time transformation from one timezone to another timezone
def transform(us_central):
    try:
        # Create a datetime object from the user input
        us_central_dt = datetime.strptime(us_central, '%Y-%m-%d %H:%M:%S')

        # Get the timezone object for US/Central timezone
        us_central_tz = pytz.timezone('US/Central')

        # Associate the datetime object with the timezone
        us_central_dt = us_central_tz.localize(us_central_dt, is_dst=None)

        # Convert the datetime object to the Asia/Kolkata timezone
        asia_kolkata_tz = pytz.timezone('Asia/Kolkata')
        asia_kolkata_dt = us_central_dt.astimezone(asia_kolkata_tz)

        return asia_kolkata_dt.strftime('%m/%d/%Y %A %I:%M %p %Z')    
    
    except Exception as e:
        return False

if __name__ == "__main__":
    
    # Get the user input for the date-time in US/Central timezone
    input_dt_str = input("Enter date-time in US/Central timezone (YYYY-MM-DD HH:MM:SS): ")

    # Calling the function to perform the date-time transformation from one timezone to another timezone
    target_dt = transform(input_dt_str)

    if target_dt:
        # Print the result in different formats
        #print(target_dt.strftime('%Y-%m-%d %H:%M:%S %Z%z')) # YYYY-MM-DD HH:MM:SS Timezone+-offset
        print("The date-time in Asia/Kolkata timezone is:", target_dt)
        
    else:
        print("Please enter a valid DateTime!!!")