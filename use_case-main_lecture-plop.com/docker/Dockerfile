FROM debian:jessie
MAINTAINER Erwan Labynocle Ben Souiden "erwan@aleikoum.net"

ENV NRPE_DIR /etc/nagios
ENV NAGIOS_DIR /etc/nagios3
ENV SNMP_DIR /etc/snmp
ENV HOST_FILE /etc/hosts
ENV APACHE_DIR /etc/apache2

RUN apt-get update \
	&& apt-get -y upgrade \
	&& DEBIAN_FRONTEND=noninteractive apt-get install -y \
		build-essential \
		git \
		snmp \
		snmpd \
		apache2 \
		nagios3 \
		nagios-plugins \
		nagios-nrpe-plugin \
		nagios-nrpe-server \
		wget \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

RUN cd /tmp \
	&& git clone https://github.com/labynocle/talk-td_tp/ \
	&& cd talk-td_tp \
	&& rm -rf ${NRPE_DIR}/* \
	&& cp -rp use_case-main_lecture-plop.com/etc_nagios/* ${NRPE_DIR}/ \
	&& rm -rf ${NAGIOS_DIR}/* \
	&& cp -rp use_case-main_lecture-plop.com/etc_nagios3/* ${NAGIOS_DIR}/ \
	&& rm -rf ${SNMP_DIR}/* \
	&& cp -rp use_case-main_lecture-plop.com/etc_snmp/* ${SNMP_DIR}/ \
	&& cp ${NAGIOS_DIR}/apache2.conf ${APACHE_DIR}/sites-enabled/nagios.conf \
	&& rm -rf use_case-main_lecture-plop.com/ \
	&& mkdir /data

RUN mkdir /usr/lib/nagios/plugins-perso/ \
	&& cd /usr/lib/nagios/plugins-perso/ \
	&& wget http://nagios.manubulon.com/check_snmp_load.pl \
	&& chmod +x check_snmp_load.pl

RUN chmod a+x /var/lib/nagios3 \
	&& chgrp www-data /var/lib/nagios3/rw \
	&& chmod g+s /var/lib/nagios3/rw

EXPOSE 80
