adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
print("task 01")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)
# task 02 ==
""" Замініть .... на пробіл
"""
print("task 02")
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print("task 03")
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())
print(adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print("task 04")
h_count = adwentures_of_tom_sawer.count("h")
print(f"літера 'h' зустрічається у тексті {h_count} разів")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print("task 05")
list_1 = adwentures_of_tom_sawer.split()
i = 0
for word in list_1:
    if word.istitle():
        i += 1

print(f"{i} слів у тексті починається з Великої літери")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print("task 06")
ind_1 = adwentures_of_tom_sawer.find("Tom")
ind_2 = adwentures_of_tom_sawer.find("Tom", ind_1 + 1)
print(f"{ind_2} - позиція, на якій слово Tom зустрічається вдруге")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
print("task 07")
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.replace(". ", ".\n")
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print("task 08")
print("четверте речення з adwentures_of_tom_sawer_sentences:", adwentures_of_tom_sawer_sentences.split(".\n")[3])

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print("task 09")
print(adwentures_of_tom_sawer_sentences.startswith("By the time"))

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print("task 10")
spl_to_list = adwentures_of_tom_sawer_sentences.split("\n")

last_sent = spl_to_list[len(adwentures_of_tom_sawer_sentences.split("\n")) - 1]
count = len(last_sent.split(" "))
print(f"{count} - кількість слів останнього речення з adwentures_of_tom_sawer_sentences")