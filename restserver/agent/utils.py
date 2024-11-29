import subprocess
import boto3
import os
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# # Path to the PowerShell script
# POWERSHELL_SCRIPT_PATH = "C:/Users/krush/OneDrive/Desktop/Project-2024/stayvillas-api/scripts/amazonses.ps1"


# # Run the PowerShell script to set environment variables
# try:
#     subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", POWERSHELL_SCRIPT_PATH], check=True)
#     print("PowerShell script executed successfully.")
# except subprocess.CalledProcessError as e:
#     print(f"Error executing PowerShell script: {e}")
#     exit(1)

AWS_REGION = os.getenv('AWS_REGION_NAME', 'ap-southeast-1')  # Adjust as needed
CHARSET = "UTF-8"
SENDER = "support@stayvillas.co"  # Replace with your verified SES email

def send_reset_email(recipient, subject, body_text, body_html):
    """
    Utility function to send booking emails using Amazon SES.
    """
    try:
        ses_client = boto3.client(
            'ses',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
            region_name=AWS_REGION
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
