from django.http import JsonResponse
from ctransformers import AutoModelForCausalLM, AutoTokenizer
from transformers import pipeline, Conversation
from django.views.decorators.csrf import csrf_exempt
import json
import torch

# Load the model and tokenizer
model_repo = "TheBloke/Kuchiki-L2-7B-GGUF"
model = AutoModelForCausalLM.from_pretrained(model_repo, hf=True)
tokenizer = AutoTokenizer.from_pretrained(model)

@csrf_exempt
def generateTalkingPoints(request):

    if request.method == 'POST':
        try:
            # Get user input text from the POST request
            request_data = json.loads(request.body.decode('utf-8'))
            user_input = request_data.get('user_input', '')

            # Check if the user input is empty
            if not user_input.strip():
                return JsonResponse({'error': 'Empty user input'}, status=400)

            # Tokenize the user input with padding on the left side
            input_ids = tokenizer.encode(user_input, return_tensors="pt", padding="max_length", max_length=100, truncation=True)

            # Generate text using the model
            with torch.no_grad():
                output = model.generate(input_ids, max_length=100, num_return_sequences=1)

            # Decode the generated text
            generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

            return JsonResponse({'generated_text': generated_text})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
    return JsonResponse({'error': 'Invalid request method'}, status=400)
    
