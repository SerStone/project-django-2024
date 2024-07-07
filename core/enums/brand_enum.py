from enum import Enum


class CarBrand(Enum):
    TOYOTA = 'Toyota'
    VOLKSWAGEN = 'Volkswagen'
    FORD = 'Ford'
    HONDA = 'Honda'
    CHEVROLET = 'Chevrolet'
    NISSAN = 'Nissan'
    HYUNDAI = 'Hyundai'
    MERCEDES_BENZ = 'Mercedes-Benz'
    BMW = 'BMW'
    AUDI = 'Audi'
    KIA = 'Kia'
    MAZDA = 'Mazda'
    SUBARU = 'Subaru'
    LEXUS = 'Lexus'
    PEUGEOT = 'Peugeot'
    FIAT = 'Fiat'
    MITSUBISHI = 'Mitsubishi'
    JEEP = 'Jeep'
    SUZUKI = 'Suzuki'
    RAM = 'RAM'
    PORSCHE = 'Porsche'
    LAND_ROVER = 'Land Rover'
    JAGUAR = 'Jaguar'
    CADILLAC = 'Cadillac'
    CHRYSLER = 'Chrysler'
    TESLA = 'Tesla'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
