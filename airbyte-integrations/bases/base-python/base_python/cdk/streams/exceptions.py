#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#


from typing import Union

import requests


class BaseBackoffException(requests.exceptions.HTTPError):
    pass


class UserDefinedBackoffException(BaseBackoffException):
    """
    An exception that exposes how long it attempted to backoff
    """

    def __init__(self, backoff: Union[int, float], request: requests.PreparedRequest, response: requests.Response):
        """
        :param backoff: how long to backoff in seconds
        :param request: the request that triggered this backoff exception
        :param response: the response that triggered the backoff exception
        """
        self.backoff = backoff
        super().__init__(request=request, response=response)


class DefaultBackoffException(BaseBackoffException):
    pass
