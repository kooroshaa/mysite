from django.http import HttpResponse,JsonResponse

def http_test(request):
    return HttpResponse('this is HTTP!')

def json_test(request):
    return JsonResponse({'method' : 'Json!'})