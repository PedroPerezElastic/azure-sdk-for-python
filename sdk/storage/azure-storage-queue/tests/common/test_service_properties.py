# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import unittest

from msrest.exceptions import ValidationError  # TODO This should be an azure-core error.
from azure.core.exceptions import HttpResponseError

from azure.storage.queue import (
    QueueServiceClient,
    QueueClient,
    Logging,
    Metrics,
    CorsRule,
    RetentionPolicy,
)

from tests.testcase import (
    StorageTestCase,
    record,
    not_for_emulator,
)


# ------------------------------------------------------------------------------


class ServicePropertiesTest(StorageTestCase):
    def setUp(self):
        super(ServicePropertiesTest, self).setUp()

        url = self._get_queue_url()
        credential = self._get_shared_key_credential()
        self.qsc = QueueServiceClient(url, credential=credential)

    # --Helpers-----------------------------------------------------------------
    def _assert_properties_default(self, prop):
        self.assertIsNotNone(prop)

        self._assert_logging_equal(prop.logging, Logging())
        self._assert_metrics_equal(prop.hour_metrics, Metrics())
        self._assert_metrics_equal(prop.minute_metrics, Metrics())
        self._assert_cors_equal(prop.cors, list())

    def _assert_logging_equal(self, log1, log2):
        if log1 is None or log2 is None:
            self.assertEqual(log1, log2)
            return

        self.assertEqual(log1.version, log2.version)
        self.assertEqual(log1.read, log2.read)
        self.assertEqual(log1.write, log2.write)
        self.assertEqual(log1.delete, log2.delete)
        self._assert_retention_equal(log1.retention_policy, log2.retention_policy)

    def _assert_delete_retention_policy_equal(self, policy1, policy2):
        if policy1 is None or policy2 is None:
            self.assertEqual(policy1, policy2)
            return

        self.assertEqual(policy1.enabled, policy2.enabled)
        self.assertEqual(policy1.days, policy2.days)

    def _assert_static_website_equal(self, prop1, prop2):
        if prop1 is None or prop2 is None:
            self.assertEqual(prop1, prop2)
            return

        self.assertEqual(prop1.enabled, prop2.enabled)
        self.assertEqual(prop1.index_document, prop2.index_document)
        self.assertEqual(prop1.error_document404_path, prop2.error_document404_path)

    def _assert_delete_retention_policy_not_equal(self, policy1, policy2):
        if policy1 is None or policy2 is None:
            self.assertNotEqual(policy1, policy2)
            return

        self.assertFalse(policy1.enabled == policy2.enabled
                         and policy1.days == policy2.days)

    def _assert_metrics_equal(self, metrics1, metrics2):
        if metrics1 is None or metrics2 is None:
            self.assertEqual(metrics1, metrics2)
            return

        self.assertEqual(metrics1.version, metrics2.version)
        self.assertEqual(metrics1.enabled, metrics2.enabled)
        self.assertEqual(metrics1.include_apis, metrics2.include_apis)
        self._assert_retention_equal(metrics1.retention_policy, metrics2.retention_policy)

    def _assert_cors_equal(self, cors1, cors2):
        if cors1 is None or cors2 is None:
            self.assertEqual(cors1, cors2)
            return

        self.assertEqual(len(cors1), len(cors2))

        for i in range(0, len(cors1)):
            rule1 = cors1[i]
            rule2 = cors2[i]
            self.assertEqual(len(rule1.allowed_origins), len(rule2.allowed_origins))
            self.assertEqual(len(rule1.allowed_methods), len(rule2.allowed_methods))
            self.assertEqual(rule1.max_age_in_seconds, rule2.max_age_in_seconds)
            self.assertEqual(len(rule1.exposed_headers), len(rule2.exposed_headers))
            self.assertEqual(len(rule1.allowed_headers), len(rule2.allowed_headers))

    def _assert_retention_equal(self, ret1, ret2):
        self.assertEqual(ret1.enabled, ret2.enabled)
        self.assertEqual(ret1.days, ret2.days)

    # --Test cases per service ---------------------------------------

    @record
    def test_queue_service_properties(self):
        # Arrange

        # Act
        resp = self.qsc.set_service_properties(
            logging=Logging(),
            hour_metrics=Metrics(),
            minute_metrics=Metrics(),
            cors=list())

        # Assert
        self.assertIsNone(resp)
        self._assert_properties_default(self.qsc.get_service_properties())


    # --Test cases per feature ---------------------------------------

    @record
    def test_set_logging(self):
        # Arrange
        logging = Logging(read=True, write=True, delete=True, retention_policy=RetentionPolicy(enabled=True, days=5))

        # Act
        self.qsc.set_service_properties(logging=logging)

        # Assert
        received_props = self.qsc.get_service_properties()
        self._assert_logging_equal(received_props.logging, logging)

    @record
    def test_set_hour_metrics(self):
        # Arrange
        hour_metrics = Metrics(enabled=True, include_apis=True, retention_policy=RetentionPolicy(enabled=True, days=5))

        # Act
        self.qsc.set_service_properties(hour_metrics=hour_metrics)

        # Assert
        received_props = self.qsc.get_service_properties()
        self._assert_metrics_equal(received_props.hour_metrics, hour_metrics)

    @record
    def test_set_minute_metrics(self):
        # Arrange
        minute_metrics = Metrics(enabled=True, include_apis=True,
                                 retention_policy=RetentionPolicy(enabled=True, days=5))

        # Act
        self.qsc.set_service_properties(minute_metrics=minute_metrics)

        # Assert
        received_props = self.qsc.get_service_properties()
        self._assert_metrics_equal(received_props.minute_metrics, minute_metrics)

    @record
    def test_set_cors(self):
        # Arrange
        cors_rule1 = CorsRule(['www.xyz.com'], ['GET'])

        allowed_origins = ['www.xyz.com', "www.ab.com", "www.bc.com"]
        allowed_methods = ['GET', 'PUT']
        max_age_in_seconds = 500
        exposed_headers = ["x-ms-meta-data*", "x-ms-meta-source*", "x-ms-meta-abc", "x-ms-meta-bcd"]
        allowed_headers = ["x-ms-meta-data*", "x-ms-meta-target*", "x-ms-meta-xyz", "x-ms-meta-foo"]
        cors_rule2 = CorsRule(
            allowed_origins,
            allowed_methods,
            max_age_in_seconds=max_age_in_seconds,
            exposed_headers=exposed_headers,
            allowed_headers=allowed_headers)

        cors = [cors_rule1, cors_rule2]

        # Act
        self.qsc.set_service_properties(cors=cors)

        # Assert
        received_props = self.qsc.get_service_properties()
        self._assert_cors_equal(received_props.cors, cors)

    # --Test cases for errors ---------------------------------------
    @record
    def test_retention_no_days(self):
        # Assert
        self.assertRaises(ValueError,
                          RetentionPolicy,
                          True, None)

    @record
    def test_too_many_cors_rules(self):
        # Arrange
        cors = []
        for i in range(0, 6):
            cors.append(CorsRule(['www.xyz.com'], ['GET']))

        # Assert
        self.assertRaises(HttpResponseError,
                          self.qsc.set_service_properties, None, None, None, cors)

    @record
    def test_retention_too_long(self):
        # Arrange
        minute_metrics = Metrics(enabled=True, include_apis=True,
                                 retention_policy=RetentionPolicy(enabled=True, days=366))

        # Assert
        self.assertRaises(HttpResponseError,
                          self.qsc.set_service_properties,
                          None, None, minute_metrics)


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
