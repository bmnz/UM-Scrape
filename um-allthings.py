from bs4 import BeautifulSoup
import sqlite3
import urllib.request

def main():
    """Main function to read through data and run some debug stuff from the interactive python shell."""
    print("Running um-allthings main.")

def get_string_from_file(filename):
    f = open(filename, 'r')
    filestring = f.read()
    f.close()
    return filestring

def get_soup_from_file(filename):
    soup = BeautifulSoup(get_string_from_file(filename), 'html.parser')
    return soup

def get_soup_show_name(show):
    #show is a soup object
    return show.h3.get_text()

def get_soup_show_date(show):
    #show is a soup object
    return show.h3.find(class_='setlistdate').get_text()

def get_soup_show_string(show):
    #show is a soup object
    show_strings = []
    show_strings.append(get_soup_show_date(show))
    for p in show.find_all('p'):
        show_strings.append(p.get_text())
    return '\n'.join(show_strings)

def get_soup_show_songs(show):
    #show is a soup object
    show_songs = []
    for song in show.find_all('a'):
        if song.get('title'):
            show_songs.append(song.get('title'))
    return show_songs

def db_populate_songs_table(soup,filename):
    conn = sqlite3.connect('um.db')
    dbcurs = conn.cursor()
    dbcurs.execute("CREATE TABLE songs(dbid INT, song TEXT, show TEXT, track INT)")

    #This dbid only good for one pass-through
    dbid = 0
    for show in allthings_soup.find_all(class_='setlist'):
        #fill variables that are same for shows, then move on to songs
        show_name = get_soup_show_name(show)
        track = 0
        for song in get_soup_show_songs(show):
            dbid += 1
            track += 1
            dbcurs.execute("INSERT INTO songs VALUES(?,?,?,?)",(dbid, song, show_name, track)) 
            
    #Cross Fingers
    conn.commit()
    conn.close()


if __name__ == "__main__":
    #Parse html with beautiful soup
    file_allthings = '2017.html'
    file_db = 'um.db'
    #allthings_soup = get_soup_from_file(file_allthings)
    #allthings_soup = get_soup_from_http(http_allthings)
    #for site in http_allthings_sites:
        #allthings_soup = get_soup_from_http(site)
        #db_populate_songs_table(allthings_soup,file_db)
    #print(allthings_soup.prettify())
    #db_populate_songs_table(allthings_soup,file_db)

