# create ssh config file
file { '/etc/ssh/ssh_config':
	ensure => file
}

file_line { 'identitiy_file':
	ensure => created,
	path => '/etc/ssh/ssh_config',
	match => 'IdentityFile',
	line => 'IdentityFile /c/Users/Rehema/.ssh/id_rsa.pub'
}

file_line { 'refuse_password':
	ensure => created,
	path => '/etc/ssh/ssh_config',
	match => 'PasswordAuthentication',
	line => 'PasswordAuthentication no'
}	
