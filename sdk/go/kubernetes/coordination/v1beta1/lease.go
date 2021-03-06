// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package v1beta1

import (
	"context"
	"reflect"

	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v2/go/kubernetes/meta/v1"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Lease defines a lease concept.
type Lease struct {
	pulumi.CustomResourceState

	// APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
	ApiVersion pulumi.StringPtrOutput `pulumi:"apiVersion"`
	// Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
	Kind pulumi.StringPtrOutput `pulumi:"kind"`
	// More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
	Metadata metav1.ObjectMetaPtrOutput `pulumi:"metadata"`
	// Specification of the Lease. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
	Spec LeaseSpecPtrOutput `pulumi:"spec"`
}

// NewLease registers a new resource with the given unique name, arguments, and options.
func NewLease(ctx *pulumi.Context,
	name string, args *LeaseArgs, opts ...pulumi.ResourceOption) (*Lease, error) {
	if args == nil {
		args = &LeaseArgs{}
	}
	args.ApiVersion = pulumi.StringPtr("coordination.k8s.io/v1beta1")
	args.Kind = pulumi.StringPtr("Lease")
	aliases := pulumi.Aliases([]pulumi.Alias{
		{
			Type: pulumi.String("kubernetes:coordination.k8s.io/v1:Lease"),
		},
	})
	opts = append(opts, aliases)
	var resource Lease
	err := ctx.RegisterResource("kubernetes:coordination.k8s.io/v1beta1:Lease", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetLease gets an existing Lease resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLease(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *LeaseState, opts ...pulumi.ResourceOption) (*Lease, error) {
	var resource Lease
	err := ctx.ReadResource("kubernetes:coordination.k8s.io/v1beta1:Lease", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Lease resources.
type leaseState struct {
	// APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
	ApiVersion *string `pulumi:"apiVersion"`
	// Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
	Kind *string `pulumi:"kind"`
	// More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
	Metadata *metav1.ObjectMeta `pulumi:"metadata"`
	// Specification of the Lease. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
	Spec *LeaseSpec `pulumi:"spec"`
}

type LeaseState struct {
	// APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
	ApiVersion pulumi.StringPtrInput
	// Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
	Kind pulumi.StringPtrInput
	// More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
	Metadata metav1.ObjectMetaPtrInput
	// Specification of the Lease. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
	Spec LeaseSpecPtrInput
}

func (LeaseState) ElementType() reflect.Type {
	return reflect.TypeOf((*leaseState)(nil)).Elem()
}

type leaseArgs struct {
	// APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
	ApiVersion *string `pulumi:"apiVersion"`
	// Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
	Kind *string `pulumi:"kind"`
	// More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
	Metadata *metav1.ObjectMeta `pulumi:"metadata"`
	// Specification of the Lease. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
	Spec *LeaseSpec `pulumi:"spec"`
}

// The set of arguments for constructing a Lease resource.
type LeaseArgs struct {
	// APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
	ApiVersion pulumi.StringPtrInput
	// Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
	Kind pulumi.StringPtrInput
	// More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
	Metadata metav1.ObjectMetaPtrInput
	// Specification of the Lease. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
	Spec LeaseSpecPtrInput
}

func (LeaseArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*leaseArgs)(nil)).Elem()
}

type LeaseInput interface {
	pulumi.Input

	ToLeaseOutput() LeaseOutput
	ToLeaseOutputWithContext(ctx context.Context) LeaseOutput
}

func (Lease) ElementType() reflect.Type {
	return reflect.TypeOf((*Lease)(nil)).Elem()
}

func (i Lease) ToLeaseOutput() LeaseOutput {
	return i.ToLeaseOutputWithContext(context.Background())
}

func (i Lease) ToLeaseOutputWithContext(ctx context.Context) LeaseOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LeaseOutput)
}

type LeaseOutput struct {
	*pulumi.OutputState
}

func (LeaseOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LeaseOutput)(nil)).Elem()
}

func (o LeaseOutput) ToLeaseOutput() LeaseOutput {
	return o
}

func (o LeaseOutput) ToLeaseOutputWithContext(ctx context.Context) LeaseOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(LeaseOutput{})
}
