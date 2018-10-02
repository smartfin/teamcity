# coding: utf-8

"""
    TeamCity REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 10.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.debug_api import DebugApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDebugApi(unittest.TestCase):
    """DebugApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.debug_api.DebugApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_current_remember_me(self):
        """Test case for delete_current_remember_me

        """
        pass

    def test_empty_task(self):
        """Test case for empty_task

        """
        pass

    def test_execute_db_query(self):
        """Test case for execute_db_query

        """
        pass

    def test_get_current_session(self):
        """Test case for get_current_session

        """
        pass

    def test_get_current_session_max_inactive_interval(self):
        """Test case for get_current_session_max_inactive_interval

        """
        pass

    def test_get_current_user_permissions(self):
        """Test case for get_current_user_permissions

        """
        pass

    def test_get_date(self):
        """Test case for get_date

        """
        pass

    def test_get_environment_variables(self):
        """Test case for get_environment_variables

        """
        pass

    def test_get_hashed(self):
        """Test case for get_hashed

        """
        pass

    def test_get_request_details(self):
        """Test case for get_request_details

        """
        pass

    def test_get_scrambled(self):
        """Test case for get_scrambled

        """
        pass

    def test_get_sessions(self):
        """Test case for get_sessions

        """
        pass

    def test_get_system_properties(self):
        """Test case for get_system_properties

        """
        pass

    def test_get_thread_dump(self):
        """Test case for get_thread_dump

        """
        pass

    def test_get_unscrambled(self):
        """Test case for get_unscrambled

        """
        pass

    def test_invalidate_current_session(self):
        """Test case for invalidate_current_session

        """
        pass

    def test_list_db_tables(self):
        """Test case for list_db_tables

        """
        pass

    def test_new_remember_me(self):
        """Test case for new_remember_me

        """
        pass

    def test_save_memory_dump(self):
        """Test case for save_memory_dump

        """
        pass

    def test_schedule_checking_for_changes(self):
        """Test case for schedule_checking_for_changes

        """
        pass

    def test_set_current_session_max_inactive_interval(self):
        """Test case for set_current_session_max_inactive_interval

        """
        pass


if __name__ == '__main__':
    unittest.main()
