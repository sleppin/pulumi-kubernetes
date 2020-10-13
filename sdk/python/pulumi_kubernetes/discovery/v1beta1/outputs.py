# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from ... import _utilities, _tables
from . import outputs
from ... import core as _core
from ... import meta as _meta

__all__ = [
    'Endpoint',
    'EndpointConditions',
    'EndpointPort',
    'EndpointSlice',
]

@pulumi.output_type
class Endpoint(dict):
    """
    Endpoint represents a single logical "backend" implementing a service.
    """
    def __init__(__self__, *,
                 addresses: Sequence[str],
                 conditions: Optional['outputs.EndpointConditions'] = None,
                 hostname: Optional[str] = None,
                 target_ref: Optional['_core.v1.outputs.ObjectReference'] = None,
                 topology: Optional[Mapping[str, str]] = None):
        """
        Endpoint represents a single logical "backend" implementing a service.
        :param Sequence[str] addresses: addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. Consumers must handle different types of addresses in the context of their own capabilities. This must contain at least one address but no more than 100.
        :param 'EndpointConditionsArgs' conditions: conditions contains information about the current status of the endpoint.
        :param str hostname: hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname should be considered fungible (e.g. multiple A values in DNS). Must be lowercase and pass DNS Label (RFC 1123) validation.
        :param '_core.v1.ObjectReferenceArgs' target_ref: targetRef is a reference to a Kubernetes object that represents this endpoint.
        :param Mapping[str, str] topology: topology contains arbitrary topology information associated with the endpoint. These key/value pairs must conform with the label format. https://kubernetes.io/docs/concepts/overview/working-with-objects/labels Topology may include a maximum of 16 key/value pairs. This includes, but is not limited to the following well known keys: * kubernetes.io/hostname: the value indicates the hostname of the node
                 where the endpoint is located. This should match the corresponding
                 node label.
               * topology.kubernetes.io/zone: the value indicates the zone where the
                 endpoint is located. This should match the corresponding node label.
               * topology.kubernetes.io/region: the value indicates the region where the
                 endpoint is located. This should match the corresponding node label.
        """
        pulumi.set(__self__, "addresses", addresses)
        if conditions is not None:
            pulumi.set(__self__, "conditions", conditions)
        if hostname is not None:
            pulumi.set(__self__, "hostname", hostname)
        if target_ref is not None:
            pulumi.set(__self__, "target_ref", target_ref)
        if topology is not None:
            pulumi.set(__self__, "topology", topology)

    @property
    @pulumi.getter
    def addresses(self) -> Sequence[str]:
        """
        addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. Consumers must handle different types of addresses in the context of their own capabilities. This must contain at least one address but no more than 100.
        """
        return pulumi.get(self, "addresses")

    @property
    @pulumi.getter
    def conditions(self) -> Optional['outputs.EndpointConditions']:
        """
        conditions contains information about the current status of the endpoint.
        """
        return pulumi.get(self, "conditions")

    @property
    @pulumi.getter
    def hostname(self) -> Optional[str]:
        """
        hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname should be considered fungible (e.g. multiple A values in DNS). Must be lowercase and pass DNS Label (RFC 1123) validation.
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter(name="targetRef")
    def target_ref(self) -> Optional['_core.v1.outputs.ObjectReference']:
        """
        targetRef is a reference to a Kubernetes object that represents this endpoint.
        """
        return pulumi.get(self, "target_ref")

    @property
    @pulumi.getter
    def topology(self) -> Optional[Mapping[str, str]]:
        """
        topology contains arbitrary topology information associated with the endpoint. These key/value pairs must conform with the label format. https://kubernetes.io/docs/concepts/overview/working-with-objects/labels Topology may include a maximum of 16 key/value pairs. This includes, but is not limited to the following well known keys: * kubernetes.io/hostname: the value indicates the hostname of the node
          where the endpoint is located. This should match the corresponding
          node label.
        * topology.kubernetes.io/zone: the value indicates the zone where the
          endpoint is located. This should match the corresponding node label.
        * topology.kubernetes.io/region: the value indicates the region where the
          endpoint is located. This should match the corresponding node label.
        """
        return pulumi.get(self, "topology")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class EndpointConditions(dict):
    """
    EndpointConditions represents the current condition of an endpoint.
    """
    def __init__(__self__, *,
                 ready: Optional[bool] = None):
        """
        EndpointConditions represents the current condition of an endpoint.
        :param bool ready: ready indicates that this endpoint is prepared to receive traffic, according to whatever system is managing the endpoint. A nil value indicates an unknown state. In most cases consumers should interpret this unknown state as ready.
        """
        if ready is not None:
            pulumi.set(__self__, "ready", ready)

    @property
    @pulumi.getter
    def ready(self) -> Optional[bool]:
        """
        ready indicates that this endpoint is prepared to receive traffic, according to whatever system is managing the endpoint. A nil value indicates an unknown state. In most cases consumers should interpret this unknown state as ready.
        """
        return pulumi.get(self, "ready")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class EndpointPort(dict):
    """
    EndpointPort represents a Port used by an EndpointSlice
    """
    def __init__(__self__, *,
                 app_protocol: Optional[str] = None,
                 name: Optional[str] = None,
                 port: Optional[int] = None,
                 protocol: Optional[str] = None):
        """
        EndpointPort represents a Port used by an EndpointSlice
        :param str app_protocol: The application protocol for this port. This field follows standard Kubernetes label syntax. Un-prefixed names are reserved for IANA standard service names (as per RFC-6335 and http://www.iana.org/assignments/service-names). Non-standard protocols should use prefixed names such as mycompany.com/my-custom-protocol.
        :param str name: The name of this port. All ports in an EndpointSlice must have a unique name. If the EndpointSlice is dervied from a Kubernetes service, this corresponds to the Service.ports[].name. Name must either be an empty string or pass DNS_LABEL validation: * must be no more than 63 characters long. * must consist of lower case alphanumeric characters or '-'. * must start and end with an alphanumeric character. Default is empty string.
        :param int port: The port number of the endpoint. If this is not specified, ports are not restricted and must be interpreted in the context of the specific consumer.
        :param str protocol: The IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP.
        """
        if app_protocol is not None:
            pulumi.set(__self__, "app_protocol", app_protocol)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)

    @property
    @pulumi.getter(name="appProtocol")
    def app_protocol(self) -> Optional[str]:
        """
        The application protocol for this port. This field follows standard Kubernetes label syntax. Un-prefixed names are reserved for IANA standard service names (as per RFC-6335 and http://www.iana.org/assignments/service-names). Non-standard protocols should use prefixed names such as mycompany.com/my-custom-protocol.
        """
        return pulumi.get(self, "app_protocol")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of this port. All ports in an EndpointSlice must have a unique name. If the EndpointSlice is dervied from a Kubernetes service, this corresponds to the Service.ports[].name. Name must either be an empty string or pass DNS_LABEL validation: * must be no more than 63 characters long. * must consist of lower case alphanumeric characters or '-'. * must start and end with an alphanumeric character. Default is empty string.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def port(self) -> Optional[int]:
        """
        The port number of the endpoint. If this is not specified, ports are not restricted and must be interpreted in the context of the specific consumer.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def protocol(self) -> Optional[str]:
        """
        The IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP.
        """
        return pulumi.get(self, "protocol")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class EndpointSlice(dict):
    """
    EndpointSlice represents a subset of the endpoints that implement a service. For a given service there may be multiple EndpointSlice objects, selected by labels, which must be joined to produce the full set of endpoints.
    """
    def __init__(__self__, *,
                 address_type: str,
                 endpoints: Sequence['outputs.Endpoint'],
                 api_version: Optional[str] = None,
                 kind: Optional[str] = None,
                 metadata: Optional['_meta.v1.outputs.ObjectMeta'] = None,
                 ports: Optional[Sequence['outputs.EndpointPort']] = None):
        """
        EndpointSlice represents a subset of the endpoints that implement a service. For a given service there may be multiple EndpointSlice objects, selected by labels, which must be joined to produce the full set of endpoints.
        :param str address_type: addressType specifies the type of address carried by this EndpointSlice. All addresses in this slice must be the same type. This field is immutable after creation. The following address types are currently supported: * IPv4: Represents an IPv4 Address. * IPv6: Represents an IPv6 Address. * FQDN: Represents a Fully Qualified Domain Name.
        :param Sequence['EndpointArgs'] endpoints: endpoints is a list of unique endpoints in this slice. Each slice may include a maximum of 1000 endpoints.
        :param str api_version: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        :param str kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        :param '_meta.v1.ObjectMetaArgs' metadata: Standard object's metadata.
        :param Sequence['EndpointPortArgs'] ports: ports specifies the list of network ports exposed by each endpoint in this slice. Each port must have a unique name. When ports is empty, it indicates that there are no defined ports. When a port is defined with a nil port value, it indicates "all ports". Each slice may include a maximum of 100 ports.
        """
        pulumi.set(__self__, "address_type", address_type)
        pulumi.set(__self__, "endpoints", endpoints)
        if api_version is not None:
            pulumi.set(__self__, "api_version", 'discovery.k8s.io/v1beta1')
        if kind is not None:
            pulumi.set(__self__, "kind", 'EndpointSlice')
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if ports is not None:
            pulumi.set(__self__, "ports", ports)

    @property
    @pulumi.getter(name="addressType")
    def address_type(self) -> str:
        """
        addressType specifies the type of address carried by this EndpointSlice. All addresses in this slice must be the same type. This field is immutable after creation. The following address types are currently supported: * IPv4: Represents an IPv4 Address. * IPv6: Represents an IPv6 Address. * FQDN: Represents a Fully Qualified Domain Name.
        """
        return pulumi.get(self, "address_type")

    @property
    @pulumi.getter
    def endpoints(self) -> Sequence['outputs.Endpoint']:
        """
        endpoints is a list of unique endpoints in this slice. Each slice may include a maximum of 1000 endpoints.
        """
        return pulumi.get(self, "endpoints")

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[str]:
        """
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        """
        return pulumi.get(self, "api_version")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def metadata(self) -> Optional['_meta.v1.outputs.ObjectMeta']:
        """
        Standard object's metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def ports(self) -> Optional[Sequence['outputs.EndpointPort']]:
        """
        ports specifies the list of network ports exposed by each endpoint in this slice. Each port must have a unique name. When ports is empty, it indicates that there are no defined ports. When a port is defined with a nil port value, it indicates "all ports". Each slice may include a maximum of 100 ports.
        """
        return pulumi.get(self, "ports")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


