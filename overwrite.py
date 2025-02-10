import requests
import os
import yaml

# Define the URL to download the configuration file
SUB_URL = "https://oss3.cauenvao.click/api/v1/client/subscribe?token=225098b044cc17d41346237bc44bb2e8"
# Define the path to save the configuration file
config_file_path = "./configs/config.yaml"
# proxies = {
#     "http": "http://127.0.0.1:7890",  # 替换为你的 HTTP 代理
#     "https": "http://127.0.0.1:7890",  # 替换为你的 HTTPS 代理（如果需要）
# }

def download_config(url, file_path):
    """Download the configuration file from the specified URL and save it locally."""
    try:
        # response = requests.get(url, headers={"User-Agent": "clash.meta"}, proxies=proxies, allow_redirects=True)
        response = requests.get(url, headers={"User-Agent": "clash.meta"}, allow_redirects=True)

        response.raise_for_status()  # Raise an error for bad responses
        
        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Write the content to the file
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print("配置文件下载成功。")
    
    except requests.RequestException as e:
        print(f"请求失败: {e}")
    except IOError as e:
        print(f"文件操作失败: {e}")

def load_config(file_path):
    """Load the YAML configuration from a file."""
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file) or {}

def save_config(config, file_path):
    """Save the updated configuration back to the YAML file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        yaml.dump(config, file, allow_unicode=True)

def update_config(config):
    """Update the configuration based on the provided rules."""
    # Update proxy groups
    config["proxy-groups"] = [
        {
            "icon": "https://raw.githubusercontent.com/Orz-3/mini/master/Color/Static.png",
            "include-all": False,
            "exclude-filter": "(?i)GB|流量|到期|重置|官网",
            "name": "PROXY",
            "type": "select",
            "proxies": ["自动选择", "香港节点", "新加坡节点", "日本节点", "美国节点", "台湾节点"],
        },
        {
            "icon": "https://raw.githubusercontent.com/Orz-3/mini/master/Color/Urltest.png",
            "include-all": True,
            "exclude-filter": "(?i)GB|流量|到期|重置|官网|Argent|Germ|Britain|India|Luxem",
            "name": "自动选择",
            "tolerance": 50,
            "type": "url-test",
            "interval": 150,
        },
        {
            "icon": "https://raw.githubusercontent.com/Orz-3/mini/master/Color/OpenAI.png",
            "name": "国外AI",
            "type": "select",
            "proxies": ["香港节点", "新加坡节点", "日本节点", "美国节点", "台湾节点"],
        },
        {
            "icon": "https://raw.githubusercontent.com/Orz-3/mini/master/Color/Telegram.png",
            "name": "电报服务",
            "type": "select",
            "proxies": ["香港节点", "新加坡节点", "日本节点", "美国节点", "台湾节点"],
        },
        {
            "icon": "https://raw.githubusercontent.com/Orz-3/mini/master/Color/Google.png",
            "name": "谷歌服务",
            "type": "select",
            "proxies": ["香港节点", "新加坡节点", "日本节点", "美国节点", "台湾节点"],
        },
        {
            "icon": "https://raw.githubusercontent.com/Orz-3/mini/master/Color/HK.png",
            "include-all": True,
            "exclude-filter": "(?i)GB|流量|到期|重置|官网",
            "filter": "(?i)香港|Hong Kong|HK|🇭🇰",
            "name": "香港节点",
            "tolerance": 50,
            "type": "url-test",
            "interval": 300,
        },
        {
            "icon": "https://raw.githubusercontent.com/Orz-3/mini/master/Color/SG.png",
            "include-all": True,
            "exclude-filter": "(?i)GB|流量|到期|重置|官网",
            "filter": "(?i)新加坡|Singapore|🇸🇬",
            "name": "新加坡节点",
            "tolerance": 50,
            "type": "url-test",
            "interval": 300,
        },
        {
            "icon": "https://raw.githubusercontent.com/Orz-3/mini/master/Color/JP.png",
            "include-all": True,
            "exclude-filter": "(?i)GB|流量|到期|重置|官网",
            "filter": "(?i)日本|Japan|🇯🇵",
            "name": "日本节点",
            "tolerance": 50,
            "type": "url-test",
            "interval": 300,
        },
        {
            "icon": "https://raw.githubusercontent.com/Orz-3/mini/master/Color/US.png",
            "include-all": True,
            "exclude-filter": "(?i)GB|流量|到期|重置|官网",
            "filter": "(?i)美国|USA|🇺🇸",
            "name": "美国节点",
            "tolerance": 50,
            "type": "url-test",
            "interval": 300,
        },
        {
            "icon": "https://raw.githubusercontent.com/Orz-3/mini/master/Color/TW.png",
            "include-all": True,
            "exclude-filter": "(?i)GB|流量|到期|重置|官网",
            "filter": "(?i)台湾|TW|🇹🇼|tw|taiwan|tai wan",
            "name": "台湾节点",
            "tolerance": 50,
            "type": "url-test",
            "interval": 300,
        },
        {
            "icon": "https://raw.githubusercontent.com/Orz-3/mini/master/Color/Global.png",
            "include-all": True,
            "exclude-filter": "(?i)GB|流量|到期|重置|官网",
            "proxies": ["自动选择", "香港节点", "新加坡节点", "日本节点", "美国节点", "台湾节点"],
            "name": "GLOBAL",
            "type": "select",
        }
    ]

    # Ensure rule-providers exists
    if 'rule-providers' not in config:
        config['rule-providers'] = {}

    # Update rule-providers
    config["rule-providers"].update({
        "private": {
            "url": "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/private.yaml",
            "path": "./ruleset/private.yaml",
            "behavior": "domain",
            "interval": 86400,
            "format": "yaml",
            "type": "http",
        },
        "cn_domain": {
            "url": "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/cn.yaml",
            "path": "./ruleset/cn_domain.yaml",
            "behavior": "domain",
            "interval": 86400,
            "format": "yaml",
            "type": "http",
        },
        "telegram_domain": {
            "url": "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/telegram.yaml",
            "path": "./ruleset/telegram_domain.yaml",
            "behavior": "domain",
            "interval": 86400,
            "format": "yaml",
            "type": "http",
        },
        "google_domain": {
            "url": "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/google.yaml",
            "path": "./ruleset/google_domain.yaml",
            "behavior": "domain",
            "interval": 86400,
            "format": "yaml",
            "type": "http",
        },
        "geolocation-!cn": {
            "url": "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/geolocation-!cn.yaml",
            "path": "./ruleset/geolocation-!cn.yaml",
            "behavior": "domain",
            "interval": 86400,
            "format": "yaml",
            "type": "http",
        },
        "cn_ip": {
            "url": "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geoip/cn.yaml",
            "path": "./ruleset/cn_ip.yaml",
            "behavior": "ipcidr",
            "interval": 86400,
            "format": "yaml",
            "type": "http",
        },
        "telegram_ip": {
            "url": "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geoip/telegram.yaml",
            "path": "./ruleset/telegram_ip.yaml",
            "behavior": "ipcidr",
            "interval": 86400,
            "format": "yaml",
            "type": "http",
        },
        "google_ip": {
            "url": "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geoip/google.yaml",
            "path": "./ruleset/google_ip.yaml",
            "behavior": "ipcidr",
            "interval": 86400,
            "format": "yaml",
            "type": "http",
        },
        "bing": {
            "url": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Bing/Bing.yaml",
            "path": "./ruleset/bing.yaml",
            "behavior": "classical",
            "interval": 86400,
            "format": "yaml",
            "type": "http",
        },
        "copilot": {
            "url": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Copilot/Copilot.yaml",
            "path": "./ruleset/copilot.yaml",
            "behavior": "classical",
            "interval": 86400,
            "format": "yaml",
            "type": "http",
        },
        "claude": {
            "url": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Claude/Claude.yaml",
            "path": "./ruleset/claude.yaml",
            "behavior": "classical",
            "interval": 86400,
            "format": "yaml",
            "type": "http",
        },
        "bard": {
            "url": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/BardAI/BardAI.yaml",
            "path": "./ruleset/bard.yaml",
            "behavior": "classical",
            "interval": 86400,
            "format": "yaml",
            "type": "http",
        },
        "openai": {
            "url": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/OpenAI/OpenAI.yaml",
            "path": "./ruleset/openai.yaml",
            "behavior": "classical",
            "interval": 86400,
            "format": "yaml",
            "type": "http",
        },
    })

    # Update rules
    config["rules"] = [
        "RULE-SET,private,DIRECT",
        "RULE-SET,bing,国外AI",
        "RULE-SET,copilot,国外AI",
        "RULE-SET,bard,国外AI",
        "RULE-SET,openai,国外AI",
        "RULE-SET,claude,国外AI",
        "RULE-SET,telegram_domain,电报服务",
        "RULE-SET,telegram_ip,电报服务",
        "RULE-SET,google_domain,谷歌服务",
        "RULE-SET,google_ip,谷歌服务",
        "RULE-SET,geolocation-!cn,PROXY",
        "RULE-SET,cn_domain,DIRECT",
        "RULE-SET,cn_ip,DIRECT",
        "MATCH,PROXY",
    ]

def main():
    """Main function to download, load, update, and save the configuration."""
    # Step 1: Download the configuration
    download_config(SUB_URL, config_file_path)

    # Step 2: Load the downloaded configuration
    config = load_config(config_file_path)

    # Step 3: Update the configuration
    update_config(config)

    # Step 4: Save the updated configuration back to the file
    save_config(config, config_file_path)
    print("配置文件更新成功。")

if __name__ == "__main__":
    main()
