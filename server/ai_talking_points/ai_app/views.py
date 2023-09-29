from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from transformers import GPT2Tokenizer, GPT2LMHeadModel

model_name = "gpt2"  # Choose the model name
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

@csrf_exempt
def generate_talking_points(request):
    if request.method == 'POST':
        user_input = "Can you tell me the temperature in Chicago, Illinois."
        input_ids = tokenizer.encode(user_input, return_tensors="pt")

        # Generate a response
        response_ids = model.generate(input_ids, max_length=50, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)

        # Decode the response
        response_text = tokenizer.decode(response_ids[0], skip_special_tokens=True)
        print(response_text)

        return JsonResponse({'aiResponse': response_text})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)