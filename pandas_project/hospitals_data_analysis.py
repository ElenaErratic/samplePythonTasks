import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Stage 1
pd.set_option('display.max_columns', 8)
general = pd.read_csv('datasets/general.csv')
prenatal = pd.read_csv('datasets/prenatal.csv')
sports = pd.read_csv('datasets/sports.csv')
# print(ah.shape)

# Stage 2
prenatal.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)
sports.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)

'''ah = (
    pd.concat([general, prenatal, sports], ignore_index=True)
        .drop(columns='Unnamed: 0')
)
print(ah.sample(n=20, random_state=30))
'''

# Stage 3
ah = (
    pd.concat([general, prenatal, sports], ignore_index=True)
        .drop(columns='Unnamed: 0')
        .dropna(axis=0, thresh=1)
        .replace(['female', 'male', 'woman', 'man'], ['f', 'm', 'f', 'm'])
        .fillna({'gender': 'f'})
        .fillna({'bmi': 0, 'diagnosis': 0, 'blood_test': 0, 'ecg': 0, 'ultrasound': 0, 'mri': 0, 'xray': 0, 'children': 0, 'months': 0})
)
# print(ah.sample(n=20, random_state=30))

# Stage 4
answer_one = ah.hospital.value_counts().idxmax()

answer_two = (ah.hospital.loc[(ah['hospital'] == 'general') & (ah['diagnosis'] == 'stomach')].count() / ah.hospital.loc[(ah['hospital'] == 'general')].count()).round(3)

answer_three = (ah.hospital.loc[(ah['hospital'] == 'sports') & (ah['diagnosis'] == 'dislocation')].count() / ah.hospital.loc[(ah['hospital'] == 'sports')].count()).round(3)

age_in_general = ah.age.loc[(ah['hospital'] == 'general')].median()
age_in_sports = ah.age.loc[(ah['hospital'] == 'sports')].median()
answer_four = abs(int(age_in_general - age_in_sports))

max_hospital = ah.loc[ah.blood_test == 't'].hospital.value_counts().idxmax()
n = ah.loc[ah.blood_test == 't'].hospital.value_counts().max()
answer_five = f'{max_hospital}, {n} blood tests'


message = 'The answer to the {} question is'
dictionary = {'1st': answer_one, '2nd': answer_two, '3rd': answer_three, '4th': answer_four, '5th': answer_five}
for key, value in dictionary.items():
    print(f'{message} {value}'.format(key))


# Stage 5
bins_list = [0, 15, 35, 55, 70, 80]
ah.plot(y=['age'], kind='hist', bins=bins_list)
plt.show()
ah['diagnosis'].value_counts().plot(kind='pie', subplots=True)
plt.show()

# https://towardsdatascience.com/violin-plots-explained-fb1d115e023d

def plot_comparison(x, title):
    fig, ax = plt.subplots(3, 1, sharex=True)
    sns.distplot(x, ax=ax[0])
    ax[0].set_title('Histogram + KDE')
    sns.boxplot(x, ax=ax[1])
    ax[1].set_title('Boxplot')
    sns.violinplot(x, ax=ax[2])
    ax[2].set_title('Violin plot')
    fig.suptitle(title, fontsize=16)
    plt.show()
plot_comparison(ah.height, 'Height Distribution by Hospitals')

print('The answer to the 1st question: 15-35')
print('The answer to the 2nd question: pregnancy')
print('The answer to the 3rd question: It\'s because of different units of measurement in general, prenatal (m) and sports(ft)')
