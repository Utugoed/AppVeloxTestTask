from django.http import QueryDict


def is_done_deact(request):
    if isinstance(request.data, QueryDict):
        request.data._mutable = True
    request.data.update({'is_done': 'False'})
    return request

def is_done_act(request):
    if isinstance(request.data, QueryDict):
        request.data._mutable = True
    request.data.clear()
    request.data.update({'is_done': 'True'})
    return request
