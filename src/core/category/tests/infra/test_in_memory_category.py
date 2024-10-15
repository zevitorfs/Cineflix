from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category import InMemoryCategoryRepository


class TestInMemoryCategoryRepository:

    def test_can_save_category(self):
        repository = InMemoryCategoryRepository()
        category = Category(name="Filme", description= "Categoria de filme",)

        repository.save(category)
        
        # esse assert serve para verificar se a categoria foi salva
        assert len(repository.categories) == 1
        # esse assert serve para verificar se a categoria salva é a mesma que foi passada
        assert repository.categories[0] == category
