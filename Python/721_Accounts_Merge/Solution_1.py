class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        def build_graph(org_accounts):
            graph = collections.defaultdict(list)
            for index, account in enumerate(org_accounts):
                for email_index in range(1, len(account)):
                    graph[account[email_index]].append(index)
            return graph
            
        email_account_mapping = build_graph(accounts)
        visited_accounts = [False] * len(accounts)
        result = []
        
        def merge_account_dfs(i, emails):
            if visited_accounts[i]:
                return None
            visited_accounts[i] = True
            for index in range(1, len(accounts[i])):
                emails.add(accounts[i][index])
                for neighbor_index in email_account_mapping[accounts[i][index]]:
                    merge_account_dfs(neighbor_index, emails)
            
        for index, account in enumerate(accounts):
            if visited_accounts[index]:
                continue
            emails = set()
            merge_account_dfs(index, emails)
            result.append([account[0]] + sorted(emails))
            
        return result