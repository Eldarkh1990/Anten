from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)


@app.route('/')
def home():
    return "Rango.Ai is running."


@app.route('/check-signal', methods=['POST'])
def check_signal():
    data = request.get_json()
    city = data.get('city', '').lower()
    hour = datetime.datetime.now().hour

    if city == "tehran":
        status = "قوی" if 9 <= hour <= 11 or 17 <= hour <= 20 else "ضعیف"
    elif city == "mashhad":
        status = "متوسط"
    else:
        status = "نامشخص"

    return jsonify({
        "city": city,
        "signal_status": status,
        "suggestion": "اتصال خودکار فعال شود."
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)