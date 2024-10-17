from unittest.mock import MagicMock, create_autospec
from uuid import UUID
import uuid
import pytest
from src.core.category.application.category_repository import CategoryRepository
from src.core.category.application.use_cases.create_category import CreateCategory, CreateCategoryRequest
from src.core.category.application.use_cases.exceptions import CategoryNotFound, InvalidCategoryData
from src.core.category.application.use_cases.get_category import GetCategory, GetCategoryRequest, GetCategoryResponse
from src.core.category.domain.category import Category



class TestGetCategory:
     
    def test_when_category_exists_then_return_response_dto(self) :
        mock_category = Category(
            id=uuid.uuid4(),
            name="Filme",
            description="Categoria para filmes",
            is_active=True,
        )

        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id. return_value = mock_category

        use_case = GetCategory(repository=mock_repository)
        request = GetCategoryRequest(id=mock_category.id)

        response = use_case. execute(request)

        assert response == GetCategoryResponse(
            id=mock_category.id,
            name="Filme",
            description="Categoria para filmes",
            is_active=True,
        )


    def test_when_category_not_found_then_raise_exceptions(self):
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = None

        use_case = GetCategory(repository=mock_repository)
        request = GetCategoryRequest(
            id=uuid.uuid4()
        )

        with pytest.raises(CategoryNotFound):
            use_case.execute(request)


            

      