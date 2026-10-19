import pytest
import requests

from lessons.lesson_25.api.cars_controller import CarsController
import json

@pytest.fixture(scope="class", autouse=True)
def cars_ctrl(request):
    request.cls.cars_ctrl = CarsController(log_file="test_search")


def print_response(response: requests.Response):
    print(json.dumps(response.json(), indent=4, ensure_ascii=False))


class TestCars:

    def test_get_cars(self):
        response = self.cars_ctrl.get_cars()
        cars_count = len(response.json())
        assert cars_count == 25, "Cars count should be 25"


    def test_get_cars_limit(self):
        limit = 3
        response = self.cars_ctrl.get_cars(limit=limit)
        cars_count = len(response.json())
        assert cars_count == limit, f"Cars count should be {limit}"


    def test_get_cars_sort_by_brand(self):
        response = self.cars_ctrl.get_cars(sort_by="brand")
        cars = response.json()
        sorted_cars_by_brand = sorted(cars, key=lambda k: k["brand"])
        assert response.json() == sorted_cars_by_brand, "Response should be sorted by brand"


    @pytest.mark.parametrize("sort_parameter", ["brand", "year", "engine_volume", "price"])
    def test_get_cars_sort_by(self, sort_parameter):
        response = self.cars_ctrl.get_cars(sort_by=sort_parameter)
        cars = response.json()
        sorted_cars_by_param = sorted(cars, key=lambda k: k[sort_parameter])
        assert cars == sorted_cars_by_param, f"Response should be sorted by {sort_parameter}"


    @pytest.mark.parametrize("sort_parameter, limit_value",
                             [("brand", 5), ("year", 10), ("engine_volume", 15), ("price", 20)])
    def test_get_cars_sort_by_and_limit(self, sort_parameter, limit_value):
        response = self.cars_ctrl.get_cars(sort_by=sort_parameter, limit=limit_value)
        cars = response.json()
        sorted_cars_by_param = sorted(cars, key=lambda k: k[sort_parameter])
        assert cars == sorted_cars_by_param, f"Response should be sorted by {sort_parameter}"
        assert len(cars) == limit_value, f"Cars count should be {limit_value}"