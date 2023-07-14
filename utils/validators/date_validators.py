import datetime


def validate_created_at(actual_value: str, schema: str):
    return datetime.datetime.strptime(actual_value, schema)