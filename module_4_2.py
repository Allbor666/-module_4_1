def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    return inner_function


# Получаем функцию через вызов test_function
func = test_function()
func() # Вызов inner_function через переменную func

# Попытка вызвать inner_function напрямую вне test_function
try:
    inner_function()  # Это вызовет ошибку, так как inner_function не доступна здесь
except NameError as e:
    print(f"Ошибка: {e}")  # Обработка ошибки, если inner_function недоступна
