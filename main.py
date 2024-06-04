from iam_user_fetcher import IAMUserFetcher
from security_group_analyzer import SecurityGroupAnalyzer

def main():
    iam_fetcher = IAMUserFetcher()
    users = iam_fetcher.get_all_users()
    sg_analyzer = SecurityGroupAnalyzer()
    sgs = sg_analyzer.get_security_groups()

    invalid_entries = sg_analyzer.extract_sg_rules_descriptions(sgs)
    invalid_entries_filtered = sg_analyzer.filter_unmatched_sg_rules_iam(invalid_entries, users)

    for sg, list_inbounds in invalid_entries_filtered.items():
        print("Security Groups with IAM User Unmatched Ingress Rules: ", sg)
        for rule in list_inbounds:
            print("\tRule ", list_inbounds.index(rule) + 1, ": ", rule)
        

if __name__ == '__main__':
    main()
