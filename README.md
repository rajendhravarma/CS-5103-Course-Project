# CS-5103-Course-Project
**Date Time Transformation:** In this project we are writing a program to transform the given datetime string to different format.

**Filenames:**

**project.py:** This file transforms input date-time string from the user from US/central to Asia/Kolkata Timezone.

**testcases.py:** This file contains the test cases for the project.py file. 

**Test cases are :** 

1. test_valid_output_dst 
2. test_valid_output_non_dst, 
3. test_invalid_time,
4. test_invalid_hours_format, 
5. test_invalid_date_format, 
6. test_invalid_format_all_zeros,
7. test_invalid_date_time.

**Steps:**

1) Running the program in VScode:
Download the project.py and the testcases.py.
Run the file project.py by giving the command python project.py. Once the program is ran, you will be asked to enter the input of the datetime string(Follow the format that was mentioned while giving the input). By default the input given by the user is taken as CST format. Then the date-time conversion is done for the user input string from US/Central to Asia/Kolkata and O/P is generated.

As per the first requirement change, we are populating the day of the week along with the DateTimeTransformation.

**Output format:** MM/DD/YYYY DayofWeek HH:MM:SS TimeZone
![image](https://user-images.githubusercontent.com/52074918/234763214-f2817aa0-2dfb-4734-8243-c3b535063119.png)

![image](https://user-images.githubusercontent.com/52074918/234763308-ce54cf59-9a71-4424-8ea0-3f6e19c3997a.png)

2) Run the file testcases.py by giving the command python testcases.py. Once the program is ran, you will be displayed with the results of the test cases if they are passed or not.

![image](https://user-images.githubusercontent.com/52074918/234763411-e1c75cb9-2c94-4bba-982b-be34a3b7a9b0.png)

![image](https://user-images.githubusercontent.com/52074918/234763462-8746c495-671b-448c-be03-d042e8674419.png)


