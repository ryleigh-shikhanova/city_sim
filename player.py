class Player:
    def __init__(self, city_name, money):
        self.city_name = city_name
        self.money = money
        self.buildings = []
        self.production_capacity = 0  # Total production capacity from all buildings

    def __str__(self):
        return f"{self.city_name} (Money: {self.money}) Total Production Capacity: {self.production_capacity}  "

    def add_money(self, amount):
        self.money += amount

    def rename_city(self, new_name):
        self.city_name = new_name

    def add_building(self, building):
        self.buildings.append(building)
        self.production_capacity += building.production  # Update total production capacity 

    def remove_building(self, building):
        #remove a building from the player's list of buildings
        pass