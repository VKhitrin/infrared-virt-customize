---
config:
    plugin_type: other
subparsers:
    virt-customize:
        description: Customize virtual disk images
        include_groups: ["Ansible options", "Inventory", "Common options", "Answers file"]
        groups:
            - title: node
              options:
                  host-address:
                      type: Value
                      help: 'Address/FQDN of the invoker host'
                      required: yes
                      default: undercloud
                  host-user:
                      type: Value
                      help: 'User to SSH to the host with'
                      default: root
                  host-key:
                      type: Value
                      help: "User's SSH key"
                      required: false

            - title: image
              options:
                  image:
                      type: Value
                      help: 'Comma seperated list of images to be invoked upon'
                      required: yes

            - title: virt-customize variables
              options:
                  memory:
                      type: Value
                      help: 'Amount of memory to be assigned to guest disk image'
                      required: false
                  cpu:
                      type: Value
                      help: 'Amount of cpu to be assigned to guest disk image'
                      required: false
                  verbosity:
                      type: Bool
                      help: 'Enable virt-customize verbosity'
                      default: False
                      required: false
                  trace:
                      type: Bool
                      help: 'Enable virt-customize trace'
                      default: False
                      required: false
                  skip-install-tools:
                      type: Bool
                      help: 'Skip installation of libguestfs tools on executor node'
                      default: False
                      required: false

            - title: virt-customize actions
              options:
                 install:
                     type: Value
                     help: 'Packages to install on guest disk image'
                     required: false
                 uninstall:
                     type: Value
                     help: 'Packages to uninstall on guest disk image'
                     required: false
                 update:
                     type: Bool
                     help: 'Update packages on guest disk image'
                     default: False
                     required: false
                 firstboot-install:
                     type: Value
                     help: 'Packages to install on guest disk image during firstboot'
                     required: false
                 commands-file:
                     type: FileValue
                     help: 'Customize commands to be executed from file'
                     required: false
                 copy-to:
                     type: Value
                     help: 'Copy files/directories from host to directory on guest disk image'
                     required: false
                 copy-inside:
                     type: Value
                     help: 'Copy files inside guest disk image'
                     required: false
                 delete:
                     type: Value
                     help: 'Delete files/directories on guest disk image'
                 firstboot-file:
                     type: FileValue
                     help: 'Script to run on guest disk image during firstboot'
                     required: false
                 firstboot-command:
                     type: Value
                     help: 'Command to run on guest disk image during firstboot'
                     required: false
                 guest-hostname:
                     type: Value
                     help: 'Sets the hostname inside guest disk image'
                     required: false
                 user-password:
                     type: Value
                     help: "Sets user's password inside guest disk image"
                     required: false
                 root-password:
                     type: Value
                     help: "Sets root's password inside guest disk image"
                     required: false
                 run-script:
                     type: Value
                     help: "Run script inside guest disk image"
                     required: false
                 run-command:
                     type: Value
                     help: "Run command inside guest disk image"
                     required: false
                 guest-timezone:
                     type: Value
                     help: "Set the default timezone inside guest disk image"
                     required: false
                 selinux-relabel:
                     type: Bool
                     help: "Relabel SELinux file contexts inside guest disk image"
                     required: false
                 append-line:
                     type: Value
                     help: "Append line to file inside guest disk image"
                     required: false
                 guest-permission:
                     type: Value
                     help: "Change permissions to file inside guest disk image"
                     required: false
                 guest-link:
                     type: Value
                     help: "Create symbolic link to file inside guest disk image"
                     required: false
                 guest-directory:
                     type: Value
                     help: "Creates directory inside guest disk image"
                     required: false

            - title: ansible facts
              options:
                  collect-ansible-facts:
                      type: Bool
                      help: Save ansible facts as json file(s)
                      default: False
