from dataclasses import dataclass
from uuid import UUID
from src.core.category.domain.category_repository import CategoryRepository
from src.core.category.application.use_cases.exceptions import CategoryNotFound


@dataclass
class UpdateCategoryRequest:
    id: UUID
    name: str

class UpdateCategory:
    def __init__(self,repository: CategoryRepository):
        self.repository = repository

    
    def execute (self,request: UpdateCategoryRequest) -> None:
        category = self.repository.get_by_id(id=request.id)
        if category is None:
            raise CategoryNotFound(f"Category with id {request.id} not found")
        
        category.name = request.name

        self.repository.update(category)
        