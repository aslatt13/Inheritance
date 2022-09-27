
class Plant:
    def __init__(self,color):
        self.__color = color


    def get_color(self):
        return self.__color


class Flower(Plant): #flower subclass to plant
    def __init__(self,color,petals):
        Plant.__init__(self,color) #call plant cant create subclass if superclass does not exist

        self.__petals = petals #only to flowers not plant

    def get_petals(self):
        return self.__petals

#one way relationship
#works top down
#superclass cant access subclass methods