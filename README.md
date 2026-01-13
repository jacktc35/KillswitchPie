# KillswitchPie
### A Web Server that runs on a Raspberry Pi Zero W to allow hardware power button control remotely.

<img width="1640" height="664" alt="Banner" src="https://github.com/user-attachments/assets/914fcd53-587e-4733-a423-a43143f11c45" />

## What is KillswitchPie?
KillswitchPie is a web server designed to run on a low powered SBC that acts as a virtual power button to a real computer. In simple terms, you click the button on the site, the site tells the SBC (in this case, a RPI Zero W) to turn on and off a relay accordingly, which is hooked up to the power button connections on a motherboard, shorting the connection and turning on/off the machine.

## Why?
KillswitchPie was initially a quite niche use case for my needs, and is still a WIP. I am using consumer hardware to host a server; is not designed to be up 24/7, only when needed. KillswitchPie is intended to fill the gap between a 24/7 server and having to be there in person to turn on your machine every time.

## How does it work?
KillswitchPie is complete for my use case. It is written in Python (Flask & RPI GPIO Control), HTML and CSS. The concept and site is very simple by design. Currently, I have the Pi successfully turning on and off the relay via a button on a local webpage, with some very basic QOL improvements such as confirmation on button presses and confirmation boxes for pressing the power button more than once, force shutting down etc. This project is intended to work over any network; This is why I opted for a Linux-based RPI.This way, I can hook it up to my Tailnet using Tailscale and access the site from anywhere securely (you don't want anyone stumbling on the site and turning off your PC!) and without worrying about port forwarding.
 
## External Resources

The Pi that I am currently using is at: https://thepihut.com/products/raspberry-pi-zero-w and the relay is at: https://thepihut.com/products/grove-relay.

