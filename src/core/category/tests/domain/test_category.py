import unittest 
from uuid import UUID
import uuid
from src.core.category.domain.category import Category
import pytest

class TestCategory(unittest.TestCase):
    def test_name_is_required(self):
        #Esse assert precisa esta no bloco with
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'"):
        # with self.assertRaisesRegex(TypeError, "missing 1 required positional argument: 'name'"):
            Category()
            #O category vazio lança um typeError, pois o nome é obrigatório

    def test_name_must_have_less_than_255_characters(self):
        with pytest.raises(ValueError, match="name must have less than 256 characters"):
        # with self.assertRaisesRegex(ValueError, "name must have less than 256 characters"):
            Category(name="a" * 256)
            #O category vazio lança um ValueError, pois o nome tem que ter menos de 255 caracteres

    def test_category_must_be_created_with_id_as_uuid(self):
        category = Category(name="Filme")
        assert isinstance(category.id, UUID)
        #Bem mais simples usar o asset, que é uma função do pytest
        # self.assertEqual(type(category.id), UUID)
        #O category é criado com um id que é uma string
    
    def test_created_category_with_default_values(self):
        category = Category(name="Filme")
        assert category.name == "Filme"
        assert category.description == ""
        assert category.is_active is True
        # self.assertEqual(category.name, "Filme")
        # self.assertEqual(category.description, "")
        # self.assertTrue(category.is_active)
        #O category é criado com valores padrões
# Esse if esta disendo que esta executando o modulo, serve para executa o teste

    def test_category_is_created_as_active_by_default(self):
        category = Category(name="Filme")
        assert category.is_active is True
        # self.assertTrue(category.is_active)
        #O category é criado como ativo por padrão

    def test_category_is_created_with_provide_values(self):
        cat_id = uuid.uuid4()
        category = Category(
                            id=cat_id,
                            name="Filme", 
                            description="Filme de ação", 
                            is_active=False,
        )
        assert category.id == cat_id
        assert category.name == "Filme"
        assert category.description == "Filme de ação"
        assert category.is_active is False
        # self.assertEqual(category.id, cat_id)
        # self.assertEqual(category.name, "Filme")
        # self.assertEqual(category.description, "Filme de ação")
        # self.assertFalse(category.is_active)
        #O category é criado com valores fornecidos

# if __name__ == "__main__":
#     unittest.main() essa função é do unittest, ela executa o modulo
    def test_cannot_create_category_with_empty_name(self):
        with pytest.raises(ValueError, match="name cannot be empty"):
            Category(name="")
            #O category vazio lança um ValueError, pois o nome tem que ter menos de 255 caracteres



class TestUpdateCategory:
    def test_update_category_with_name_and_description(self):
        #Podemos separa o teste em tres partes

        #Arrange
        category = Category(name="Filme", description="Filme de ação")  

        #Execução
        category.update_category(name="Série", description="Série em geral")

        #Assert
        assert category.name == "Série"
        assert category.description == "Série em geral"
        
    def test_update_category_invalid_name(self):
        #Arrange
        category = Category(name="Filme", description="Filme de ação")  

        with pytest.raises(ValueError, match="name must have less than 256 characters"):
            category.update_category(name="a" * 256, description="Série em geral")

    
    def test_cannot_create_category_with_empty_name(self):
        with pytest.raises(ValueError, match="name cannot be empty"):
            Category(name="")
    
class TestActive:
    def test_activate_inactive_category(self):
        #Arrange
        category = Category(name="Filme", description="Filme de ação", is_active=False)  

        #Execução
        category.activate()

        #Assert
        assert category.is_active is True

    def test_activate_active_category(self):
        #Arrange
        category = Category(name="Filme", description="Filme de ação", is_active=True)  

        #Execução
        category.activate()

        #Assert
        assert category.is_active is True

    
class TestEquality:
    def test_when_categories_have_same_id_they_are_equal(self):
        cat_id = uuid.uuid4()
        category_1 = Category(id=cat_id, name="Filme", description="Filme de ação", is_active=False)
        category_2 = Category(id=cat_id, name="Filme", description="Filme de ação", is_active=False)

        assert category_1 == category_2

    def test_equality_diferent_classes(self):
        cat_id = uuid.uuid4()
        category = Category(id=cat_id, name="Filme", description="Filme de ação", is_active=False)

        assert category != "Category"
        