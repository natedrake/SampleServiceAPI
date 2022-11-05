# -*- coding: utf-8 -*-
"""Create anapplication instance."""
from flask.helpers import get_debug_flag

from SampleServiceAPI.app import create_app
from SampleServiceAPI.settings import DevConfig, ProdConfig

CONFIG = DevConfig if get_debug_flag() else ProdConfig

app = create_app(CONFIG)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
