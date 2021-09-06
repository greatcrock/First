"""
"На протяжении веков, левши страдали от дискриминации в мире, созданном для правшей."
Santrock, John W. (2008). Motor, Sensory, and Perceptual Development.

"Большинство людей (70-95%) правши, меньшинство (5-30 %) левши, и неопределеное число людей вероятно лучше всего охарактеризовать, как "симметричные"."
Scientific American. www.scientificamerican.com

Один робот был занят простой задачей: объединить последовательность строк в одно выражение для создания инструкции по обходу корабля.
Но робот был левша и зачастую шутил и запутывал своих друзей правшей.
Дана последовательность строк. Вы должны объединить эти строки в блок текста, разделив изначальные строки запятыми.
В качестве шутки над праворукими роботами, вы должны заменить все вхождения слова "right" на слова "left", даже если это часть другого слова.
Все строки даны в нижнем регистре.

Входные данные: Последовательность строк.
Выходные данные: Текст, как строка.
"""

def left_join(phrases: tuple) -> str:
    """
    Join strings and replace "right" to "left"
    """
    text = ''
    for i in phrases:
        if len(text) < 1:
            text += i
        else:
            text += ", " + i
    return text.replace('right', 'left')

print(left_join(("left", "right", "left", "stop")))

import re

t = r'.'

txt = "dsa"
if txt[0].isalpha():
    print(txt[0])
print(re.sub(r'.*([A-z]+).*','\1', '49568486hel4lo'.rstrip() ))