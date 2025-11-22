import requests  # Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyse):  
    # URL of the emotion prediction service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # JSON payload with the text to analyze
    myobj = { 
        "raw_document": { 
            "text": text_to_analyse 
        } 
    }
    
    # Required headers
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Send the POST request
    response = requests.post(url, json=myobj, headers=headers)
    
    # Return response text
    return response.text
