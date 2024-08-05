package main

import (
	"github.com/komminarlabs/pulumi-influxdb3/sdk/go/influxdb3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		signals, err := influxdb3.NewDatabase(ctx, "signals", &influxdb3.DatabaseArgs{
			Name:            pulumi.String("signals"),
			RetentionPeriod: pulumi.Int(604800),
		})
		if err != nil {
			return err
		}

		ctx.Export("databaseId", signals.ID())
		return nil
	})
}
