import requests, json, spotipy, statistics as s
from spotipy.oauth2 import SpotifyClientCredentials
from flask import Flask

#Add your spotify developer client ID and client secret codes into these strings.
CLIENT_ID=""
CLIENT_SECRET=""

#Lines 10-14 connect to the API. Don't worry about understanding this.
token = spotipy.oauth2.SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
accessToken = token.get_access_token()
clientCredentialsManager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=clientCredentialsManager)
cache_token: object = token.get_access_token()

#Create a function to gather the input of a spotify songs URI (Uniform Resource Identifier).
def getURI():
    URI = sp.audio_features(input('\nCopy the Spotify URI of your song and paste it here: '))
    return URI

#Call the function and add it to a varaible called inData.
inData = getURI()

#Create a function to write the inData to JSON file.
def writeToJSONFile(path, fileName, inData):
    filePathNameWExt = './' + path + '/' + fileName +'.json'
    with open (filePathNameWExt, 'w') as fp:
        json.dump(inData, fp, indent = 4)

#Create variables to assign to the JSON file.
path = './'
fileName = 'songData'
data = inData

#Call the writeToJSONFile function.
writeToJSONFile(path, fileName, data)

#Open the JSON file and add the attributes to a dictionary variable called dictData.
with open("songData.json") as read_file:
    dictData = json.load(read_file)[0]

#Print the dictData variable to see what we got.
print(dictData)

#Create variables for each metric you want to pull out of the dictionary.
songKey = dictData['key']
songValence = dictData['valence']
songTempo = dictData['tempo']
songTimeSignature = dictData['time_signature']
songMode = dictData['mode']

#Create simple if/else statement find whether the song mode is major or minor.
if songMode == 0:
    songMode = 'Minor'
else:
    songMode = 'Major'

#Create a function that will assign literal song keys to the coordinated number signature returned from the dictionary.
def matchSongKey():
    songKeyShaper = {
        'C': 0,
        'C# / Db': 1,
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
        if match == songKey: print("\nThe key of the song that you entered is:", key, songMode)

#Call the match song key function.
matchSongKey()

#Create an output details function that formats song tempo to 0 float values, and prints out the song tempo and the time signature / 4.
def outputDetails():
    print("\nThe tempo is: {:0.0f}".format(songTempo),
        "BPM, and the time signature is:",
        songTimeSignature, "/ 4")

#Call the output details function.
outputDetails()

#Ask for an input to exit the program.
input("\nPress Enter to exit")
