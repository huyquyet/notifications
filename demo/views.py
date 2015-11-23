from django.views.generic import ListView
from swampdragon.permissions import login_required

from .models import Notification


class Notifications(ListView):
    model = Notification
    template_name = 'home.html'

    def get_queryset(self):
        return self.model.objects.order_by('-pk')[:5]

    @login_required
    def subscribe(self, **kwargs):
        super().subscribe(**kwargs)

    def get_subscription_contexts(self, **kwargs):
        return {'user_id': self.connection.user.pk}
