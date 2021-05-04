Task- 10
Automating everything using Packer.

```


Installation:

1. Install homebrew(package manager for Mac OS) 
2. Brew install packer
3. Packer —version

-> Packer is the automated test suite which helps us to create custom images using AMI.
-> Custom Images of the particular tasks can be obtained and automatically starts.
-> Important components of the Packer ( Builders, Provisioners and PostProcesses)
-> Builders -> Main component used to creating machine and generating Images.
-> Provisioners -> Use builtin and third party software to install and configure machine image after booting.	 		
-> Post Processors -> After building an Image what the particular image should do. 			 	 		 	       
```

```

{
    "builders": [
    {
        "type": "virtualbox-iso",
        "guest_os_type": "Ubuntu_64",
        "iso_url": "https://releases.ubuntu.com/20.04/ubuntu-20.04.2-live-server-amd64.iso",
        "iso_checksum": "d1f2bf834bbe9bb43faf16f9be992a6f3935e65be0edece1dee2aa6eb1767423",
        "ssh_username": "packer",
        "ssh_password": "packer",
        "shutdown_command": "echo 'packer' | sudo -S shutdown -P now",
        "vm_name": "TEST9"  	
    }
	 ],
    "post-processors": [
      ],
      "provisioners": [
      ]
  }

The above code is done with inistating the Virtual Machine.



# Create kanaka user account.
d-i passwd/user-fullname string kanaka
d-i passwd/username string kanaka_intern
d-i passwd/user-password password 1234
d-i passwd/user-password-again password 1234
d-i user-setup/allow-password-weak boolean true
d-i user-setup/encrypt-home boolean false
d-i passwd/user-default-groups vagrant sudo
d-i passwd/user-uid string 900

The above code must be hhtp folder where preseed.cong file exists.



```

