from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def predict(request):
    if request.method == 'POST':
        try:
            # Get the image data from the request body
            image_data = request.POST.get('image')
            
            # Log the received data
            print("Received image data:", image_data)
            
            
            # Return the prediction as a JSON response
            return JsonResponse({'prediction': 'jsp placeholder for now'})
        except Exception as e:
            
            print("Error:", e)
            return JsonResponse({'error': 'An error occurred while processing the request'}, status=500)
    else:
       
        return JsonResponse({'error': 'Invalid request method'}, status=400)
