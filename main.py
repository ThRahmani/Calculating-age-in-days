import datetime
birthday = datetime.date(int(input()),int(input()),int(input()))
def day_calculator(date):
    date = date.split('-')
    NewDate = datetime.date(int(date[0]) , int(date[1]) , int(date[2]))
    if -(birthday-NewDate).days > 0: return -(birthday-NewDate).days
    else: return "Not yet born"
print(birthday)
print(day_calculator('2025-03-07'))
