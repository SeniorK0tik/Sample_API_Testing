import asyncio
from asyncio import BaseEventLoop

import pytest
import pytest_asyncio

from base.async_client import AsyncClient, aget_client
from base.client import get_client, Client
from models.authentication import Authentication


@pytest.fixture(scope="session")
def session_client(request: pytest.FixtureRequest) -> Client:
    """
        The function `session_client` is a pytest fixture that returns a client object with authentication and
        closes the client connection after the test session.

        :param request: The `request` parameter is an instance of the `pytest.FixtureRequest` class. It represents
        the request for a fixture from a test or other fixture. It provides various methods and attributes to access
        information about the fixture request, such as the test item, the scope of the fixture
        :type request: pytest.FixtureRequest
        :return: an instance of the `Client` class.
        """
    auth = Authentication()
    client = get_client(auth=auth, auth_stage=False)
    request.addfinalizer(client.close)
    return client


@pytest.fixture(scope="session")
def event_loop(request) -> BaseEventLoop:
    """
       The above function is a pytest fixture that creates and yields an asyncio event loop with a session scope.
    """
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()

    request.addfinalizer(loop.close)
    yield loop


@pytest_asyncio.fixture(scope="session")
async def async_client(request: pytest.FixtureRequest, event_loop: BaseEventLoop) -> AsyncClient:
    """
        The above function is a pytest fixture that returns an asynchronous client and ensures that it is closed
        after the test session is finished.

        :param request: The `request` parameter is an instance of `pytest.FixtureRequest` and is used to access
         information about the test fixture being requested, such as the test function that is using the fixture
        :type request: pytest.FixtureRequest
        :param event_loop: The `event_loop` parameter is an instance of the `BaseEventLoop` class, which is
        responsible for executing asynchronous tasks in Python. It provides methods for scheduling and running
         coroutines, as well as managing callbacks and timers. In the context of the fixture you provided,
          the `event_loop`
        :type event_loop: BaseEventLoop
        :return: The fixture is returning an instance of the `AsyncClient` class.
        """
    auth = Authentication()
    client = await aget_client(auth=auth, auth_stage=False)
    assert type(client) == AsyncClient, 'Not ASYNC Client'

    def session_finalizer():
        async def session_afinalizer():
            # await task using loop provided by event_loop fixture
            # RuntimeError is raised if task is created on a different loop
            await client.aclose()
        event_loop.run_until_complete(session_afinalizer())

    request.addfinalizer(session_finalizer)
    return client


def pytest_generate_tests(metafunc):
    """
    The function `pytest_generate_tests` is used to parametrize the fixture `delete_data_comb` with three
    different values: 'not_permitted', 'not_found', and 'permitted'.

    :param metafunc: The `metafunc` parameter is an object that provides information about the test function
    being called. It allows you to dynamically generate test cases based on the test function's parameters and fixtures.
     In this case, the `pytest_generate_tests` function is a pytest hook that is called before test collection.
    """
    if "delete_data_comb" in metafunc.fixturenames:
        metafunc.parametrize(
            "delete_data_comb",
            ['not_permitted', "not_found", 'permitted'],
            indirect=True
        )
