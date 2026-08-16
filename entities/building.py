class Building:
    def __init__(self, name, cost, production):
        self.name = name
        self.cost = cost
        self.production = production

    def __str__(self):
        return f"{self.name} (Cost: {self.cost}, Production: {self.production})"
