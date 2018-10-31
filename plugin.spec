---
config:
    plugin_type: other
subparsers:
    virt-customize:
        description: Customize virtual disk images
        include_groups: ["Ansible options", "Inventory", "Common options", "Answers file"]
        groups:
            - title: Host arguments
              options:
                  host-address:
                      type: Value
                      help: 'Address/FQDN of the executor host'
                      required: false
                      default: 'undercloud'
                  host-user:
                      type: Value
                      help: 'User to SSH to the remote executor host with'
                      default: root
                  host-key:
                      type: Value
                      help: |
                            User's SSH key used to connect to remote executor host
                            Example: '/root/.ssh/id_rsa.pub'.
                      required: false

            - title: Image arguments
              options:
                  image-remote:
                      type: Value
                      help: |
                            Comma seperated list of images to be customized located on remote executor host
                            Example: '/tmp/rhel-guest-image-7-5-146-x86-64-qcow2'.
                      required: false
                  image-url:
                      type: Value
                      help: |
                            Comma seperated list of images to be customized that will be fetched from a URL
                            Example: 'https://download.fedoraproject.org/pub/fedora/linux/releases/29/Cloud/x86_64/images/Fedora-Cloud-Base-29-1.2.x86_64.qcow2'.
                      required: false
                  image-local:
                      type: Value
                      help: |
                            Comma seperated list of images to be customizec located on infrared client'
                            Example: '/tmp/rhel-guest-image-7-5-146-x86-64-qcow2'.
                      required: false
                  image-path:
                      type: Value
                      help: | 
                            Directory on the executor host that remote/url images will be fetched to
                      default: '/tmp'

            - title: Additional virt-customize flags
              options:
                  memory:
                      type: Value
                      help: |
                            Amount of memory in MBs to be assigned to guest disk image during virt-customize
                            Example: '4096'.
                      required: false
                  cpu:
                      type: Value
                      help: |
                            Amount of vCPUs (N ≥ 2) to be assigned to guest disk image during virt-customize
                            Example: '4'.
                      required: false
                  verbosity:
                      type: Bool
                      help: |
                            Enable virt-customize verbosity flag
                      default: False
                      required: false
                  trace:
                      type: Bool
                      help: |
                            Enable virt-customize trace
                      default: False
                      required: false
                  skip-install-tools:
                      type: Bool
                      help: |
                            Skip installation of libguestfs tools on executor host
                      default: False
                      required: false
                  password-crypto:
                      type: Value
                      help: |
                            Sets a password encryption method when performing password actions
                      required: false
                      choices:
                        - "md5"
                        - "sha256"
                        - "sha512"

            - title: Subscriptiom Manager manipulation arguments
              options:
                 sm-attach:
                     type: Value
                     help: |
                           Attaches a pool to guest disk image
                           Example: '8a85f9...'.
                     required: false
                 sm-remove:
                     type: Bool
                     help: |
                           Removes all attached subscriptions from guest disk image
                     default: False
                     required: false
                 sm-unregister:
                     type: Bool
                     help: |
                           Unregister guest disk image from subscription manager
                     default: False
                     required: false
                 sm-register:
                     type: Bool
                     help: |
                           Initiates the registration process with subscription manager
                     default: False
                     required: false
                 sm-credentials:
                     type: Value
                     help: "Credentials used to subscribe to subscription manager"
                     help: |
                           Credentials that will be used as part of registration process to subscription manager
                           usage: 'user@email.com:password'
                           Example:'my@domain.com:p4ssw0rd'.
                     required: false

            - title: Package manipulation arguments
              options:
                 install:
                     type: Value
                     help: |
                           Comma seperated list of packages to install on guest disk image
                           Example: 'vim, telnet'.
                     required: false
                 uninstall:
                     type: Value
                     help: |
                           Comma seperated list of packages to uninstall from guest disk image
                           Example: 'vim, telnet'.
                     required: false
                 update:
                     type: Bool
                     help: |
                           Determines whether to update packages on guest disk image
                     default: False
                     required: false
                 firstboot-install:
                     type: Value
                     help: |
                           Comma seperated list of packages to install on guest disk image during firstboot
                           Example: 'vim, telnet'.
                     required: false

            - title: Guest manipulation arguments
              options:
                 commands-file:
                     type: FileValue
                     help: |
                           File located on infrared client containing virt-customize commands to be performed on guest disk image
                           Example: '/tmp/virt-customize-commandx.txt'.
                     required: false
                 firstboot-file:
                     type: FileValue
                     help: |
                           File located on infrared client containing virt-customize actions to be perform inside guest disk image during firstboot
                           Example: '/tmp/firstboot-instructions.txt'.
                     required: false
                 firstboot-command:
                     type: Value
                     help: |
                           Command to be executed inside guest disk image during firstboot
                           Example: 'systemctl restart network'.
                     required: false
                 guest-hostname:
                     type: Value
                     help: |
                           Set default hostname inside guest disk image
                           Example: 'localhost.localdomain'.
                     required: false
                 user-password:
                     type: Value
                     help: |
                           Set a password for the specified user inside guest disk image
                           Usage: 'user:password'
                           Example: 'demouser:demopassword'.
                     required: false
                 root-password:
                     type: Value
                     help: |
                           Set a password for the root user inside guest disk image
                           Example: 'rootpassword'.
                     required: false
                 run-script:
                     type: Value
                     help: |
                           Run a script located inside guest disk image
                           Example: '/tmp/myscript.sh'.
                     required: false
                 run-command:
                     type: Value
                     help: |
                           Run a command inside guest disk image
                           Example: 'ps -ef'.
                     required: false
                 ssh-inject:
                     type: Value
                     help: |
                           Inject SSH key to the specified user inside guest disk image
                           Usage: 'user:ssh_key'
                           Example: 'root:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDoTA1TNcQMr71p12i........'.
                     required: false
                 guest-hostname:
                     type: Value
                     help: |
                           Set default hostname inside guest disk image
                           Example: 'localhost.localdomain'.
                     required: false
                 guest-timezone:
                     type: Value
                     help: |
                           Set the default timezone inside guest disk image
                           Example: 'Europe/London'.
                     required: false
                 selinux-relabel:
                     type: Bool
                     help: |
                           Relabel SELinux file contexts inside guest disk image
                     required: false
            - title: File manipulation arguments
              options:
                 copy-to:
                     type: Value
                     help: |
                           File located on infrared client to be transferred to a directory inside guest disk image
                           Usage: '/path/to/source:/path/to/dest'
                           Example: '/tmp/infrared-file.txt:/tmp/'.
                     required: false
                 copy-inside:
                     type: Value
                     help: |
                           Copy files/directories recursively inside guest disk image
                           Usage: '/path/to/source:/path/to/dest'
                           Example: '/tmp:/home'.
                     required: false
                 delete:
                     type: Value
                     help: |
                           Deletes files/directories recursively inside guest disk image
                           Example: '/tmp'.
                 append-line:
                     type: Value
                     help: |
                           Append line to file inside guest disk image
                           Usage: '/path/to/file:text'
                           Example: '/tmp/myfile.txt:text'.
                     required: false
                 guest-permission:
                     type: Value
                     help: "Change permissions to file inside guest disk image"
                     help: |
                           Cange permission of a file inside guest disk image
                           Accepts decimal and octal permissions
                           Usage: 'permission:/path/to/file'
                           Example: '0644:/tmp/myfile.txt'.
                     required: false
                 guest-link:
                     type: Value
                     help: "Create symbolic link to file inside guest disk image"
                     help: |
                           Creates a symbolic link to a file inside guest disk image
                           Accepts decimal and octal permissions
                           Usage: '/path/to/target:/path/to/source'
                           Example: '/tmp/myscript:/usr/bin/myscript.sh'.
                     required: false
                 guest-directory:
                     type: Value
                     help: |
                           Creates directories recursively inside guest disk image
                           Example: '/tmp/this/is/a/long/directory'.
                     required: false
                 move-inside:
                     type: Value
                     help: |
                           Move file/directories inside guest disk image
                           Usage: '/path/to/source:/path/to/dest'
                           Example: '/usr/share/stuff:/tmp/archive'.
                     required: false
                 scrub:
                     type: Value
                     help: |
                           Scrub a file (could not be recovered) inside guest disk image
                           Example: '/tmp/secretlog'.
                     required: false
                 truncate:
                     type: Value
                     help: |
                           Truncate file to zero length inside guest disk image
                           Example: '/tmp/nonemptyfile.txt'.
                     required: false
                 truncate-recursive:
                     type: Value
                     help: |
                           Truncate files inside directories recursively to zero length inside guest disk image
                           Example: '/tmp'.
                     required: false
                 create:
                     type: Value
                     help: |
                           Create a file inside guest disk image
                           Example: '/tmp/newfile.txt'.
                     required: false
                 upload-to:
                     type: Value
                     help: |
                           Upload a file from infrarec client to guest disk image
                           Usage: '/path/to/source:/path/to/dest'
                           Example: '/tmp/infrafile.txt:/tmp/guestfile.txt'.
                     required: false
                 write-content:
                     type: Value
                     help: |
                           Write content into a file inside a guest disk image
                           Usage: '/path/to/file:content'
                           Example: '/tmp/guestfile.txt:text'.
                     required: false
                 scrub-build-log:
                     type: Bool
                     help: |
                           Scrubs build log of virt-customize from guest disk image
                     default: False
                     required: false
                 edit:
                     type: Value
                     help: |
                           Edit a file inside guest disk image using perl regular expressions
                           Usage: '/path/to/file:perl_reg_expression'
                           Example: '/tmp/guestfile.txt:s/text/next/g'.
                     required: false

            - title: ansible facts
              options:
                  collect-ansible-facts:
                      type: Bool
                      help: Save ansible facts as json file(s)
                      default: False
