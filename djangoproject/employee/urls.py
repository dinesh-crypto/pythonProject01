from django.urls import path
from .views import display, empview, created, search, send_mail, submit

urlpatterns = [
    path('display/',display),
    path('empview/',empview),
    path('created/',created),
    path('search/',search),
    path('sendmail/',send_mail),
    path('submit/',submit),
]
