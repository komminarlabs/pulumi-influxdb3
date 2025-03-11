package main

import (
	influxdb3 "github.com/komminarlabs/pulumi-influxdb3/provider"

	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/pf/tfgen"
)

func main() {
	tfgen.Main("influxdb3", influxdb3.Provider())
}
