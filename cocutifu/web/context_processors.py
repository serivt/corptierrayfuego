from web.models import *

def post_types(request):
    post_types = PostType.objects.filter(active=True)
    return {'post_types': post_types}