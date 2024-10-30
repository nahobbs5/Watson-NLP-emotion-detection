import requests, json # Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } } # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header) # Send a POST request to the API with the text and headers
    

    #parsing JSON response from API
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        #Extract emotions from response
        anger_score = formatted_response.get('documentSentiment', {}).get('anger_score', 0)
        disgust_score = formatted_response.get('documentSentiment', {}).get('disgust_score', 0)
        fear_score = formatted_response.get('documentSentiment', {}).get('fear_score', 0)
        joy_score = formatted_response.get('documentSentiment', {}).get('joy_score', 0)
        sadness_score = formatted_response.get('documentSentiment', {}).get('sadness_score', 0)
        dominant_emotion = [anger_score, disgust_score, fear_score, joy_score, sadness_score]


        # Return the emotions in a dictionary
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': find_dominant_emotion(dominant_emotion)
        }

    elif response.status_code == 500:
        return {"error": "Internal Server Error"}

    # Handle other response codes if necessary
    return {"error": f"Unexpected status code: {response.status_code}"}


def find_dominant_emotion(numbers):
    if not numbers:
        return None  # Return None if the list is empty
    return max(numbers)  # Return the highest score from the list

