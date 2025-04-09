<h2>Cleaning Data in Python</h2>

https://app.datacamp.com/learn/courses/cleaning-data-in-python

<h3>Chapter 1: Common Data Problems</h3>

<b>String to Int</b>
```python
# Print sum of all Revenue column (currently an "object" dtype since it is a string)
sales['Revenue'].sum()
# Output: '2351$1457$32474$'...

# Remove $ symbol from Revenue column
sales['Revenue'] = sales['Revenue'].str.strip('$')
# int rather than float because there are no decimals
sales['Revenue'] = sales['Revenue'].astype('int')

# Verify that Revenue is now an integer; assert returns nothing if condition is met, error if not.
assert sales['Revenue'].dtype == 'int'
```

<b>Numeric vs Categorical</b>

* There is a marriage dataset with the following values representing certain categories:

`0` = Never Married
`1` = Married
`2` = Separated
`3` = Divorced

* This below code will give misleading results when interpreting statistical summaries since `marriage_status` will be 
  imported as an integer.
```python
df['marriage_status'].describe()

# Convert to categorical rather than numeric value type
df['marriage_status'] = df['marriage_status'].astype('category')

# Now this returns count, unique, top, freq — intuitive statistical summary for a categorical column 
df.describe()
```

* It is important to always check the `.dtypes` attribute or the `.info()` method of a Pandas DataFrame when working 
  with new data. Manipulating and analyzing data with incorrect data types could lead to compromised analysis as you 
  go along the analytics workflow. There are often columns that need to be converted to different data types before 
  you start any analysis.

* We'll be looking at San Francisco bicycle ride sharing data in the `ride_sharing` DataFrame throughout this chapter.
```python
# Print the information of ride_sharing
print(ride_sharing.info())

# Print summary statistics of user_type column
print(ride_sharing['user_type'].describe())
```

* The `user_type` column should be converted from int to category data type, as we saw earlier, to get more accurate 
  summary statistics.
```python
# Convert user_type from integer to category
ride_sharing['user_type_cat'] = ride_sharing['user_type'].astype('category')

# Write an assert statement confirming the change
assert ride_sharing['user_type_cat'].dtype == 'category'

# Print new summary statistics 
print(ride_sharing['user_type_cat'].describe())
```

* Another common data type problem is importing what should be numerical values as strings, which leads mathematical 
  operations such as summing and multiplication to string concatenation rather than numerical outputs.

```python
# Let's also convert user_gender to categorical dtype
ride_sharing['user_gender'] = ride_sharing['user_gender'].astype('category')

# Remove the 'minutes' from duration values so we are just left with the number of minutes; rename to duration_trim
ride_sharing['duration_trim'] = ride_sharing['duration'].str.strip('minutes')
# Convert to int now that there is just the number of minutes in the value
ride_sharing['duration_minutes'] = ride_sharing['duration_trim'].astype('int')

# Assert to make sure of the conversion
assert ride_sharing['duration_minutes'].dtype == 'int'

print(ride_sharing[['duration', 'duration_trim', 'duration_minutes']])
# Now we can easily compute the average number of minutes for a ride
print(ride_sharing['duration_minutes'].mean())
```

* As an aside here, here's how to check that the values for a column are following the same schema (e.g., validate 
  that all `bike_id` values are a 4-digit code):
```python
# Check if all bike_id values are a 4-digit numeric pattern
is_valid = ride_sharing['bike_id'].astype(str).str.match(r'^\d{4}$')
# Invert the boolean mask to get only invalid rows
invalid_entries = ride_sharing[~is_valid]

print("Invalid entries:", invalid_entries)
```

<b>Data Range Constraints</b>

* If movie or product reviews are supposed to be between 1 and 5, there shouldn't be any values outside of that 
  range. There often are though, and these are due to human or technical errors.
* Another common error is seeing events that happened in the future (e.g., a user sign up 5 years from now in the 
  future).
* How should we deal with out of range data?
  * Simplest: drop the data. However, if it is a lot of your data, you could be missing important information. As a 
    general rule, only drop data when a small portion of your dataset is impacted by out of range values. Make sure 
    you understand your dataset before dropping values.
  * Set custom minimums and maximums
  * Treat data as missing and impute it
  * Set a custom value for values that go beyond a certain range

* In the movie rating dataset, where ratings should be between 1 and 5:

```python
# Drop values using filtering
movies = movies[movies['avg_rating'] <= 5]

#Drop values using .drop() method
movies.drop(movies[movies['avg_rating'] > 5].index, inplace=True)

# Assert that avg_rating is now lte 5 after dropping
assert movies['avg_rating'].max() <= 5

# Convert avg_rating to 5 if it is beyond 5
movies.loc[movies['avg_rating'] > 5, 'avg_rating'] = 5

# Assert that change was done properly
assert movies['avg_rating'].max() <= 5

```
