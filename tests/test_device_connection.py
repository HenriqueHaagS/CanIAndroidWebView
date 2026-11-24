import subprocess


def test_android_device_is_connected():

    result = subprocess.run(
        ["adb", "devices"],
        capture_output=True,
        text=True,
        check=True
    )

    devices = result.stdout.strip().splitlines()[1:]

    connected_devices = [
        line for line in devices
        if len(line.split("\t")) == 2
           and line.split("\t")[1] == "device"]


    assert connected_devices, "Nenhum dispositivo Android conectado ao ADB."
