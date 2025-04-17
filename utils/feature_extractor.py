import re
from urllib.parse import urlparse
def extract_features(url):
    parsed = urlparse(url)
    domain = parsed.netloc
    return {
        'url_length': len(url),
        'num_dots': url.count('.'),
        'num_digits': sum(c.isdigit() for c in url),
        'num_hyphens': url.count('-'),
        'has_https': int('https' in url),
        'has_at_symbol': int('@' in url),
        'has_ip': int(bool(re.search(r'\d+\.\d+\.\d+\.\d+', url))),
        'count_special': len(re.findall(r'[^\w]', url)),
        'domain_length': len(domain),
        'num_subdomains': domain.count('.') - 1
    }
