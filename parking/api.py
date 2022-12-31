from django.http import JsonResponse


def get_available(request):
    return JsonResponse({"test": "OK"}, safe=False)
