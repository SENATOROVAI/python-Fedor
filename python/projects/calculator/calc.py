from operators.addition import add
from operators.multiplication import mult
from operators.subtraction import sub
from run import get_input_data

Flag = True
while Flag:
    try:
        num, operator, num2 = get_input_data()
        if operator == "+":
            print("Результат операции:", add(num, num2))
        elif operator == "-":
            print("Результат операции:", sub(num, num2))
        elif operator == "*":
            print("Результат операции:", mult(num, num2))
        else:
            print("Ошибка! Некорректный оператор.")

    except ValueError:
        Flag = False
        print("Ошибка, введите правильное значение")
