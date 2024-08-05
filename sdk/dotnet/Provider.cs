// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace KomminarLabs.InfluxDB3
{
    /// <summary>
    /// The provider type for the influxdb3 package. By default, resources use package-wide configuration
    /// settings, however an explicit `Provider` instance may be created and passed during resource
    /// construction to achieve fine-grained programmatic control over provider settings. See the
    /// [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
    /// </summary>
    [InfluxDB3ResourceType("pulumi:providers:influxdb3")]
    public partial class Provider : global::Pulumi.ProviderResource
    {
        /// <summary>
        /// The ID of the account that the cluster belongs to
        /// </summary>
        [Output("accountId")]
        public Output<string?> AccountId { get; private set; } = null!;

        /// <summary>
        /// The ID of the cluster that you want to manage
        /// </summary>
        [Output("clusterId")]
        public Output<string?> ClusterId { get; private set; } = null!;

        /// <summary>
        /// The InfluxDB management token
        /// </summary>
        [Output("token")]
        public Output<string?> Token { get; private set; } = null!;

        /// <summary>
        /// The InfluxDB Cloud Dedicated Management API URL
        /// </summary>
        [Output("url")]
        public Output<string?> Url { get; private set; } = null!;


        /// <summary>
        /// Create a Provider resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Provider(string name, ProviderArgs? args = null, CustomResourceOptions? options = null)
            : base("influxdb3", name, args ?? new ProviderArgs(), MakeResourceOptions(options, ""))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/komminarlabs",
                AdditionalSecretOutputs =
                {
                    "accountId",
                    "clusterId",
                    "token",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
    }

    public sealed class ProviderArgs : global::Pulumi.ResourceArgs
    {
        [Input("accountId")]
        private Input<string>? _accountId;

        /// <summary>
        /// The ID of the account that the cluster belongs to
        /// </summary>
        public Input<string>? AccountId
        {
            get => _accountId;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _accountId = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        [Input("clusterId")]
        private Input<string>? _clusterId;

        /// <summary>
        /// The ID of the cluster that you want to manage
        /// </summary>
        public Input<string>? ClusterId
        {
            get => _clusterId;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _clusterId = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        [Input("token")]
        private Input<string>? _token;

        /// <summary>
        /// The InfluxDB management token
        /// </summary>
        public Input<string>? Token
        {
            get => _token;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _token = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// The InfluxDB Cloud Dedicated Management API URL
        /// </summary>
        [Input("url")]
        public Input<string>? Url { get; set; }

        public ProviderArgs()
        {
        }
        public static new ProviderArgs Empty => new ProviderArgs();
    }
}
