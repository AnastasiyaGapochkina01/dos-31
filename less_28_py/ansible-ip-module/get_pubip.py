#!/usr/bin/python

DOCUMENTATION = '''
---
module: get_pubip
short_description: Retrieve public IP from various services
version_added: '1.0'
options:
  api_service:
    description: Service to use for IP detection
    default: 'ipify'
    choices: ['ipify', '2ip', 'ipme', 'custom']
    type: str
  api_url:
    description: Custom API URL (used only with api_service=custom)
    default: ''
    type: str
author:
  - anestesia (anastasiya.gapochkina01@yandex.ru)
'''

EXAMPLES = '''
# Get public IP from ipify (default)
- name: Get public ip from ipify
  get_pubip:

# Get public IP from 2ip.ru
- name: Get public ip from 2ip
  get_pubip:
    api_service: 2ip

# Get public IP from ip.me
- name: Get public ip from ip.me
  get_pubip:
    api_service: ipme

# Use custom API service
- name: Get public ip from custom service
  get_pubip:
    api_service: custom
    api_url: https://api.myip.com
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import fetch_url
from ansible.module_utils.common.text.converters import to_text
import json
import re

class PubIpFacts:
    def __init__(self, module):
        self.module = module
        self.api_service = module.params['api_service']
        self.api_url = module.params['api_url']

        # URL для получения IP
        self.service_urls = {
            'ipify': 'https://api.ipify.org?format=json',
            '2ip': 'https://2ip.io',  # Альтернативный сервис от 2ip
            'ipme': 'https://ifconfig.me/ip',  # Альтернатива ip.me
            'custom': self.api_url
        }

    def run(self):
        result = {'public_ip': None, 'service_used': self.api_service}

        # выбираем url на основе того, какой метод в task
        url = self.service_urls.get(self.api_service)

        if not url:
            self.module.fail_json(msg=f"Unsupported API service: {self.api_service}")

        if self.api_service == 'custom' and not self.api_url:
            self.module.fail_json(msg="Custom API service requires api_url parameter")

        # заголовки, чтобы избежать блокировки
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        response, info = fetch_url(
            module=self.module,
            url=url,
            headers=headers,
            force=True,
            timeout=30
        )

        if info['status'] != 200:
            # Если сервис недоступен, пробуем альтернативные варианты
            if self.api_service == '2ip':
                self.module.warn("2ip service unavailable, trying alternative")
                return self.try_alternative_services()
            else:
                self.module.fail_json(msg=f"API request failed with status {info['status']}")

        try:
            content = to_text(response.read()).strip()

            if self.api_service == 'ipify':
                # ipify returns JSON
                data = json.loads(content)
                result['public_ip'] = data.get('ip')
            else:
                ip_match = re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', content)
                if ip_match:
                    result['public_ip'] = content
                else:
                    ip_match = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', content)
                    if ip_match:
                        result['public_ip'] = ip_match.group(0)

            if not result['public_ip']:
                self.module.fail_json(msg=f"Could not extract IP address from response: {content}")

            return result

        except Exception as e:
            self.module.fail_json(msg=f"Failed to parse response: {str(e)}")

    def try_alternative_services(self):
        """Пробуем альтернативные сервисы, если основной недоступен"""
        alternatives = [
            'https://api.ipify.org?format=json',
            'https://ifconfig.me/ip',
            'https://ident.me',
            'https://icanhazip.com'
        ]

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        for url in alternatives:
            try:
                response, info = fetch_url(
                    module=self.module,
                    url=url,
                    headers=headers,
                    force=True,
                    timeout=15
                )

                if info['status'] == 200:
                    content = to_text(response.read()).strip()

                    # Парсим ответ в зависимости от формата
                    if 'ipify' in url:
                        data = json.loads(content)
                        ip = data.get('ip')
                    else:
                        ip_match = re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', content)
                        ip = ip_match.group(0) if ip_match else None

                    if ip:
                        return {'public_ip': ip, 'service_used': 'alternative', 'original_service': self.api_service}

            except Exception:
                continue  # следующий сервис

        self.module.fail_json(msg="All IP detection services are unavailable")

def main():
    module = AnsibleModule(
        argument_spec=dict(
            api_service=dict(
                type='str',
                default='ipify',
                choices=['ipify', '2ip', 'ipme', 'custom']
            ),
            api_url=dict(type='str', default='')
        ),
        supports_check_mode=True
    )

    try:
        pub_ip = PubIpFacts(module).run()
        module.exit_json(
            changed=False,
            ansible_facts={'pub_ip': pub_ip}
        )
    except Exception as e:
        module.fail_json(msg=str(e))

if __name__ == "__main__":
    main()
