# Project: Data Analysis for Hospitals

A project with .csv data preparation, analysis, and visualization using `dropna()`, `value_counts()`, `loc` with conditions, `pivot_table()`, `plot()`, and other pandas functions.


https://hyperskill.org/projects/152?track=10


## Tasks:

Stages 1-3
1. Read the CSV files with datasets.
2. Change the column names. The column names of the sports and prenatal tables must match the column names of the general table.
3. Merge the dataframes into one. Use the `ignore_index=True` parameter and the following order: `general`, `prenatal`, `sports`.
4. Delete the `Unnamed: 0` column.
5. Print random 20 rows of the resulting data frame. For the reproducible output set `random_state=30`.
6. Delete all the empty rows.
7. Correct all the gender column values to `f` and `m` respectively.
8. Replace the NaN values in the gender column of the prenatal hospital with `f`.
9. Replace the NaN values in the `bmi`, `diagnosis`, `blood_test`, `ecg`, `ultrasound`, `mri`, `xray`, `children`, `months` columns with zeros.
   
Stage 4:
10. Answer the 1-5 questions using the pandas library methods. Output the answers on the separate lines in the format given in the Example section.
    1. Which hospital has the highest number of patients?
    2. What share of the patients in the general hospital suffers from stomach-related issues? Round the result to the third decimal place.
    3. What share of the patients in the sports hospital suffers from dislocation-related issues? Round the result to the third decimal place.
    4. What is the difference in the median ages of the patients in the general and sports hospitals?
    5. After data processing at the previous stages, the `blood_test` column has three values: t= a blood test was taken, `f` = a blood test wasn't taken, and `0` = there is no information. In which hospital the blood test was taken the most often (there is the biggest number of t in the `blood_test` column among all the hospitals)? How many blood tests were taken?
       

Stage 5:
12. Answer questions 1-3. Output the answers in the specified format. The answers to the first two questions should be formatted as in the examples. No special form is required to answer the third question.
    1. What is the most common age of a patient among all hospitals? Plot a histogram and choose one of the following age ranges: 0-15, 15-35, 35-55, 55-70, or 70-80.
    2. What is the most common diagnosis among patients in all hospitals? Create a pie chart.
    3. Build a violin plot of height distribution by hospitals. Try to answer the questions. What is the main reason for the gap in values? Why there are two peaks, which correspond to the relatively small and big values? No special form is required to answer this question.
       There is a comprehensive explanation of violin plots by Eryk Lewinson.

