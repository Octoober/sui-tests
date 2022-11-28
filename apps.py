from tasks.apps.wizard import Wizard
from tasks.apps.sui_nft import SuiNft

APPS = [
    {
        "context": Wizard,
        "url": "https://test-wizardland.vercel.app/"
    },
    {
        "context": SuiNft,
        "url": "https://sui-wallet-demo.sui.io/"
    }
]
