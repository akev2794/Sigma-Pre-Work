from datetime import datetime

def convert_date(birth_date_str: str):
    """Converts a date inputted as a string with format DD-MM-YYYY into the datetime format"""
    birth_date = datetime.strptime(birth_date_str, "%d-%m-%Y")
    return birth_date

def find_age_difference():
    """Finds the age difference between a given date and the current date, in years"""
    while True:
        birth_date_str = input("Please enter a valid date, in DD-MM-YYYY format: ")
        try:
            birth_date = convert_date(birth_date_str)
            break
        except ValueError: #Raises an error if the inputted date is in the wrong format
            print("Please ensure that you enter a valid date in a valid format!")
    current_date = datetime.now()
    age = current_date.year - birth_date.year
    if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

if __name__ == "__main__":
    print(find_age_difference())
