from unittest.mock import create_autospec
import uuid

from src.core.category.application.category_repository import CategoryRepository
from src.core.category.application.use_cases.update_category import UpdateCategory, UpdateCategoryRequest
from src.core.category.domain.category import Category


class TestUpdateCategory:
    def test_update_category_name(self):
        mock_category = Category(
            id=uuid.uuid4(),
            name="Filme",
            description="Categoria para filmes",
            is_active=True,
        )

        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = mock_category

        use_case = UpdateCategory(repository=mock_repository)
        
        request = UpdateCategoryRequest(
            id=mock_category.id,
            name="Serie",
        )

        use_case.execute(request)

        assert mock_category.name == "Serie"
       
        assert mock_category.description == "Categoria para filmes"

        
        mock_repository.update.assert_called_once_with(mock_category)
        

    def test_update_category_description(self):
         
        mock_category = Category(
            id=uuid.uuid4(),
            name="Filme",
            description="Categoria para filmes",
            is_active=True,
        )

        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = mock_category

        use_case = UpdateCategory(repository=mock_repository)
        
        request = UpdateCategoryRequest(
            id=mock_category.id,
            description="Categoria para series",
        )

        use_case.execute(request)

        
        assert mock_category.name == "Filme"
       
        assert mock_category.description == "Categoria para series"

        mock_repository.update.assert_called_once_with(mock_category)

    def test_can_deactivate_category(self):
        pass

    def test_can_activate_category(self):
        pass