from src.core.category.application.use_cases.delete_category import DeleteCategory, DeleteCategoryRequest
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category import InMemoryCategoryRepository


class TestDeleteCategory:
    def test_delete_category_from_repository(self):
        # Teste paar caso a categoria exista         
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

        
        use_case = DeleteCategory(repository=repository)
        request = DeleteCategoryRequest(
            id = category_filme.id
            
        )

        # Importante nota que fizemos a ssert antes dos response para deixa claro que a categoria existe
        assert repository.get_by_id(category_filme.id) is not None
        response = use_case.execute(request)

        #Apois verifica que tinha a catgoria e deleta agora verifica que ele não existe
        assert repository.get_by_id(category_filme.id) is None
        assert response is None
        