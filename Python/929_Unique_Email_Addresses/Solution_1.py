class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        
        for email in emails:
            local_domain_names = email.split('@')
            unique_email = local_domain_names[0].split('+')[0].replace('.','') + '@' + local_domain_names[1]
            unique_emails.add(unique_email)
        
        return len(unique_emails)