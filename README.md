# Infrared virt-customize plugin

**This is a POC**, if you're part of RedHat, contribute to the [design sheet](https://docs.google.com/document/d/142VmEXXUblwVXF249ZX0PhT8ZC2vQ-2NYSJopMFyiIk).

Notes:

* No linting is being done at the moment

* Due to infrared's design, works only on RHEL and Fedora

* Not optimized to the way infrared works with variables at the moment

* Assumes you have an undercloud node (OpenStack undercloud is deployed via infrared), no local and or remote node execution at the moment

* Assumes that the user stack on undercloud node has rw permissions to guest disk image

* Assumes repos are configured on guest disk image

## Description

A plugin for RedHat's [infrared](https://github.com/redhat-openstack/infrared) tool.

This plugin is designed to perform customization on guest disk images using libguestfs and additional tools.

## Installation

Assuming infrared is already installed and configured ([installation guide](https://infrared.readthedocs.io/en/stable/setup.html)):

```
infrared plugin add https://github.com/VKhitrin/infrared-virt-customize
```

## Usage

**See notes on the top for some limitations in place at the moment**

#### General arguments

List of guest disk image locations on host (required=True)
```
infrared virt-customize --image '/path/to/image','/path/to/image2'
```

Enable N ≥ 2 vCPUs during execution (required=False):
```
infrared virt-customize --cpu N
```

Enable N amount in MBs of memory during execution (required=False):
```
infrared virt-customize --memory N
```

Enable virt-customize's verbosity (required=False):
```
infrared virt-customize --verbosity yes
```

Enabled virt-customize's debug (required=False):
```
infrared virt-customize --trace yes
```

Skip libguestfs tools installation on executor host (required=False):
```
infrared virt-customize --skip-install-tools yes
```

Scrub build log of virt-customize from guest disk image (required=False):
```
infrared virt-customize --scrub-build-log yes
```

Set password encrypthion method when performing password tasks (required=False):
```
infrared virt-customize --password-crypto md5|sha256|sha512
```

#### Subscription Manager manipulation

Register to subscription manager \[required both --sm-register and --sm-credentials\] (required=False):
```
infrared virt-customize --image '/path/to/image' --sm-register yes --sm-credentials user@email.com:password
```

Attach a subscription to guest disk image:
```
infrared virt-customize --image '/path/to/image' --sm-attach poolid
```

#### Package manipulation

List of packages to be installed on guest disk image (required=False):

```
infrared virt-customize --image '/path/to/image' --install package1,package2
```

List of packages to be uninstalled from guest disk image (required=False):

```
infrared virt-customize --image '/path/to/image' --uninstall package1,package2
```

Update packages on guest disk image (required=False):
```
infrared virt-customize --image '/path/to/image' --update yes
```

Install packages on guest disk image on firstboot (required=False):
```
infrared virt-customize --image '/path/to/image' --firstboot-install package1,package2
```

#### Guest manipulation

Run virt-customize commands from file on guest disk image (required=False):
```
infrared virt-customize --image '/path/to/image' --commands-file /path/to/commands-file
```

Execute a script on guest disk image on firstboot (required=False):
```
infrared virt-customize --image '/path/to/image' --firstboot /path/to/file
```

Execute a command on guest disk image on firstboot (required=False):
```
infrared virt-customize --image '/path/to/image' --firstboot-command command
```

Set a hostname in guest disk image (required=False):
```
infrared virt-customize --image '/path/to/image' --guest-hostname hostname
```

Set a user's password in guest disk image (required=False):
```
infrared virt-customize --image '/path/to/image' --user-password user:password
```

Set root's password in guest disk image (required=False):
```
infrared virt-customize --image '/path/to/image' --root-password password
```

Run script (located on disk-image) in guest disk image (required=False):
```
infrared virt-customize --image '/path/to/image' --run-script script
```

Run command in guest disk image (required=False):
```
infrared virt-customize --image '/path/to/image' --run-command command
```

Inject SSH key to user in guest disk image (required=False):
```
infrared virt-customize --image '/path/to/image' --ssh-inject user:ssh_key
```

Set a timezone in guest disk image (required=False):
```
infrared virt-customize --image '/path/to/image' --guest-timezone timezone
```

Relabel SELinux file contexets in guest disk image (required=False):
```
infrared virt-customize --image '/path/to/image' --selinux-relabel yes
```

#### File manipulation

Copy files inside guest disk image (required=False):
```
infrared virt-customize --image '/path/to/image' --copy-inside /path/to/source:/path/to/dest
```

Copy files from infrared client to guest disk image (required=False):
```
infrared virt-customize --image '/path/to/image' --copy-to /path/to/source:/path/to/dest
```

Delete files in guest disk image (required=False):
```
infrared virt-customize --image '/path/to/image' --delete /path/to/file
```

Append line to file in guest disk image (required=False):
```
infrared virt-customize --image '/path/to/image' --append-line /path/to/file:line
```

Change permission to file in guest disk image \[can be decimal or octal permission\] (required=False):
```
infrared virt-customize --image '/path/to/image' --guest-permission permission:/path/to/file
```

Create symbolic link to file in guest disk image (required=False):
```
infrared virt-customize --image '/path/to/image' --guest-link /path/to/target:/path/to/file
```

Create directories in guest disk image (required=False):
```
infrared virt-customize --image '/path/to/image' --guest-directory /path/to/directory
```

Move file/directories in guest disk image (required=False):
```
infrared virt-customize --image '/path/to/image' --move-inside /path/to/source:/path/to/dest
```

Scrub file in guest disk image (required=False):
```
infrared virt-customize --image '/path/to/image' --scrub /path/to/file
```

Truncate file to zero length in guest disk image (required=False):
```
infrared virt-customize --image '/path/to/image' --truncate /path/to/file
```

Truncate path to zero length in guest disk image (required=False):
```
infrared virt-customize --image '/path/to/image' --truncate-recursive /path/to/file
```

Create a file in guest disk image (required=False):
```
infrared virt-customize --image '/path/to/image' --create /path/to/file
```

Copy file from infrared client to guest disk image while preserving permissions (required=False):
```
infrared virt-customize --image '/path/to/image' --upload-to /path/to/source:/path/to/dest
```

Write content to file in guest disk image (required=False):
```
infrared virt-customize --image '/path/to/image' --write-content /path/to/file:content
```

Edit file's content using perl's regular expression in guest disk image (required=False):
```
infrared virt-customize --image '/path/to/image' --edit /path/to/file:perl_reg_expression
```
