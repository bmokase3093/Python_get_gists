from flask import Flask, jsonify, request
import requests
from flask_caching import Cache

app = Flask(__name__)

# Configure caching
app.config["CACHE_TYPE"] = "SimpleCache"
app.config["CACHE_DEFAULT_TIMEOUT"] = 300
cache = Cache(app)

# Endpoint to fetch a user's public gists with pagination and caching
@app.route('/<username>', methods=['GET'])
def get_gists(username):
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=5, type=int)

    github_api_url = f"https://api.github.com/users/{username}/gists?page={page}&per_page={per_page}"

    # Caching key based on username, page, and per_page
    cache_key = f"gists_{username}_page{page}_per{per_page}"
    
    # Check if the response is cached
    cached_response = cache.get(cache_key)
    if cached_response:
        return cached_response, 200

    # Try to fetch data from GitHub API
    try:
        response = requests.get(github_api_url, timeout=5)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        return jsonify({"error": "Request to GitHub timed out"}), 504
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"GitHub API error: {str(e)}"}), response.status_code

    # Parse response JSON into a list of gists
    gists = response.json()
    gist_list = [{
        "id": gist["id"],
        "url": gist["html_url"],
        "description": gist.get("description", "No description provided")
    } for gist in gists]

    # Cache the response
    cache.set(cache_key, (jsonify(gist_list), 200))

    return jsonify(gist_list), 200

# For running the app directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)