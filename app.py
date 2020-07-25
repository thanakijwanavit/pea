import boto3
from parallel_sync import wget
import sys, re, os

KEY = os.getenv('KEY')
PASS = os.getenv('PASS')


s3 = boto3.client(
    's3',
    aws_access_key_id=KEY,
    aws_secret_access_key=PASS
)
bucket = 'colab-pea'
filename = './10MB'
path = 'test.zip'
#s3.upload_file(filename, bucket, path)

urls = [
        'https://newsmaze.net/storage/new_proof_disk/Pea/Director1.7z',
        'https://newsmaze.net/storage/new_proof_disk/Pea/Director2.7z',
        'https://newsmaze.net/storage/new_proof_disk/Pea/Director3.7z',
        'https://newsmaze.net/storage/new_proof_disk/Pea/Director4.7z',
        'https://newsmaze.net/storage/new_proof_disk/Pea/Director5.7z',
        'https://newsmaze.net/storage/new_proof_disk/Pea/ELGBlockchanin.7z',
        'https://newsmaze.net/storage/new_proof_disk/Pea/EnergyProject.7z'
        ]
# wget.download('/tmp', urls)
# or a single file:
wget.download(os.path.join(os.getcwd(),'tmp'), urls, tries=10)

for url in urls:
  try:
    filename = re.search('\w*\.\w*$',url).group(0)
    path = os.path.join(os.getcwd(),'tmp', filename)
    #path = f'./tmp/{filename}'
    #wget.download(os.path.join(os.getcwd(),'tmp'), url, filenames=filename)
    print(f'uploading {filename} to s3')
    s3.upload_file(path , bucket, filename)
    #os.remove(path)



  except :
    print(f'error downloading file {url} error: {sys.exc_info()}')

