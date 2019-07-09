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


class PathRecommendation(Model):
    """Represents a path that is recommended to be allowed and its properties.

    :param path: The full path to whitelist
    :type path: str
    :param action: Possible values include: 'Recommended', 'Add', 'Remove'
    :type action: str or ~azure.mgmt.security.models.enum
    :param type: Possible values include: 'File', 'FileHash',
     'PublisherSignature', 'ProductSignature', 'BinarySignature',
     'VersionAndAboveSignature'
    :type type: str or ~azure.mgmt.security.models.enum
    :param publisher_info:
    :type publisher_info: ~azure.mgmt.security.models.PublisherInfo
    :param common: Whether the path is commonly run on the machine
    :type common: bool
    :param user_sids:
    :type user_sids: list[str]
    :param usernames:
    :type usernames: list[~azure.mgmt.security.models.UserRecommendation]
    :param file_type: Possible values include: 'Exe', 'Dll', 'Msi', 'Script',
     'Unknown'
    :type file_type: str or ~azure.mgmt.security.models.enum
    :param configuration_status: Possible values include: 'Configured',
     'NotConfigured', 'InProgress', 'Failed', 'NoStatus'
    :type configuration_status: str or ~azure.mgmt.security.models.enum
    """

    _attribute_map = {
        'path': {'key': 'path', 'type': 'str'},
        'action': {'key': 'action', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'publisher_info': {'key': 'publisherInfo', 'type': 'PublisherInfo'},
        'common': {'key': 'common', 'type': 'bool'},
        'user_sids': {'key': 'userSids', 'type': '[str]'},
        'usernames': {'key': 'usernames', 'type': '[UserRecommendation]'},
        'file_type': {'key': 'fileType', 'type': 'str'},
        'configuration_status': {'key': 'configurationStatus', 'type': 'str'},
    }

    def __init__(self, *, path: str=None, action=None, type=None, publisher_info=None, common: bool=None, user_sids=None, usernames=None, file_type=None, configuration_status=None, **kwargs) -> None:
        super(PathRecommendation, self).__init__(**kwargs)
        self.path = path
        self.action = action
        self.type = type
        self.publisher_info = publisher_info
        self.common = common
        self.user_sids = user_sids
        self.usernames = usernames
        self.file_type = file_type
        self.configuration_status = configuration_status
