import time


class Driver:

    def __init__(self, name='Александр Рыбчинский', car='Renaut'):
        self.name = name
        self.car = car

    def start_job(self):
        start_time = time.asctime().split()[-2]
        return {'Время': start_time, 'status': 'Ожидаю вызова', 'Водитель': self.name, 'авто': self.car}


dr = Driver()

if __name__ == '__main__':
    print(dr.start_job())
