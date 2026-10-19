import json

from google.ads.googleads.client import GoogleAdsClient
from google.oauth2 import service_account

API_VERSION = "v25"

GOOGLE_ADS_SCOPE = "https://www.googleapis.com/auth/adwords"

OAUTH_CONFIG_KEYS = ["oauth_client_id", "oauth_client_secret", "refresh_token"]


def validate_auth_config(config):
    if config.get("service_account_key"):
        return

    missing_keys = [key for key in OAUTH_CONFIG_KEYS if not config.get(key)]
    if missing_keys:
        raise ValueError(
            f"Config is missing required keys: {missing_keys}. "
            f"Provide either `service_account_key` or all of {OAUTH_CONFIG_KEYS}."
        )


def get_service_account_credentials(config):
    service_account_key = config["service_account_key"]
    if isinstance(service_account_key, str):
        service_account_key = json.loads(service_account_key)

    return service_account.Credentials.from_service_account_info(
        service_account_key, scopes=[GOOGLE_ADS_SCOPE]
    )


def create_sdk_client(config, login_customer_id=None):
    if config.get("service_account_key"):
        return GoogleAdsClient(
            credentials=get_service_account_credentials(config),
            login_customer_id=login_customer_id,
            use_proto_plus=False,
            version=API_VERSION,
        )

    CONFIG = {
        "use_proto_plus": False,
        "client_id": config["oauth_client_id"],
        "client_secret": config["oauth_client_secret"],
        "refresh_token": config["refresh_token"],
    }

    if login_customer_id:
        CONFIG["login_customer_id"] = login_customer_id

    sdk_client = GoogleAdsClient.load_from_dict(CONFIG, version=API_VERSION)
    return sdk_client
