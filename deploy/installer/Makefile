PREFIX?=/apps

PROJECT_VERSION=__VERSION__

NEW_VERSION_PATH=$(PREFIX)/assets_$(PROJECT_VERSION)
NEW_VENV_PATH=$(NEW_VERSION_PATH)/env
LINK_PATH=$(PREFIX)/assets


install: install_deps install_env install_wheel install_links post-install

install_deps:

install_env:
	mkdir -p $(NEW_VENV_PATH)
	virtualenv -p python2.7 --no-site-packages $(NEW_VENV_PATH)
	$(NEW_VENV_PATH)/bin/pip install -I "setuptools==2.0.2"
	$(NEW_VENV_PATH)/bin/pip install -I "wheel>=0.22"
	$(NEW_VENV_PATH)/bin/pip install --upgrade pip==1.5

install_wheel:
	$(NEW_VENV_PATH)/bin/pip install --use-wheel --no-index --find-links=wheel-dir/ -r requirements.txt

install_links:
	if [ -L $(LINK_BKP_PATH) ] ; then rm -f $(LINK_BKP_PATH); fi;
	if [ -L $(LINK_PATH) ] ; then rm -f $(LINK_PATH); fi;
	ln -s $(NEW_VERSION_PATH) $(LINK_PATH)

post-install: 

