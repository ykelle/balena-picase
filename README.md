# balena-picase
Using the Retroflag NESPI Case+ with balenaOS. 
Adding the ability of soft shutdown to balenaOS and the NESPI CASE+ on the Raspberry Pi

# Install:

## Overlay:
Log into your device:

```bash
balena ssh <applicationOrDevice>
```

Install the overlay:

```bash
wget -O - "https://raw.githubusercontent.com/ykelle/balena-picase/main/overlay.sh" | bash
```

or 

```bash
wget -O  "/mnt/boot/overlays/RetroFlag_pw_io.dtbo" "https://raw.githubusercontent.com/RetroFlag/retroflag-picase/master/RetroFlag_pw_io.dtbo"
```

Reboot your device.

## Container:
Click this to deploy this repository to balenaCloud:

[![](https://balena.io/deploy.png)](https://dashboard.balena-cloud.com/deploy?repoUrl=https://github.com/ykelle/balena-picase)

or download this repo, navigate into the folder and run

```bash
balena push <applicationOrDevice>
```
--------------------
# Further details:
This project uses files from the [Retroflag-Repo](https://github.com/RetroFlag/retroflag-picase).
The python script will run in a docker container and not directly on the Raspberry Pi.
Instead of using system calls in the script, we are interacting with the [balena Supervisor](https://www.balena.io/docs/reference/supervisor/supervisor-api/#examples-3). 
