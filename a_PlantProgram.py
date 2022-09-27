import a_PlantClass as pc

primrose = pc.Plant("Green") #instance of plant superclass

sunflower = pc.Flower("Yellow",20) #subclass of flower, add petal no.

print(primrose.get_color())

print(sunflower.get_color())
print(sunflower.get_petals())


#print(primrose.get_petals()) #superclass does not inherit subclass method
