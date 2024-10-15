from uuid import UUID
from src.core.category.application.create_category import CreateCategory, CreateCategoryRequest, CreateCategoryResponse
from src.core.category.infra.in_memory_category import InMemoryCategoryRepository

#Esse teste para use case é interesante pq nosso usuario injetou um conjunto de valores e olha que a saida é igual a esse conjunto.
#ou seja esse teste garante que o repositorio esta sendo chamado, como chama o repositorio e verifica o estado do repositorio
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
        #Uma das maneiras de estrutura o usecase, pois todos vao ter o mesmo padrão
        
        assert response.id is not None
        assert isinstance(response, CreateCategoryResponse)
        assert isinstance(response.id, UUID) 
        assert len(repository.categories) == 1

        #Com isso verificamos algo maior que o input, verificamos se o dado foi salvo no banco
        persisted_category = repository.categories[0]
        assert persisted_category.id == response.id
        assert persisted_category.name =="Filme"
        assert persisted_category.description == "Filme de ação"
        assert persisted_category.is_active == True

        
