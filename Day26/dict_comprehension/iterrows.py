# iterrows is a method in pandas that allows you to iterate over the rows of a DataFrame as (index, Series) pairs.

import pandas as pd

student_dict = {
    "student": ["Sunil", "Lily", "Alex"],
    "score": [69, 69, 69]
}

# for key, value in student_dict.items():
#     print(value)

student_data_frame = pd.DataFrame(student_dict)
# print(student_data_frame)

# iterrows Loop through rows of a dataframe
for(index,row) in student_data_frame.iterrows():
    # print(row)        # This will print each row as a Series
    # print(row.score)
    if row.student == "Sunil":
        print(row.score)
        