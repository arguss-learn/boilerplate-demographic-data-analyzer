import pandas as pd


def calculate_demographic_data(print_data=True):
    ## Read data from file
    df = pd.read_csv('adult.data.csv', sep=',', skipinitialspace=True)

    # How many of each race are represented in this data set?
    race_count = df['race'].value_counts()

    # What is the average age of men?
    men = df[df['sex'] == 'Male']
    average_age_men = round(men['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    total_people = df.shape[0]
    bachelors_count = df[df['education'] == 'Bachelors'].shape[0]
    percentage_bachelors = round((bachelors_count / total_people) * 100, 1)

    # What percentage of people with advanced education earn more than 50K?
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_count = higher_education.shape[0]
    higher_education_rich = round((higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education_count) * 100, 1)

    # What percentage of people without advanced education earn more than 50K?
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_count = lower_education.shape[0]
    lower_education_rich = round((lower_education[lower_education['salary'] == '>50K'].shape[0] / lower_education_count) * 100, 1)

    # What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min() 

    # What percentage of people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df[df['hours-per-week'] == min_work_hours]
    num_min_workers = min_workers[min_workers['salary'] == '>50K'].shape[0]
    rich_percentage = round((num_min_workers / min_workers.shape[0]) * 100, 1) if min_workers.shape[0] > 0 else 0

    # Country with the highest percentage of rich people?
    country_salary_counts = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack().fillna(0)
    country_salary_counts['>50K_percentage'] = country_salary_counts['>50K'] * 100
    highest_earning_country = country_salary_counts['>50K_percentage'].idxmax()
    highest_earning_country_percentage = round(country_salary_counts['>50K_percentage'].max(), 1)
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
