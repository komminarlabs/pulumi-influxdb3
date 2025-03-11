//go:generate go run ./generate.go

package main

import (
	"context"
	_ "embed"

	influxdb3 "github.com/komminarlabs/pulumi-influxdb3/provider"

	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/pf/tfbridge"
)

//go:embed schema.json
var pulumiSchema []byte

func main() {
	tfbridge.Main(context.Background(), "influxdb3", influxdb3.Provider(),
		tfbridge.ProviderMetadata{PackageSchema: pulumiSchema})
}
