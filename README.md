# SubTexting

Sublime Text 3 plugin which allows users to send and receive text messages. (Android Only)

## Setup

### Create an account

CTRL + SHIFT + P -> SubTexing: Sign Up

Insert username and phone number. You should then receive a confirmation text message with a key code.

Once you've received your key, press

CTRL + SHIFT + P -> SubTexting: Verify

and insert the confirmation code you've received.

### Install Android App

Download: link_to_app

Use the key you've received to log in the app and select the contacts you'd like SubTexting to know about.

SubTexting <b>DOES NOT</b> store the phone number of your contacts! To learn more, scroll down to "I Don't Want My Contacts Stored On The Could!"

### Load Contacts Onto SubTexting

Once you've loaded your contacts through the Android app, press

CTRL + SHIFT + P -> SubTexting: Load Contacts

This will download the uploaded contacts to SubTexting.

## Usage



## How does it work?

SubTexting connects to your Android device and uses the device to dispatch messages.

### Send Message
...

### Receive Message
...

## Still working on readme.

## Sending Msg

![Alt text](/doc/img/send_msg_01.png?raw=true "Send 01")

![Alt text](/doc/img/send_msg_02.png?raw=true "Send 02")

![Alt text](/doc/img/send_msg_03.png?raw=true "Send 03")


## Receive Msg

![Alt text](/doc/img/receive_01.png?raw=true "Send 01")

## I Don't Want My Contacts Stored On The Could!

We don't want it either! So we didn't!

The only information sent to the SubTexting server is: 1) Contact name and 2) the local id* of the contact. Plus they are only stored temporarely!

###"Local id of the contact? I don't get it.." 

Well! Let us explain! We don't want to be sending the number of your contacts around! So instead, we just pass the id of a contact. That Id is stored only on your device! Say you have a contact whose name is "John Smith" with the phone number: (574) 000 - xxxx. When you first saved that contact, your phone stored it with an id. Say the id is 234. Now, when you upload your contact so it can be accessed be the SubTexting, we won't be sending John's number. Instead, we'll send his id. In addition to that, the SubTexting server will store that information temporarely! Once you pull that information down using the plugin, that information will be deleted from our servers!
