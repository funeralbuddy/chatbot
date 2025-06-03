from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)

# Add this line at the top, after imports:
app.secret_key = "your_secret_key_here"  # Required for session storage

# Bot responses
comfort_messages = [
    "I'm here with you. It's okay to feel what you're feeling.",
    "Grief takes time. You're not alone.",
    "Your loved one may be gone, but the love remains.",
    "Please take this moment to breathe. I'm here.",
    "Every tear carries the weight of love.",
    "You are not alone. This moment is held with compassion.",
]

buddhist_reflections = [
    "In life and death, all things arise and pass away. This too shall pass.",
    "Death is not to be feared — it is part of the great unfolding.",
    "All conditioned things are impermanent. Understanding this brings peace.",
    "Even in sorrow, mindfulness can help us hold the pain with care.",
    "In emptiness, we find connection. In grief, we remember love.",
]

@app.route("/", methods=["GET", "POST"])
def home():
    if "history" not in session:
        session["history"] = []

    if request.method == "POST":
        user_input = request.form.get("message", "").strip()
        if user_input:
            if user_input.lower() == "reflect":
                bot_reply = random.choice(buddhist_reflections)
            elif user_input.lower() == "breathe":
                bot_reply = "Let’s breathe together: Inhale… hold… exhale…"
            else:
                bot_reply = random.choice(comfort_messages)

            # Add to history
            session["history"].append({"user": user_input, "bot": bot_reply})
            session.modified = True

        return redirect(url_for("home"))

    return render_template("index.html", history=session.get("history", []))
    
if __name__ == "__main__":
    app.run(debug=True)