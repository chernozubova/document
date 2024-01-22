class Worker:
    """Представляет сотрудника фирмы."""

    def __init__(self, name, surname, age):
        """Инициализация атрибутов класса Worker"""

        self.__name = name
        self.__surname = surname
        self.__age = age

    @property
    def name(self):
        """Уровень доступности атрибута name = private"""

        return self.__name

    @property
    def surname(self):
        """Уровень доступности атрибута surname = private"""

        return self.__surname

    @property
    def age(self):
        """Уровень доступности атрибута age = private"""

        return self.__age

    def __str__(self):
        """Вывод информации об объекте типа Worker """

        return f"{self.name} {self.surname}, Возраст: {self.age}"


class Boss:
    def __init__(self, name, surname, age):
        """Представляет директора фирмы."""

        self.__name = name
        self.__surname = surname
        self.__age = age

    @property
    def name(self):
        """Уровень доступности атрибута name = private"""

        return self.__name

    @property
    def surname(self):
        """Уровень доступности атрибута surname = private"""

        return self.__surname

    @property
    def age(self):
        """Уровень доступности атрибута age = private"""

        return self.__age

    def __str__(self):
        """Вывод информации об объекте типа Boss """

        return f"{self.name} {self.surname}, Возраст: {self.age}"


class Work:
    def __init__(self, name_of_work):
        """Представляет фирму с директором и сотрудниками."""

        self.__name_of_work = name_of_work
        self.__boss = None
        self.__workers = []

    @property
    def name_of_work(self):
        """Уровень доступности атрибута name_of_work = private"""

        return self.__name_of_work

    @property
    def boss(self):
        """Уровень доступности атрибута boss = private"""

        return self.__boss

    @property
    def workers(self):
        """Уровень доступности атрибута workers = private"""

        return self.__workers

    def make_boss(self, boss):
        """Назначает директора фирмы."""

        self.__boss = boss

    def make_worker(self, worker):
        """Добавляет сотрудника в фирму."""

        self.__workers.append(worker)

    def __str__(self):
        """Возвращает строковое представление фирмы."""

        boss_str = f"Директор: {self.boss}" if self.boss else "Директор не назначен"
        workers_str = "\n".join(str(worker) for worker in self.workers)
        return f"Фирма: {self.name_of_work}\n{boss_str}\nСотрудники:\n{workers_str}"


def create_work():
    """Создает новую фирму, запрашивая у пользователя название."""

    name_of_work = input("Введите название фирмы: ")
    return Work(name_of_work)


def create_boss():
    """Создает нового директора, запрашивая у пользователя имя, фамилию и возраст."""

    while True:
        name = input("Введите имя директора: ")
        if name.isalpha():
            break
        else:
            print("Ошибка: Имя должно состоять только из букв. Попробуйте снова.")

    surname = input("Введите фамилию директора: ")

    while True:
        age = input("Введите возраст директора: ")
        try:
            age = int(age)
            break  # Если возраст успешно преобразован в целое число, завершаем цикл
        except ValueError:
            print("Ошибка: Возраст должен быть числом. Попробуйте снова.")

    return Boss(name, surname, age)


def create_worker():
    """Создает нового сотрудника, запрашивая у пользователя имя, фамилию и возраст."""

    while True:
        name = input("Введите имя сотрудника: ")
        if name.isalpha():
            break
        else:
            print("Ошибка: Имя должно состоять только из букв. Попробуйте снова.")

    surname = input("Введите фамилию сотрудника: ")

    while True:
        age = input("Введите возраст сотрудника: ")
        try:
            age = int(age)
            break  # Если возраст успешно преобразован в целое число, завершаем цикл
        except ValueError:
            print("Ошибка: Возраст должен быть числом. Попробуйте снова.")

    return Worker(name, surname, age)


def menu():
    """Отображает главное меню и предоставляет пользователю опции для взаимодействия с программой."""

    work = None
    boss = None

    while True:
        print("Главное меню:")
        print("1. Создать фирму.")
        print("2. Создать директора(количество - 1).")
        print("3. Создать сотрудника.(количество - не ограничено)")
        print("4. Вывести информацию о сотруднике.")
        print("5. Вывести информацию о директоре.")
        print("6. Вывести информацию о фирме.")
        print("7. Выход из программы ")

        choose = input("Выберите пункт меню: ")

        if choose == "1":
            work = create_work()
            print("Фирма создана.")
            input("Нажмите Enter, чтобы продолжить...")
        elif choose == "2":
            if work:
                boss = create_boss()
                work.make_boss(boss)
                print("Директор назначен.")
            else:
                print("Сначала создайте фирму.")
            input("Нажмите Enter, чтобы продолжить...")
        elif choose == "3":
            if work:
                worker = create_worker()
                work.make_worker(worker)
                print("Сотрудник создан.")
            else:
                print("Сначала создайте фирму.")
            input("Нажмите Enter, чтобы продолжить...")
        elif choose == "4":
            if work and work.workers:
                for i, worker in enumerate(work.workers, start=1):
                    print(f"{i}. {worker}")
            else:
                print("Нет сотрудников.")
            input("Нажмите Enter, чтобы продолжить...")
        elif choose == "5":
            if boss:
                print(boss)
            else:
                print("Нет директора.")
            input("Нажмите Enter, чтобы продолжить...")
        elif choose == "6":
            if work:
                print(work)
            else:
                print("Фирма не создана.")
            input("Нажмите Enter, чтобы продолжить...")
        elif choose == "7":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите снова.")


if __name__ == "__main__":
    menu()