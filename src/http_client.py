from __future__ import annotations

import json
import typing

import httpx

USER_AGENT = (
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
)


class HTTPRequestError(Exception):
    pass


class BaseHttpClient(typing.Protocol):
    headers: typing.Dict[str, str] = {}

    def make_request(
        self, method: str, url: str, headers: dict = None, payload: dict = None
    ) -> typing.Optional[dict]:
        if headers:
            self.headers.update(headers)

        try:
            response = httpx.request(method.lower(), url, headers=self.headers, data=payload)
            return response.json()
        except (httpx.RequestError, json.JSONDecodeError, AttributeError):
            raise HTTPRequestError
