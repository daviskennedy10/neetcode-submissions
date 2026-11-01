class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        n = len(emails)
        count = set()
        
        for i in range(n):
            email = emails[i]
            local, domain = email.split("@")
            print(local)
            print(domain)
            if "+" in local:
                use,leave = local.split("+",1)
                final_use = use.replace(".","")
                new_email = final_use + "@" + domain
                count.add(new_email)
            elif "." in local:
                final_use = local.replace(".","")
                new_email = final_use + "@" + domain
                count.add(new_email)
            else:
                count.add(email)
        print(count)
        return len(count)

