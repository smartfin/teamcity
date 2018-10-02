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

from swagger_client.models.agent_pool import AgentPool  # noqa: F401,E501


class AgentPools(object):
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
        'agent_pool': 'list[AgentPool]',
        'count': 'int',
        'href': 'str',
        'next_href': 'str',
        'prev_href': 'str'
    }

    attribute_map = {
        'agent_pool': 'agentPool',
        'count': 'count',
        'href': 'href',
        'next_href': 'nextHref',
        'prev_href': 'prevHref'
    }

    def __init__(self, agent_pool=None, count=None, href=None, next_href=None, prev_href=None):  # noqa: E501
        """AgentPools - a model defined in Swagger"""  # noqa: E501

        self._agent_pool = None
        self._count = None
        self._href = None
        self._next_href = None
        self._prev_href = None
        self.discriminator = None

        if agent_pool is not None:
            self.agent_pool = agent_pool
        if count is not None:
            self.count = count
        if href is not None:
            self.href = href
        if next_href is not None:
            self.next_href = next_href
        if prev_href is not None:
            self.prev_href = prev_href

    @property
    def agent_pool(self):
        """Gets the agent_pool of this AgentPools.  # noqa: E501


        :return: The agent_pool of this AgentPools.  # noqa: E501
        :rtype: list[AgentPool]
        """
        return self._agent_pool

    @agent_pool.setter
    def agent_pool(self, agent_pool):
        """Sets the agent_pool of this AgentPools.


        :param agent_pool: The agent_pool of this AgentPools.  # noqa: E501
        :type: list[AgentPool]
        """

        self._agent_pool = agent_pool

    @property
    def count(self):
        """Gets the count of this AgentPools.  # noqa: E501


        :return: The count of this AgentPools.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this AgentPools.


        :param count: The count of this AgentPools.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def href(self):
        """Gets the href of this AgentPools.  # noqa: E501


        :return: The href of this AgentPools.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this AgentPools.


        :param href: The href of this AgentPools.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def next_href(self):
        """Gets the next_href of this AgentPools.  # noqa: E501


        :return: The next_href of this AgentPools.  # noqa: E501
        :rtype: str
        """
        return self._next_href

    @next_href.setter
    def next_href(self, next_href):
        """Sets the next_href of this AgentPools.


        :param next_href: The next_href of this AgentPools.  # noqa: E501
        :type: str
        """

        self._next_href = next_href

    @property
    def prev_href(self):
        """Gets the prev_href of this AgentPools.  # noqa: E501


        :return: The prev_href of this AgentPools.  # noqa: E501
        :rtype: str
        """
        return self._prev_href

    @prev_href.setter
    def prev_href(self, prev_href):
        """Sets the prev_href of this AgentPools.


        :param prev_href: The prev_href of this AgentPools.  # noqa: E501
        :type: str
        """

        self._prev_href = prev_href

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
        if issubclass(AgentPools, dict):
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
        if not isinstance(other, AgentPools):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
