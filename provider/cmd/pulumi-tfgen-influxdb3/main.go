package main

import (
	"github.com/pulumi/pulumi-terraform-bridge/pf/tfgen"

	influxdb3 "github.com/komminarlabs/pulumi-influxdb3/provider"
)

func main() {
	tfgen.Main("influxdb3", influxdb3.Provider())
}
