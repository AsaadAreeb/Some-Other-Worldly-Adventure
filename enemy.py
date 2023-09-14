class Enemy:
    def __init__(self, name, health, attack=1, strength=2):
        self.name = name
        self.health = health
        self.attack = attack
        self.strength = strength

    def calculate_damage(self):
        return self.attack * self.strength

    def receive_damage(self, damage):
        self.health -= damage
    
    def perform_attack(self, enemy):
        enemy.receive_damage(self.calculate_damage())