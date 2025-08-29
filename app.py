
from flask import Flask, request, jsonify
import threading
import time
import requests

app = Flask(__name__)

@app.route('/geocodage/search', methods=['GET'])
def geocodage_search():
    query = request.args.get('q', '')
    if not query:
        return jsonify({
            "error": "Missing required parameter 'q'"
        }), 404

    response = {
        "type": "FeatureCollection",
        "version": "1.0",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [2.3522, 48.8566]
                },
                "properties": {
                    "label": "Paris, France",
                    "score": 0.99,
                    "id": "123456",
                    "type": "municipality",
                    "name": "Paris",
                    "postcode": "75000",
                    "citycode": "75056",
                    "x": 2.3522,
                    "y": 48.8566
                }
            }
        ],
        "attribution": "Mock API",
        "query": query
    }

    return jsonify(response)

@app.errorhandler(404)
def not_found(error):
    return jsonify({"message": "no Route matched with those values"}), 404

def keep_alive():
    while True:
        try:
            requests.get("https://api-temp-eq05.onrender.com/geocodage/search?q=keepalive")
        except Exception as e:
            print(f"Keep-alive failed: {e}")
        time.sleep(600)  # 10 minutes

if __name__ == '__main__':
    threading.Thread(target=keep_alive, daemon=True).start()
    app.run(host='0.0.0.0', port=10000
