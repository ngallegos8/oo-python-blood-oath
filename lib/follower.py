from .bloodoath import BloodOath

class Follower:

    all = []

    def __init__(self, name, age, life_motto):
        self.name = name
        self.age = age
        self.life_motto = life_motto  
        Follower.all.append(self)

    def cults(self):
        pass

    def join_cult(self):
        pass

    @classmethod
    def all(self):
        pass

    @classmethod
    def of_a_certain_age(self):
        pass

    