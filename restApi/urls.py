from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from restApi import views

urlpatterns = [
    path("ticket_api/tickets/", views.TicketList.as_view()),
    path("ticket_api/tickets/<int:pk>/", views.TicketDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)  # type: ignore
