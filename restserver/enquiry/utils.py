import os
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError


AWS_REGION = os.getenv('AWS_REGION_NAME', 'ap-southeast-1')
AWS_KEY_ID = os.getenv('AWS_SECRET_KEY_ID', 'AKIAXEVXYOKKUVONZJEZ')
AWS_SECRET_ACCESS_KEY = os.getenv(
    'AWS_SECRET_ACCESS_KEY',
    'CjH5AEcDVIBCrrXGj25kF3fnOkLf1a6E1FX12luI'
)

CHARSET = "UTF-8"
SENDER = "support@stayvillas.co"  # Replace with your verified SES email


def send_booking_enquiry_mail(recipient, subject, body_text, body_html):
    try:
        ses_client = boto3.client(
            'ses',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
            region_name=AWS_REGION
        )

        response = ses_client.send_email(
            Source=SENDER,
            Destination={'ToAddresses': [SENDER]},
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
