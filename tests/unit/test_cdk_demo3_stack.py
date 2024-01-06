import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_demo3.cdk_demo3_stack import CdkDemo3Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_demo3/cdk_demo3_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkDemo3Stack(app, "cdk-demo3")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
