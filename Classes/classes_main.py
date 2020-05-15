from shapes import *
from animals import *

"""  Examples """


# domestic().get_home()
# domestic().get_food()

# herbivores().get_home()
# herbivores().get_food()

# wild().get_home()
# wild().get_food()

# carnivores().get_home()
# carnivores().get_food()


#PUBLIC MEMBER ; 

"""
print(ellipse().property) #No error
"""

#PRIVATE MEMBER -CANNOT BE ACCESSED FROM OUTSIDE - GIVES ERRORS
"""
print(ellipse().__a) #Error in accessing a (as it is private startng with double underscore)

"""


#--------------------  SHAPES  -----------------------

el = ellipse(4,2)
print(el.area())
el.draw()
input()

sq = square(40)
sq.draw()
input() #for holding the image on the screen

pl = parallelogram(60,100)
pl.draw()
input()

rh = parallelogram(60,40)
rh.draw()
input() 



#-----------------  ANIMALS   --------------------------

print("cow")
cow = cow()
cow.get_food()
cow.get_home()
cow.get_unique()

cow.set_food("grass")
cow.set_home("homes")
cow.set_unique("serves as livelihood in rural areas ")

cow.get_food()
cow.get_home()
cow.get_unique()


print("dog")
dog = dog()
dog.get_food()
dog.get_home()
dog.get_unique()

dog.set_food("rotis")
dog.set_home("kennel")
dog.set_unique("protects homes")

dog.get_food()
dog.get_home()
dog.get_unique()


print("dolphin")
dolphin = dolphin()
dolphin.get_food()
dolphin.get_home()
dolphin.get_unique()

dolphin.set_food("sea food")
dolphin.set_home("seas /oceans")
dolphin.set_unique()

dolphin.get_food()
dolphin.get_home()
dolphin.get_unique()


print("lion")
lion = lion()
lion.get_food()
lion.get_home()
lion.get_unique()

lion.set_food("flesh of other animals")
lion.set_home("den")
lion.set_unique("furious")

lion.get_food()
lion.get_home()
lion.get_unique()
