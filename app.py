# pip3 install flask
from flask import Flask, request, jsonify
import address

app = Flask(__name__)

@app.route('/smart_address', methods=['POST'])
def handle_smart_address():
    data = request.get_json()

    text = data.get('text', '')
    town_village = data.get('town_village', True)
    change2new = data.get('change2new', False)
    
    try:
        result = address.run(text, town_village, change2new)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)