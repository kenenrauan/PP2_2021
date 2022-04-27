import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http.response import JsonResponse, Http404
from rest_framework import mixins, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Company, Vacancy
from .serializers import CompanySerializer, CompanySerializer2, VacancySerializer


def hello(request):
    return render(request, 'api/1.html')


@csrf_exempt
def companyList(request):
    if request.method == "GET":
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = json.loads(request.body)
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            # call create function
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)


@csrf_exempt
@permission_classes((IsAuthenticated, ))
def companyDetail(request, id):
    try:
        category = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    if request.method == "GET":
        return JsonResponse(category.to_json(), safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = CompanySerializer2(instance=category, data=data)
        if serializer.is_valid():
            # call create function
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({'message': 'deleted'}, status=204)


@api_view(['GET', 'POST'])
def vacancyList(request):
    if request.method == 'GET':
        categories = Vacancy.objects.all()

        serializer = VacancySerializer(categories, many=True)
        # categoreis_json = [category.to_json() for category in categories]
        return Response(serializer.data)
    elif request.method == 'POST':
        # json string to dict

        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            # call create function
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class VacancyDetailAPIViews(APIView):
    def get_object(self, id):
        try:
            return Vacancy.objects.get(pk=id)
        except Vacancy.DoesNotExist as e:
            raise Http404

    def get(self, reqeust, id=None):
        vacancy = self.get_object(id)
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)

    def put(self, reqeust, id=None):
        vacancy = self.get_object(id)
        serializer = VacancySerializer(instance=vacancy, data=reqeust.data)
        if serializer.is_valid():
            # call create function
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, reqeust, id=None):
        vacancy = self.get_object(id)
        vacancy.delete()
        return Response({'message': 'deleted'}, status=204)


class CompanyVacListAPIView(mixins.ListModelMixin,
                            generics.GenericAPIView):

    serializer_class = VacancySerializer

    def get_queryset(self, *args, **kwargs):
        return Vacancy.objects.filter(company_id=self.kwargs['id'])

    def get(self, request, *args, **kwargs):
        return self.list(request)





class vacancyTopTenAPIView(generics.ListAPIView):
    queryset = Vacancy.objects.all().order_by('-salary')[:10]
    serializer_class = VacancySerializer
    permission_classes = [IsAuthenticated]
