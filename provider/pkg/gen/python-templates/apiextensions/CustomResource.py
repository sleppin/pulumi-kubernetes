# *** WARNING: this file was generated by the Pulumi Kubernetes codegen tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings

import pulumi
import pulumi.runtime
from pulumi import ResourceOptions

from .. import _utilities, _tables


class CustomResource(pulumi.CustomResource):
    def __init__(self, resource_name, api_version, kind, spec=None, metadata=None, opts=None,
                 __name__=None, __opts__=None):
        """
        CustomResource represents an instance of a CustomResourceDefinition (CRD). For example, the
        CoreOS Prometheus operator exposes a CRD `monitoring.coreos.com/ServiceMonitor`; to
        instantiate this as a Pulumi resource, one could call `new CustomResource`, passing the
        `ServiceMonitor` resource definition as an argument.

        :param str resource_name: _Unique_ name used to register this resource with Pulumi.
        :param str api_version: The API version of the apiExtensions.CustomResource we
               wish to select, as specified by the CustomResourceDefinition that defines it on the
               API server.
        :param str kind: The kind of the apiextensions.CustomResource we wish to select,
               as specified by the CustomResourceDefinition that defines it on the API server.
        :param pulumi.Input[Any] spec: Specification of the CustomResource.
        :param Optional[pulumi.Input[Any]] metadata: Standard object metadata; More info:
               https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata.
        :param Optional[pulumi.ResourceOptions] opts: A bag of options that control this
               resource's behavior.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['apiVersion'] = api_version
        __props__['kind'] = kind
        __props__['spec'] = spec
        __props__['metadata'] = metadata

        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(version=_utilities.get_version()))

        super(CustomResource, self).__init__(
            f"kubernetes:{api_version}:{kind}",
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, api_version, kind, id, opts=None):
        """
        Get the state of an existing `CustomResource` resource, as identified by `id`.
        Typically this ID  is of the form [namespace]/[name]; if [namespace] is omitted,
        then (per Kubernetes convention) the ID becomes default/[name].

        Pulumi will keep track of this resource using `resource_name` as the Pulumi ID.

        :param str resource_name: _Unique_ name used to register this resource with Pulumi.
        :param str api_version: The API version of the apiExtensions.CustomResource we
               wish to select, as specified by the CustomResourceDefinition that defines it on the
               API server.
        :param str kind: The kind of the apiextensions.CustomResource we wish to select,
               as specified by the CustomResourceDefinition that defines it on the API server.
        :param pulumi.Input[str] id: An ID for the Kubernetes resource to retrieve.
               Takes the form <namespace>/<name> or <name>.
        :param Optional[pulumi.ResourceOptions] opts: A bag of options that control this
               resource's behavior.
        """

        opts = ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))
        return CustomResource(resource_name=resource_name, api_version=api_version, kind=kind, opts=opts)

    def translate_output_property(self, prop: str) -> str:
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop: str) -> str:
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
