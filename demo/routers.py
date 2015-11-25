from swampdragon import route_handler
from swampdragon.route_handler import ModelRouter

from .models import Notification
from .serializers import NotificationSerializer


class NotificationRouter(ModelRouter):
    valid_verbs = ['subscribe']
    route_name = 'notifications'
    model = Notification
    serializer_class = NotificationSerializer

    def get_query_set(self, **kwargs):
        return self.model.objects.all()


route_handler.register(NotificationRouter)
