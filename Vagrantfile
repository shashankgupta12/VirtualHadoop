# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.define "master" do |subconfig|
    subconfig.vm.box = "base-hadoop"
    subconfig.vm.hostname = "master"
    subconfig.vm.network :private_network, ip: "10.0.0.10"
  end
  config.vm.define "node1" do |subconfig|
    subconfig.vm.box = "base-hadoop"
    subconfig.vm.hostname = "node1"
    subconfig.vm.network :private_network, ip: "10.0.0.20"
  end
  config.vm.define "node2" do |subconfig|
    subconfig.vm.box = "base-hadoop"
    subconfig.vm.hostname = "node2"
    subconfig.vm.network :private_network, ip: "10.0.0.30"
  end
  config.vm.define "node3" do |subconfig|
    subconfig.vm.box = "base-hadoop"
    subconfig.vm.hostname = "node3"
    subconfig.vm.network :private_network, ip: "10.0.0.40"
  end
  config.vm.define "node4" do |subconfig|
    subconfig.vm.box = "base-hadoop"
    subconfig.vm.hostname = "node4"
    subconfig.vm.network :private_network, ip: "10.0.0.50"
  end

end