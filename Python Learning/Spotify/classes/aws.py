import boto3
from PIL import Image
from dotenv import load_dotenv
from io import BytesIO
import os
import base64
load_dotenv()


def get_album_image_s3(artist: str, album: str):
    try:
        s3key = "artists/{0}/{1}.jpg".format(artist.lower(), album.lower())
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(os.getenv('S3_BUCKET'))
        image = bucket.Object(s3key)
        response = image.get()
        file_stream = response['Body']
        im = Image.open(file_stream)
        output = BytesIO()
        im.save(output, format='JPEG')
        return str(base64.b64encode(output.getvalue()))
    except:
        return None
