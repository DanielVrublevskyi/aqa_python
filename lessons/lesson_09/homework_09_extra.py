# 1) Опишіть клас Вагон
# 2) Вагон повинен містити список пасажирів і дозволяти додавати пасажирів
# 3) У Вагоні може бути не більше 10 пасажирів
# 4) Під час використання функції len у вагоні я хочу бачити кількість пасажирів
# 5) Кожен вагон повинен мати номер
# 6) Опишіть об’єкт «Поїзд»
# 7) Клас повинен містити поля та метод для додавання вагонів(необхідно додати об’єкти та екземпляри класу вагонів)
# 8) В поїзді завжди є 1 вагон і це локомотив(він не приймає пасажирів)
# 9) Використовуючи len у поїзді, я хочу бачити кількість вагонів без локомотива

class Passenger:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name


class Carriage:
    capacity = 10
    number = 0
    def __init__(self, passengers: list = None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers[:self.capacity]


    def __len__(self):
        return len(self.passengers)

    def add_passenger(self, passenger: Passenger):
        if len(self) < self.capacity:
            self.passengers.append(passenger)
        else:
            print(f"No available seat for mr/mrs {passenger.name}")

class Locomotive:
    def __init__(self):
        pass

class Train:
    def __init__(self, carriages: list = None):
        self.locomotive = Locomotive()
        self.carriages = []

        if carriages is not None:
            for carriage in carriages:
                self.add_carriage(carriage)

    def add_carriage(self, carriage: Carriage):
        self.carriages.append(carriage)
        carriage.number = len(self.carriages)

    def __len__(self):
        return len(self.carriages)




passenger_1 = Passenger("John", "Smith")
passenger_2 = Passenger("Anna", "Brown")
passenger_3 = Passenger("Michael", "Johnson")
passenger_4 = Passenger("Emily", "Davis")
passenger_5 = Passenger("Daniel", "Wilson")
passenger_6 = Passenger("Sofia", "Taylor")
passenger_7 = Passenger("David", "Anderson")
passenger_8 = Passenger("Olivia", "Thomas")
passenger_9 = Passenger("James", "Moore")
passenger_10 = Passenger("Emma", "Martin")
passenger_11 = Passenger("Robert", "Clark")
passenger_12 = Passenger("Mia", "Lewis")

print("\n--- CASE 1: Empty carriage ---")

carriage_empty = Carriage()

print("Passenger count:", len(carriage_empty))


print("\n--- CASE 2: Carriage with initial passengers ---")

pas_list = [
    passenger_1, passenger_2, passenger_3, passenger_4,
    passenger_5, passenger_6, passenger_7, passenger_8
]

carriage_1 = Carriage(pas_list)

print("Passenger count:", len(carriage_1))


print("\n--- CASE 3: Add passenger to carriage ---")

carriage_1.add_passenger(passenger_9)

print("Passenger count after adding passenger:", len(carriage_1))


print("\n--- CASE 4: Fill carriage to maximum capacity ---")

carriage_1.add_passenger(passenger_10)

print("Passenger count:", len(carriage_1))
print("Expected maximum capacity:", carriage_1.capacity)


print("\n--- CASE 5: Try to add passenger to full carriage ---")

carriage_1.add_passenger(passenger_11)

print("Passenger count after failed attempt:", len(carriage_1))


print("\n--- CASE 6: Create carriage with more than 10 passengers ---")

all_passengers = [
    passenger_1, passenger_2, passenger_3, passenger_4,
    passenger_5, passenger_6, passenger_7, passenger_8,
    passenger_9, passenger_10, passenger_11, passenger_12
]

carriage_full = Carriage(all_passengers)

print("Passengers passed to constructor:", len(all_passengers))
print("Passengers actually added:", len(carriage_full))


print("\n--- CASE 7: Create empty train ---")

train_empty = Train()

print("Train length without locomotive:", len(train_empty))
print("Locomotive:", train_empty.locomotive)


print("\n--- CASE 8: Create train with existing carriages ---")

carriage_2 = Carriage([passenger_1, passenger_2])
carriage_3 = Carriage([passenger_3, passenger_4, passenger_5])

train_1 = Train([carriage_2, carriage_3])

print("Train length:", len(train_1))
print("Carriage 2 number:", carriage_2.number)
print("Carriage 3 number:", carriage_3.number)


print("\n--- CASE 9: Add carriage to existing train ---")

carriage_4 = Carriage([passenger_6])

train_1.add_carriage(carriage_4)

print("Train length after adding carriage:", len(train_1))
print("New carriage number:", carriage_4.number)


print("\n--- CASE 10: Check all carriage numbers ---")

for carriage in train_1.carriages:
    print("Carriage number:", carriage.number, "| Passengers:", len(carriage))


