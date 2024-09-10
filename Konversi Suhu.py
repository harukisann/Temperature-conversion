import os
import time

def clear_screen():
    if os.name == 'nt': 
        os.system('cls')
    else:
        os.system('clear')

def print_separator(char='=', length=24):
    print(char * length)

def fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celcius_to_fahrenheit(celcius):
    return celcius * 9/5 + 32

def celcius_to_kelvin(celcius):
    return celcius + 273.15

def kelvin_to_celcius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def reamur_to_celcius(reamur):
    return (5/4) * reamur

def celcius_to_reamur(celcius):
    return (4/5) * celcius

def reamur_to_fahrenheit(reamur):
    return reamur * (9/4) + 32

def fahrenheit_to_reamur(fahrenheit):
    return (fahrenheit - 32) * (4/9)

def reamur_to_kelvin(reamur):
    return reamur * (5/4) + 273.15

def kelvin_to_reamur(kelvin):
    return (kelvin - 273.15) * (4/5)

input_options = [
    "Celcius",
    "Fahrenheit",
    "Kelvin",
    "Reamur"
]

output_options = {
    "Celcius": ["Fahrenheit", "Kelvin", "Reamur"],
    "Fahrenheit": ["Celcius", "Kelvin", "Reamur"],
    "Kelvin": ["Celcius", "Fahrenheit", "Reamur"],
    "Reamur": ["Celcius", "Fahrenheit", "Kelvin"]
}

unit_symbols = {
    "Celcius": "°C",
    "Fahrenheit": "°F",
    "Kelvin": "K",
    "Reamur": "°R"
}

conversions = {
    ("Celcius", "Fahrenheit"): celcius_to_fahrenheit,
    ("Celcius", "Kelvin"): celcius_to_kelvin,
    ("Celcius", "Reamur"): celcius_to_reamur,
    ("Fahrenheit", "Celcius"): fahrenheit_to_celcius,
    ("Fahrenheit", "Kelvin"): fahrenheit_to_kelvin,
    ("Fahrenheit", "Reamur"): fahrenheit_to_reamur,
    ("Kelvin", "Celcius"): kelvin_to_celcius,
    ("Kelvin", "Fahrenheit"): kelvin_to_fahrenheit,
    ("Kelvin", "Reamur"): kelvin_to_reamur,
    ("Reamur", "Celcius"): reamur_to_celcius,
    ("Reamur", "Fahrenheit"): reamur_to_fahrenheit,
    ("Reamur", "Kelvin"): reamur_to_kelvin
}

while True:
    clear_screen()
    print_separator()
    print("Program Konversi suhu")
    print_separator()

    print("Pilih suhu input:")
    for i, option in enumerate(input_options, start=1):
        print(f"{i}. {option}")
    
    print_separator()
    input_choice = input("Masukan pilihan Input: ")

    if input_choice not in ('1', '2', '3', '4'):
        print("invalid Input. Pilih opsi yang benar")
        continue

    input_unit = input_options[int(input_choice) - 1]

    print_separator()
    print(f"Pilih suhu Output:")
    for i, option in enumerate(output_options[input_unit], start=1):
        print(f"{i}. {option}")

    print_separator()
    output_choice = input("Masukan pilihan output: ")

    if output_choice not in ('1', '2', '3'):
        print("Invalid input. Masukan opsi yang benar")
        continue

    output_unit = output_options[input_unit][int(output_choice) - 1]

    while True:
        try:
            print_separator()
            heat = float(input(f"Masukan suhu dalam {unit_symbols[input_unit]}: "))
            break
        except ValueError:
            print("Invalid input. Masukan angka yang benar")
        
    result = conversions[(input_unit, output_unit)](heat)

    print_separator()
    print(f"Hasil: {result:.2f} {unit_symbols[output_unit]}")
    print_separator()

    while True:
        repeat = input("Ulangi? (yes/no): ").lower()
        if repeat in ('yes', 'y'):
            break
        elif repeat in ('no', 'n'):
            print("Program ditutup")
            print_separator()
            time.sleep(3)
            exit()
        else:
            print("invalid input pilih yes atau no!")