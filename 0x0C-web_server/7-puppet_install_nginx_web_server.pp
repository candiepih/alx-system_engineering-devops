# configure nginx server to listen to port 80
# with permanent redirect for /redirect_me and handle
# custom error 404 page

exec {'apt-get-update':
  command => '/usr/bin/apt-get update'
}

package {'nginx':
  ensure => installed,
}

file {'/var/www/html/index.html':
  ensure  => present,
  content => 'Holberton School',
}

file_line {'server_name _;':
  path  => '/etc/nginx/sites-available/default',
  line  => "\n\tlocation /redirect_me {\n\t\trewrite ^/redirect_me(.*)$ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;\n\t}",
  after => 'server_name _;'
}

file {'/var/www/html/404.html':
  ensure  => present,
  content => "Ceci n'est pas une page",
}

file_line {'server_name _; ':
  path  => '/etc/nginx/sites-enabled/default',
  line  => "\n\terror_page 404 /404.html;\n\tlocation = /404.html {\n\t\troot /var/www/html;\n\t\tinternal;\n\t}",
  after => 'server_name _;'
}

service {'nginx':
  ensure  => running,
  require => Package['nginx']
}
