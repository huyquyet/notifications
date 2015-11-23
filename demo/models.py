from django.contrib.auth.models import User

from django.db import models
from swampdragon.models import SelfPublishModel
from swampdragon.permissions import login_required

from .serializers import NotificationSerializer


class Notification(SelfPublishModel, models.Model):
    serializer_class = NotificationSerializer
    message = models.TextField()
    user = models.ForeignKey(User)

    @login_required
    def subscribe(self, **kwargs):
        super().subscribe(**kwargs)

    def get_subscription_contexts(self, **kwargs):
        return {'user_id': self.connection.user.pk}
