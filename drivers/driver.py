import time


class Driver:

    def __init__(self, name='Александр Рыбчинский', car='Renault'):
        self.name = name
        self.car = car
        self.start_timer = 0

    def run(self):
        pass

    def start_job(self):
        """
        Ожидаю вызова
        """
        start_time = time.asctime().split()[-2]
        return {'Время': start_time, 'статус': 'Ожидаю вызова', 'Водитель': self.name, 'авто': self.car}

    def drive_for_client(self):
        """
        Еду за пассажиром
        """
        start_time = time.asctime().split()[-2]
        return {'Время': start_time, 'статус': 'Еду за пассажиром', 'Водитель': self.name, 'авто': self.car}

    def waiting_client(self):
        """
        Ожидание пассажира
        """
        self.start_timer = time.time()
        start_time = time.asctime().split()[-2]
        return {'Время': start_time, 'статус': 'Жду пассажира', 'Водитель': self.name, 'авто': self.car}

    def order_execution(self):
        """
        Везу пассажира
        """
        stop_timer = time.time()
        timer = round((stop_timer - self.start_timer) / 60)
        self.start_timer = 0
        start_time = time.asctime().split()[-2]
        return {
            'Время': start_time, 'Время ожидания': timer, 'статус': 'Везу пассажира',
            'Водитель': self.name, 'авто': self.car
        }

    def end_job(self):
        """
        Конец работы
        """
        end_time = time.asctime().split()[-2]
        return {'Время': end_time, 'статус': 'Отдых', 'Водитель': self.name, 'авто': self.car}


if __name__ == '__main__':
    dr = Driver()
    print(dr.drive_for_client())
    print(dr.start_job.__doc__, type(dr.start_job.__name__))
