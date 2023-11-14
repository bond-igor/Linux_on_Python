'''Условие:
Дополнить проект тестами, проверяющими команды вывода списка файлов (l) и разархивирования с путями (x).
*Задание 2. *
• Установить пакет для расчёта crc32
sudo apt install libarchive-zip-perl
• Доработать проект, добавив тест команды расчёта хеша (h). Проверить, что хеш совпадает с рассчитанным командой crc32.'''

import subprocess


tst = "/home/user/tst"
out = "/home/user/out"
folder1 = "/home/user/folder1"
folder2 = "/home/user/folder2"

def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def test_step1():
# test1 =================== создать архив
    result1 = checkout(f"cd {tst}; 7z a {out}/arx2", "Everything is Ok")
# проверьте, включен ли arx2.7z в out
    result2 = checkout(f"cd {out}; ls", "arx2.7z")
    assert result1 and result2, "Test1 FAIL"


def test_step2():
# test1 ======== возьмите документы из папки: out и скопируйте эти документы в folder1
    result1 = checkout(f"cd {out}; 7z e arx2.7z -o{folder1} -y", "Everything is Ok")
    result2 = checkout(f"cd {folder1}; ls", "one")
    result3 = checkout(f"cd {folder1}; ls", "two")
    assert result1 and result2 and result3, "Test2 FAIL"


def test_step3():
# test3 =========показать информацию об arx2.7z
    assert checkout(f"cd {out}; 7z t arx2.7z", "Everything is Ok"), "Test3 FAIL"


def test_step4():
# test4 ========= добавить обновление архива
    assert checkout(f"cd {tst}; 7z u {out}/arx2.7z", "Everything is Ok"), "Test4 FAIL"

def test_step5():
    # test5 ====== вывод списка файлов
    result1 = checkout(f"cd {out}; 7z l arx2.7z", "")
    result2 = checkout(f"cd {out}; 7z l arx2.7z", "one")
    result3 = checkout(f"cd {out}; 7z l arx2.7z", "two")
    assert result1 and result2 and result3, "test5 FAIL"


def test_step6():
    # test6 ===== команда разархивирования с путями
    result1 = checkout(f"cd {out}; 7z x arx2.7z -o{folder2}", "Everything is Ok")
    result2 = checkout(f"cd {folder2}; ls", "one")
    result3 = checkout(f"cd {folder2}; ls", "two")
    assert result1 and result2 and result3, "test6 FAIL"

def test_step7():
# test5 ========= удалите документы один и два из архива в папке out
    assert checkout(f"cd {out}; 7z d arx2.7z", "Everything is Ok"), "Test7 FAIL"
