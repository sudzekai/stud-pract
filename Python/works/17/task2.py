import os
import subprocess
import signal
import sys

def list_processes():
    if os.name == "nt":
        os.system("tasklist")
    else:
        os.system("ps -e")

def run_program(path):
    try:
        subprocess.Popen(path)
    except Exception as e:
        print("Ошибка:", e)

def kill_process(pid):
    try:
        os.system(f"taskkill /PID {pid} /F")
    except Exception as e:
        print("Ошибка:", e)


while True:
    print("\n===== ДИСПЕТЧЕР ЗАДАЧ =====")
    print("1. Список процессов")
    print("2. Запустить программу")
    print("3. Завершить процесс")
    print("0. Выход")

    var = input("Выбор: ")

    if var == '1':
        list_processes()

    elif var == '2':
        run_program(input("Путь к программе: "))

    elif var == '3':
        kill_process(input("PID процесса: "))

    elif var == '0':
        print("Выход")
        break

    else:
        print("Неверная команда")