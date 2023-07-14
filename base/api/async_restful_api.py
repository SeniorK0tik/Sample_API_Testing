import allure
from httpx import Response

from base.async_client import AsyncClient
from models.restful_objects import DefaultRestfulObject, UpdateDefaultRestfulObject, PatchedDefaultRestfulObject
from utils.constants.routes import APIRoutes


@allure.step('Getting the objects with id "{object_id}"')
async def aget_restful_objects_api(
    client: AsyncClient,
    object_id: str | None = None,
) -> Response:
    url = f'{APIRoutes.OBJECTS}?{object_id}' if object_id else APIRoutes.OBJECTS
    resp = await client.aget(url)
    return resp


@allure.step('Getting the object with id "{object_id}"')
async def aget_restful_object_api(
    client: AsyncClient,
    object_id: int = None,
) -> Response:
    url = f'{APIRoutes.OBJECTS}/{object_id}'
    return await client.aget(url)


@allure.step('Creating an object')
async def acreate_restful_object_api(
    client: AsyncClient,
    payload: DefaultRestfulObject,
) -> Response:
    return await client.apost(APIRoutes.OBJECTS, json=payload.model_dump(by_alias=True))


@allure.step('Fully updating the object with id "{object_id}"')
async def aupdate_restful_object_api(
    client: AsyncClient,
    object_id: int,
    payload: UpdateDefaultRestfulObject,
) -> Response:
    return await client.aput(
        f'{APIRoutes.OBJECTS}/{object_id}',
        json=payload.model_dump(by_alias=True)
    )


@allure.step('Patching the object with id "{object_id}"')
async def apatch_restful_object_api(
    client: AsyncClient,
    object_id: int,
    payload: PatchedDefaultRestfulObject,
) -> Response:
    return await client.apatch(
        f'{APIRoutes.OBJECTS}/{object_id}',
        json=payload.model_dump(by_alias=True)
    )


@allure.step('Deleting the object with id "{object_id}"')
async def adelete_restful_object_api(
    client: AsyncClient,
    object_id: int,
) -> Response:
    return await client.adelete(f'{APIRoutes.OBJECTS}/{object_id}')


async def acreate_restful_object(client: AsyncClient) -> DefaultRestfulObject:
    payload = DefaultRestfulObject()

    response = await acreate_restful_object_api(payload=payload, client=client)
    return DefaultRestfulObject(**response.json())
