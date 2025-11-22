"""
Flask web server for the Emotion Detection project.

This module exposes two routes:
1. "/"                  → returns the main HTML page
2. "/emotionDetector"   → processes user input text and returns a formatted
                          emotion analysis string.

The server interacts with the `emotion_detector` function in the
EmotionDetection package and formats the model output for display.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    """
    Render the main index page.

    Returns:
        str: The rendered HTML content of index.html.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detection_route():
    """
    Process the GET request from the client and return an emotion analysis.

    The function reads text from the "textToAnalyze" GET parameter,
    sends it to the Watson NLP emotion detector, and formats the output.

    If the emotion detector returns None for dominant_emotion
    (which means blank or invalid text), a friendly error message is returned.

    Returns:
        str: A formatted message containing emotion scores and the
             dominant emotion, or an error message for invalid input.
    """
    # Read text exactly as the JavaScript code sends it
    text_to_analyse = request.args.get("textToAnalyze", "").strip()

    # Run the emotion detector (it handles blank and invalid input)
    result = emotion_detector(text_to_analyse)

    # If no valid dominant emotion, return an error message
    if result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    # Extract emotion scores
    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant = result["dominant_emotion"]

    # Construct the required output string
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )

    return response_text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
