
def is_done_deact(request):
    request.data['is_done'] = False
    return request

def is_done_act(request):
    request.data.clear()
    request.data['is_done'] = True
    return request
