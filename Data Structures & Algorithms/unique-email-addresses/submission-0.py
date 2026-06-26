class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emails_lst = []

        for email in emails:
            email = email.split("@")

            first = ''.join(email[0])
            first = first.replace(".", "")
            email[0] = first

            first = first.split("+")
            email[0] = first[0]

            emails_lst.append(f"{email[0]}@{email[1]}")
            
        res = len(set(emails_lst))
        return res

