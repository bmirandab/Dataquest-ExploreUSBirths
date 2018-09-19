## Dataquest-ExploreUSBirths

### 1: Introduction to Dataset
1. Read the CSV file "US_births_1994-2003_CDC_NCHS.csv" into a string.
2. Split the string on the newline character ("\n").
3. Display the first 10 values in the resulting list.

### 2: Converting Data Into A List Of Lists
1. Create a function named read_csv() that:
* Takes a single, required argument, a string representing the file name of the CSV file.
* Reads the file into a string, splits the string on the newline character ("\n"), and removes the header row. Assign this list to string_list and create an empty list named final_list.
* Uses a for loop to:
  * Iterate over string_list,
  * Create an empty list named int_fields,
  * Splits each row on the comma delimiter (,) and assigns the resulting list to string_fields,
  * Converts each value in string_fields to an integer and appends to int_fields,
  * Appends int_fields to final_list.
* Returns final_list.
2. Use the read_csv() function to read in the file "US_births_1994-2003_CDC_NCHS.csv" and assign the result to cdc_list.
3. Display the first 10 rows of cdc_list to confirm it's a list of lists, containing only integer values, and no header row.

### 3: Calculating Number Of Births Each Month
1. Create a function named month_births() that:
* Takes a single, required argument, a list of lists.
* Creates an empty dictionary, births_per_month, to store the monthly totals.
* Uses a for loop to:
 * Iterate over the list of lists,
 * Extract the value in the month and births columns,
 * If the month value already exists as a key in births_per_month, the births value is added to the existing value,
 * If the month value doesn't exist as a key in births_per_month, it's created and the associated value is the births value.
* After the loop, return the births_per_month dictionary.
2. Use the month_births() function to calculate the monthly totals for the dataset and assign the result to cdc_month_births. Display the dictionary.

### 4: Calculating Number Of Births Each Day Of Week
1. Create a function named dow_births() that takes a single, required argument (a list of lists) and returns a dictionary containing the total number of births for each unique value of the day_of_week column.
2. Use the dow_births() function to return the day-of-week totals for the dataset and assign the result to cdc_day_births. Display the dictionary.

### 5: Creating A More General Function
1. Create a function named calc_counts() that:
* Takes two, required parameters:
  * data: a list of lists
  * column: the column number we want to calculate the totals for
* Populates and returns a dictionary containing the total number of births for each unique value in the column at position column.
2. Use the calc_counts() function to:
* Return the yearly totals for the dataset and assign the result to cdc_year_births.
* Return the monthly totals for the dataset and assign the result to cdc_month_births.
* Return the day-of-month totals for the dataset and assign the result to cdc_dom_births.
* Return the day-of-week totals for the dataset and assign the result to cdc_dow_births.
  
### 6: Next Steps
1. Write a function that can calculate the min and max values for any dictionary that's passed in.
2. Write a function that extracts the same values across years and calculates the differences between consecutive values to show if number of births is increasing or decreasing.
  * For example, how did the number of births on Saturday change each year between 1994 and 2003?
3. Find a way to combine the CDC data with the SSA data, which you can find here. Specifically, brainstorm ways to deal with the overlapping time periods in the datasets.
