from .models import VkUser

def settings(request):
    return {'settings': VkUser.load()}