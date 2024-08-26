'''
This file handles the API requests.
'''
import requests
# Function to get the song recommendation based on the current time
def get_song_recommendation(current_time):
    # Make a request to the live database to get the song recommendation
    response = requests.get(f"https://api.example.com/recommendation/{current_time}")
    if response.status_code == 200:
        return response.json()
    else:
        return []