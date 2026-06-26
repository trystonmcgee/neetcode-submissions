class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_emails = set()  # Use a set immediately to avoid duplicates
        
        for email in emails:
            # 1. Split into local and domain parts once
            local, domain = email.split('@')
            
            # 2. Cut off everything after the '+' sign
            local = local.split('+')[0]
            
            # 3. Remove all dots
            local = local.replace('.', '')
            
            # 4. Store the cleaned email straight into the set
            unique_emails.add(f"{local}@{domain}")
            
        return len(unique_emails)
