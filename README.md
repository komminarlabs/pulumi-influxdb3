# InfluxDB V3 Resource Provider

The InfluxDB V3 Resource Provider lets you manage [InfluxDB V3](https://www.influxdata.com/products/influxdb-overview/#overview) resources.

## ⚠️ Deprecation Notice

This Pulumi provider for **InfluxDB V3** is **deprecated** and is no longer actively maintained as of **October 2025**.  
While earlier versions were published, **no further updates, bug fixes, or support will be provided**.

- Existing releases may continue to work, but compatibility with future Pulumi or InfluxDB V3 versions is not guaranteed.  
- Do **not** use this provider for new projects.  
- The repository is archived and remains public for reference purposes only.  
- If you require continued usage, you may **fork the repository** and maintain your own version.

## Supported InfluxDB flavours

* [InfluxDB Cloud Dedicated](https://www.influxdata.com/products/influxdb-cloud/dedicated/)

## Installing

This package is available for several languages/platforms:

### Node.js (JavaScript/TypeScript)

To use from JavaScript or TypeScript in Node.js, install using either `npm`:

```bash
npm install @komminarlabs/influxdb3
```

or `yarn`:

```bash
yarn add @komminarlabs/influxdb3
```

### Python

To use from Python, install using `pip`:

```bash
pip install komminarlabs-influxdb3
```

### Go

To use from Go, use `go get` to grab the latest version of the library:

```bash
go get github.com/komminarlabs/pulumi-influxdb3/sdk/go/...
```

### .NET

To use from .NET, install using `dotnet add package`:

```bash
dotnet add package KomminarLabs.InfluxDB3
```

## Configuration

The following configuration points are available for the `influxdb3` provider:

- `influxdb3:account_id` (environment: `INFLUXDB3_ACCOUNT_ID`) - The ID of the account that the cluster belongs to
- `influxdb3:cluster_id` (environment: `INFLUXDB3_CLUSTER_ID`) - The ID of the cluster that you want to manage
- `influxdb3:token` (environment: `INFLUXDB3_TOKEN`) - The InfluxDB management token

## Reference

For detailed reference documentation, please visit [the Pulumi registry](https://www.pulumi.com/registry/packages/influxdb3/api-docs/).
