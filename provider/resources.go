package influxdb3

import (
	"context"
	"fmt"
	"path"

	// Allow embedding bridge-metadata.json in the provider.
	_ "embed"

	influxdb3shim "github.com/komminarlabs/terraform-provider-influxdb3/shim"

	pf "github.com/pulumi/pulumi-terraform-bridge/pf/tfbridge"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge/tokens"
	shim "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"

	// Import custom shim
	"github.com/komminarlabs/pulumi-influxdb3/provider/pkg/version"
)

// all of the token components used below.
const (
	// This variable controls the default name of the package in the package
	// registries for nodejs and python:
	mainPkg = "influxdb3"
	// modules:
	mainMod = "index" // the influxdb module
)

// preConfigureCallback is called before the providerConfigure function of the underlying provider.
// It should validate that the provider can be configured, and provide actionable errors in the case
// it cannot be. Configuration variables can be read from `vars` using the `stringValue` function -
// for example `stringValue(vars, "accessKey")`.
func preConfigureCallback(resource.PropertyMap, shim.ResourceConfig) error {
	return nil
}

func computeDatabaseID(_ context.Context, state resource.PropertyMap) (resource.ID, error) {
	return resource.ID(state["name"].StringValue()), nil
}

//go:embed cmd/pulumi-resource-influxdb3/bridge-metadata.json
var metadata []byte

// Provider returns additional overlaid schema and metadata associated with the provider..
func Provider() tfbridge.ProviderInfo {
	prov := tfbridge.ProviderInfo{
		// Instantiate the Terraform provider
		P:                    pf.ShimProvider(influxdb3shim.NewProvider()),
		Name:                 "influxdb3",
		DisplayName:          "InfluxDB3",
		Publisher:            "komminarlabs",
		Version:              version.Version,
		LogoURL:              "https://avatars.githubusercontent.com/u/5713248?s=200&v=4",
		PluginDownloadURL:    "github://api.github.com/komminarlabs",
		Description:          "A Pulumi package for creating and managing InfluxDB V3 resources.",
		Keywords:             []string{"pulumi", "influxdb3", "category/database"},
		License:              "Apache-2.0",
		Homepage:             "https://www.influxdata.com",
		Repository:           "https://github.com/komminarlabs/pulumi-influxdb3",
		GitHubOrg:            "komminarlabs",
		MetadataInfo:         tfbridge.NewProviderMetadata(metadata),
		PreConfigureCallback: preConfigureCallback,
		Resources: map[string]*tfbridge.ResourceInfo{
			"influxdb3_database": {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Database"), ComputeID: computeDatabaseID},
			"influxdb3_token":    {Tok: tfbridge.MakeResource(mainPkg, mainMod, "Token")},
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{
			"influxdb3_database":  {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getDatabase")},
			"influxdb3_databases": {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getDatabases")},
			"influxdb3_token":     {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getToken")},
			"influxdb3_tokens":    {Tok: tfbridge.MakeDataSource(mainPkg, mainMod, "getTokens")},
		},
		JavaScript: &tfbridge.JavaScriptInfo{
			PackageName: "@komminarlabs/influxdb3",
			Dependencies: map[string]string{
				"@pulumi/pulumi": "^3.0.0",
			},
			DevDependencies: map[string]string{
				"@types/node": "^10.0.0",
				"@types/mime": "^2.0.0",
			},
		},
		Python: &tfbridge.PythonInfo{
			PackageName: "komminarlabs_influxdb3",
			Requires: map[string]string{
				"pulumi": ">=3.0.0,<4.0.0",
			},
		},
		Golang: &tfbridge.GolangInfo{
			ImportBasePath: path.Join(
				fmt.Sprintf("github.com/komminarlabs/pulumi-%[1]s/sdk/", mainPkg),
				tfbridge.GetModuleMajorVersion(version.Version),
				"go",
				mainPkg,
			),
			GenerateResourceContainerTypes: true,
		},
		CSharp: &tfbridge.CSharpInfo{
			RootNamespace: "KomminarLabs",
			PackageReferences: map[string]string{
				"Pulumi": "3.*",
			},
			Namespaces: map[string]string{
				"influxdb3": "InfluxDB3",
			},
		},
	}

	prov.MustComputeTokens(tokens.SingleModule("influxdb3_", mainMod,
		tokens.MakeStandard(mainPkg)))
	prov.MustApplyAutoAliases()
	prov.SetAutonaming(255, "-")

	return prov
}
