from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# URLs de exemplo (substitua pelas suas URLs)
M3U_URL = "https://exemplo.com/playlist.m3u"
XTREAM_API_URL = "https://exemplo.com/xtream/api.php"
XTREAM_USER = "usuario"
XTREAM_PASSWORD = "senha"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/load_m3u", methods=["POST"])
def load_m3u():
    url = request.json.get("url")
    if not url:
        return jsonify({"error": "URL não fornecida"}), 400

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route("/load_xtream", methods=["POST"])
def load_xtream():
    try:
        # Exemplo de requisição à API Xtream
        params = {
            "username": XTREAM_USER,
            "password": XTREAM_PASSWORD
        }
        response = requests.get(XTREAM_API_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Usa a porta do Render ou 5000 localmente
    app.run(host="0.0.0.0", port=port)
