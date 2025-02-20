# flake8: noqa
"""
Copyright 2021 - Present Okta, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# AUTO-GENERATED! DO NOT EDIT FILE DIRECTLY
# SEE CONTRIBUTOR DOCUMENTATION

from okta.okta_object import OktaObject
from okta.models import allowed_for_enum\
    as allowed_for_enum


class AuthenticatorSettings(
    OktaObject
):
    """
    A class for AuthenticatorSettings objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            if "allowedFor" in config:
                if isinstance(config["allowedFor"],
                              allowed_for_enum.AllowedForEnum):
                    self.allowed_for = config["allowedFor"]
                elif config["allowedFor"] is not None:
                    self.allowed_for = allowed_for_enum.AllowedForEnum(
                        config["allowedFor"].upper()
                    )
                else:
                    self.allowed_for = None
            else:
                self.allowed_for = None
            self.token_lifetime_in_minutes = config["tokenLifetimeInMinutes"]\
                if "tokenLifetimeInMinutes" in config else None
        else:
            self.allowed_for = None
            self.token_lifetime_in_minutes = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "allowedFor": self.allowed_for,
            "tokenLifetimeInMinutes": self.token_lifetime_in_minutes
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format
