// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package v1beta1

import (
	"reflect"

	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v2/go/kubernetes/meta/v1"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Deployment enables declarative updates for Pods and ReplicaSets.
//
// This resource waits until its status is ready before registering success
// for create/update, and populating output properties from the current state of the resource.
// The following conditions are used to determine whether the resource creation has
// succeeded or failed:
//
// 1. The Deployment has begun to be updated by the Deployment controller. If the current
//    generation of the Deployment is > 1, then this means that the current generation must
//    be different from the generation reported by the last outputs.
// 2. There exists a ReplicaSet whose revision is equal to the current revision of the
//    Deployment.
// 3. The Deployment's '.status.conditions' has a status of type 'Available' whose 'status'
//    member is set to 'True'.
// 4. If the Deployment has generation > 1, then '.status.conditions' has a status of type
//    'Progressing', whose 'status' member is set to 'True', and whose 'reason' is
//    'NewReplicaSetAvailable'. For generation <= 1, this status field does not exist,
//    because it doesn't do a rollout (i.e., it simply creates the Deployment and
//    corresponding ReplicaSet), and therefore there is no rollout to mark as 'Progressing'.
//
// If the Deployment has not reached a Ready state after 10 minutes, it will
// time out and mark the resource update as Failed. You can override the default timeout value
// by setting the 'customTimeouts' option on the resource.
type Deployment struct {
	pulumi.CustomResourceState

	// APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
	ApiVersion pulumi.StringPtrOutput `pulumi:"apiVersion"`
	// Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
	Kind pulumi.StringPtrOutput `pulumi:"kind"`
	// Standard object metadata.
	Metadata metav1.ObjectMetaPtrOutput `pulumi:"metadata"`
	// Specification of the desired behavior of the Deployment.
	Spec DeploymentSpecPtrOutput `pulumi:"spec"`
	// Most recently observed status of the Deployment.
	Status DeploymentStatusPtrOutput `pulumi:"status"`
}

// NewDeployment registers a new resource with the given unique name, arguments, and options.
func NewDeployment(ctx *pulumi.Context,
	name string, args *DeploymentArgs, opts ...pulumi.ResourceOption) (*Deployment, error) {
	if args == nil {
		args = &DeploymentArgs{}
	}
	args.ApiVersion = pulumi.StringPtr("extensions/v1beta1")
	args.Kind = pulumi.StringPtr("Deployment")
	aliases := pulumi.Aliases([]pulumi.Alias{
		{
			Type: pulumi.String("kubernetes:apps/v1:Deployment"),
		},
		{
			Type: pulumi.String("kubernetes:apps/v1beta1:Deployment"),
		},
		{
			Type: pulumi.String("kubernetes:apps/v1beta2:Deployment"),
		},
	})
	opts = append(opts, aliases)
	var resource Deployment
	err := ctx.RegisterResource("kubernetes:extensions/v1beta1:Deployment", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDeployment gets an existing Deployment resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDeployment(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DeploymentState, opts ...pulumi.ResourceOption) (*Deployment, error) {
	var resource Deployment
	err := ctx.ReadResource("kubernetes:extensions/v1beta1:Deployment", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Deployment resources.
type deploymentState struct {
	// APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
	ApiVersion *string `pulumi:"apiVersion"`
	// Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
	Kind *string `pulumi:"kind"`
	// Standard object metadata.
	Metadata *metav1.ObjectMeta `pulumi:"metadata"`
	// Specification of the desired behavior of the Deployment.
	Spec *DeploymentSpec `pulumi:"spec"`
	// Most recently observed status of the Deployment.
	Status *DeploymentStatus `pulumi:"status"`
}

type DeploymentState struct {
	// APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
	ApiVersion pulumi.StringPtrInput
	// Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
	Kind pulumi.StringPtrInput
	// Standard object metadata.
	Metadata metav1.ObjectMetaPtrInput
	// Specification of the desired behavior of the Deployment.
	Spec DeploymentSpecPtrInput
	// Most recently observed status of the Deployment.
	Status DeploymentStatusPtrInput
}

func (DeploymentState) ElementType() reflect.Type {
	return reflect.TypeOf((*deploymentState)(nil)).Elem()
}

type deploymentArgs struct {
	// APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
	ApiVersion *string `pulumi:"apiVersion"`
	// Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
	Kind *string `pulumi:"kind"`
	// Standard object metadata.
	Metadata *metav1.ObjectMeta `pulumi:"metadata"`
	// Specification of the desired behavior of the Deployment.
	Spec *DeploymentSpec `pulumi:"spec"`
}

// The set of arguments for constructing a Deployment resource.
type DeploymentArgs struct {
	// APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
	ApiVersion pulumi.StringPtrInput
	// Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
	Kind pulumi.StringPtrInput
	// Standard object metadata.
	Metadata metav1.ObjectMetaPtrInput
	// Specification of the desired behavior of the Deployment.
	Spec DeploymentSpecPtrInput
}

func (DeploymentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*deploymentArgs)(nil)).Elem()
}