from django.http import JsonResponse

# Create your views here.
myself = {

    "Name": "Adeyinka Adewojo",

    "Track": "Backend(Python)",

    "Message": "Looking forward to becoming a great Software Developer."

}


def index(request):
    return JsonResponse(myself, json_dumps_params={'indent': 2})
