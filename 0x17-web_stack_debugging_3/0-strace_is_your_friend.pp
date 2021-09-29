# Editing wordpress setting file typo causing
# server error 500

exec {'Fixing typos':
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
  path    => '/usr/bin/:/usr/local/bin/:/bin/'
}
