from __future__ import annotations

import typing

from http_client import BaseHttpClient, HTTPRequestError

USER_AGENT = (
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
)


class TinkoffAPIRequestError(Exception):
    pass


class TinkoffHttpClient(BaseHttpClient):
    def __init__(self) -> None:
        self.headers = {
            'authority': 'www.tinkoff.ru',
            'user-agent': USER_AGENT,
            'content-type': 'application/x-www-form-urlencoded',
            'accept': '*/*',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.tinkoff.ru/login/',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,ru;q=0.7',
        }

    def make_request(
        self, method: str, url: str, headers: dict = None, payload: dict = None
    ) -> typing.Optional[dict]:
        try:
            return super().make_request(method, url, headers, payload)
        except HTTPRequestError:
            raise TinkoffAPIRequestError
