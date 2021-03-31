from __future__ import annotations

from base_controller import BaseController
from http_client import BaseHttpClient
from tinkoff.constants import (
    CANDIDATE_ACCESS_LEVEL_MARKER,
    CLIENT_ACCESS_LEVEL_MARKER,
    LEVEL_UP_URL,
    SESSION_URL,
    SIGN_UP_FORM_PAYLOAD,
    SIGN_UP_URL,
)
from tinkoff.controllers.exceptions import ImproperlySignedUpException
from tinkoff.http_client import TinkoffHttpClient


class TinkoffAuthController(BaseController):
    """
    Tinkoff auth controller.

    Auth flow contains 3 steps:
    * get initial session id
    * sign up with password and get signed up session id
    * boost access level to CLIENT access level

    After these steps we can make requests for api.
    """

    def __init__(self, http_client: BaseHttpClient = None) -> None:
        self.http = http_client or TinkoffHttpClient()

    def run(self) -> str:
        initial_session_id = self.get_initial_session_id()
        signed_up_session = self.sign_up(initial_session_id)
        self.make_level_up(signed_up_session)
        return signed_up_session

    def get_initial_session_id(self) -> str:
        """Get inital session id for api requests"""
        data = self.http.make_request('GET', url=SESSION_URL)

        return data['payload']

    def sign_up(self, session_id: str) -> str:
        """
        Make auth request and achieve CANDIDATE access level

        sign_up endpoint returns *new* signed up session id
        """
        data = self.http.make_request(
            'POST', url=SIGN_UP_URL.format(session_id=session_id), payload=SIGN_UP_FORM_PAYLOAD
        )

        self._check_access_level(data, CANDIDATE_ACCESS_LEVEL_MARKER)

        return data['payload']['sessionid']

    def make_level_up(self, signed_up_session_id: str) -> None:
        """Boost access level to CLIENT (can make financial api requests)"""
        data = self.http.make_request(
            'GET', url=LEVEL_UP_URL.format(signed_up_session_id=signed_up_session_id)
        )

        self._check_access_level(data, CLIENT_ACCESS_LEVEL_MARKER)

    def _check_access_level(self, data: dict, access_level_marker: str) -> None:
        if data.get('payload', {}).get('accessLevel', '') != access_level_marker:
            raise ImproperlySignedUpException
