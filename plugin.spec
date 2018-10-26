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

            - title: ansible facts
              options:
                  collect-ansible-facts:
                      type: Bool
                      help: Save ansible facts as json file(s)
                      default: False