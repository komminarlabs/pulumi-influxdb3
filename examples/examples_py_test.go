//go:build python || all
// +build python all

package examples

import (
	"path"
	"path/filepath"
	"testing"

	"github.com/pulumi/pulumi/pkg/v3/testing/integration"
)

func getPythonBaseOptions(t *testing.T) integration.ProgramTestOptions {
	base := getBaseOptions()
	basePython := base.With(integration.ProgramTestOptions{
		Dependencies: []string{
			filepath.Join("..", "sdk", "python", "bin"),
		},
	})

	return basePython
}

func TestAccDatabasePython(t *testing.T) {
	test := getPythonBaseOptions(t).
		With(integration.ProgramTestOptions{
			Dir: path.Join(getCwd(t), "database", "python"),
		})
	integration.ProgramTest(t, &test)
}
