from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()
router.register("types", TypeViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('Type1/',Type1View.as_view()),

    path('Type2/',Type2View.as_view()),

    path('Type3/',Type3View.as_view()),

    path('Type4/',Type4View.as_view()),
    # path('type/',TypeView.as_view()),

]

