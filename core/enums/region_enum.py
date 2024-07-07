from enum import Enum


class Region(Enum):
    VINNYTSIA = 'VINNYTSIA'
    VOLYN = 'VOLYN'
    LVIV = 'LVIV'
    DNIPRO = 'DNIPRO'
    DONETSK = 'DONETSK'
    ZHYTOMYR = 'ZHYTOMYR'
    ZAKARPATTIA = 'ZAKARPATTIA'
    ZAPORIZHIA = 'ZAPORIZHIA'
    IVANO_FRANKIVSK = 'IVANO_FRANKIVSK'
    KYIV = 'KYIV'
    KIROVOHRAD = 'KIROVOHRAD'
    LUGANSK = 'LUGANSK'
    MYKOLAIV = 'MYKOLAIV'
    ODESA = 'ODESA'
    POLTAVA = 'POLTAVA'
    RIVNE = 'RIVNE'
    SUMY = 'SUMY'
    TERNOPIL = 'TERNOPIL'
    KHARKIV = 'KHARKIV'
    CHERKASY = 'CHERKASY'
    CHERNIHIV = 'CHERNIHIV'
    CHERNIVTSI = 'CHERNIVTSI'
    KHMELNYTSK = 'KHMELNYTSK'
    SEVASTOPOL = 'SEVASTOPOL'
    CRIMEA = 'CRIMEA'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
