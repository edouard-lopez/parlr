# -*- coding: utf-8 -*-
import config
from server import app

config.configure_logging()

if __name__ == '__main__':
    app.run()
