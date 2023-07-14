import allure
from httpx import Response

from base.client import Client
from models.restful_objects import DefaultRestfulObject, UpdateDefaultRestfulObject, PatchedDefaultRestfulObject
from utils.constants.routes import APIRoutes


@allure.step('Getting the objects with id "{object_id}"')
def get_restful_objects_api(
    client: Client,
    object_id: str | None = None,
) -> Response:
    url = f'{APIRoutes.OBJECTS}?{object_id}' if object_id else APIRoutes.OBJECTS
    return client.get(url)


@allure.step('Getting the object with id "{object_id}"')
def get_restful_object_api(
    client: Client,
    object_id: int = None,
) -> Response:
    url = f'{APIRoutes.OBJECTS}/{object_id}'
    return client.get(url)


@allure.step('Creating an object')
def create_restful_object_api(
    client: Client,
    payload: DefaultRestfulObject,
) -> Response:
    return client.post(APIRoutes.OBJECTS, json=payload.model_dump(by_alias=True))


@allure.step('Fully updating the object with id "{object_id}"')
def update_restful_object_api(
    client: Client,
    object_id: int,
    payload: UpdateDefaultRestfulObject,
) -> Response:
    return client.put(
        f'{APIRoutes.OBJECTS}/{object_id}',
        json=payload.model_dump(by_alias=True)
    )


@allure.step('Patching the object with id "{object_id}"')
def patch_restful_object_api(
    client: Client,
    object_id: int,
    payload: PatchedDefaultRestfulObject,
) -> Response:
    return client.patch(
        f'{APIRoutes.OBJECTS}/{object_id}',
        json=payload.model_dump(by_alias=True)
    )


@allure.step('Deleting the object with id "{object_id}"')
def delete_restful_object_api(
    client: Client,
    object_id: int,
) -> Response:
    return client.delete(f'{APIRoutes.OBJECTS}/{object_id}')


def create_restful_object(client: Client) -> DefaultRestfulObject:
    payload = DefaultRestfulObject()

    response = create_restful_object_api(payload=payload, client=client)
    return DefaultRestfulObject(**response.json())
