from unittest.mock import MagicMock
from uuid import UUID
import pytest
from src.core.category.application.category_repository import CategoryRepository
from src.core.category.application.use_cases.create_category import CreateCategory, CreateCategoryRequest
from src.core.category.application.use_cases.exceptions import InvalidCategoryData



class TestCreateCategory:
     #Essa classe serve para casos mais gerais,ou seja, de borda
    def test_create_category_with_valid_data(self):
        mock_repository = MagicMock(CategoryRepository) #Quando utilizamos o mock estamos realizando o teste de unidades
        #Crie esse mock para deixa mais facil de escrever os testes
        use_case = CreateCategory(repository=mock_repository)
        request = CreateCategoryRequest(
            name="Filme", 
            description="Filme de ação",
            is_active=True, #default
        )

        response = use_case.execute(request)
        #Uma das maneiras de estrutura o usecase, pois todos vao ter o mesmo padrão
        
        assert response.id is not None
        assert isinstance(response.id, UUID) 
        assert mock_repository.save.called is True 

    def test_create_category_with_invalid_data(self):
        use_case = CreateCategory(repository=MagicMock(CategoryRepository))
        with pytest.raises(InvalidCategoryData, match="name cannot be empty") as exc_info:  
                use_case.execute(CreateCategoryRequest(name=""))  

        assert exc_info.type is InvalidCategoryData
        assert str(exc_info.value) == "name cannot be empty"
            

      