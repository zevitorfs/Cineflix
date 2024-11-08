from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_200_OK

from src.core.category.application.use_cases.list_category import (
    ListCategory, ListCategoryRequest, ListCategoryResponse)

from django_project.category_app.repository import DjangoORMCategoryRepository

class CategoryViewSet(viewsets.ViewSet):
    #Apos isso tem a função que receber um request e retorna response
    def list(self, request: Request) -> Response:

        # Extração dos argumentos de requisição
        input = ListCategoryRequest()
        
        #Como fiz essa injeção de dependencia, agora a view pega o orm e passa pelo usecase e não encosta na camadad e aplicação com isso pode ate ter ouutro desenvolvedor so ssabdneo a interface da use_case
        #Execução do use_case
        use_case = ListCategory(repository=DjangoORMCategoryRepository())
        output = use_case.execute(input)

        #Montagem da nossa resposta
        
        categories = [
            {
                "id": str(category.id),
                "name": category.name,
                "description": category.description,
                "is_active": category.is_active,
            } for category in output.data
        ]

        #Resposta
        return Response(
            status=HTTP_200_OK, 
            data=categories,
        )
           
