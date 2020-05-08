# Abstract base class;
class animals():
    def set_food(self):
        pass

    def get_food(self):
        pass

    def set_unique(self):
        pass

    def get_unique(self):
        pass

    def get_home(self):
        pass

    def set_home(self):
        pass


class herbivores(animals):
    def get_food(self,derive = False):
        food = 'Generally - Herbs,plants and vegeterian products'
        if derive == True:
            return food
        print(food)


class carnivores(animals):
    def get_food(self,derive = False):
        food = 'Generally - flesh, other animals, non-vegeterain '
        if derive == True:
            return food
        print(food)


class omnivores(herbivores, carnivores):
    def get_food(self,derive = False):
        if derive == True: 
            return herbivores().get_food(True) + '\n' + carnivores().get_food(True)
        else:
            herbivores().get_food()
            carnivores().get_food()

class domestic(herbivores):
    def get_home(self,derive = False):
        home = "Generally - At homes or live at stray places like streets etc. .. "
        if derive:
            return  home
        else:
            print(home)

class wild(carnivores):
    def get_home(self,derive = False):
        home = "Gererally -In Forests or wild furious places like seas etc. " 
        if derive == True:
            return home
        else:
            print(home)


class dog(omnivores,domestic):  
    def __init__(self,home = None,food = None,unique = "loyal"):
        if home == None:
            self.home = domestic().get_home(True) + "Specifc - On streets, at people's homes / Kennel"
        else:
            self.home = home
        
        if food == None:
            self.food = omnivores().get_food(True) + "Specific - flesh, dog-food, rotis etc. "
        else:
            self.food = food
        
        self.unique = unique

    def get_food(self):
        print(self.food)

    def get_home(self):
        print(self.home)

    def set_home(self,home = "Kennel"):
        self.home = home
    
    def set_food(self,food = "flesh, dog-food, rotis etc. "):
        self.food = food

    def get_unique(self):
        print(self.unique)

    def set_unique(self,unique = "loyal"):
        self.unique = unique
    

class dolphin(wild):
    def __init__(self,home = None,food = None,unique = "friendly"):
        if home == None:
            self.home = wild().get_home(True) + "Specific -Oceans , Seas etc." 
        else:
            self.home = home
        
        if food == None:
            self.food = wild().get_food(True)  + "Specific - Other fish etc. "
        else:
            self.food = food
        
        self.unique = unique

    def get_food(self):
        print(self.food)

    def get_home(self):
        print(self.home)

    def set_home(self,home = "Oceans , Seas etc."):
        self.home = home
    
    def set_food(self,food = "Other fish etc."):
        self.food = food

    def get_unique(self):
        print(self.unique)

    def set_unique(self,unique = "frirendly"):
        self.unique = unique


class cow(domestic):
    def __init__(self,home = None,food = None,unique = "live-stock"):
        if home == None:
            self.home = domestic().get_home(True) 
        else:
            self.home = home
        
        if food == None:
            self.food = domestic().get_food(True)  + "Specific - grass, shrubs etc."
        else:
            self.food = food
        
        self.unique = unique

    def get_food(self):
        print(self.food)

    def get_home(self):
        print(self.home)

    def set_home(self,home = domestic().get_home(True)):
        self.home = home
    
    def set_food(self,food = "grass, shrubs etc."):
        self.food = food

    def get_unique(self):
        print(self.unique)

    def set_unique(self,unique = "live-stock"):
        self.unique = unique

class lion(wild):
    def __init__(self,home = None,food = None,unique = "King Of Forest"):
        if home == None:
            self.home = wild().get_home(True)  + " Specifc - Forests/Den"
        else:
            self.home = home
        
        if food == None:
            self.food = wild().get_food(True)  + "Specific - All other animals"
        else:
            self.food = food
        
        self.unique = unique

    def get_food(self):
        print(self.food)

    def get_home(self):
        print(self.home)

    def set_home(self,home = "Forests/Den"):
        self.home = home
    
    def set_food(self,food = "All other animals"):
        self.food = food

    def get_unique(self):
        print(self.unique)

    def set_unique(self,unique = "king of forest"):
        self.unique = unique


