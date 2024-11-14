from uuid import UUID
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import ( 
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND
    )

from src.core.category.application.use_cases.exceptions import CategoryNotFound
from src.core.category.application.use_cases.get_category import GetCategory, GetCategoryRequest
from src.core.category.application.use_cases.list_category import (
    ListCategory, ListCategoryRequest, ListCategoryResponse)

from django_project.category_app.repository import DjangoORMCategoryRepository

class CategoryViewSet(viewsets.ViewSet):

    def list(self, request: Request) -> Response:

       
        input = ListCategoryRequest()
        
        #Como fiz essa injeção de dependencia, agora a view pega o orm e passa pelo usecase e não encosta na camadad e aplicação com isso pode ate ter ouutro desenvolvedor so ssabdneo a interface da use_case
        #Execução do use_case
        use_case = ListCategory(repository=DjangoORMCategoryRepository())
        output = use_case.execute(input)

        #Montagem da nossa resposta
        #Aqui é uma lista para devolver todos os dados
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
    
    #Agora vamos fazer a função de retrieve que faz op mapemaento da url para o método
    # o pk é para simboliza a primary key que esta tenta busca no banco
    def retrieve(self, request: Request, pk=None) -> Response:
        #Exeção para hhhtp_400_bad_request
        try:
            category_pk = UUID(pk)

        except ValueError:
            return Response(status=HTTP_400_BAD_REQUEST)
        
        use_case = GetCategory(repository=DjangoORMCategoryRepository())
        #Execeção para caso for HHTP_404_NOT_FOUND
        try:
            result = use_case.execute(request=GetCategoryRequest(id=category_pk))

        #Essa execção vem da camada de aplicação
        except CategoryNotFound:
            return Response(status=HTTP_404_NOT_FOUND)
        
        #Processamento
        
        use_case = GetCategory(repository=DjangoORMCategoryRepository())
        result = use_case.execute(GetCategoryRequest(id=category_pk))

        #Esse vai ser o processamento para json
        category_output = {
            "id": str(result.id),
            "name": result.name,
            "description": result.description,
            "is_active": result.is_active,
        }

        #saida
        # Verifica se o response é o do rest_framework
        return Response(
            status=HTTP_200_OK, 
            data=category_output
        )

        
        
           
