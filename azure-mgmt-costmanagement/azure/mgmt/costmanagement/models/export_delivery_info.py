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


class ExportDeliveryInfo(Model):
    """The delivery information associated with a export.

    All required parameters must be populated in order to send to Azure.

    :param destination: Required. Has destination for the export being
     delivered.
    :type destination:
     ~azure.mgmt.costmanagement.models.ExportDeliveryDestination
    """

    _validation = {
        'destination': {'required': True},
    }

    _attribute_map = {
        'destination': {'key': 'destination', 'type': 'ExportDeliveryDestination'},
    }

    def __init__(self, **kwargs):
        super(ExportDeliveryInfo, self).__init__(**kwargs)
        self.destination = kwargs.get('destination', None)