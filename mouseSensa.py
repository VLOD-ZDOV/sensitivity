import os
import subprocess
import psutil
def set_mouse_sensitivity(sensitivity_percentage):
    # Максимальная чувствительность мыши
    max_sensitivity = 20
    # Рассчитываем новую чувствительность
    new_sensitivity = max(1, min(max_sensitivity, max_sensitivity * sensitivity_percentage // 100))
    
    # Записываем текущую чувствительность и выбор программы в файл с настройками
    with open(os.path.join(os.path.dirname(__file__), "settings.txt"), "r+") as f:
        current_sensitivity, _, apply_to_program = map(str.strip, f.readlines())
        f.seek(0)
        f.write(f"{current_sensitivity}\n{sensitivity_percentage}\n{apply_to_program}")

    # Устанавливаем новую чувствительность мыши
    os.system(f"powershell -Command \"$SetPoint = (New-Object -ComObject 'WScript.Shell').CreateShortcut('{os.path.basename(__file__)}.lnk').TargetPath; Start-Process -__file__Path $SetPoint -ArgumentList '-s', '{new_sensitivity}' -NoNewWindow -Verb RunAs\"")

    # Применяем чувствительность к программе (если указана)
    if apply_to_program != "0" and os.path.basename(apply_to_program) in (p.name() for p in psutil.process_iter()):
        apply_to_program(apply_to_program)

def apply_to_program(program_name):
    # Применяем чувствительность к указанной программе
    with open(os.path.join(os.path.dirname(__file__), "program_settings.txt"), "w") as f:
        f.write(program_name)

def main():
    # Путь к файлу с настройками
    settings___file__ = os.path.join(os.path.dirname(__file__), "settings.txt")
    
    # Если файл с настройками отсутствует, создаем его и закрываем программу
    if not os.path.exists(settings___file__):
        with open(settings___file__, "w") as f:
            f.write("50\n0\n0")  # Записываем значения по умолчанию
        return
    
    # В противном случае программа завершает работу
    return


main()