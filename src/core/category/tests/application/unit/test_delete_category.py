from typing import Self
from unittest.mock import create_autospec
from urllib import request
import uuid

import pytest
from src.core.category.application.category_repository import CategoryRepository
from src.core.category.application.use_cases.delete_category import DeleteCategory, DeleteCategoryRequest
from src.core.category.application.use_cases.exceptions import CategoryNotFound
from src.core.category.domain.category import Category


class TestDeleteCategory:
    def test_delete_category_from_repository(self):
       category = Category(
            name = "Filme",
            description = "Filme de ação",
            is_active = True,
        )
       
       mock_repository = create_autospec(CategoryRepository)
        #usar o create inves do mock, 
        #Precisa busca a entidade no repositorio, para isso ele retorna a categoria
       mock_repository.get_by_id.return_value = category

       use_case = DeleteCategory(mock_repository)
       use_case.execute(DeleteCategoryRequest(id=category.id))


       mock_repository.delete.assert_called_once_with(category.id)



    def test_when_category_does_not_exist_then_raise_exception(self):
       
       mock_repository = create_autospec(CategoryRepository)
       #usar o create inves do mock, 
       #Precisa busca a entidade no repositorio, para isso ele retorna a categoria
       mock_repository.get_by_id.return_value = None

       use_case = DeleteCategory(mock_repository)
      


       with pytest.raises(CategoryNotFound):
          use_case.execute(DeleteCategoryRequest(id=uuid.uuid4()))
            
       mock_repository.delete.assert_not_called()  
       assert mock_repository.delete.called is False