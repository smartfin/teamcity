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

from swagger_client.models.project import Project  # noqa: F401,E501
from swagger_client.models.properties import Properties  # noqa: F401,E501


class NewProjectDescription(object):
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
        'build_types_ids_map': 'Properties',
        'copy_all_associated_settings': 'bool',
        'id': 'str',
        'name': 'str',
        'parent_project': 'Project',
        'projects_ids_map': 'Properties',
        'source_project': 'Project',
        'source_project_locator': 'str',
        'vcs_roots_ids_map': 'Properties'
    }

    attribute_map = {
        'build_types_ids_map': 'buildTypesIdsMap',
        'copy_all_associated_settings': 'copyAllAssociatedSettings',
        'id': 'id',
        'name': 'name',
        'parent_project': 'parentProject',
        'projects_ids_map': 'projectsIdsMap',
        'source_project': 'sourceProject',
        'source_project_locator': 'sourceProjectLocator',
        'vcs_roots_ids_map': 'vcsRootsIdsMap'
    }

    def __init__(self, build_types_ids_map=None, copy_all_associated_settings=False, id=None, name=None, parent_project=None, projects_ids_map=None, source_project=None, source_project_locator=None, vcs_roots_ids_map=None):  # noqa: E501
        """NewProjectDescription - a model defined in Swagger"""  # noqa: E501

        self._build_types_ids_map = None
        self._copy_all_associated_settings = None
        self._id = None
        self._name = None
        self._parent_project = None
        self._projects_ids_map = None
        self._source_project = None
        self._source_project_locator = None
        self._vcs_roots_ids_map = None
        self.discriminator = None

        if build_types_ids_map is not None:
            self.build_types_ids_map = build_types_ids_map
        if copy_all_associated_settings is not None:
            self.copy_all_associated_settings = copy_all_associated_settings
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if parent_project is not None:
            self.parent_project = parent_project
        if projects_ids_map is not None:
            self.projects_ids_map = projects_ids_map
        if source_project is not None:
            self.source_project = source_project
        if source_project_locator is not None:
            self.source_project_locator = source_project_locator
        if vcs_roots_ids_map is not None:
            self.vcs_roots_ids_map = vcs_roots_ids_map

    @property
    def build_types_ids_map(self):
        """Gets the build_types_ids_map of this NewProjectDescription.  # noqa: E501


        :return: The build_types_ids_map of this NewProjectDescription.  # noqa: E501
        :rtype: Properties
        """
        return self._build_types_ids_map

    @build_types_ids_map.setter
    def build_types_ids_map(self, build_types_ids_map):
        """Sets the build_types_ids_map of this NewProjectDescription.


        :param build_types_ids_map: The build_types_ids_map of this NewProjectDescription.  # noqa: E501
        :type: Properties
        """

        self._build_types_ids_map = build_types_ids_map

    @property
    def copy_all_associated_settings(self):
        """Gets the copy_all_associated_settings of this NewProjectDescription.  # noqa: E501


        :return: The copy_all_associated_settings of this NewProjectDescription.  # noqa: E501
        :rtype: bool
        """
        return self._copy_all_associated_settings

    @copy_all_associated_settings.setter
    def copy_all_associated_settings(self, copy_all_associated_settings):
        """Sets the copy_all_associated_settings of this NewProjectDescription.


        :param copy_all_associated_settings: The copy_all_associated_settings of this NewProjectDescription.  # noqa: E501
        :type: bool
        """

        self._copy_all_associated_settings = copy_all_associated_settings

    @property
    def id(self):
        """Gets the id of this NewProjectDescription.  # noqa: E501


        :return: The id of this NewProjectDescription.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NewProjectDescription.


        :param id: The id of this NewProjectDescription.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this NewProjectDescription.  # noqa: E501


        :return: The name of this NewProjectDescription.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NewProjectDescription.


        :param name: The name of this NewProjectDescription.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parent_project(self):
        """Gets the parent_project of this NewProjectDescription.  # noqa: E501


        :return: The parent_project of this NewProjectDescription.  # noqa: E501
        :rtype: Project
        """
        return self._parent_project

    @parent_project.setter
    def parent_project(self, parent_project):
        """Sets the parent_project of this NewProjectDescription.


        :param parent_project: The parent_project of this NewProjectDescription.  # noqa: E501
        :type: Project
        """

        self._parent_project = parent_project

    @property
    def projects_ids_map(self):
        """Gets the projects_ids_map of this NewProjectDescription.  # noqa: E501


        :return: The projects_ids_map of this NewProjectDescription.  # noqa: E501
        :rtype: Properties
        """
        return self._projects_ids_map

    @projects_ids_map.setter
    def projects_ids_map(self, projects_ids_map):
        """Sets the projects_ids_map of this NewProjectDescription.


        :param projects_ids_map: The projects_ids_map of this NewProjectDescription.  # noqa: E501
        :type: Properties
        """

        self._projects_ids_map = projects_ids_map

    @property
    def source_project(self):
        """Gets the source_project of this NewProjectDescription.  # noqa: E501


        :return: The source_project of this NewProjectDescription.  # noqa: E501
        :rtype: Project
        """
        return self._source_project

    @source_project.setter
    def source_project(self, source_project):
        """Sets the source_project of this NewProjectDescription.


        :param source_project: The source_project of this NewProjectDescription.  # noqa: E501
        :type: Project
        """

        self._source_project = source_project

    @property
    def source_project_locator(self):
        """Gets the source_project_locator of this NewProjectDescription.  # noqa: E501


        :return: The source_project_locator of this NewProjectDescription.  # noqa: E501
        :rtype: str
        """
        return self._source_project_locator

    @source_project_locator.setter
    def source_project_locator(self, source_project_locator):
        """Sets the source_project_locator of this NewProjectDescription.


        :param source_project_locator: The source_project_locator of this NewProjectDescription.  # noqa: E501
        :type: str
        """

        self._source_project_locator = source_project_locator

    @property
    def vcs_roots_ids_map(self):
        """Gets the vcs_roots_ids_map of this NewProjectDescription.  # noqa: E501


        :return: The vcs_roots_ids_map of this NewProjectDescription.  # noqa: E501
        :rtype: Properties
        """
        return self._vcs_roots_ids_map

    @vcs_roots_ids_map.setter
    def vcs_roots_ids_map(self, vcs_roots_ids_map):
        """Sets the vcs_roots_ids_map of this NewProjectDescription.


        :param vcs_roots_ids_map: The vcs_roots_ids_map of this NewProjectDescription.  # noqa: E501
        :type: Properties
        """

        self._vcs_roots_ids_map = vcs_roots_ids_map

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
        if issubclass(NewProjectDescription, dict):
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
        if not isinstance(other, NewProjectDescription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
