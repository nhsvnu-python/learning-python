import pandas as pd

df = pd.read_csv("1000employee.csv")
today = pd.Timestamp.today()
print(today)
print('Name', 'Life day')
for index, row in df.iterrows():
    First_name = row['First Name']
    Last_name = row['Last Name']
    date_of_birth = row['Date of Birth']
    date_of_birth = date_of_birth[:6] + '19' + date_of_birth[6:]

    # dob = row["Date of Birth"]d
    # df["Date of Birth"].format(format='%m/%d/%y')

    DayLives = today - pd.to_datetime(date_of_birth, format='%m/%d/%y')

    print(First_name, Last_name, date_of_birth, DayLives.days)
