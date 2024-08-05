// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";

export interface GetDatabasesDatabase {
    /**
     * The ID of the account that the cluster belongs to.
     */
    accountId: string;
    /**
     * The ID of the cluster that you want to manage.
     */
    clusterId: string;
    /**
     * The maximum number of columns per table for the cluster database.
     */
    maxColumnsPerTable: number;
    /**
     * The maximum number of tables for the cluster database.
     */
    maxTables: number;
    /**
     * The name of the cluster database.
     */
    name: string;
    /**
     * The retention period of the cluster database in nanoseconds.
     */
    retentionPeriod: number;
}

export interface GetTokenPermission {
    /**
     * The action the database token permission allows.
     */
    action: string;
    /**
     * The resource the database token permission applies to. `*` refers to all databases.
     */
    resource: string;
}

export interface GetTokensToken {
    /**
     * The access token that can be used to authenticate query and write requests to the cluster. The access token is never stored by InfluxDB and is only returned once when the token is created. If the access token is lost, a new token must be created.
     */
    accessToken: string;
    /**
     * The ID of the account that the database token belongs to.
     */
    accountId: string;
    /**
     * The ID of the cluster that the database token belongs to.
     */
    clusterId: string;
    /**
     * The date and time that the database token was created. Uses RFC3339 format.
     */
    createdAt: string;
    /**
     * The description of the database token.
     */
    description: string;
    /**
     * The ID of the database token.
     */
    id: string;
    /**
     * The list of permissions the database token allows.
     */
    permissions: outputs.GetTokensTokenPermission[];
}

export interface GetTokensTokenPermission {
    /**
     * The action the database token permission allows.
     */
    action: string;
    /**
     * The resource the database token permission applies to. `*` refers to all databases.
     */
    resource: string;
}

export interface TokenPermission {
    /**
     * The action the database token permission allows. Valid values are `read` or `write`.
     */
    action: string;
    /**
     * The resource the database token permission applies to. `*` refers to all databases.
     */
    resource: string;
}

