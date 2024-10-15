from dataclasses import dataclass
from uuid import UUID

from src.core.category.application.category_repository import CategoryRepository
from src.core.category.application.exceptions import InvalidCategoryData
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category import InMemoryCategoryRepository


@dataclass
class CreateCategoryRequest:
   name: str
   description: str = ""
   is_active: bool = True

@dataclass
class CreateCategoryResponse:
   id: UUID


class CreateCategory:
   def __init__(self, repository: CategoryRepository): #o repository não pode depender de um level menor tem que depender, importa de uma interface
      self.repository = repository
   
   def execute(self, request: CreateCategoryRequest) -> CreateCategoryResponse: 
      
      try:
         category = Category(
            name=request.name,
            description=request.description,
            is_active=request.is_active,
        )
      except ValueError as err:
         raise InvalidCategoryData(str(err))


      self.repository.save(category)

      return CreateCategoryResponse(id=category.id)
 
      

   