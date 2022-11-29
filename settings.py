
# Enable and Disable timeout
SLEEP = True

# Interval between account creation
INTERVAL: int = 10

# Timeout at runtime
RANDOM_SLEEP: list = [2, 4]

# Character set speed
RANDOM_SLEEP_WRITE: list = [0.1, 0.2]

# Master password
PASSWORD: str = 'TestPass101'

# Number of accounts to be created.
# Set 0 for infinite.
COUNT: int = False

# Run browser in background.
# WARN: No tested.
HEADLESS: int = False
