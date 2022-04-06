# Text-Extractor-img
Inorder to extract text from Images, use both the Parent and Child lambda functions to generate text output.

#Stage 1

Configure the Source S3 bucket into which images to be processed are added. Then, deploy the parent lambda function which returns the 'JobId' of the textraction process.
Note that lambda has a Resource policy to be invoked by S3 and Execution policy to invoke child lambda, use textract and create CloudWatch Logs.

#Stage 2

Deploy the child lambda function to return the output of textraction process. This lambda is invoked asynchronously and the Event JobId is passed as Payload. Configure Lambda with execution policy to push Logs and call Textract service of AWS.

#Stage 3

Lambda will retun the response of textraction process. Use Result_extraction file in your local machine to extract the text from the response.

#Optional

We can also use SNS notification to a Lambda function to pass the JobId to the child Lambda function. This will also be an asynchronous Invocation.
