from datetime import date
def date_time():
    current_datetime = date.today()
    print(current_datetime)
def calculate_salary():
    print('Расчет заработной платы')
    a = int(input('Введите ежедневный оклад: '))
    d = int(input('Введите количество отработанных дней: '))
    s = a * d / 100 * 87
    print(s)

if __name__=='__main__':
    date_time()
    calculate_salary()