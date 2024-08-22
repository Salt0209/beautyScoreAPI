from django.urls import path
from .views import age, get_age, sample_data, quality_ugc, get_quality_ugc

urlpatterns = [
    path('age/', age),
    path('get_age/', get_age),
    path('sample_data/', sample_data),
    path('quality_ugc/', quality_ugc),
    path('get_quality_ugc/', get_quality_ugc),
]