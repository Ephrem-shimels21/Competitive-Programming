class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visit_count = {}

        for domain in cpdomains:
            num, domain = domain.split()
            domain_list = domain.split(".")
            
            for i in range(len(domain_list)):
                dom  = ".".join(domain_list[i:])
                visit_count[dom] = int(num) + visit_count.get(dom, 0)
        ans = []

        for key in visit_count:
            count_domain = str(visit_count[key]) + " " + key
            ans.append(count_domain)
        
        return ans
        