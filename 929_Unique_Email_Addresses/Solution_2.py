class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        def email_parser(email):
            local_name, domain_name = email.split('@')
            local_name = local_name.split('+')[0].replace('.',"")
            return local_name+'@'+domain_name
        
        return len(set(map(email_parser, emails)))