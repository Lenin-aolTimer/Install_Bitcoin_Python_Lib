import subprocess

subprocess.call('sudo git clone https://github.com/petertodd/python-bitcoinlib', shell=True)

subprocess.call('sudo python setup.py build', shell=True, cwd="python-bitcoinlib")

subprocess.call('sudo python setup.py install', shell=True, cwd="python-bitcoinlib")

subprocess.call('sudo python3 setup.py build', shell=True, cwd="python-bitcoinlib")

subprocess.call('sudo python3 setup.py install', shell=True, cwd="python-bitcoinlib")

