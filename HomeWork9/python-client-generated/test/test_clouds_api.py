# coding: utf-8

"""
    Заказ ресурсов на облаке

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.clouds_api import CloudsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestCloudsApi(unittest.TestCase):
    """CloudsApi unit test stubs"""

    def setUp(self):
        self.api = CloudsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_cloud(self):
        """Test case for create_cloud

        Создание заказа на облако  # noqa: E501
        """
        pass

    def test_get_all_clouds(self):
        """Test case for get_all_clouds

        Метод получения списка ресурсов на облако  # noqa: E501
        """
        pass

    def test_get_cloud_by_id(self):
        """Test case for get_cloud_by_id

        Метод получения заказа на облако по ID  # noqa: E501
        """
        pass

    def test_get_cloud_by_id_0(self):
        """Test case for get_cloud_by_id_0

        Метод удаления заказа из облака по ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
