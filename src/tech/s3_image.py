import io

import boto3

access_key = 'AKIAXLEOIF4EZ37R4W6B'
secret_key = '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'
bucket_name ='devops-training-504956989193'
s3 = boto3.resource('s3', aws_access_key_id=access_key,
                    aws_secret_access_key=secret_key)

def get_image_from_s3(asset_id: str) -> io.BytesIO | None:
    try:
        response = s3.get_object(Bucket=s3.Bucket(bucket_name), Key='group3/store_first/' +  'image/' + asset_id)
        image_file = io.BytesIO(response['Body'].read())

        image_file.seek(0)

        return image_file

    except Exception as e:
        logger.info(f'Error getting object from S3 bucket {bucket_name}: {e}')
        return None