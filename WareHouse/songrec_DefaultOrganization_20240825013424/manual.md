# Music Recommendation Program User Manual

## Introduction

The Music Recommendation Program is a Python application that recommends a list of songs based on the current time. It uses a live database to search for songs that match the desired mood based on the time of day. For example, if it is 1AM, the program will recommend calm songs like R&B, and if it is 2PM, it will recommend energetic songs like EDM.

This user manual provides instructions on how to install the necessary dependencies and how to use the program.

## Installation

To install the Music Recommendation Program, follow these steps:

1. Make sure you have Python installed on your system. You can download Python from the official website: https://www.python.org/downloads/

2. Clone or download the program files from the GitHub repository: [link to repository]

3. Open a terminal or command prompt and navigate to the directory where you downloaded the program files.

4. Run the following command to install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

   This will install the necessary packages for the program to run.

## Usage

To use the Music Recommendation Program, follow these steps:

1. Open a terminal or command prompt and navigate to the directory where you downloaded the program files.

2. Run the following command to start the program:

   ```
   python music_recommendation.py
   ```

3. The program will open a window displaying a list of recommended songs based on the current time. The list will be initially populated with songs from the live database.

4. To update the song recommendations, click the "Update" button. The program will fetch the current time and retrieve the corresponding song recommendations from the live database.

5. You can scroll through the list of songs using the scrollbar on the right side of the window.

6. To exit the program, close the window or press Ctrl+C in the terminal or command prompt.

## Customization

If you want to customize the program to use a different live database or modify the recommendation criteria, you can make changes to the `music_recommendation.py` and `api.py` files.

In the `music_recommendation.py` file, you can modify the URL in the `get_song_recommendation` function to point to a different API endpoint. Make sure the API returns a JSON response with the song recommendations based on the current time.

In the `api.py` file, you can modify the `get_song_recommendation` function to handle the API request and response according to your requirements.

## Conclusion

The Music Recommendation Program is a simple yet powerful tool for recommending songs based on the current time. By following the installation and usage instructions in this user manual, you can easily use and customize the program to suit your needs. Enjoy your personalized music recommendations!