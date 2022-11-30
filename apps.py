from tasks.apps import Wizard, SuiNft, EthosGame, Cleo

APPS = [
    {
        "worker": Wizard,
        "url": "https://test-wizardland.vercel.app/"
    },
    {
        "worker": EthosGame,
        "url": "https://ethoswallet.github.io/2048-demo/"
    },
    {
        "worker": Cleo,
        "url": "https://cleo-mint.vercel.app/"
    },
    {
        "worker": SuiNft,
        "url": "https://sui-wallet-demo.sui.io/"
    },
]
