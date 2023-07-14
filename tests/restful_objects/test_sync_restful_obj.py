from http import HTTPStatus
from typing import Any, Callable

import allure
import pytest

from base.api.restful_api import get_restful_objects_api, get_restful_object_api, create_restful_object_api, \
    update_restful_object_api, patch_restful_object_api, delete_restful_object_api
from base.client import Client
from models.restful_objects import RestfulObjectDict, DefaultRestfulObjects, DefaultRestfulObject, \
    UpdateDefaultRestfulObject, NewRestfulObjectDict, NewRestfulObject, UpdatedRestfulObjectDict, \
    UpdatedDefaultRestfulObject
from tests.restful_objects.conftest import DataToDelete
from utils.assertions.api.rest_object import assert_restful_object
from utils.assertions.base.solutions import assert_status_code
from utils.assertions.schema import validate_schema


@pytest.mark.sync_api
@allure.feature('RestFul Objects')
@allure.story('RestFul Objects API')
class TestSyncRestFulObjs:
    @allure.title('Get restful objects')
    def test_get_restful_objs(self, session_client: Client):
        response = get_restful_objects_api(client=session_client)
        json_response: list[RestfulObjectDict] = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)

        validate_schema(json_response, DefaultRestfulObjects.model_json_schema(by_alias=True))

    @allure.title('Get restful object')
    @pytest.mark.parametrize(
        "object_id, status_code", [
            (1, HTTPStatus.OK),
            (-100, HTTPStatus.NOT_FOUND),
            (0, HTTPStatus.NOT_FOUND),
            (1123456, HTTPStatus.NOT_FOUND),
            ('asfagasg', HTTPStatus.NOT_FOUND)
        ]
    )
    def test_get_restful_obj(self, session_client: Client, object_id: Any, status_code: HTTPStatus):
        response = get_restful_object_api(client=session_client, object_id=object_id)
        json_response: RestfulObjectDict = response.json()

        assert_status_code(response.status_code, status_code)
        if status_code == HTTPStatus.OK:
            validate_schema(json_response, DefaultRestfulObject.model_json_schema(by_alias=True))

    @allure.title('Create restful object')
    @pytest.mark.parametrize(
        'payload, status_code', [
            (DefaultRestfulObject(), HTTPStatus.OK),
        ]
    )
    def test_create_restful_object(
            self,
            session_client: Client,
            payload: DefaultRestfulObject | UpdateDefaultRestfulObject,
            status_code: HTTPStatus
    ):
        response = create_restful_object_api(session_client, payload)
        json_response: NewRestfulObjectDict = response.json()

        assert_status_code(response.status_code, status_code)
        assert_restful_object(
            expected_rest_obj=payload,
            actual_restful_obj=json_response
        )
        validate_schema(json_response, NewRestfulObject.model_json_schema(by_alias=True))

    @allure.title('Update restful object')
    @pytest.mark.parametrize(
        'update_func, description, status', [
            (update_restful_object_api, 'UPDATE OBJECT', HTTPStatus.OK),
            (patch_restful_object_api, 'PATCH OBJECT', HTTPStatus.OK)
        ]
    )
    def test_update_restful_object(
            self,
            session_client: Client,
            new_obj: NewRestfulObjectDict,
            update_func: Callable,
            description: str,
            status: HTTPStatus
    ):
        obj_id = new_obj['id']
        updated_obj = UpdateDefaultRestfulObject()

        allure.dynamic.title(description)

        response = update_func(session_client, obj_id, updated_obj)
        json_response: UpdatedRestfulObjectDict = response.json()

        assert_status_code(response.status_code, status)
        validate_schema(json_response, UpdatedDefaultRestfulObject.model_json_schema(by_alias=True))
        assert_restful_object(
            expected_rest_obj=updated_obj,
            actual_restful_obj=json_response
        )

    @allure.title('Delete restful object')
    def test_delete_restful_object(
            self,
            session_client: Client,
            delete_data_comb: DataToDelete
    ):
        response = delete_restful_object_api(session_client, delete_data_comb.id)
        assert_status_code(response.status_code, delete_data_comb.status_code)
