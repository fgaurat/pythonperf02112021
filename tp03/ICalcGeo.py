


from abc import ABC, ABCMeta, abstractmethod


class ICalcGeo(metaclass=ABCMeta):

    @abstractmethod 
    def surface(self):
        pass