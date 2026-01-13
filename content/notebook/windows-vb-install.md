---
title: Windows VirtualBox Install Process
tags:
  - virtualbox
  - windows
  - choco
weight: 99
---


1. Install
1. Update
1. Remove Unused Programs
1. Turn off hibernation

    ```powershell
    powercfg.exe -h off
    ```

1. Turn off page file

1. Clean C: drive, purging old system files and prior windows installations

1. Install Chocolatey and Packages

    ```powershell
    Set-ExecutionPolicy AllSigned
    # this next line enables tls1.2
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
    choco install -y firefox vlc adobereader 7zip
    choco install -y teamviewer
    choco install -y tailscale
    choco install -y pandoc gpg4win grepwin kdiff3 vcxsrv notepadplusplus putty.install wiztree winscp winfsp rclone unifying fritzing winmerge ffmpeg
    choco install -y git.install --params "/NoShellIntegration /NoCredentialManager /GitAndUnixToolsOnPath"
    choco install -y gitextensions
    choco install -y syncthing
    #choco install -y miniconda3 --params="'/AddToPath:1 /InstallationType:AllUsers /D:C:\Anaconda3'"
    #choco install -y google-drive-file-stream dropbox
    ```

External References

* <https://arstechnica.com/gadgets/2024/02/what-i-do-to-clean-up-a-clean-install-of-windows-11-23h2-and-edge/>
* <https://techwizard.cloud/2019/04/13/powershell-tip-exception-calling-downloadstring-with-1-arguments/>