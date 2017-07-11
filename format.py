from datetime import datetime
from pytz import timezone

def to_int(list):
    return int(''.join(list))


# Takes up the row from the CSV and edits it to be like the database
def format_list(row):
    new_list = []
    print(row)

    # Convert date to a datetime object
    date = datetime(to_int(row[1][:4]), to_int(row[1][4:6]), to_int(row[1][6:8]), to_int(row[1][8:10]), 30, 00)
    date = timezone('US/Central').localize(date)
    # Insert the date into the new list
    new_list.insert(0,date)

    # Add the rest of the elements to the new list
    for i in range(4,len(row)):
        # If cell is empty, add a zero (This will later be turned to NULL)
        if row[i] == '*':
            new_list.append(0)
        else:
            new_list.append(row[i])
            print(type(row[i]), row[i])
    return new_list
