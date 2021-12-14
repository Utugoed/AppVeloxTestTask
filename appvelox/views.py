from django.http import JsonResponse


def custom_404(request, exception=None):
    return JsonResponse({
                    'status_code': '404',
                    'error': 'This resource was not found'
                    })
