# AWS Lambda & EventBridge EC2 Automation

## Overview
I configured a scheduled EventBridge trigger for a Python Lambda function that uses Boto3 to request an EC2 instance stop.

**Services:** AWS Lambda, Amazon EventBridge, Amazon EC2  
**Technology:** Python, Boto3

## Implementation
- Configured a Lambda function and its execution settings.
- Set up an EventBridge rule with a recurring schedule.
- Linked the schedule to the Lambda function as a trigger.
- Updated the Python function with the designated EC2 instance identifier.
- Used the Boto3 EC2 client to request a stop action for that instance.
- Saved the function update in the Lambda console.

## Validation Scope
The screenshots confirm the scheduled trigger and the updated function code. They do not show a successful scheduled invocation or confirm that the instance stopped.

## Security Considerations
- Grant the Lambda execution role only the EC2 actions needed, scoped to the designated resources where supported.
- Avoid embedding fixed instance IDs or account identifiers when tags or configuration parameters are more maintainable.
- Use CloudWatch Logs and metrics to verify executions and inspect failures.
- Configure appropriate scheduling, retry, and alerting behavior.
- Use safe approval and exclusion rules before automating production instance shutdowns.


## Screenshots

### EventBridge Scheduled Trigger

![Lambda Eventbridge Trigger](screenshots/lambda-eventbridge-trigger.png)

### Lambda Python Code

![Lambda Boto3 Code](screenshots/lambda-boto3-code.png)

