// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace KomminarLabs.InfluxDB3.Inputs
{

    public sealed class TokenPermissionGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The action the database token permission allows. Valid values are `read` or `write`.
        /// </summary>
        [Input("action", required: true)]
        public Input<string> Action { get; set; } = null!;

        /// <summary>
        /// The resource the database token permission applies to. `*` refers to all databases.
        /// </summary>
        [Input("resource", required: true)]
        public Input<string> Resource { get; set; } = null!;

        public TokenPermissionGetArgs()
        {
        }
        public static new TokenPermissionGetArgs Empty => new TokenPermissionGetArgs();
    }
}
