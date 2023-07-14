import typing
from functools import lru_cache

import allure
from httpx import AsyncClient as AsyncHttpxClient
from httpx import Response
from httpx._client import UseClientDefault
from httpx._types import (AuthTypes, CookieTypes, HeaderTypes, QueryParamTypes,
                          RequestContent, RequestData, RequestExtensions,
                          RequestFiles, TimeoutTypes, URLTypes)

from base.api.authentication_api import get_auth_token
from models.authentication import Authentication
from settings import base_settings
from utils.logger_loguru.logger import logger


class AsyncClient(AsyncHttpxClient):
    @allure.step('Making GET request to "{url}"')
    async def aget(
        self,
        url: URLTypes,
        *,
        params: typing.Optional[QueryParamTypes] = None,
        headers: typing.Optional[HeaderTypes] = None,
        cookies: typing.Optional[CookieTypes] = None,
        auth: typing.Union[AuthTypes, UseClientDefault] = None,
        follow_redirects: typing.Union[bool, UseClientDefault] = None,
        timeout: typing.Union[TimeoutTypes, UseClientDefault] = None,
        extensions: typing.Optional[RequestExtensions] = None
    ) -> Response:
        logger.debug(
            f"Client.get() --- URL: {self._merge_url(url)}, Parameters: {self._merge_queryparams(params)},"
            f" Headers: {self._merge_headers(headers)}, Cookies: {self._merge_cookies(cookies)},"
            f" Authentication: {auth}, Folowing Redirects: {follow_redirects}, timeout: {timeout},"
            f" extensions: {extensions}"
        )
        return await super().get(
            url=url,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=auth,
            follow_redirects=follow_redirects,
            timeout=timeout,
            extensions=extensions
        )

    @allure.step('Making POST request to "{url}"')
    async def apost(
        self,
        url: URLTypes,
        *,
        content: typing.Optional[RequestContent] = None,
        data: typing.Optional[RequestData] = None,
        files: typing.Optional[RequestFiles] = None,
        json: typing.Optional[typing.Any] = None,
        params: typing.Optional[QueryParamTypes] = None,
        headers: typing.Optional[HeaderTypes] = None,
        cookies: typing.Optional[CookieTypes] = None,
        auth: typing.Union[AuthTypes, UseClientDefault] = None,
        follow_redirects: typing.Union[bool, UseClientDefault] = None,
        timeout: typing.Union[TimeoutTypes, UseClientDefault] = None,
        extensions: typing.Optional[RequestExtensions] = None
    ) -> Response:
        logger.debug(
            f"Client.post() --- URL: {self._merge_url(url)}, Content: {content}, Data: {data}, Files: {files},"
            f" Json: {json}, Parameters: {self._merge_queryparams(params)}, Headers: {self._merge_headers(headers)},"
            f" Cookies: {self._merge_cookies(cookies)}, Authentication: {auth}, Folowing Redirects: {follow_redirects},"
            f" timeout: {timeout}, extensions: {extensions}"
        )
        return await super().post(
            url=url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=auth,
            follow_redirects=follow_redirects,
            timeout=timeout,
            extensions=extensions
        )

    @allure.step('Making PUT request to "{url}"')
    async def aput(
            self,
            url: URLTypes,
            *,
            content: typing.Optional[RequestContent] = None,
            data: typing.Optional[RequestData] = None,
            files: typing.Optional[RequestFiles] = None,
            json: typing.Optional[typing.Any] = None,
            params: typing.Optional[QueryParamTypes] = None,
            headers: typing.Optional[HeaderTypes] = None,
            cookies: typing.Optional[CookieTypes] = None,
            auth: typing.Union[AuthTypes, UseClientDefault] = None,
            follow_redirects: typing.Union[bool, UseClientDefault] = None,
            timeout: typing.Union[TimeoutTypes, UseClientDefault] = None,
            extensions: typing.Optional[RequestExtensions] = None
    ) -> Response:
        logger.debug(
            f"Client.put() --- URL: {self._merge_url(url)}, Content: {content}, Data: {data}, Files: {files},"
            f" Json: {json}, Parameters: {self._merge_queryparams(params)}, Headers: {self._merge_headers(headers)},"
            f" Cookies: {self._merge_cookies(cookies)}, Authentication: {auth}, Folowing Redirects: {follow_redirects},"
            f" timeout: {timeout}, extensions: {extensions}"
        )
        return await super().put(
            url=url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=auth,
            follow_redirects=follow_redirects,
            timeout=timeout,
            extensions=extensions
        )

    @allure.step('Making PATCH request to "{url}"')
    async def apatch(
        self,
        url: URLTypes,
        *,
        content: typing.Optional[RequestContent] = None,
        data: typing.Optional[RequestData] = None,
        files: typing.Optional[RequestFiles] = None,
        json: typing.Optional[typing.Any] = None,
        params: typing.Optional[QueryParamTypes] = None,
        headers: typing.Optional[HeaderTypes] = None,
        cookies: typing.Optional[CookieTypes] = None,
        auth: typing.Union[AuthTypes, UseClientDefault] = None,
        follow_redirects: typing.Union[bool, UseClientDefault] = None,
        timeout: typing.Union[TimeoutTypes, UseClientDefault] = None,
        extensions: typing.Optional[RequestExtensions] = None
    ) -> Response:
        logger.debug(
            f"Client.patch() --- URL: {self._merge_url(url)}, Content: {content}, Data: {data}, Files: {files},"
            f" Json: {json} Parameters: {self._merge_queryparams(params)}, Headers: {self._merge_headers(headers)},"
            f" Cookies: {self._merge_cookies(cookies)}, Authentication: {auth}, Folowing Redirects: {follow_redirects},"
            f" timeout: {timeout}, extensions: {extensions}"
        )

        return await super().patch(
            url=url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=auth,
            follow_redirects=follow_redirects,
            timeout=timeout,
            extensions=extensions
        )

    @allure.step('Making DELETE request to "{url}"')
    async def adelete(
        self,
        url: URLTypes,
        *,
        params: typing.Optional[QueryParamTypes] = None,
        headers: typing.Optional[HeaderTypes] = None,
        cookies: typing.Optional[CookieTypes] = None,
        auth: typing.Union[AuthTypes, UseClientDefault] = None,
        follow_redirects: typing.Union[bool, UseClientDefault] = None,
        timeout: typing.Union[TimeoutTypes, UseClientDefault] = None,
        extensions: typing.Optional[RequestExtensions] = None
    ) -> Response:
        logger.debug(
            f"Client.delete() --- URL: {self._merge_url(url)}, Parameters: {self._merge_queryparams(params)},"
            f" Headers: {self._merge_headers(headers)}, Cookies: {self._merge_cookies(cookies)},"
            f" Authentication: {auth}, Folowing Redirects: {follow_redirects}, timeout: {timeout},"
            f" extensions: {extensions}"
        )
        return await super().delete(
            url=url,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=auth,
            follow_redirects=follow_redirects,
            timeout=timeout,
            extensions=extensions
        )


@lru_cache(maxsize=None)
async def aget_client(
    auth_stage: bool = True,
    auth: Authentication | None = None,
    base_url: str = base_settings.api_url,
    headers: dict[str, str] | None = None
) -> AsyncClient:
    headers: dict[str, str] = {} if not headers else headers

    if auth_stage:
        if auth is None:
            return AsyncClient(base_url=base_url, trust_env=True)

        if (not auth.auth_token) and (not auth.user):
            raise NotImplementedError(
                'Please provide "username" and "password" or "auth_token"'
            )

        if (not auth.auth_token) and auth.user:
            token = get_auth_token(auth.user)
            headers = {**headers, 'Authorization': f'Token {token}'}

        if auth.auth_token and (not auth.user):
            headers = {**headers, 'Authorization': f'Token {auth.auth_token}'}

    return AsyncClient(base_url=base_url, headers=headers, trust_env=True)
