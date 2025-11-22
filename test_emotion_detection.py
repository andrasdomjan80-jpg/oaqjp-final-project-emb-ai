import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        test_cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear")
        ]

        for text, expected_dominant in test_cases:
            with self.subTest(text=text):
                result = emotion_detector(text)

                # Check dominant emotion matches expected
                self.assertEqual(result["dominant_emotion"], expected_dominant)

                # Optional sanity checks: required keys exist
                self.assertIn("anger", result)
                self.assertIn("disgust", result)
                self.assertIn("fear", result)
                self.assertIn("joy", result)
                self.assertIn("sadness", result)
                self.assertIn("dominant_emotion", result)


if __name__ == "__main__":
    unittest.main()
