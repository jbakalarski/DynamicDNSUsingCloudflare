# Dynamic DNS using Cloudflare
# Author: Jędrzej Bakalarski
# Github: https://github.com/jedrzejme/DynamicDNSUsingCloudflare

# --- Import libraries ---
import os
from cloudflare import Cloudflare as cloudflare
import requests
import time
import logging
import sys
from dotenv import load_dotenv

# --- Read environment variables ---
load_dotenv()
record_type = os.getenv('RECORD_TYPE', 'A')
interval = int(os.getenv('INTERVAL', '300'))
api_token = os.getenv('API_TOKEN')
zone_identifier = os.getenv('ZONE_IDENTIFIER')
domain = os.getenv('DOMAIN')
name = os.getenv('NAME')
ttl = int(os.getenv('TTL', '1'))
proxied = os.getenv('PROXIED', 'False').lower() in ('true', '1', 't')
comment = os.getenv('COMMENT', '')

# --- Configure logging ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

logger = logging.getLogger(__name__)

# --- Function to get current public IP address ---
def get_public_ip():
    try:
        if record_type == 'A':
            response = requests.get('https://api.ipify.org')
        elif record_type == 'AAAA':
            response = requests.get('https://api6.ipify.org')
        else:
            raise ValueError(f"Unsupported record type: {record_type}")
        
    except Exception as e:
        logger.error(f"Failed to get public IP address: {e}")
        raise

    logger.info(f"Current public IP address: {response.text.strip()}")
    return response.text.strip()

# --- Cloudflare API ---
# Initialize Cloudflare client
try:
    cf = cloudflare(api_token=api_token)
    logger.info("Successfully initialized Cloudflare client")
except Exception as e:
    logger.error(f"Failed to initialize Cloudflare client: {e}")
    raise

# Check if DNS record already exists
def get_dns_id():
    try:
        logger.debug(f"Fetching DNS records for zone: {zone_identifier}")
        dns_list = cf.dns.records.list(zone_id=zone_identifier)
        
    except Exception as e:
        logger.error(f"Failed to fetch DNS records from Cloudflare API: {e}")
        logger.error("Check your API token, zone identifier, and network connection")
        raise
    
    dns_id = None
    
    for record in dns_list:
        if record.name == f"{name}.{domain}" and record.type == record_type:
            dns_id = record.id
            logger.debug(f"Found existing DNS record: {record.name} (ID: {record.id}, Type: {record.type})")
    
    if dns_id is None:
        logger.info(f"No existing DNS record found for '{name}.{domain}' with type '{record_type}'")
    else:
        logger.info(f"Found DNS record ID: {dns_id} for '{name}.{domain}'")
    
    return dns_id

# --- Main logic ---
# Create DNS record if it doesn't exist
if get_dns_id() is None:
    try:
        logger.info(f"Creating new DNS record: {name}.{domain} ({record_type})")
        current_ip = get_public_ip()
        result = cf.dns.records.create(
            zone_id=zone_identifier,
            type=record_type,
            name=name,
            content=current_ip,
            ttl=ttl,
            proxied=proxied,
            comment=comment
        )
        logger.info(f"Successfully created DNS record: {name}.{domain} -> {current_ip}")
        logger.debug(f"Record details: {result}")
    except Exception as e:
        logger.error(f"Failed to create DNS record: {e}")
        raise

# Update DNS record in a loop
else:
    logger.info(f"DNS record already exists, starting update loop with interval: {interval} seconds")
    while True:
        try:
            current_ip = get_public_ip()
            dns_id = get_dns_id()
            logger.info(f"Updating DNS record {name}.{domain} (ID: {dns_id}) -> {current_ip}")
            
            result = cf.dns.records.update(
                zone_id=zone_identifier,
                dns_record_id=dns_id,
                type=record_type,
                name=name,
                content=current_ip,
                ttl=ttl,
                proxied=proxied,
                comment=comment
            )
            
            logger.info(f"Successfully updated DNS record: {name}.{domain} -> {current_ip}")
            logger.debug(f"Update result: {result}")
            
        except Exception as e:
            logger.error(f"Failed to update DNS record: {e}")
        
        logger.info(f"Waiting {interval} seconds until next update...")
        time.sleep(interval)