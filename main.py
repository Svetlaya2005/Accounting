from application.salary import date_time, calculate_salary
from application.db.people import get_employees
def main():
    print(date_time())
    print(calculate_salary())
    print(get_employees())

if __name__ == 'main':
    main()

