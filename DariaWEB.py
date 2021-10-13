import functools
import time

def cache(func): #кэширующий декоратор
    @functools.wraps(func)  #обертка функции
    def wrapper(*args, **kwargs):#функция проверки и добавления в кэш результата работы(обертка)
        cache_key = args + tuple(kwargs.items())#как ключ к кэшу мы записываем аргументы функции
        if cache_key not in wrapper.cache:#если ключа нет в кэше
            wrapper.cache[cache_key] = func(*args, **kwargs)#записываем результат работы функции в кэш
        return wrapper.cache[cache_key]#как результат обертки вызываем значение функции
    wrapper.cache = dict()#кэш обертки - словарь
    return wrapper# результат работы декоратора - результат работы обертки

@cache#прописываем декоратор для функции
def newton(a, x, n, accuracy=0.0000000000000001):#число, приближение, степень, точность
    xn = 1/n * ((n-1)*x + a/(pow(x, (n-1))))# формула Ньютона для вычисления нового приближения
    if ((x-xn) <= accuracy):#проверка на точность
        return xn# если проверка прошла - заканчиваем работу
    else:#
        return newton(a, xn, n)#если нет вызываем рекурсию

def IsPrime(n):#проверка на простоту
    d = 2#
    while n % d != 0:#делим исходное число на все до него
        d += 1#инкримент если есть остаток
    return d == n#если числа равны - число простое, если нет, то нет

def Reverse(n):# воспроизводим число наоборот
    x = str(abs(n))#переводим модуль числа в строку
    s = ""#
    for a in range(len(x)):#разбиваем на символы
        s += str(x[((len(x)-1)-a)])#воспроиводим наоборот
    if (n < 0):# если исходное число отрицательное, добавляем минус
        return -int(s)#
    return int(s)#возвращаем число

def palindrom(n):#
    return n==Reverse(n)#используем предыдущую функцию чтобы проверить палиндром

def lists(x = list()):#передаем список
    s = list()#назначаем списки
    a = list()#
    v = list()#
    for i in range(len(x)):#проходим по исходному и по проверке делимости распределяем между списками
        if ((x[i] % 2) == 0):#
            s.append(x[i])#
        if ((x[i] % 3) == 0):#
            a.append(x[i])#
        if ((x[i] % 5) == 0):#
            v.append(x[i])#
    return s, a, v#возвращаем списки


#выводим результаты
print(newton(8,8,3))
print(IsPrime(99331))
print(Reverse(-3314434))
print(palindrom(123))
print(lists(list([3,4,5,6,7,8, 787, 555])))
print(newton(8,8,3))
start = time.perf_counter() #проверки скорости работы с кэшем и без
print('Time run:', time.perf_counter() - start)
