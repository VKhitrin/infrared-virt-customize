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
                 move-inside:
                     type: Value
                     help: "Move file/directory inside guest disk image"
                     required: false
                 scrub:
                     type: Value
                     help: "Scrub file inside guest disk image"
                     required: false
                 truncate:
                     type: Value
                     help: "Truncate file inside guest disk image"
                     required: false
                 truncate-recursive:
                     type: Value
                     help: "Truncate files/directories recursively inside guest disk image"
                     required: false
                 create:
                     type: Value
                     help: "Create a file inside guest disk image"
                     required: false
                 upload-to:
                     type: Value
                     help: "Upload a file from infrared client to guest disk image"
                     required: false
                 write-content:
                     type: Value
                     help: "Write content into a file from inside guest disk image"
                     required: false
                 scrub-build-log:
                     type: Bool
                     help: "Scrub build log of virt-customize"
                     default: False
                     required: false
                 ssh-inject:
                     type: Value
                     help: "Inject SSH key to user inside guest disk image"
                     required: false
                 password-crypto:
                     type: Value
                     help: "Set password encryption method"
                     required: false
                     choices:
                       - "md5"
                       - "sha256"
                       - "sha512"
                 edit:
                     type: Value
                     help: "Edit a file inside guest disk image using perl's regular expressions"
                     required: false
                 sm-register:
                     type: Bool
                     help: "Starts the registration process with subscription manager"
                     default: False
                     required: false
                 sm-credentials:
                     type: Value
                     help: "Credentials used to subscribe to subscription manager"
                     required: false
                 sm-attach:
                     type: Value
                     help: "Attach pool to guest disk image"
                     required: false
                 sm-remove:
                     type: Bool
                     help: "Remove all subscriptions from guest disk image"
                     default: False
                     required: false

            - title: ansible facts
              options:
                  collect-ansible-facts:
                      type: Bool
                      help: Save ansible facts as json file(s)
                      default: False
