from models.restful_objects import NewRestfulObjectDict, DefaultRestfulObject, NewRestfulObject, \
    UpdatedDefaultRestfulObject, UpdatedRestfulObjectDict, UpdateDefaultRestfulObject
from utils.assertions.base.expect import expect
from utils.validators.date_validators import validate_created_at


def assert_restful_object(
    expected_rest_obj: DefaultRestfulObject | NewRestfulObject | UpdateDefaultRestfulObject,
    actual_restful_obj: NewRestfulObjectDict | UpdatedRestfulObjectDict
):

    expect(expected_rest_obj.name) \
        .set_description('Restful object "name"') \
        .to_be_equal(actual_restful_obj['name'])

    expect(expected_rest_obj.data) \
        .set_description('Restful object "data"') \
        .to_be_equal(actual_restful_obj['data'])

    if isinstance(expected_rest_obj, DefaultRestfulObject):
        expect('%Y-%m-%dT%H:%M:%S.%f%z') \
            .set_description('Restful object "createdAt"') \
            .is_valid(
            actual_restful_obj['createdAt'],
            method=validate_created_at,
            method_args=[actual_restful_obj['createdAt'], '%Y-%m-%dT%H:%M:%S.%f%z']
        )
    if isinstance(expected_rest_obj, UpdateDefaultRestfulObject):
        expect('%Y-%m-%dT%H:%M:%S.%f%z') \
            .set_description('Restful object "updatedAt"') \
            .is_valid(
            actual_restful_obj['updatedAt'],
            method=validate_created_at,
            method_args=[actual_restful_obj['updatedAt'], '%Y-%m-%dT%H:%M:%S.%f%z']
        )
