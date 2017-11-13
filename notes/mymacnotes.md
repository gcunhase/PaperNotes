## My Mac Notes

TLDR; Important notes related to Mac

### [Create Ubuntu live USB with MacOS](https://computers.tutsplus.com/tutorials/how-to-create-a-bootable-ubuntu-usb-drive-for-pc-on-a-mac--cms-21187)
1. [Download Ubuntu](https://www.ubuntu.com/download/desktop)
2. Convert *.iso* to *.img*/*.dmg* file
```
hdiutil convert -format UDRW ~/path/to/target.iso -o ~/path/to/ubuntu.img
```
3. Determine the Device Node for the USB Drive, in my case *N=2*
```
diskutil list
diskutil unmountDisk /dev/diskN
```
4. Create the Bootable USB Drive
```
sudo dd if=/path/to/ubuntu-14.04-desktop-i386.dmg of=/dev/rdiskN bs=1m
```
5. Don't click in any button, instead type
```
diskutil eject /dev/disk2
```

### [Create bootable installer for MacOS](https://support.apple.com/en-us/HT201372)
1. Download Installer: App Store downloads it to *Applications folder* as a single file with a name that begins with *Install*
2. Terminal: *createinstallmedia*
  ```
  createinstallmedia --volume [volumepath(usb)] --applicationpath [installerpath]
  sudo /Applications/Install\ OS\ X\ El\ Capitan.app/Contents/Resources/createinstallmedia --volume /Volumes/MyVolume --applicationpath /Applications/Install\ OS\ X\ El\ Capitan.app
  ```

### [How to Dualboot Mac and Windows](https://www.laptopmag.com/articles/dual-boot-windows-os-x-mac)

### [Installing Xcode, Homebrew, Git, RVM, Ruby & Rails on Mac OS X](https://www.moncefbelyamani.com/how-to-install-xcode-homebrew-git-rvm-ruby-on-mac/)

```
bash <(curl -s https://raw.githubusercontent.com/monfresh/laptop/master/laptop)
```

### Matlab
* [2016b](http://www.mactorrents.org/matlab-r2016b-9-1-0/)
* [2017](https://downloadly.ir/software/engineering-specialized/mathworks-matlab-download/)

