import uuid
import pytest
from rest_framework.test import APIClient
from django_project.category_app.repository import DjangoORMCategoryRepository
from src.core.category.domain.category import Category
from rest_framework import status


# Aas fixture para utiliza as entidades em mais teste sem precisa cria toda vez em teste novos
@pytest.fixture
def category_movie():
    return Category(
        name="Movie",
        description="Movie description",
    )


@pytest.fixture
def category_documentary():
    return Category(
        name="Documentary",
        description="Documentary description",
    )


@pytest.fixture
def category_repository() -> DjangoORMCategoryRepository:
    return DjangoORMCategoryRepository()


@pytest.mark.django_db
class TestCategoryAPI:
    def test_list_categories(
        self,
        category_movie: Category,
        category_documentary: Category,
        category_repository: DjangoORMCategoryRepository,
    ) -> None:
        category_repository.save(category_movie)
        category_repository.save(category_documentary)

        url = "/api/categories/"
        response = APIClient().get(url)
        # Criação de duas entidades

        expected_data = {
            "data": [
                {
                    "id": str(category_movie.id),
                    "name": "Movie",
                    "description": "Movie description",
                    "is_active": True
                },
                {
                    "id": str(category_documentary.id),
                    "name": "Documentary",
                    "description": "Documentary description",
                    "is_active": True
                },
            ]
        }

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["data"]) == 2
        assert response.data == expected_data
        # self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data, expected_data)


@pytest.mark.django_db
class TestRetriverAPI:
    def test_when_id_is_invalid_return_400(self) -> None:
        url = "/api/categories/123123123/"
        response = APIClient().get(url)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_return_category_when_exists(
        self,
        category_movie: Category,
        category_documentary: Category,
        category_repository: DjangoORMCategoryRepository,
    ) -> None:
        category_repository.save(category_movie)
        category_repository.save(category_documentary)

        url = f"/api/categories/{category_documentary.id}/"
        response = APIClient().get(url)
        # Criação de duas entidades

        # A diferença é que agora a api so vai devolver um id não uma lista
        expected_data = {
            "data": {
                "id": str(category_documentary.id),
                "name": "Documentary",
                "description": "Documentary description",
                "is_active": True,
            }
        }

        assert response.status_code == status.HTTP_200_OK
        assert response.data == expected_data

    def test_return_404_when_category_not_exists(self):
        # sÓ PARA TESTA
        url = f"/api/categories/{uuid.uuid4()}/"
        response = APIClient().get(url)

        assert response.status_code == status.HTTP_404_NOT_FOUND
