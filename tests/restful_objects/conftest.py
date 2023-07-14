from http import HTTPStatus
from typing import NamedTuple

import pytest
import pytest_asyncio

from base.api.async_restful_api import acreate_restful_object_api
from base.async_client import AsyncClient
from models.restful_objects import DefaultRestfulObject, NewRestfulObjectDict


class DataToDelete(NamedTuple):
    id: str | int
    status_code: HTTPStatus | int


@pytest_asyncio.fixture(scope='function')
async def new_obj(async_client: AsyncClient) -> NewRestfulObjectDict:
    """
        The above function is a pytest fixture that creates a new RESTful object using an async client
         and returns the JSON response.

        :param async_client: The `async_client` parameter is an instance of the `AsyncClient` class,
            which is used to make asynchronous HTTP requests. It is likely used to send the request to the API
            endpoint for creating a new RESTful object
        :type async_client: AsyncClient
        :return: a JSON response in the form of a dictionary, which is annotated as `NewRestfulObjectDict`.
    """
    payload = DefaultRestfulObject()
    response = await acreate_restful_object_api(async_client, payload)
    json_response: NewRestfulObjectDict = response.json()
    return json_response


@pytest_asyncio.fixture(scope='function')
async def delete_data_comb(
        new_obj: NewRestfulObjectDict,
        request: pytest.FixtureRequest
) -> DataToDelete:
    """
        The function `delete_data_comb` is a pytest fixture that returns a `DataToDelete` object based on the value
         of the `request.param` parameter.

        :param new_obj: The `new_obj` parameter is a dictionary that represents a new restful object. It contains
        information about the object, such as its ID and other attributes
        :type new_obj: NewRestfulObjectDict
        :param request: The `request` parameter is an instance of the `pytest.FixtureRequest` class. It represents
         the request for a fixture in a test function or method. It provides information about the test context and
         allows access to the test item, configuration, and other fixtures. In this case, it is used
        :type request: pytest.FixtureRequest
        :return: The function `delete_data_comb` returns an instance of the `DataToDelete` class.
         The specific instance returned depends on the value of the `request.param` parameter. If `request.param`
          is equal to `'not_permitted'`, then the function returns a `DataToDelete` instance with the values `1` and
          `HTTPStatus.METHOD_NOT_ALLOWED`. If `request.param`
        is equal
        """
    if request.param == 'not_permitted':
        return DataToDelete(1, HTTPStatus.METHOD_NOT_ALLOWED)
    elif request.param == 'not_found':
        return DataToDelete("aaaaaa", HTTPStatus.NOT_FOUND)
    elif request.param == 'permitted':
        return DataToDelete(new_obj['id'], HTTPStatus.OK)
