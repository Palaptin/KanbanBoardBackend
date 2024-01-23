from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from restApi import views

urlpatterns = [
    path("tickets/", views.TicketList.as_view()),
    path("tickets/<int:pk>/", views.TicketDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)  # type: ignore
