#No python não tem a definição de interfaces, definimos interface com classe abstrata

from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from src.core.category.domain.category import Category


class CategoryRepository(ABC): #Precisa definir a interface
    @abstractmethod
    def save(self, category):
        raise NotImplementedError
    
    @abstractmethod
    def get_by_id(self, id: UUID) -> Category | None:
        raise NotImplementedError

   