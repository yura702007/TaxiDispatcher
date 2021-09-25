import time


class Driver:

    def __init__(self, name='Александр Рыбчинский', car='Renault'):
        self.name = name
        self.car = car

    def run(self):
        pass

    def start_job(self):
        start_time = time.asctime().split()[-2]
        return {'Время': start_time, 'статус': 'Ожидаю вызова', 'Водитель': self.name, 'авто': self.car}


if __name__ == '__main__':
    dr = Driver()
    print(dr.start_job())
    print(dr.start_job.__name__, type(dr.start_job.__name__))
