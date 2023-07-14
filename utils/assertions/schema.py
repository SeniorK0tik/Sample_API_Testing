from typing import List, Dict

import allure
from jsonschema import validate

from utils.logger_loguru.logger import logger


@allure.step('Validating schema')
def validate_schema(instance: List[Dict] | Dict, schema: List[Dict] | Dict) -> None:
    logger.info(f"Validating that {instance} is corresponds to schema {schema}")
    validate(instance=instance, schema=schema)
