def caching_fibonacci():   #Створюємо функцію
    cache = {}   #Створюємо пустий словник

    def fibonacci(n):   #Створюємо другу функцію
        if n <= 0:    #Задаємо умови та повертаємо результат
            return 0
        elif n == 1:
            return 1
        else:
            if n in cache:
                return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)     #Додаємо елемент в словник
        return cache[n]     #Повертаємо елемент зі словника

    return fibonacci    #Повертаємо результат функції

fib = caching_fibonacci()    # Отримуємо функцію fibonacci

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610