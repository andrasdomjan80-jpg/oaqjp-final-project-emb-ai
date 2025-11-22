from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    """Render the index page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detection_route():
    """
    Process the GET request from mywebscript.js and return formatted string.
    """
    # Read input exactly how the JS sends it
    text_to_analyse = request.args.get("textToAnalyze", "").strip()

    # Run the emotion detector (it handles blank and invalid input)
    result = emotion_detector(text_to_analyse)

    # Check for valid result based on dominant_emotion
    if result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    # Extract values
    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant = result["dominant_emotion"]

    # Build customer-required formatted sentence
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )

    return response_text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
