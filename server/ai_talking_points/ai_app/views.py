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
        try:
            data = json.loads(request.body)
            input_text = data.get('input_text', '')

            if not input_text:
                return JsonResponse({'error': 'Missing input_text in the request'}, status=400)

            token = os.environ['API_TOKEN']
            response = bardapi.core.Bard(token).get_answer(input_text)

            return JsonResponse({'aiResponse': response})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)