import boto3
from datetime import datetime, timezone

iam = boto3.client('iam')

print("=== IAM Policy Auditor - Project 6 ===\n")

users = iam.list_users()['Users']

for u in users:
    name = u['UserName']
    print(f"User: {name}")

    # Check MFA
    try:
        mfa = iam.list_mfa_devices(UserName=name)['MFADevices']
        if not mfa:
            print(f"  [HIGH] {name} -> NO MFA")
        else:
            print(f"  [OK] MFA enabled")
    except Exception as e:
        print(f"  [HIGH] {name} -> NO MFA")

    # Check Groups
    groups = iam.list_groups_for_user(UserName=name)['Groups']
    if groups:
        for g in groups:
            print(f"  [OK] Member of: {g['GroupName']}")
    else:
        print(f"  [WARN] No groups")

    # Check Access Keys
    keys = iam.list_access_keys(UserName=name)['AccessKeyMetadata']
    for k in keys:
        age = (datetime.now(timezone.utc) - k['CreateDate']).days
        print(f"  [INFO] Key {k['AccessKeyId'][:10]}... - {age} days old - {k['Status']}")

    print("")

print("Audit Complete - Ready for GitHub")
