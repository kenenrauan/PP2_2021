from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.urls import path
from . import views
from .views import VacancyDetailAPIViews, CompanyVacListAPIView, vacancyTopTenAPIView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('',  views.hello),

    path('companies', views.companyList),
    path('companies/<int:id>', views.companyDetail),
    path('companies/<int:id>/vacancies', CompanyVacListAPIView.as_view()),
    path('vacancies', views.vacancyList),
    path('vacancies/<int:id>', VacancyDetailAPIViews.as_view()),
    path('vacancies/top_ten', vacancyTopTenAPIView.as_view()),
]
