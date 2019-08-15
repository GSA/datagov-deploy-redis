[![CircleCI](https://circleci.com/gh/GSA/datagov-deploy-redis.svg?style=svg)](https://circleci.com/gh/GSA/datagov-deploy-redis)

# datagov-deploy-redis

This project is part of [datagov-deploy](https://github.com/GSA/datagov-deploy).

Ansible role to deploy redis.


## Usage

Include this role in your `requirements.yml`.

```yaml
- src: https://github.com/gsa/datagov-deploy-redis.git
```


### Variables



## Prerequisites for development

- [Ruby](https://www.ruby-lang.org/) 2.3+
- [Docker](https://www.docker.com/)
- [Python](https://www.python.org/) 2.7 or 3.5+ in a virtualenv


## Development

Install dependencies.

    $ make setup

Run the tests.

    $ make test

You can debug the container after it runs. See `kitchen help` for additional
commands.

    $ bundle exec kitchen login
