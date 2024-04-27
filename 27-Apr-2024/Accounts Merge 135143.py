# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def find(account):
            if parent[account] != account:
                parent[account] = find(parent[account])
            return parent[account]
        
        no_accounts = len(accounts)
        parent = list(range(no_accounts))
        email_account = {}

        for idx, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_account:
                    parent[find(idx)] = find(email_account[email])
                else:
                    email_account[email] = idx
        
        email_parent = defaultdict(set)

        for idx, account in enumerate(accounts):
            root = find(idx)  
            for email in account[1:]:
                email_parent[root].add(email)
        
        merged_accounts = []
        for parent_idx, emails in email_parent.items():
            sorted_emails = sorted(list(emails))  
            account_name = [accounts[parent_idx][0]]  
            merged = account_name + sorted_emails
            merged_accounts.append(merged)
        
        return merged_accounts
