from aws_cdk import (
    aws_sns as sns,
    Stack,
    aws_sns_subscriptions as subscriptions
)
from constructs import Construct


class CdkDemo3Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        topic = sns.Topic(self, "DehSNStopic")

        # Add an email subscription
        topic.add_subscription(subscriptions.EmailSubscription("8619sachin@gmail.com"))
