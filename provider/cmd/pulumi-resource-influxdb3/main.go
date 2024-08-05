//go:generate go run ./generate.go

package main

import (
	"context"

	_ "embed"

	"github.com/pulumi/pulumi-terraform-bridge/pf/tfbridge"

	influxdb3 "github.com/komminarlabs/pulumi-influxdb3/provider"
)

//go:embed schema-embed.json
var pulumiSchema []byte

//go:embed bridge-metadata.json
var bridgeMetadata []byte

func main() {
	meta := tfbridge.ProviderMetadata{PackageSchema: pulumiSchema, BridgeMetadata: bridgeMetadata}
	tfbridge.Main(context.Background(), "influxdb3", influxdb3.Provider(), meta)
}
