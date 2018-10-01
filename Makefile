.PHONY: setup test

setup:
	bundle install
	pip install -r requirements.txt
	ansible-galaxy install -r requirements.yml

test:
	bundle exec kitchen test
