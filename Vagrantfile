# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.
 
  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "ubuntu/bionic64"                #[1]
  config.vm.box_version = "~> 20200304.0.0"        #[2]
 
  config.vm.network "forwarded_port", guest: 8000, host: 8000  #[3]
 
  config.vm.provision "shell", inline: <<-SHELL #[4]
    systemctl disable apt-daily.service         #[5]
    systemctl disable apt-daily.timer           #[6]
  
    sudo apt-get update                         #[7]
    sudo apt-get install -y python3-venv zip    #[8]
    touch /home/vagrant/.bash_aliases           #[9]
    if ! grep -q PYTHON_ALIAS_ADDED /home/vagrant/.bash_aliases; then   #[10]
      echo "# PYTHON_ALIAS_ADDED" >> /home/vagrant/.bash_aliases        #[11]
      echo "alias python='python3'" >> /home/vagrant/.bash_aliases      #[12]
    fi
  SHELL
 end



# [1] config.vm.box = "ubuntu/bionic64"
# This line sets the base box for the virtual machine to "ubuntu/bionic64". A base box is a pre-configured virtual machine image that serves as the starting point for creating new virtual machines.



# [2]config.vm.box_version = "~> 20200304.0.0"
# This line specifies the version constraint for the base box. The ~> operator means to use a version greater than or equal to the specified version, but less than the next significant release. In this case, it indicates that the version should be greater than or equal to "20200304.0.0" but less than the next major release.


# [3]config.vm.network "forwarded_port", guest: 8000, host: 8000
# This line sets up port forwarding from the host machine to the guest machine. It maps port 8000 on the host to port 8000 on the guest. This allows accessing services running on the guest machine through the specified port on the host machine.


# [4]config.vm.provision "shell", inline: <<-SHELL ...
# This line specifies the provisioner to use for configuring the virtual machine. In this case, it uses the "shell" provisioner, which executes inline shell commands.


# [5]systemctl disable apt-daily.service
# This command disables the "apt-daily.service" service. The "apt-daily" service is responsible for automatically updating package indexes on Ubuntu systems. Disabling it ensures that the automatic update process does not interfere with the provisioning step.


# [6]systemctl disable apt-daily.timer
# This command disables the "apt-daily.timer" timer. The "apt-daily.timer" triggers the "apt-daily.service" at regular intervals. Disabling the timer prevents it from automatically triggering the update process.


# [7]sudo apt-get update
# This command updates the package lists for the system. It retrieves information about available package updates from the configured package repositories.


# [8]sudo apt-get install -y python3-venv zip
# This command installs the packages "python3-venv" and "zip" using the package manager (apt-get) with the "-y" flag, which automatically answers "yes" to any prompts. These packages are required for creating Python virtual environments and working with ZIP archives.


# [9]touch /home/vagrant/.bash_aliases
# This command creates an empty file named ".bash_aliases" in the home directory of the "vagrant" user. The ".bash_aliases" file is typically used to define custom command aliases.


# [10]if ! grep -q PYTHON_ALIAS_ADDED /home/vagrant/.bash_aliases; then ...
# This line checks if the string "PYTHON_ALIAS_ADDED" exists in the ".bash_aliases" file. The condition "! grep -q ..." checks if the pattern is not found.

# [11]echo "# PYTHON_ALIAS_ADDED" >> /home/vagrant/.bash_aliases
# If the string "PYTHON_ALIAS_ADDED" does not exist in the ".bash_aliases" file, this line appends the comment "# PYTHON_ALIAS_ADDED" to the file.

# [11]echo "alias python='python3'" >> /home/vagrant/.bash_aliases

# [12]If the string "PYTHON_ALIAS_ADDED" does not exist in the ".bash_aliases" file, this line appends the command alias "alias python='python3'" to the file. It creates an alias named "python" that points to the "python3" executable, ensuring that the "python" command refers to Python 3.