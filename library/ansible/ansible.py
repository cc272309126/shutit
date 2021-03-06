"""ShutIt module. See http://shutit.tk
"""
#Copyright (C) 2014 OpenBet Limited
#
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is furnished
#to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
#FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
#COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
#IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
#CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from shutit_module import ShutItModule

class ansible(ShutItModule):

	def is_installed(self, shutit):
		return False

	def build(self, shutit):
		shutit.install('git')
		shutit.install('python2.7-dev')
		shutit.install('python-pip')
		shutit.install('python-simplejson')
		shutit.install('sshpass')
		shutit.send('pushd /opt')
		shutit.send('git clone git://github.com/ansible/ansible.git')
		shutit.send('source /opt/ansible/hacking/env-setup')
		shutit.add_to_bashrc('source /opt/ansible/hacking/env-setup')
		shutit.send('easy_install pip')
		shutit.send('pip install paramiko PyYAML jinja2 httplib2')
		shutit.send('echo "127.0.0.1" > /opt/ansible_hosts')
		shutit.add_to_bashrc('export ANSIBLE_HOSTS=/opt/ansible_hosts')
		shutit.send('popd')
		return True

	def test(self, shutit):
		send = 'ansible all -m ping'
		expect=['assword', shutit.cfg['expect_prompts']['base_prompt'],'authenticity of host']
		while True:
			res = shutit.send(send, expect=expect)
			if res == 1:
				break
			elif res == 0:
				send = shutit.cfg['target']['password']
			elif res == 2:
				send = 'yes'
		return True

def module():
	return ansible(
		'shutit.tk.ansible.ansible', 0.7656,
		description='',
		depends=['shutit.tk.setup', 'shutit.tk.ssh_server.ssh_server','shutit.tk.ssh_key.ssh_key']
	)

