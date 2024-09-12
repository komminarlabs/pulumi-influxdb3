CHANGELOG
=========

## [1.2.2] - 2024-09-12

### Added:

* Added [retry mechanism](github.com/hashicorp/go-retryablehttp) to retry InfluxDB v3 API request at least 3 times before erroring.

## [1.2.1] - 2024-08-21

### Added:

* Added [partition_template](https://docs.influxdata.com/influxdb/cloud-dedicated/admin/custom-partitions/partition-templates/) support. **Note:** Database and table partitions can only be defined on create. You [cannot update the partition strategy](https://docs.influxdata.com/influxdb/cloud-dedicated/admin/databases/create/#partition-templates-can-only-be-applied-on-create) of a database or table after it has been created. An update will result in resource replacement. 

## [1.0.1] - 2024-08-13

### Updated:

- Support new [terraform provider version](https://github.com/komminarlabs/terraform-provider-influxdb3/releases/tag/v1.0.1).
- Updated readme

## [1.0.0] - 2024-08-05

Initial release of the provider

#### New resources:

- `index/token.Token`
- `index/database.Database`

#### New functions:

- `index/getDatabase.getDatabase`
- `index/getDatabases.getDatabases`
- `index/getToken.getToken`
- `index/getTokens.getTokens`
