class Car:
    def __init__(self, color, car_type, year):
        self.color = color
        self.type = car_type
        self.year = year
        self.is_running = False

    def start(self):
        if not self.is_running:
            print("Автомобиль заведен")
            self.is_running = True
        else:
            print("Автомобиль уже заведен")

    def stop(self):
        if self.is_running:
            print("Автомобиль заглушен")
            self.is_running = False
        else:
            print("Автомобиль уже заглушен")

    def set_year(self, new_year):
        self.year = new_year
        print(f"Год выпуска изменен на {new_year}")

    def set_type(self, new_type):
        self.type = new_type
        print(f"Тип автомобиля изменен на {new_type}")

    def set_color(self, new_color):
        self.color = new_color
        print(f"Цвет автомобиля изменен на {new_color}")

my_car = Car(color="Синий",car_type="Седан" ,year=2020)
print(my_car)
my_car.start()
my_car.stop()
my_car.set_year(2023)
my_car.set_type("Кроссовер")
my_car.set_color("Красный")
