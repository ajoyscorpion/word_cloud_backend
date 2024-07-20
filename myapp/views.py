from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import base64

def generate_image(request):
    if request.method == 'POST':
        data = request.POST
        image = request.FILES
        print(image)
        print(data)
        text = data.get('text')
        image = image.get('image')
        image_data = image.read()
        base64_image = base64.b64encode(image_data).decode('utf-8')
        image_data_url = f"data:image/{image.content_type.split('/')[1]};base64,{base64_image}"

        # Remove background Image

        #print(image_data)
        print(text)
        print(image)
        print("came over here")

        return JsonResponse({'image':image_data_url})
    #return HttpResponse("All good",{'image':image})
