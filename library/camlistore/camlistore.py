
# Created from dockerfile: /space/git/dockerfiles_repos/SvenDowideit/dockerfiles/camlistore//Dockerfile
from shutit_module import ShutItModule

class camlistore(ShutItModule):

	def is_installed(self, shutit):
		return False

	def build(self, shutit):
		shutit.install('git golang',force=True)
		shutit.send('pushd /opt')
		shutit.send('git clone https://github.com/bradfitz/camlistore.git')
		shutit.send('chmod 777 camlistore')
		shutit.send('pushd camlistore')
		shutit.send('go run make.go')
		shutit.send('popd')
		return True

	def finalize(self, shutit):
		return True

	def test(self, shutit):
		return True

	def is_installed(self, shutit):
		return False

	def get_config(self, shutit):
		return True

def module():
		return camlistore(
				'shutit.tk.camlistore.camlistore', 0.1567436346,
				depends=['shutit.tk.setup']
		)
