from flask import Flask, request, jsonify, render_template
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Initialize Flask app
app = Flask(__name__)

# Spotify API Credentials (Replace with your credentials)
CLIENT_ID = "your_spotify_client_id"
CLIENT_SECRET = "your_spotify_client_secret"

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["GET"])
def recommend():
    genre = request.args.get("genre", "pop")  # Default genre is "pop"
    
    # Fetch Spotify recommendations
    results = sp.recommendations(seed_genres=[genre], limit=10)
    
    recommendations = []
    for track in results["tracks"]:
        song = {
            "name": track["name"],
            "artist": track["artists"][0]["name"],
            "url": track["external_urls"]["spotify"],
            "image": track["album"]["images"][0]["url"]
        }
        recommendations.append(song)
    
    return jsonify(recommendations)

if __name__ == "__main__":
    app.run(debug=True)
