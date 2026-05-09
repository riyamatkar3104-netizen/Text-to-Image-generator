import os
import time
import requests
from flask import Flask, render_template, request, send_file, jsonify
import io

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "fallback-secret-key-change-this")

# 🔐 Set this in your hosting environment variables
STABILITY_API_KEY = os.environ.get("STABILITY_API_KEY", "")

# ✅ Ensure static/images folder exists
os.makedirs("static/images", exist_ok=True)


# ---------------- ROUTES ----------------

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form.get('prompt', '').strip()

    if not prompt:
        return jsonify({"error": "Prompt cannot be empty!"}), 400

    if not STABILITY_API_KEY:
        return jsonify({"error": "API key not configured on server!"}), 500

    try:
        url = "https://api.stability.ai/v2beta/stable-image/generate/core"

        headers = {
            "Authorization": f"Bearer {STABILITY_API_KEY.strip()}",
            "Accept": "image/*"
        }

        files = {
            "prompt": (None, prompt),
            "output_format": (None, "png"),
            "width": (None, "512"),
            "height": (None, "512")
        }

        response = requests.post(url, headers=headers, files=files, timeout=60)

        if response.status_code == 200:
            # Save image temporarily with unique name
            filename = f"gen_{int(time.time())}.png"
            image_path = f"static/images/{filename}"

            with open(image_path, "wb") as f:
                f.write(response.content)

            return jsonify({
                "success": True,
                "image_url": f"/static/images/{filename}",
                "filename": filename
            })

        else:
            print("API ERROR:", response.status_code, response.text)
            return jsonify({"error": f"Image generation failed! ({response.status_code})"}), 500

    except requests.exceptions.Timeout:
        return jsonify({"error": "Request timed out. Please try again."}), 504

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": "Server error occurred!"}), 500


@app.route('/download/<filename>')
def download(filename):
    # Sanitize filename to prevent path traversal
    filename = os.path.basename(filename)
    file_path = os.path.join("static", "images", filename)

    if not os.path.exists(file_path):
        return jsonify({"error": "File not found!"}), 404

    return send_file(
        file_path,
        as_attachment=True,
        download_name=filename,
        mimetype='image/png'
    )


# ---------------- RUN ----------------

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    debug = os.environ.get("FLASK_ENV", "production") != "production"
    app.run(debug=debug, host='0.0.0.0', port=port)
