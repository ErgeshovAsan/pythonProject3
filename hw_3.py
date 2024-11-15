class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def __eq__(self, other):
        return self.__memory == other.__memory
    def __ne__(self, other):
        return self.__memory != other.__memory
    def __lt__(self, other):
        return self.__memory < other.__memory
    def __gt__(self, other):
        return self.__memory > other.__memory
    def __le__(self, other):
        return self.__memory <= other.__memory
    def __ge__(self, other):
        return self.__memory >= other.__memory

    def __str__(self):
        return f'CPU: {self.__cpu}, MEMORY: {self.__memory}.'

    @property
    def cpu(self):
        return self.__cpu
    @cpu.setter
    def cpu(self, cpu):
        self.__cpu = cpu
    @property
    def memory(self):
        return self.__memory
    @memory.setter
    def memory(self, memory):
        self.__memory = memory

    def make_computations(self):
        return f"Сумма CPU и MEMORY: {self.__cpu + self.__memory}"

class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def __str__(self):
        return f'SIM_CARDS_LIST: {self.__sim_cards_list}.'
    @property
    def sim_cards_list(self):
        return self.__sim_cards_list
    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        try:
            sim_card = self.__sim_cards_list[sim_card_number - 1]
            print(f"Идет звонок на номер {call_to_number} с SIM-карты-{sim_card_number} - {sim_card}")
        except IndexError:
            print("Указанный номер SIM-карты не существует")

class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def __str__(self):
        return f'CPU: {self.cpu}, MEMORY: {self.memory}, SIM_CARDS_LIST: {self.sim_cards_list}.'

    def use_gps(self, location):
        return f'Построен маршрут до локации {location}.'

computer = Computer(4.2, 8)
phone = Phone(['Bilain', 'Megacom'])
smartphone = SmartPhone(3.2, 8, 'Bilain')
smartphone1 = SmartPhone(2.4, 16, ['Megacom', 'O!'])
print(computer)
print(phone)
print(smartphone)
print(smartphone1)
print(smartphone.use_gps('Bishkek'))
print(computer.make_computations())
phone.call(1, "+996 777 99 88 11")
phone.call(2, "+996 555 11 22 33")
smartphone1.call(1, "+996 700 55 44 33")
print(f'{smartphone == smartphone1}')
print(f'{smartphone != smartphone1}')
print(f'{smartphone < smartphone1}')
print(f'{smartphone > smartphone1}')
print(f'{smartphone <= smartphone1}')
print(f'{smartphone >= smartphone1}')
computer.cpu = 3.0
computer.memory = 32
print(computer)