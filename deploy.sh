#!/bin/bash
sudo yum update -y
sudo yum install git -y
git clone https://github.com/NathanMilhomen/muribo.git
cd muribo
pip3 install -r requeriments.txt
echo '{
    "bot_prefix": ".",
    "token": "NzA2NjAzOTg3OTM1Mjk3NTU3.Xq8qPg.-5MMWus-PJWPo_ljSO_SaF5oULE",
    "application_id": "706603987935297557",
    "locales_domain": "base",
    "locales_path": "locales",
    "locales_languages": [
        "pt-br"
    ]
}' > config.json
echo '{
    "ids": []
}' > blacklist.json
make mo
python3 main.py
