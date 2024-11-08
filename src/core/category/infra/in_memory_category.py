from uuid import UUID
from src.core.category.domain.category_repository import CategoryRepository
from src.core.category.domain.category import Category


class InMemoryCategoryRepository(CategoryRepository):
    def __init__(self, categories=None):
        self.categories = categories or []

    def save(self, category: Category) -> None:
        self.categories.append(category)

    def get_by_id(self, id: UUID) -> Category | None:
        for category in self.categories:
            if category.id == id:
                return category
        return None
    def delete(self, id: UUID) -> None:

        category= self.get_by_id(id)
        self.categories.remove(category)
    
    def update(self, category: Category) -> None:
        old_category = self.get_by_id(category.id)
        if old_category:
            self.delete(category.id)
            self.save(category)
    
    def list(self) -> list[Category]:
        # Retorna isso usar alist conprehension para cria uma copiad da lista com isso pessoa de for anão pode altera lista
        return [category for category in self.categories]
        

   