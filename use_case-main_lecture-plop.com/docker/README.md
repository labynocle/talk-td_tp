
first draft of the Dockerfile

Build the container:
	docker build -t nagios ./
Run it
	docker run --add-host="bdd.plop.com:127.0.0.1" --add-host="web.plop.com:127.0.0.1" --add-host="nagios.plop.com:127.0.0.1" --add-host 'firewall.plop.com:127.0.0.1' -it nagios /bin/bash
