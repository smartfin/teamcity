# coding: utf-8

"""
    TeamCity REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 10.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.branch import Branch  # noqa: F401,E501


class Branches(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'branch': 'list[Branch]',
        'count': 'int'
    }

    attribute_map = {
        'branch': 'branch',
        'count': 'count'
    }

    def __init__(self, branch=None, count=None):  # noqa: E501
        """Branches - a model defined in Swagger"""  # noqa: E501

        self._branch = None
        self._count = None
        self.discriminator = None

        if branch is not None:
            self.branch = branch
        if count is not None:
            self.count = count

    @property
    def branch(self):
        """Gets the branch of this Branches.  # noqa: E501


        :return: The branch of this Branches.  # noqa: E501
        :rtype: list[Branch]
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this Branches.


        :param branch: The branch of this Branches.  # noqa: E501
        :type: list[Branch]
        """

        self._branch = branch

    @property
    def count(self):
        """Gets the count of this Branches.  # noqa: E501


        :return: The count of this Branches.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Branches.


        :param count: The count of this Branches.  # noqa: E501
        :type: int
        """

        self._count = count

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Branches, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Branches):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
