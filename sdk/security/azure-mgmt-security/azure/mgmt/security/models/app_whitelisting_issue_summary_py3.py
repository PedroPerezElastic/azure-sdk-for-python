# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AppWhitelistingIssueSummary(Model):
    """Represents a summary of the alerts of the VM/server group.

    :param issue: Possible values include: 'ViolationsAudited',
     'ViolationsBlocked', 'MsiAndScriptViolationsAudited',
     'MsiAndScriptViolationsBlocked', 'ExecutableViolationsAudited',
     'RulesViolatedManually'
    :type issue: str or ~azure.mgmt.security.models.enum
    :param number_of_vms: The number of machines in the VM/server group that
     have this alert
    :type number_of_vms: float
    """

    _attribute_map = {
        'issue': {'key': 'issue', 'type': 'str'},
        'number_of_vms': {'key': 'numberOfVms', 'type': 'float'},
    }

    def __init__(self, *, issue=None, number_of_vms: float=None, **kwargs) -> None:
        super(AppWhitelistingIssueSummary, self).__init__(**kwargs)
        self.issue = issue
        self.number_of_vms = number_of_vms
