from flask import Flask, jsonify, render_template

app = Flask(__name__, static_folder="frontend/static", template_folder="frontend")

data = {
    "USA": {"incidents": 50, "recent_event": "Sample Event 1"},
    "CAN": {"incidents": 10, "recent_event": "Sample Event 2"}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data/<country_code>')
def get_country_data(country_code):
    return jsonify(data.get(country_code, {}))

if __name__ == "__main__":
    app.run()