class Building:
    def __init__(self, name, cost, color, production, x, y):
        self.name = name
        self.cost = cost
        self.color = color
        self.production = production
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.name} (Cost: {self.cost}, Production: {self.production}, self.color, self.x, self.y)"
