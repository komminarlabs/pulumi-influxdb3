# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'DatabasePartitionTemplate',
    'TokenPermission',
    'GetDatabasePartitionTemplateResult',
    'GetDatabasesDatabaseResult',
    'GetDatabasesDatabasePartitionTemplateResult',
    'GetTokenPermissionResult',
    'GetTokensTokenResult',
    'GetTokensTokenPermissionResult',
]

@pulumi.output_type
class DatabasePartitionTemplate(dict):
    def __init__(__self__, *,
                 type: str,
                 value: str):
        """
        :param str type: The type of template part. Valid values are `bucket`, `tag` or `time`.
        :param str value: The value of template part. **Note:** For `bucket` partition template type use `jsonencode()` function to encode the value to a string.
        """
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of template part. Valid values are `bucket`, `tag` or `time`.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value of template part. **Note:** For `bucket` partition template type use `jsonencode()` function to encode the value to a string.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class TokenPermission(dict):
    def __init__(__self__, *,
                 action: str,
                 resource: str):
        """
        :param str action: The action the database token permission allows. Valid values are `read` or `write`.
        :param str resource: The resource the database token permission applies to. `*` refers to all databases.
        """
        pulumi.set(__self__, "action", action)
        pulumi.set(__self__, "resource", resource)

    @property
    @pulumi.getter
    def action(self) -> str:
        """
        The action the database token permission allows. Valid values are `read` or `write`.
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter
    def resource(self) -> str:
        """
        The resource the database token permission applies to. `*` refers to all databases.
        """
        return pulumi.get(self, "resource")


@pulumi.output_type
class GetDatabasePartitionTemplateResult(dict):
    def __init__(__self__, *,
                 type: str,
                 value: str):
        """
        :param str type: The type of template part.
        :param str value: The value of template part.
        """
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of template part.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value of template part.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class GetDatabasesDatabaseResult(dict):
    def __init__(__self__, *,
                 account_id: str,
                 cluster_id: str,
                 max_columns_per_table: int,
                 max_tables: int,
                 name: str,
                 partition_templates: Sequence['outputs.GetDatabasesDatabasePartitionTemplateResult'],
                 retention_period: int):
        """
        :param str account_id: The ID of the account that the cluster belongs to.
        :param str cluster_id: The ID of the cluster that you want to manage.
        :param int max_columns_per_table: The maximum number of columns per table for the cluster database.
        :param int max_tables: The maximum number of tables for the cluster database.
        :param str name: The name of the cluster database.
        :param Sequence['GetDatabasesDatabasePartitionTemplateArgs'] partition_templates: The template partitioning of the cluster database.
        :param int retention_period: The retention period of the cluster database in nanoseconds.
        """
        pulumi.set(__self__, "account_id", account_id)
        pulumi.set(__self__, "cluster_id", cluster_id)
        pulumi.set(__self__, "max_columns_per_table", max_columns_per_table)
        pulumi.set(__self__, "max_tables", max_tables)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "partition_templates", partition_templates)
        pulumi.set(__self__, "retention_period", retention_period)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        """
        The ID of the account that the cluster belongs to.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        """
        The ID of the cluster that you want to manage.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="maxColumnsPerTable")
    def max_columns_per_table(self) -> int:
        """
        The maximum number of columns per table for the cluster database.
        """
        return pulumi.get(self, "max_columns_per_table")

    @property
    @pulumi.getter(name="maxTables")
    def max_tables(self) -> int:
        """
        The maximum number of tables for the cluster database.
        """
        return pulumi.get(self, "max_tables")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the cluster database.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partitionTemplates")
    def partition_templates(self) -> Sequence['outputs.GetDatabasesDatabasePartitionTemplateResult']:
        """
        The template partitioning of the cluster database.
        """
        return pulumi.get(self, "partition_templates")

    @property
    @pulumi.getter(name="retentionPeriod")
    def retention_period(self) -> int:
        """
        The retention period of the cluster database in nanoseconds.
        """
        return pulumi.get(self, "retention_period")


@pulumi.output_type
class GetDatabasesDatabasePartitionTemplateResult(dict):
    def __init__(__self__, *,
                 type: str,
                 value: str):
        """
        :param str type: The type of template part.
        :param str value: The value of template part.
        """
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of template part.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value of template part.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class GetTokenPermissionResult(dict):
    def __init__(__self__, *,
                 action: str,
                 resource: str):
        """
        :param str action: The action the database token permission allows.
        :param str resource: The resource the database token permission applies to. `*` refers to all databases.
        """
        pulumi.set(__self__, "action", action)
        pulumi.set(__self__, "resource", resource)

    @property
    @pulumi.getter
    def action(self) -> str:
        """
        The action the database token permission allows.
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter
    def resource(self) -> str:
        """
        The resource the database token permission applies to. `*` refers to all databases.
        """
        return pulumi.get(self, "resource")


@pulumi.output_type
class GetTokensTokenResult(dict):
    def __init__(__self__, *,
                 access_token: str,
                 account_id: str,
                 cluster_id: str,
                 created_at: str,
                 description: str,
                 id: str,
                 permissions: Sequence['outputs.GetTokensTokenPermissionResult']):
        """
        :param str access_token: The access token that can be used to authenticate query and write requests to the cluster. The access token is never stored by InfluxDB and is only returned once when the token is created. If the access token is lost, a new token must be created.
        :param str account_id: The ID of the account that the database token belongs to.
        :param str cluster_id: The ID of the cluster that the database token belongs to.
        :param str created_at: The date and time that the database token was created. Uses RFC3339 format.
        :param str description: The description of the database token.
        :param str id: The ID of the database token.
        :param Sequence['GetTokensTokenPermissionArgs'] permissions: The list of permissions the database token allows.
        """
        pulumi.set(__self__, "access_token", access_token)
        pulumi.set(__self__, "account_id", account_id)
        pulumi.set(__self__, "cluster_id", cluster_id)
        pulumi.set(__self__, "created_at", created_at)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "permissions", permissions)

    @property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> str:
        """
        The access token that can be used to authenticate query and write requests to the cluster. The access token is never stored by InfluxDB and is only returned once when the token is created. If the access token is lost, a new token must be created.
        """
        return pulumi.get(self, "access_token")

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        """
        The ID of the account that the database token belongs to.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        """
        The ID of the cluster that the database token belongs to.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        The date and time that the database token was created. Uses RFC3339 format.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the database token.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the database token.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def permissions(self) -> Sequence['outputs.GetTokensTokenPermissionResult']:
        """
        The list of permissions the database token allows.
        """
        return pulumi.get(self, "permissions")


@pulumi.output_type
class GetTokensTokenPermissionResult(dict):
    def __init__(__self__, *,
                 action: str,
                 resource: str):
        """
        :param str action: The action the database token permission allows.
        :param str resource: The resource the database token permission applies to. `*` refers to all databases.
        """
        pulumi.set(__self__, "action", action)
        pulumi.set(__self__, "resource", resource)

    @property
    @pulumi.getter
    def action(self) -> str:
        """
        The action the database token permission allows.
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter
    def resource(self) -> str:
        """
        The resource the database token permission applies to. `*` refers to all databases.
        """
        return pulumi.get(self, "resource")


