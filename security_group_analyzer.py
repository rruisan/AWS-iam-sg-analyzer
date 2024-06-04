import boto3
from fuzzywuzzy import fuzz
from utils import is_similar_to_any


class SecurityGroupAnalyzer:
    def __init__(self):
        self.ec2_client = boto3.client('ec2')
    
    def get_security_groups(self):
        security_groups = []
        paginator = self.ec2_client.get_paginator('describe_security_groups')
        for page in paginator.paginate():
            for sg in page['SecurityGroups']:
                security_groups.append(sg)
        return security_groups


    def extract_sg_rules_descriptions(self, security_groups):
        sg_rules_description = {}
        for sg in security_groups:
            group_id = sg["GroupId"]
            descriptions = sg_rules_description.setdefault(group_id, [])
            for permission in sg["IpPermissions"]:
                descriptions.extend(ipv4_range["Description"] for ipv4_range in permission.get("IpRanges", []) if "Description" in ipv4_range)
                descriptions.extend(ipv6_range["Description"] for ipv6_range in permission.get("Ipv6Ranges", []) if "Description" in ipv6_range)
        return sg_rules_description


    def filter_unmatched_sg_rules_iam(self, sg_rules, users):
        filtered_dict = {}
        for key, values in sg_rules.items():
            filtered_values = [value for value in values if not is_similar_to_any(value, users)]
            if filtered_values:
                filtered_dict[key] = filtered_values
        return filtered_dict
