import requests
import json
import spotipy
import statistics as s
import math
from spotipy.oauth2 import SpotifyClientCredentials
<<<<<<< HEAD
#from convertToJSON import convert
import keys as k

CLIENT_ID= k.ID
CLIENT_SECRET= k.SECRET
"""
Using spotipy, another API, we can authenticate Spotify accounts using Oauth2

Set a variable, token, = the spotipy.oauth2.SpotifyClientCredentials request
print(token) to make sure we're finding it

Set a variable, cache_token = token.get_access_token()
This returns the string form of the previous class we were looking at

cache_token: object = token.get_access_token()
^^^ This creates an object of the access token ^^^
print(cache_token) to make sure we're finding it
"""
=======
#Lines 10-14 connect to the API. Don't worry about understanding this.
token = spotipy.oauth2.SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
accessToken = token.get_access_token(as_dict=False)
clientCredentialsManager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=clientCredentialsManager)
cache_token: object = token.get_access_token(as_dict=False)


"""
This function will get playlist tracks and track features
The data is organized in a dictionary 
"""
indata = sp.playlist_tracks("6sMmJun3rrgXQwKJnsoNPO?si=xAwrEBknQR6gnC1CdOZoZg")
#get playlist tracks and track data
def getPlaylistData():
    jsonDict = {}

    headers = {'Authorization': "Bearer " + accessToken}
    for track in indata['tracks']['items']:
        songId = track['track']['id']
        url = "https://api.spotify.com/v1/audio-features/" + songId
        response = requests.get(url, headers=headers)
        jsonDict[track['track']['name']] = json.loads(response.text)
    return jsonDict

#Return the songs and song features for the playlist
out = getPlaylistData()
#print(out)



#Create a function to write the inData to JSON file.
def writeToJSONFile(path, fileName, indata):
    filePathNameWExt = './' + path + '/' + fileName +'.json'
    with open (filePathNameWExt, 'w') as fp:
        json.dump(indata, fp, indent = 4)
        
#Create variables to assign to the JSON file.
path = './'
fileName = 'playlistData'
data = out

#Call the writeToJSONFile function.
writeToJSONFile(path, fileName, data)

#Sometimes we can comment block out code that would be useful for testing, but not necessary for everything.
'''
def get_energy():
    temp = data['Ghost Safari']
    for question_data in temp:
        replies_access = question_data['items']
        for replies_data in replies_access:
            energy = replies_data['track']['energy']
            save_energy.append(energy)

save_energy = []
get_energy()
save_energy
'''

#Create a function that will get playlist averages and print the output.
def getAvgPlaylistData():
    energy = round(s.mean([data[track]['energy'] for track in data]), 3)
    valence = round(s.mean([data[track]['valence'] for track in data]), 3)
    tempo = round(s.mean([data[track]['tempo'] for track in data]), 3)
    loudness = round(s.mean([data[track]['loudness'] for track in data]), 3)
    print("Average energy is: ", energy)
    print("Average valence is: ", valence)
    print("Average tempo is: ", tempo)
    print("Average loudness is: ", loudness)

#Call the function
getAvgPlaylistData()
songKey = s.mode([data[track]['key'] for track in data])

#Create a function that will assign literal song keys to the coordinated number signature returned from the dictionary.
def matchSongKey():
    songKeyShaper = {
        'C': 0,
        'C#': 1,
        'D': 2,
        'D# / Eb': 3,
        'E': 4,
        'F': 5,
        'F# / Gb': 6,
        'G': 7,
        'G#': 8,
        'A': 9,
        'A# / Bb': 10,
        'B': 11}

#Create a for loop that pairs song keys and song modes and prints a statement with your matched output.
    for key, match in songKeyShaper.items():
        if match == songKey: print("The key is: ", key)
            
#Call the match song key function.
matchSongKey()

#Try to create a dictionary that will map song keys to HTML color codes.
#Could be useful for data visualizations.
songKeyColor = {
          0: '#f00',
          1: '#90f',
          2: '#ff0',
          3: '#c49',
          4: '#cff',
          5: '#b03',
          6: '#89f',
          7: '#f80',
          8: '#c7f',
          9: '#3d3',
         10: '#b68',
         11: '#9df'}
