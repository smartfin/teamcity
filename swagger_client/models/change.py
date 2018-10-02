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

from swagger_client.models.changes import Changes  # noqa: F401,E501
from swagger_client.models.file_changes import FileChanges  # noqa: F401,E501
from swagger_client.models.items import Items  # noqa: F401,E501
from swagger_client.models.user import User  # noqa: F401,E501
from swagger_client.models.vcs_root_instance import VcsRootInstance  # noqa: F401,E501


class Change(object):
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
        'comment': 'str',
        '_date': 'str',
        'files': 'FileChanges',
        'href': 'str',
        'id': 'int',
        'internal_version': 'str',
        'locator': 'str',
        'parent_changes': 'Changes',
        'parent_revisions': 'Items',
        'personal': 'bool',
        'registration_date': 'str',
        'user': 'User',
        'username': 'str',
        'vcs_root_instance': 'VcsRootInstance',
        'version': 'str',
        'web_url': 'str'
    }

    attribute_map = {
        'comment': 'comment',
        '_date': 'date',
        'files': 'files',
        'href': 'href',
        'id': 'id',
        'internal_version': 'internalVersion',
        'locator': 'locator',
        'parent_changes': 'parentChanges',
        'parent_revisions': 'parentRevisions',
        'personal': 'personal',
        'registration_date': 'registrationDate',
        'user': 'user',
        'username': 'username',
        'vcs_root_instance': 'vcsRootInstance',
        'version': 'version',
        'web_url': 'webUrl'
    }

    def __init__(self, comment=None, _date=None, files=None, href=None, id=None, internal_version=None, locator=None, parent_changes=None, parent_revisions=None, personal=False, registration_date=None, user=None, username=None, vcs_root_instance=None, version=None, web_url=None):  # noqa: E501
        """Change - a model defined in Swagger"""  # noqa: E501

        self._comment = None
        self.__date = None
        self._files = None
        self._href = None
        self._id = None
        self._internal_version = None
        self._locator = None
        self._parent_changes = None
        self._parent_revisions = None
        self._personal = None
        self._registration_date = None
        self._user = None
        self._username = None
        self._vcs_root_instance = None
        self._version = None
        self._web_url = None
        self.discriminator = None

        if comment is not None:
            self.comment = comment
        if _date is not None:
            self._date = _date
        if files is not None:
            self.files = files
        if href is not None:
            self.href = href
        if id is not None:
            self.id = id
        if internal_version is not None:
            self.internal_version = internal_version
        if locator is not None:
            self.locator = locator
        if parent_changes is not None:
            self.parent_changes = parent_changes
        if parent_revisions is not None:
            self.parent_revisions = parent_revisions
        if personal is not None:
            self.personal = personal
        if registration_date is not None:
            self.registration_date = registration_date
        if user is not None:
            self.user = user
        if username is not None:
            self.username = username
        if vcs_root_instance is not None:
            self.vcs_root_instance = vcs_root_instance
        if version is not None:
            self.version = version
        if web_url is not None:
            self.web_url = web_url

    @property
    def comment(self):
        """Gets the comment of this Change.  # noqa: E501


        :return: The comment of this Change.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this Change.


        :param comment: The comment of this Change.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def _date(self):
        """Gets the _date of this Change.  # noqa: E501


        :return: The _date of this Change.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this Change.


        :param _date: The _date of this Change.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def files(self):
        """Gets the files of this Change.  # noqa: E501


        :return: The files of this Change.  # noqa: E501
        :rtype: FileChanges
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this Change.


        :param files: The files of this Change.  # noqa: E501
        :type: FileChanges
        """

        self._files = files

    @property
    def href(self):
        """Gets the href of this Change.  # noqa: E501


        :return: The href of this Change.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Change.


        :param href: The href of this Change.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def id(self):
        """Gets the id of this Change.  # noqa: E501


        :return: The id of this Change.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Change.


        :param id: The id of this Change.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def internal_version(self):
        """Gets the internal_version of this Change.  # noqa: E501


        :return: The internal_version of this Change.  # noqa: E501
        :rtype: str
        """
        return self._internal_version

    @internal_version.setter
    def internal_version(self, internal_version):
        """Sets the internal_version of this Change.


        :param internal_version: The internal_version of this Change.  # noqa: E501
        :type: str
        """

        self._internal_version = internal_version

    @property
    def locator(self):
        """Gets the locator of this Change.  # noqa: E501


        :return: The locator of this Change.  # noqa: E501
        :rtype: str
        """
        return self._locator

    @locator.setter
    def locator(self, locator):
        """Sets the locator of this Change.


        :param locator: The locator of this Change.  # noqa: E501
        :type: str
        """

        self._locator = locator

    @property
    def parent_changes(self):
        """Gets the parent_changes of this Change.  # noqa: E501


        :return: The parent_changes of this Change.  # noqa: E501
        :rtype: Changes
        """
        return self._parent_changes

    @parent_changes.setter
    def parent_changes(self, parent_changes):
        """Sets the parent_changes of this Change.


        :param parent_changes: The parent_changes of this Change.  # noqa: E501
        :type: Changes
        """

        self._parent_changes = parent_changes

    @property
    def parent_revisions(self):
        """Gets the parent_revisions of this Change.  # noqa: E501


        :return: The parent_revisions of this Change.  # noqa: E501
        :rtype: Items
        """
        return self._parent_revisions

    @parent_revisions.setter
    def parent_revisions(self, parent_revisions):
        """Sets the parent_revisions of this Change.


        :param parent_revisions: The parent_revisions of this Change.  # noqa: E501
        :type: Items
        """

        self._parent_revisions = parent_revisions

    @property
    def personal(self):
        """Gets the personal of this Change.  # noqa: E501


        :return: The personal of this Change.  # noqa: E501
        :rtype: bool
        """
        return self._personal

    @personal.setter
    def personal(self, personal):
        """Sets the personal of this Change.


        :param personal: The personal of this Change.  # noqa: E501
        :type: bool
        """

        self._personal = personal

    @property
    def registration_date(self):
        """Gets the registration_date of this Change.  # noqa: E501


        :return: The registration_date of this Change.  # noqa: E501
        :rtype: str
        """
        return self._registration_date

    @registration_date.setter
    def registration_date(self, registration_date):
        """Sets the registration_date of this Change.


        :param registration_date: The registration_date of this Change.  # noqa: E501
        :type: str
        """

        self._registration_date = registration_date

    @property
    def user(self):
        """Gets the user of this Change.  # noqa: E501


        :return: The user of this Change.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Change.


        :param user: The user of this Change.  # noqa: E501
        :type: User
        """

        self._user = user

    @property
    def username(self):
        """Gets the username of this Change.  # noqa: E501


        :return: The username of this Change.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Change.


        :param username: The username of this Change.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def vcs_root_instance(self):
        """Gets the vcs_root_instance of this Change.  # noqa: E501


        :return: The vcs_root_instance of this Change.  # noqa: E501
        :rtype: VcsRootInstance
        """
        return self._vcs_root_instance

    @vcs_root_instance.setter
    def vcs_root_instance(self, vcs_root_instance):
        """Sets the vcs_root_instance of this Change.


        :param vcs_root_instance: The vcs_root_instance of this Change.  # noqa: E501
        :type: VcsRootInstance
        """

        self._vcs_root_instance = vcs_root_instance

    @property
    def version(self):
        """Gets the version of this Change.  # noqa: E501


        :return: The version of this Change.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Change.


        :param version: The version of this Change.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def web_url(self):
        """Gets the web_url of this Change.  # noqa: E501


        :return: The web_url of this Change.  # noqa: E501
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        """Sets the web_url of this Change.


        :param web_url: The web_url of this Change.  # noqa: E501
        :type: str
        """

        self._web_url = web_url

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
        if issubclass(Change, dict):
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
        if not isinstance(other, Change):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
