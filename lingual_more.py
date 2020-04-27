import random
print(" Cейчас вам будет предоставлена возможность введения слов")
print(" Когда заходите остановиться, просто введите q")

slovar = {}

while True:
    key = input("Ведите слово на английском\n: ").strip().lower()
    if key == 'q':
        break
    value = input("Ведите слово на русском\n: ").strip().lower()
    slovar[key] = value

print("Сейчас у нас будет проверка, больше 3 ошибок нельзя")

errors = 0
bonus = 0

while len(slovar) != 0:
	item = random.choice(list(slovar.keys()))	
	print("Ввeдите перевод слова", item, ": ")
	answer = input(": ").strip().lower()
	if slovar[item] == answer:
		bonus += 1
		print("Ваш счет составляет", bonus)
	elif errors > 3:
		print("game over")
		break
	else:
		errors +=1
		print(slovar[item], "- правильный ответ")
	slovar.pop(item)