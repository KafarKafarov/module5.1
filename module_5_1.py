class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor ):

        self.new_floor = new_floor

        if new_floor >= self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for num in range(1, new_floor + 1):
                print(num)



while True:
    user_input_house = list(input('Введите ЖК и этажность через запятую в формате (Эльбрус, 30) : ').split(','))
    answer = House(user_input_house[0], int(user_input_house[1]))
    user_input_floors = int(input('Введите число этажей: '))
    answer.go_to(user_input_floors)
    print('\n')