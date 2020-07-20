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

from okta.okta_object import OktaObject
from okta.models.password_policy_rule_action\
    import PasswordPolicyRuleAction


class PasswordPolicyRuleActions(
    OktaObject
):
    """
    A class for PasswordPolicyRuleActions objects.
    """

    def __init__(self, config=None):
        if config:
            if "passwordChange" in config:
                if isinstance(config["passwordChange"],
                              PasswordPolicyRuleAction):
                    self.password_change = config["passwordChange"]
                else:
                    self.password_change = PasswordPolicyRuleAction(
                        config["passwordChange"]
                    )
            else:
                self.password_change = None
            if "selfServicePasswordReset" in config:
                if isinstance(config["selfServicePasswordReset"],
                              PasswordPolicyRuleAction):
                    self.self_service_password_reset = config["selfServicePasswordReset"]
                else:
                    self.self_service_password_reset = PasswordPolicyRuleAction(
                        config["selfServicePasswordReset"]
                    )
            else:
                self.self_service_password_reset = None
            if "selfServiceUnlock" in config:
                if isinstance(config["selfServiceUnlock"],
                              PasswordPolicyRuleAction):
                    self.self_service_unlock = config["selfServiceUnlock"]
                else:
                    self.self_service_unlock = PasswordPolicyRuleAction(
                        config["selfServiceUnlock"]
                    )
            else:
                self.self_service_unlock = None
        else:
            self.password_change = None
            self.self_service_password_reset = None
            self.self_service_unlock = None

    def request_format(self):
        return {
            "passwordChange": self.password_change,
            "selfServicePasswordReset": self.self_service_password_reset,
            "selfServiceUnlock": self.self_service_unlock
        }
