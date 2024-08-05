//go:build go || all
// +build go all

package examples

import (
	"path"
	"testing"

	"github.com/pulumi/pulumi/pkg/v3/testing/integration"
)

func getGoBaseOptions(t *testing.T) integration.ProgramTestOptions {
	base := getBaseOptions()
	baseGo := base.With(integration.ProgramTestOptions{
		Dependencies: []string{
			"github.com/komminarlabs/pulumi-influxdb3/sdk",
		},
	})

	return baseGo
}

func TestAccDatabaseGo(t *testing.T) {
	test := getGoBaseOptions(t).
		With(integration.ProgramTestOptions{
			Dir: path.Join(getCwd(t), "database", "go"),
		})
	integration.ProgramTest(t, &test)
}
