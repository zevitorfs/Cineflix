from uuid import UUID
from src.core.category.application.get_category import GetCategory, GetCategoryRequest, GetCategoryResponse
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category import InMemoryCategoryRepository

class TestGetCategory:
     def test_get_category_by_id(self):

       
        category_filme = Category(
            name = "Filme",
            description = "Filme de ação",
            is_active = True,

        )
        category_serie = Category(
            name="Serie",
            description="Serie de ação",
            is_active=True,
        )

        
        repository = InMemoryCategoryRepository (
            categories=[category_filme, category_serie]
        ) 

        
        use_case = GetCategory(repository=repository)
        request = GetCategoryRequest(
            id = category_filme.id
            
        )

        response = use_case.execute(request)
        
        
        assert response == GetCategoryResponse(
            id = category_filme.id,
            name = "Filme",
            description = "Filme de ação",
            is_active = True,
        )

        
