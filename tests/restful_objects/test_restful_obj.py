from http import HTTPStatus
from typing import Any, Coroutine, Callable

import allure
import pytest

from base.api.async_restful_api import aget_restful_objects_api, aget_restful_object_api, acreate_restful_object_api, \
    aupdate_restful_object_api, apatch_restful_object_api, adelete_restful_object_api
from base.async_client import AsyncClient
from models.restful_objects import RestfulObjectDict, DefaultRestfulObjects, DefaultRestfulObject, \
    UpdateDefaultRestfulObject, NewRestfulObjectDict, NewRestfulObject, UpdatedRestfulObjectDict, \
    UpdatedDefaultRestfulObject
from tests.restful_objects.conftest import DataToDelete
from utils.assertions.api.rest_object import assert_restful_object
from utils.assertions.base.solutions import assert_status_code
from utils.assertions.schema import validate_schema
from utils.async_wrapper import to_thread


@pytest.mark.async_api
@allure.feature('RestFul Objects')
@allure.story('RestFul Objects API')
class TestRestFulObjs:
    @allure.title('Get restful objects')
    @pytest.mark.asyncio
    async def test_aget_restful_objs(self, async_client: AsyncClient):
        assert type(async_client) == AsyncClient, 'NOT AsyncClient FUNC '
        response = await aget_restful_objects_api(client=async_client)
        json_response: list[RestfulObjectDict] = response.json()

        await to_thread(assert_status_code, response.status_code, HTTPStatus.OK)
        await to_thread(validate_schema, json_response, DefaultRestfulObjects.model_json_schema(by_alias=True))

    @allure.title('Get restful object')
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "object_id, status_code", [
            (1, HTTPStatus.OK),
            (-100, HTTPStatus.NOT_FOUND),
            (0, HTTPStatus.NOT_FOUND),
            (1123456, HTTPStatus.NOT_FOUND),
            ('asfagasg', HTTPStatus.NOT_FOUND)
        ]
    )
    async def test_aget_restful_obj(self, async_client: AsyncClient, object_id: Any, status_code: HTTPStatus):
        response = await aget_restful_object_api(client=async_client, object_id=object_id)
        json_response: RestfulObjectDict = response.json()

        await to_thread(assert_status_code, response.status_code, status_code)

        if status_code == HTTPStatus.OK:
            await to_thread(validate_schema, json_response, DefaultRestfulObject.model_json_schema(by_alias=True))

    @allure.title('Create restful object')
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        'payload, status_code', [
            (DefaultRestfulObject(), HTTPStatus.OK),
        ]
    )
    async def test_create_restful_object(
            self,
            async_client: AsyncClient,
            payload: DefaultRestfulObject | UpdateDefaultRestfulObject,
            status_code: HTTPStatus
    ):
        response = await acreate_restful_object_api(async_client, payload)
        json_response: NewRestfulObjectDict = response.json()

        await to_thread(assert_status_code, response.status_code, status_code)
        await to_thread(assert_restful_object, payload, json_response)
        await to_thread(validate_schema, json_response, NewRestfulObject.model_json_schema(by_alias=True))

    @allure.title('Update restful object')
    @pytest.mark.parametrize(
        'update_func, description, status', [
            (aupdate_restful_object_api, 'UPDATE OBJECT', HTTPStatus.OK),
            (apatch_restful_object_api, 'PATCH OBJECT',  HTTPStatus.OK)
        ]
    )
    @pytest.mark.asyncio
    async def test_update_restful_object(
            self,
            async_client: AsyncClient,
            new_obj: NewRestfulObjectDict,
            update_func: Callable[..., Coroutine],
            description: str,
            status: HTTPStatus
    ):
        obj_id = new_obj['id']
        updated_obj = UpdateDefaultRestfulObject()

        allure.dynamic.title(description)

        response = await update_func(async_client, obj_id, updated_obj)
        json_response: UpdatedRestfulObjectDict = response.json()

        await to_thread(assert_status_code, response.status_code, status)
        await to_thread(validate_schema, json_response, UpdatedDefaultRestfulObject.model_json_schema(by_alias=True))
        await to_thread(assert_restful_object, updated_obj, json_response)

    @allure.title('Delete restful object')
    @pytest.mark.asyncio
    async def test_delete_restful_object(self,  async_client: AsyncClient, delete_data_comb: DataToDelete):
        response = await adelete_restful_object_api(async_client, delete_data_comb.id)
        await to_thread(assert_status_code, response.status_code, delete_data_comb.status_code)
