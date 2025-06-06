
import json

def lambda_handler(event, context):
    # Simple addition program
    add_value = print(10 + 15)
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'message': 'Addition completed',
            'result': add_value
        }) 
    }