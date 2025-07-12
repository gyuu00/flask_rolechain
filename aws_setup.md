## AWS 설정 요약

1. EC2 인스턴스에 Role 부여: `web-role`
2. `web-role` 정책:
   - sts:AssumeRole → `flag-reader-role`
3. `flag-reader-role`은 다음 정책 포함:
   - s3:GetObject (for flag.txt in super-secret-bucket)

S3 버킷: `super-secret-bucket`
객체: `flag.txt`

EC2 메타데이터 접근 URL:
http://169.254.169.254/latest/meta-data/iam/security-credentials/web-role
