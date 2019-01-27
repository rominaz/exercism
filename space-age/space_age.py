class SpaceAge(object):

    @staticmethod
    def year_to_seconds():
        return 365.25 * 24 * 3600

    # I used this static function to calculate earth year
    # to seconds and then used it on my functions


    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        return round(self.seconds / SpaceAge.year_to_seconds(), 2)

    def on_mercury(self):
        return round(self.seconds / (SpaceAge.year_to_seconds() * 0.2408467) , 2)

    def on_venus(self):
        return round(self.seconds / (SpaceAge.year_to_seconds() * 0.61519726) , 2)

    def on_mars(self):
        return round(self.seconds / (SpaceAge.year_to_seconds() * 1.8808158) , 2)

    def on_jupiter(self):
        return round(self.seconds / (SpaceAge.year_to_seconds() * 11.862615) , 2)
    
    def on_saturn(self):
        return round(self.seconds / (SpaceAge.year_to_seconds() * 29.447498) , 2)

    def on_uranus(self):
        return round(self.seconds / (SpaceAge.year_to_seconds() * 84.016846) , 2)

    def on_neptune(self):
        return round(self.seconds / (SpaceAge.year_to_seconds() * 164.79132) , 2)
