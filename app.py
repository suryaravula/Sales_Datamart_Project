#!/usr/bin/env python3
import os

import aws_cdk as cdk

from sales_datamart_project.sales_datamart_project_stack import LambdaStack

app = cdk.App()
LambdaStack(app,"LambdaStack")

app.synth()
