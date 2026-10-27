# Project 6 - IAM Policy Auditor (boto3)

AWS IAM security auditor built with Python boto3.

**What I did:**
- Created IAM user audit-test-user
- Created group AuditorGroup with IAMReadOnlyAccess (best practice - policy on group, not user)
- Created and rotated access keys - left 1 active key

**Result from auditor:**
User: audit-test-user
  [HIGH] -> NO MFA (expected - console access disabled)
  [OK] Member of: AuditorGroup
  [INFO] Key Active

**Screenshots:** /screenshots folder

**Tools:** AWS CloudShell, IAM, boto3, Python 3.13
