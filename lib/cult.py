from .bloodoath import BloodOath

class Cult:

    all = []

    def __init__(self, name, location, founding_year, slogan):
        self.name = name    
        self.location = location
        self.founding_year = founding_year
        self.slogan = slogan
        Cult.all.append(self)

    def recruit_follower(self, follower):
        pass

    def cult_population(self):
        pass

    @classmethod
    def all(self):
        pass
    
    @classmethod
    def find_by_name(self):
        pass

    @classmethod
    def find_by_location(self):
        pass

    @classmethod
    def find_by_founding_year(self):
        pass
