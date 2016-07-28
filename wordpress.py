#!/usr/bin/env python
# -*- coding: utf-8 -*-
#coded by @cyberh99

import sys
import os
def root():
	if (os.geteuid() != 0):
		print "You shoul run this script as root"
		print "Do you continue? y/n"
		an = raw_input("<: ")
		if (an == "y" or an == "Y"):
			pass
		elif(an == "n" or an == "N"):
			sys.exit()
		else:
			main()
def wpconfig(db,dbuser,dbpass,dbserver):
	i = "<?php"
	p="define('DB_NAME', '"+str(db)+"');\n"
	s="define('DB_USER', '"+str(dbuser)+"');\n"
	t="define('DB_PASSWORD', '"+str(dbpass)+"');\n"
	c="define('DB_HOST', '"+str(dbserver)+"');\n"
	q='''define('DB_CHARSET', 'utf8');
	define('DB_COLLATE', '');
	define('AUTH_KEY',         'put your unique phrase here');
	define('SECURE_AUTH_KEY',  'put your unique phrase here');
	define('LOGGED_IN_KEY',    'put your unique phrase here');
	define('NONCE_KEY',        'put your unique phrase here');
	define('AUTH_SALT',        'put your unique phrase here');
	define('SECURE_AUTH_SALT', 'put your unique phrase here');
	define('LOGGED_IN_SALT',   'put your unique phrase here');
	define('NONCE_SALT',       'put your unique phrase here');
	$table_prefix  = 'wp_';
	define('WP_DEBUG', false);
	if ( !defined('ABSPATH') )
		define('ABSPATH', dirname(__FILE__) . '/');
	require_once(ABSPATH . 'wp-settings.php');'''
	wp = "wp-config.php"
	archivo = open(wp, 'a')
	archivo.write(i)
	archivo.write(p)
	archivo.write(s)
	archivo.write(t)
	archivo.write(c)
	archivo.write(q)
	archivo.close()

def config():
		db = raw_input("Data Base Name: ")
		dbuser = raw_input("User db: ")
		dbpass = raw_input("Pass db: ")
		dbserver = raw_input("Host db: ")
		wpconfig(db,dbuser,dbpass,dbserver)
		os.system("mkdir wp-content/uploads")
		os.system("chmod 755 * ")
		os.system("mkdir /var/www/html/wordpress")
		os.system("mv * /var/www/html/wordpress")
		os.system("clear")
		print "Wordpress instalado correctamente"
			
def install():
	os.chdir("/tmp")
	os.system("wget https://wordpress.org/latest.tar.gz")
	os.system("tar xfv latest.tar.gz")
	os.chdir("/tmp/wordpress")
	config()
	
def uninstall():
	
	print "Esto eliminará todo el contenido de la carpeta /var/www/html"
	d = raw_input("¿Quieres continuar? Y/N: ")
	if (d == "Y" or d == "y"):
		os.system("rm -rf /var/www/html/wordpress")
	elif (d == "n" or d == "N"):
		sys.exit()
	else:
		print "Opción incorrecta"
def main():
	os.system("clear")
	try:
		if (sys.argv[1] == "--install"):
			root()
			install()
		elif (sys.argv[1] == "--uninstall"):
			root()
			uninstall()
		else:
			print "Parametro incorrecto"
	except(IndexError):
		 print "You must use the argument --install or --uninstall"

if __name__ == '__main__':
	main()
