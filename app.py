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

urls = ['https://newsmaze.net/storage/new_proof_disk/Pea/p.log',
        'https://newsmaze.net/storage/new_proof_disk/Pea/Manager1.zip',
        'https://newsmaze.net/storage/new_proof_disk/Pea/Manager2.zip',
        'https://newsmaze.net/storage/new_proof_disk/Pea/Main6.zip',
        'https://newsmaze.net/storage/new_proof_disk/Pea/00.7z',
        'https://newsmaze.net/storage/new_proof_disk/Pea/01.7z',
        'https://newsmaze.net/storage/new_proof_disk/Pea/02.7z',
        'https://newsmaze.net/storage/new_proof_disk/Pea/03.7z',
        'https://newsmaze.net/storage/new_proof_disk/Pea/04.7z',
        'https://newsmaze.net/storage/new_proof_disk/Pea/05.7z',
        'https://newsmaze.net/storage/new_proof_disk/Pea/2.7z',
        'https://newsmaze.net/storage/new_proof_disk/Pea/3.7z',
        'https://newsmaze.net/storage/new_proof_disk/Pea/4.7z',
        'https://newsmaze.net/storage/new_proof_disk/Pea/5.7z',
        'https://newsmaze.net/storage/new_proof_disk/Pea/CAN.7z',
        'https://newsmaze.net/storage/new_proof_disk/Pea/CovidDocs.7z',
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
for url in urls:
  try:
    filename = re.search('\w*\.\w*$',url).group(0)
    path = f'/tmp/{filename}'
    wget.download('/tmp', url, filenames=filename)
    s3.upload_file(path , bucket, filename)
    os.remove(path)



  except :
    print(f'error downloading file {url} error: {sys.exc_info()}')

