from django.urls import path
from restapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('drink/',views.drinkAPIView.as_view()),
    path('drink/<int:id>/',views.drinklist.as_view()),
    path('generic/drink/<int:id>/',views.GenericAPIView.as_view()),
    #path('drink/<int:pk>/',views.drink_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)