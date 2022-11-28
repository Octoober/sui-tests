import json
import os
from typing import Union

from constants import WALLETS_JSON_FILE


def get_wallets() -> dict:
    if not os.path.exists(WALLETS_JSON_FILE):
        return {}
    with open(WALLETS_JSON_FILE, 'r') as file:
        wallets = json.loads(file.read())['wallets']

    return wallets


def create_default_wallets_file():
    default_object = {
        'wallets': []
    }
    if not os.path.exists(WALLETS_JSON_FILE):
        with open(WALLETS_JSON_FILE, 'w') as json_file:
            json.dump(default_object, json_file)


def save_wallet(wallet_hash: str, recovery_phrase: str):
    with open(WALLETS_JSON_FILE, 'r') as json_file:
        data = json.load(json_file)

    data['wallets'].append({
        "hash": wallet_hash,
        "phrase": recovery_phrase
    })

    with open(WALLETS_JSON_FILE, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def check_login():
    pass
