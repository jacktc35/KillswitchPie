

# KillswitchPie
<img width="4736" height="668" alt="KillswitchBanner" src="https://github.com/user-attachments/assets/b44c94d4-ecde-4c88-a4a9-568dd47a2d1a" />

## What is KillswitchPie?

KillswitchPie is a web server designed to run on a low powered SBC that acts as a virtual power button to a real computer. In simple terms, you click the button on the site, the site tells the microcontroller (in this case, a Raspberry Pi Zero W) to turn on and off a relay accordingly, which is hooked up to the power button connections on a motherboard, shorting the connection and turning on/off the machine.

## Why?
KSP was a quite niche use case for my needs. I am using consumer hardware to host a server, which is not designed to be up 24/7, only when needed. KSP is intended to fill the gap between a 24/7 server and having to be there in person to turn on your machine every time.

## External Resources

The Pi that I am currently using is at: https://thepihut.com/products/raspberry-pi-zero-w and the relay is at: https://thepihut.com/products/grove-relay.
