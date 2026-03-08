
class Vehicle:
    """
    Базовый класс для транспортных средств.
    """

    def __init__(self, brand: str, max_speed: int) -> None:
        """
        Инициализация транспортного средства.

        :param brand: Марка транспортного средства
        :param max_speed: Максимальная скорость (км/ч)
        """
        self._brand = brand          # защищённый атрибут
        self._max_speed = max_speed  # защищённый атрибут

    def move(self) -> str:
        """
        Описывает процесс движения транспортного средства.

        :return: Строка с описанием движения
        """
        return "Транспортное средство движется"

    def __str__(self) -> str:
        """
        Строковое представление объекта.

        :return: Человекочитаемая строка
        """
        return f"Транспорт: {self._brand}, макс. скорость {self._max_speed} км/ч"

    def __repr__(self) -> str:
        """
        Формальное представление объекта.

        :return: Строка для воссоздания объекта
        """
        return f"Vehicle(brand='{self._brand}', max_speed={self._max_speed})"


class Car(Vehicle):
    """
    Класс легкового автомобиля.
    """

    def __init__(self, brand: str, max_speed: int, doors: int) -> None:
        """
        Инициализация автомобиля.

        :param brand: Марка автомобиля
        :param max_speed: Максимальная скорость (км/ч)
        :param doors: Количество дверей
        """
        super().__init__(brand, max_speed)
        self.doors = doors

    def move(self) -> str:
        """
        Переопределённый метод движения автомобиля.

        Причина переопределения:
        автомобилю требуется более конкретное описание поведения,
        чем у абстрактного транспортного средства.

        :return: Строка с описанием движения автомобиля
        """
        return "Автомобиль едет по дороге"

    def __str__(self) -> str:
        """
        Строковое представление автомобиля.

        :return: Человекочитаемая строка
        """
        return (
            f"Автомобиль: {self._brand}, "
            f"{self.doors} двери, "
            f"макс. скорость {self._max_speed} км/ч"
        )

    def __repr__(self) -> str:
        """
        Формальное представление автомобиля.

        :return: Строка для воссоздания объекта
        """
        return (
            f"Car(brand='{self._brand}', "
            f"max_speed={self._max_speed}, "
            f"doors={self.doors})"
        )


if __name__ == "__main__":
    vehicle = Vehicle("Generic", 120)
    car = Car("Toyota", 180, 4)

    print(vehicle)
    print(car)

    print(vehicle.move())
    print(car.move())

    print([vehicle, car])