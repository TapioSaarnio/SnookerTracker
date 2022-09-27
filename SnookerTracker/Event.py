class Event:

    def __init__(self, data):

        self.id = data['ID']
        self.name = data['Name']
        self.venue = data['Venue']
        self.country = data['Country']
        self.city = data['City']


    def printEvent(self):

        print(self.name)
        print(self.country)
        print(self.city)
        print(self.venue)
        