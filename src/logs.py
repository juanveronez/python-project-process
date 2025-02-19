import sentry_sdk

import os

from dotenv import load_dotenv

load_dotenv()

sentry_dsn = os.getenv('SENTRY_DSN')

sentry_sdk.init(
    dsn=sentry_dsn,
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
)