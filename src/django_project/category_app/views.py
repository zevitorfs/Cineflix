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

from django_project.category_app.serializers import CategoryResponseSerialezer, ListCategoryResponseSerializer, RetriveCategoryResponseSerializer, RetriverCategoryResquestSerializer
from src.core.category.application.use_cases.exceptions import CategoryNotFound
from src.core.category.application.use_cases.get_category import GetCategory, GetCategoryRequest
from src.core.category.application.use_cases.list_category import (
    ListCategory, ListCategoryRequest, ListCategoryResponse)

from django_project.category_app.repository import DjangoORMCategoryRepository

class CategoryViewSet(viewsets.ViewSet):

    def list(self, request: Request) -> Response:

        #Como fiz essa injeção de dependencia, agora a view pega o orm e passa pelo usecase e não encosta na camadad e aplicação com isso pode ate ter ouutro desenvolvedor so ssabdneo a interface da use_case
        #Execução do use_case
        use_case = ListCategory(repository=DjangoORMCategoryRepository())
        response = use_case.execute(request=ListCategoryRequest())
        

        #Montagem da nossa resposta
        #Aqui é uma lista para devolver todos os dados
        serializer = ListCategoryResponseSerializer(instance=response)

        #Resposta
        return Response(
            status=HTTP_200_OK, 
            data=serializer.data,
        )
    
    #Agora vamos fazer a função de retrieve que faz op mapemaento da url para o método
    # o pk é para simboliza a primary key que esta tenta busca no banco
    def retrieve(self, request: Request, pk=None) -> Response:
        #Vai serializa os dados que passei o pk, o serializer verifica que id é um se não for vai da um error 400
        serializer = RetriverCategoryResquestSerializer(data={"id": pk})
        #Exeção para hhhtp_400_bad_request
        serializer.is_valid(raise_exception=True)
        
        use_case = GetCategory(repository=DjangoORMCategoryRepository())
        #Execeção para caso for HHTP_404_NOT_FOUND
        try:
            result = use_case.execute(request=GetCategoryRequest(id=serializer.validated_data["id"]))

        #Essa execção vem da camada de aplicação
        except CategoryNotFound:
            return Response(status=HTTP_404_NOT_FOUND)
        
        #Processamento
        
        #use_case = GetCategory(repository=DjangoORMCategoryRepository())
        #result = use_case.execute(GetCategoryRequest(id=category_pk))

        #Esse vai ser o processamento para json
        category_output = RetriveCategoryResponseSerializer(instance=result)
            
        

        #saida
        # Verifica se o response é o do rest_framework
        return Response(
            status=HTTP_200_OK, 
            data=category_output.data,
        )

        
        
           
