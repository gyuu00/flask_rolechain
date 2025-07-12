# flask_rolechain

## 🎯 목표
Flask 서버의 취약점을 이용해 AWS 자격증명을 탈취하고, 
다른 Role을 Assume하여 S3의 flag.txt를 획득하세요.

## 🐍 주요 힌트
- `.py` 파일 업로드 → 서버에서 실행됨 (importlib RCE)
- EC2 메타데이터 서버 → 자격증명 획득
- `sts:AssumeRole`로 권한 상승

## 📁 업로드 예시
evil_template.py 참고

## 🏁 플래그 위치
S3 버킷: `super-secret-bucket`
파일: `flag.txt`
