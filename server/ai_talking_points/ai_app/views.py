from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import bardapi
import os
import dotenv

dotenv.load_dotenv()

@csrf_exempt
def generate_talking_points(request):
    if request.method == 'POST':
    # set your input text
        input_text = input("How can I help? ")
    # Send an API request and get a response.
        token = os.environ['API_TOKEN']
        response = bardapi.core.Bard(token).get_answer(input_text)
        
        return JsonResponse({'aiResponse': response})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    