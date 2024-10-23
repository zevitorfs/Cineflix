import uuid

from src.core.category.application.use_cases.update_category import UpdateCategory, UpdateCategoryRequest
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category import InMemoryCategoryRepository


class TestUpdateCatgeory:
    def test_can_update_category_name_and_description(self):
        mock_category = Category(
            name="Filme",
            description="Categoria para filmes",
        )

        repository = InMemoryCategoryRepository()
        repository.save(mock_category)

        use_case = UpdateCategory(repository=repository)
       
        request = UpdateCategoryRequest(
            id=mock_category.id,
            name="Serie",
            description="Categoria para series",
        )

        use_case.execute(request)

       
        update_category = repository.get_by_id(mock_category.id)
        assert update_category.name == "Serie"
        assert update_category.description == "Categoria para series"

    