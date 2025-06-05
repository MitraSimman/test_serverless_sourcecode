import json
import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    AWS Lambda function to perform addition operation
    Accepts two numbers and returns their sum
    """
    
    try:
        # Log the incoming event
        logger.info(f"Received event: {json.dumps(event)}")
        
        # Handle different event sources (API Gateway, direct invocation)
        if 'body' in event and event['body']:
            # API Gateway event
            if isinstance(event['body'], str):
                body = json.loads(event['body'])
            else:
                body = event['body']
        else:
            # Direct invocation
            body = event
        
        # Extract numbers from the request
        num1 = body.get('num1')
        num2 = body.get('num2')
        
        # Validate inputs
        if num1 is None or num2 is None:
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
                    'Access-Control-Allow-Headers': 'Content-Type'
                },
                'body': json.dumps({
                    'error': 'Missing required parameters',
                    'message': 'Please provide both num1 and num2 parameters'
                })
            }
        
        # Convert to float and perform addition
        try:
            number1 = float(num1)
            number2 = float(num2)
            result = number1 + number2
            
            logger.info(f"Addition operation: {number1} + {number2} = {result}")
            
            # Return successful response
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
                    'Access-Control-Allow-Headers': 'Content-Type'
                },
                'body': json.dumps({
                    'num1': number1,
                    'num2': number2,
                    'result': result,
                    'operation': 'addition',
                    'message': f'{number1} + {number2} = {result}'
                })
            }
            
        except ValueError as ve:
            logger.error(f"Value conversion error: {str(ve)}")
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({
                    'error': 'Invalid input',
                    'message': 'Both num1 and num2 must be valid numbers'
                })
            }
            
    except json.JSONDecodeError as je:
        logger.error(f"JSON decode error: {str(je)}")
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'error': 'Invalid JSON',
                'message': 'Request body must be valid JSON'
            })
        }
        
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'error': 'Internal server error',
                'message': 'An unexpected error occurred'
            })
        }