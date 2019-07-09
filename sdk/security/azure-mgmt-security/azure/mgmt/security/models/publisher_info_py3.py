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


class PublisherInfo(Model):
    """Represents the publisher information of a process/rule.

    :param publisher_name: The Subject field of the x.509 certificate used to
     sign the code, using the following fields -  O = Organization, L =
     Locality, S = State or Province, and C = Country
    :type publisher_name: str
    :param product_name: The product name taken from the file's version
     resource
    :type product_name: str
    :param binary_name: The "OriginalName" field taken from the file's version
     resource
    :type binary_name: str
    :param version: The binary file version taken from the file's version
     resource
    :type version: str
    """

    _attribute_map = {
        'publisher_name': {'key': 'publisherName', 'type': 'str'},
        'product_name': {'key': 'productName', 'type': 'str'},
        'binary_name': {'key': 'binaryName', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(self, *, publisher_name: str=None, product_name: str=None, binary_name: str=None, version: str=None, **kwargs) -> None:
        super(PublisherInfo, self).__init__(**kwargs)
        self.publisher_name = publisher_name
        self.product_name = product_name
        self.binary_name = binary_name
        self.version = version
