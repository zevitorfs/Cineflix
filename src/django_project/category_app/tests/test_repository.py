import pytest
from core.category.domain.category import Category
from django_project.category_app.repository import DjangoORMCategoryRepository
from django_project.category_app.models import Category as CategoryModel

@pytest.mark.django_db
class TestSave:
    def test_save_category_in_database(self):
        category = Category(
            name='test',
            description='test description',
        )

        repository = DjangoORMCategoryRepository()
        
        #Garanti que o banco de dados esta vazio
        #Estou testando meu repositorio e ele faz mutação no banco de dados

        assert CategoryModel.objects.count() == 0
        repository.save(category)
        assert CategoryModel.objects.count() == 1


        category_db = CategoryModel.objects.get() 
        assert category_db.id == category.id
        assert category_db.name == category.name
        assert category_db.description == category.description
        assert category_db.is_active == category.is_active
