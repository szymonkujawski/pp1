class Song():
    def __init__(self,performer,title,album,year):
        self.performer = performer
        self.title = title
        self.album = album
        self.year = str(year)
    
    def __str__(self):
        return "Performer: " + self.performer + "\n" + "Song: " + self.title + "\n" + "Album: " + self.album + "\n" + "Year: " + self.year + "\n"

song1 = Song("Ed Sheeran","Hearts Don't Break Around Me","Devide",2017)
song2 = Song("Tutaj autor","Tutaj Tytul","Tutaj Album",2023)
print(song1)
print(song2)