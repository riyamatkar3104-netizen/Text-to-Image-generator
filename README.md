# ✦ AI Image Generator

A simple web app built with **Flask** that generates images from text prompts using the **Stability AI API**. No database, no login — just type a prompt and get an image instantly.

---

## 🚀 Features

- Text to image generation
- Download generated images
- No login or database required
- Deploy-ready (Render / Railway)

---

## 📁 Project Structure

```text
ai-image-generator/
├── app.py                  # Main Flask app
├── requirements.txt        # Python dependencies
├── static/
│   └── images/             # Generated images saved here
└── templates/
    └── index.html          # Frontend UI
```

---

## 🔑 Get Your Stability AI API Key

1. Go to [https://platform.stability.ai](https://platform.stability.ai)
1. Sign up / Log in
1. Click your profile → **API Keys**
1. Click **"Create API Key"** and copy it

---

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/sakshi142004/ai-image-generator-flask.git
cd ai-image-generator-flask
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your API Key

Open `app.py` and replace this line:

```python
STABILITY_API_KEY = os.environ.get("STABILITY_API_KEY", "")
```

With your actual key:

```python
STABILITY_API_KEY = "sk-your-actual-api-key-here"
```

### 4. Run the app

```bash
python app.py
```

Open your browser and go to → `http://localhost:5001`

---

## ☁️ Deploy on Render

1. Push your code to GitHub
1. Go to [https://render.com](https://render.com) → **New Web Service**
1. Connect your GitHub repo
1. Set the following:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
1. Add **Environment Variables:**

| Key | Value |
| --- | --- |
| `STABILITY_API_KEY` | `sk-your-api-key-here` |
| `SECRET_KEY` | `any-random-string` |
| `FLASK_ENV` | `production` |

1. Click **Deploy** ✅

> ⚠️ Before deploying, revert your API key line back to:
>
> ```python
> STABILITY_API_KEY = os.environ.get("STABILITY_API_KEY", "")
> ```

---

## ⚡ Keep Render App Awake (Free Tier)

Render free tier sleeps after 15 mins of inactivity. To fix this:

1. Go to [https://cron-job.org](https://cron-job.org) and create a free account
1. Create a new cron job:
   - **URL:** `https://your-app.onrender.com/`
   - **Schedule:** Every 10 minutes
1. Save — your app will never sleep again ✅

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Image Generation:** Stability AI API (Stable Diffusion)
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** Render

---
