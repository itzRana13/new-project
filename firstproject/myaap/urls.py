from django.urls import path
from myaap import views
urlpatterns = [path('',views.homepageview),
               path('check',views.datapage),
]