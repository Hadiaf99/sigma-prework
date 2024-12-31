import datetime


def date_calculator(x):

    x = datetime.datetime.strptime(x, "%d-%m-%Y")
    date_now = datetime.datetime.now()
    # date_now = datetime.datetime.strptime(str(date_now), "%d-%m-%Y")
    age = date_now.year - x.year
    return age


result = date_calculator('04-12-1972')
print(f'The age between the two dates is: {result} years')
