import numexpr

from colorama import init
from colorama import Fore, Back, Style
init()

print(Fore.MAGENTA)
expr = input("Введите математическое выражение: ")

result = numexpr.evaluate(expr)

print(Fore.RED)
print(f"Результат: {result}")
