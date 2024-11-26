import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

AWS_REGION = "ap-southeast-1"
CHARSET = "UTF-8"
SENDER = "support@stayvillas.co"  # Replace with your verified SES email

def send_booking_enquiry_mail(recipient, subject, body_text, body_html):
    try:
        ses_client = boto3.client(
            'ses',
            aws_access_key_id='',
            aws_secret_access_key='',
            region_name='ap-southeast-1'
        )

        response = ses_client.send_email(
            Source=SENDER,
            Destination={'ToAddresses': [recipient]},
            Message={
                'Subject': {'Data': subject, 'Charset': CHARSET},
                'Body': {
                    'Text': {'Data': body_text, 'Charset': CHARSET},
                    'Html': {'Data': body_html, 'Charset': CHARSET},
                },
            }
        )
        return response['MessageId']
    except NoCredentialsError:
        raise Exception("AWS credentials are not configured.")
    except PartialCredentialsError:
        raise Exception("Incomplete AWS credentials configuration.")
    except Exception as e:
        raise Exception(f"Error sending email: {str(e)}")
