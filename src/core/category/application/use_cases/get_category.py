from dataclasses import dataclass
from uuid import UUID

from src.core.category.application.category_repository import CategoryRepository
from src.core.category.application.use_cases.exceptions import CategoryNotFound, InvalidCategoryData
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category import InMemoryCategoryRepository


@dataclass
class GetCategoryRequest:
   id: UUID

@dataclass
class GetCategoryResponse:
   id: UUID
   name : str
   description : str
   is_active : bool


class GetCategory:
   def __init__(self, repository: CategoryRepository): #o repository não pode depender de um level menor tem que depender, importa de uma interface
      self.repository = repository
   
   def execute(self, request: GetCategoryRequest) -> GetCategoryResponse: 
      
      category = self.repository.get_by_id(id=request.id)

      if category is None:
         raise CategoryNotFound(f"Category with id {request.id} not found")
      
      return GetCategoryResponse(
         id=category.id,
         name=category.name,
         description=category.description,
         is_active=category.is_active,
      )
 
      

   