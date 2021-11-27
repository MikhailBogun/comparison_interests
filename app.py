from flask import Flask, request, jsonify

from similar_interests import similar_interests


app = Flask(__name__)


@app.route("/api/predict-interests", methods=['POST'])
def get_closest_interests():
    user_interests = request.json.get('interests', [])
    suggested_interests = similar_interests(user_interests)
    return jsonify({'suggestedInterests': suggested_interests})


