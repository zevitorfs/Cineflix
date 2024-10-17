from uuid import UUID
from src.core.category.application.use_cases.create_category import CreateCategory, CreateCategoryRequest, CreateCategoryResponse
from src.core.category.infra.in_memory_category import InMemoryCategoryRepository


class TestCreateCategory:
     def test_create_category_with_valid_data(self):
        repository = InMemoryCategoryRepository () #Porem aqui botariamos nosso banco  de dados, a referencia, como SQL Alchemy
        use_case = CreateCategory(repository=repository)
        request = CreateCategoryRequest(
            name="Filme", 
            description="Filme de ação",
            is_active=True, #default
        )

        response = use_case.execute(request)
       
        
        assert response.id is not None
        assert isinstance(response, CreateCategoryResponse)
        assert isinstance(response.id, UUID) 
        assert len(repository.categories) == 1

       
        persisted_category = repository.categories[0]
        assert persisted_category.id == response.id
        assert persisted_category.name =="Filme"
        assert persisted_category.description == "Filme de ação"
        assert persisted_category.is_active == True

        
