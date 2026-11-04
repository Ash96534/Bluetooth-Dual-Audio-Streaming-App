#!/usr/bin/env python3
"""Bluetooth Dual-Audio Streaming App - Stream audio to multiple Bluetooth devices simultaneously."""

import bluetooth


class BluetoothAudioStreamer:
    def __init__(self):
        self.devices = []
        self.connected_devices = []

    def scan_devices(self):
        print("Scanning for Bluetooth devices...")
        self.devices = bluetooth.discover_devices(lookup_names=True)
        for addr, name in self.devices:
            print(f"{addr} - {name}")
        return self.devices

    def connect_device(self, address):
        try:
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            sock.connect((address, 1))
            self.connected_devices.append(sock)
            print(f"Connected to {address}")
            return sock
        except Exception as e:
            print(f"Failed to connect: {e}")
            return None

    def stream_audio(self, audio_data):
        for sock in self.connected_devices:
            try:
                sock.send(audio_data)
            except Exception as e:
                print(f"Stream error: {e}")


if __name__ == "__main__":
    streamer = BluetoothAudioStreamer()
    streamer.scan_devices()
