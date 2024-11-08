from dataclasses import dataclass
from typing import List
from uuid import UUID

from src.core.category.domain.category_repository import CategoryRepository
from src.core.category.application.use_cases.exceptions import CategoryNotFound, InvalidCategoryData
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category import InMemoryCategoryRepository


@dataclass
class ListCategoryRequest:
   pass


@dataclass
class CategoryOutput:
    id: UUID
    name : str
    description : str
    is_active : bool


@dataclass
class ListCategoryRequest:
   pass


@dataclass
class ListCategoryResponse:
   data: List[CategoryOutput]


class ListCategory:
   def __init__(self, repository: CategoryRepository): #o repository não pode depender de um level menor tem que depender, importa de uma interface
      self.repository = repository
   
   def execute(self, request: ListCategoryRequest) -> ListCategoryResponse: 
      
      categories = self.repository.list()

      
      return ListCategoryResponse(
         #Esse é uma maneira de cria uma lista em python dentro de varias outras listas é a list comprehension
         data =[
            CategoryOutput(
                id=category.id,
                name=category.name,
                description=category.description,
                is_active=category.is_active,
            ) for category in categories
         ]
      )
 
      

   