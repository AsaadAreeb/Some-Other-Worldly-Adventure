class Player:
    def __init__(self, name=None, profession=None, hp=10, attack=2, strength=5, luck=5, sentiments=1, friends=None):
        self.name = name
        self.profession = profession
        self.hp = hp
        self.attack = attack
        self.strength = strength
        self.damage = self.attack * self.strength
        self.luck = luck
        self.sentiments = sentiments
        if friends is None:
            friends = []
        self.friends = friends
    
    def calculate_damage(self):
        return self.attack * self.strength

    def perform_attack(self, enemy):
        enemy.receive_damage(self.calculate_damage())

    def receive_damage(self, damage):
        self.hp -= damage
    
    def become_friend(self, friend):
        friend = str(friend)
        self.friends.append(friend)
    

