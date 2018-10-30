from collections import Counter

class Driver:
    _all = []
    _count = 0

    def __init__(self, name, car_make, car_model):
        self._name = name
        self._car_make = car_make
        self._car_model = car_model
        Driver._all.append(self)
        Driver._count += 1

    @classmethod
    def fleet_size(cls):
        return Driver._count

    @classmethod
    def driver_names(cls):
        return list(map(lambda item: item.name, Driver._all))

    @classmethod
    def fleet_makes(cls):
        return list(map(lambda item: item.car_make, Driver._all))

    @classmethod
    def fleet_models(cls):
        return list(map(lambda item: item.car_model, Driver._all))

    @classmethod
    def fleet_makes_count(cls):
        return Counter(Driver.fleet_makes())

    @classmethod
    def fleet_models_count(cls):
        return Counter(Driver.fleet_models())

    @classmethod
    def percent_of_fleet(cls, word):
        result = round((Driver.fleet_makes_count()[word])/float((Driver._count)), 2)
        return str(result*100) + "%"

    @property
    def name(self):
        return self._name

    @property
    def car_make(self):
        return self._car_make

    @property
    def car_model(self):
        return self._car_model
