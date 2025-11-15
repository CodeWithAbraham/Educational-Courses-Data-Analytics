import pandas as pd 
import numpy as np

#Loading the dataset
df=pd.read_csv("courses_en.csv") 

# Count duplicates before drop
duplicates_before = df.duplicated().sum()
print("Duplicate rows before removing:", duplicates_before)

# Remove duplicate rows 
df = df.drop_duplicates(keep='first')

#preview the first few rows 
print(df.head(5)) 

#Using iloc to select first 10 rows and first 5 columns
print("\nFirst 10 rows and first 5 columns using iloc:")
print(df.iloc[:10, :5])

#Check basic info  
print(df.info(5))

#check descriptive statistics
print(df.describe())     

# Value counts for categorical columns 
print("Category distribution:\n", df['category'].value_counts())

# Course Duration - cyclical assignment
course_duration = ['Short', 'Medium', 'Long'] * ((len(df) // 3) + 1)
course_duration = course_duration[:len(df)]
df.insert(7, column='Course_Duration', value=course_duration) 

# Course Format - repeated pattern
course_format = ['Video', 'Text', 'Interactive', 'Mixed'] * ((len(df) // 4) + 1)
course_format = course_format[:len(df)]
df.insert(9, column='Course_Format', value=course_format)

# Show missing values count
print("Missing values per column:")
print(df.isnull().sum())  

# Sort the dataset by a specific column 
df = df.sort_values(by='name', ascending=True) 
print(df) 

# Group by 'Category' and count the number of entries in a specific column 'Name'
grouped_counts = df.groupby('category')['name'].count()
print(grouped_counts)

# Create a sample 'other_df' for demonstration 
other_df = pd.DataFrame({
    'category': ['Information Technology', 'Business'],
    'Extra_Info': [10, 20]
})

# Merge the dataframes on the 'category' column
merged_df = pd.merge(df, other_df, on='category', how='inner') 
 
# Print the merged DataFrame
print(merged_df) 

# Map 'Course_Duration' to numerical values
duration_map = {'Short': 1, 'Medium': 2, 'Long': 3}
df['Course_Duration_Num'] = np.array(df['Course_Duration'].map(duration_map))

# Convert course names to their length (number of characters) for numeric std calculation
name_length = np.array(df['name'].str.len())

# Compute statistics with NumPy on numeric columns
mean_duration = np.mean(df['Course_Duration_Num'])
std_name_length = np.std(name_length)

print("Average Course Duration (numeric):", mean_duration)
print("Std Dev of Name Length:", std_name_length)

# Detect missing values in 'Course_Duration_Num' 
missing_duration = np.sum(np.isnan(df['Course_Duration_Num']))
print("Missing values in Course_Duration_Num:",missing_duration)

# convert csv to excel
df.to_excel("final_courses_dataset2.xlsx", index=False)

