"""
Copyright 2020 - Present Okta, Inc.

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

from okta.models.application_settings_application\
    import ApplicationSettingsApplication


class BasicApplicationSettingsApplication(
    ApplicationSettingsApplication
):
    """
    A class for BasicApplicationSettingsApplication objects.
    """

    def __init__(self, config=None):
        if config:
            self.auth_url = config["authUrl"]\
                if "authUrl" in config else None
            self.url = config["url"]\
                if "url" in config else None
        else:
            self.auth_url = None
            self.url = None

    def request_format(self):
        return {
            "authURL": self.auth_url,
            "url": self.url
        }
