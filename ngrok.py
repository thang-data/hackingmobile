import os
import ssl
from multiprocessing import context

from pyngrok import ngrok, conf, installer

pyngrok_config = conf.get_default()

if not os.path.exists(pyngrok_config.ngrok_path):
    myssl = ssl.create_default_context();
    myssl.check_hostname=False
    myssl.verify_mode=ssl.CERT_NONE
    installer.install_ngrok(pyngrok_config.ngrok_path, context=context)

public_url = ngrok.connect(5000).public_url