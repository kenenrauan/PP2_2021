from .views import companies_list, company_detail, company_vacancies, vacancies_list, vacancies_top_ten, vacancy_detail
from django.urls import path

urlpatterns = [
    path('companies/', companies_list),
    path('companies/<int:id>/', company_detail),
    path('companies/<int:id>/vacancies/', company_vacancies),
    path('vacancies/', vacancies_list),
    path('vacancies/<int:id>/', vacancy_detail),
    path('vacancies/top_ten/', vacancies_top_ten),
]