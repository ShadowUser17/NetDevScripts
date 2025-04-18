### Scripts for network devices...

#### Configure environment:
```bash
python3 -m venv --upgrade-deps env && \
./env/bin/pip3 install -r requirements.txt
```

#### Scan project dependencies:
```bash
./env/bin/pip-audit -f json | python3 -m json.tool
```

#### Validate project files:
```bash
./env/bin/flake8 --ignore="E501" *.py
```

#### URLs:
- [netmiko](https://github.com/ktbyers/netmiko/blob/develop/README.md)
- [scripting](https://wiki.mikrotik.com/wiki/Manual:Scripting)
