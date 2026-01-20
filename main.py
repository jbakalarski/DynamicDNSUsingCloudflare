# Dynamic DNS using Cloudflare
# Author: Jędrzej Bakalarski
# Github: https://github.com/jedrzejme/DynamicDNSUsingCloudflare

# --- Import libraries ---
import os
from cloudflare import Cloudflare as cloudflare
import requests
import time
from dotenv import load_dotenv

# --- Read environment variables ---
load_dotenv()
interval = int(os.getenv('INTERVAL', '300'))
api_token = os.getenv('API_TOKEN')
zone_identifier = os.getenv('ZONE_IDENTIFIER')
domain = os.getenv('DOMAIN')
name = os.getenv('NAME')
ttl = int(os.getenv('TTL', '1'))
proxied = os.getenv('PROXIED', 'False').lower() in ('true', '1', 't')
comment = os.getenv('COMMENT', '')

# --- Function to get current public IP address ---
def get_public_ip():
    response = requests.get('https://api.ipify.org')
    return response.text.strip()

# --- Cloudflare API ---
# Initialize Cloudflare client
cf = cloudflare(api_token=api_token)

# Check if DNS record already exists
def get_dns_id():
    dns_list = cf.dns.records.list(zone_id=zone_identifier)

    domain_id = None
    for record in dns_list:
        if record.name == f"{name}.{domain}" and record.type == "A":
            domain_id = record.id
            break

    return domain_id

# --- Main logic ---
if get_dns_id() is None:
    cf.dns.records.create(
        zone_id=zone_identifier,
        type="A",
        name=name,
        content=get_public_ip(),
        ttl=ttl,
        proxied=proxied,
        comment=comment
    )

else:
    while True:
        cf.dns.records.update(
            zone_id=zone_identifier,
            dns_record_id=get_dns_id(),
            type="A",
            name=name,
            content=get_public_ip(),
            ttl=ttl,
            proxied=proxied,
            comment=comment
        )
        time.sleep(interval)