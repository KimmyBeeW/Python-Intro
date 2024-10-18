import requests
import re


class RequestGuard:
    def __init__(self, domain):
        self.domain = domain
        self.forbidden = self.parse_robots()

    def parse_robots(self):
        robots_obj = requests.get(f'{self.domain}/robots.txt')
        return re.findall(r"Disallow: (.*)", robots_obj.text)

    def can_follow_link(self, url):
        if not url.startswith(self.domain):
            return False
        for path in self.forbidden:
            if url.startswith(self.domain+path):
                return False
        return True

    def make_get_request(self, *args, **kwargs):
        if self.can_follow_link(args[0]):
            requests.get(args[0], **kwargs)
        else:
            return None
