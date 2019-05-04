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

from .step_properties import StepProperties


class WaitStepProperties(StepProperties):
    """Defines the properties of a Wait step.

    All required parameters must be populated in order to send to Azure.

    :param step_type: Required. Constant filled by server.
    :type step_type: str
    :param attributes: The Wait attributes
    :type attributes: ~azure.mgmt.deploymentmanager.models.WaitStepAttributes
    """

    _validation = {
        'step_type': {'required': True},
    }

    _attribute_map = {
        'step_type': {'key': 'stepType', 'type': 'str'},
        'attributes': {'key': 'attributes', 'type': 'WaitStepAttributes'},
    }

    def __init__(self, **kwargs):
        super(WaitStepProperties, self).__init__(**kwargs)
        self.attributes = kwargs.get('attributes', None)
        self.step_type = 'Wait'