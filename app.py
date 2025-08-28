
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/geocodage', methods=['GET'])
def geocodage():
    query = request.args.get('q', '')
    limit = request.args.get('limit', '1')

    response = {
        "type": "FeatureCollection",
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
        "version": "1.0",
        "query": query,
        "limit": limit
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
