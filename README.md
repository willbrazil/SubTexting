# SubTexting - Send and receive text messages through Sublime

Sublime Text 3 plugin which allows users to send and receive text messages. (Android Only)

If you'd like to design an icon for the Android app/this project. Check out [this issue](https://github.com/wguedes01/subtexting-app/issues/1).

Feel free to contact me if you have any issues: **willbrazil.usa@gmail.com**

## Setup

### Installing the Plugin

#### Using <a href='https://packagecontrol.io/'>Sublime Package Manager</a>
<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> -> **Package Control: Install Package** -> **SubTexting**

#### Manually
Clone this repo into your Sublime packages folder.

---

#### Creating an account

<kbd>CTRL</kbd> + <kbd>SHIFT</kbd> + <kbd>P</kbd> -> **SubTexting: Sign Up**

Insert username and your phone number and you should then receive a confirmation
 text message with a key code.

Once you've received your key, press

<kbd>CTRL</kbd> + <kbd>SHIFT</kbd> + <kbd>P</kbd> -> **SubTexting: Verify**

and insert the confirmation code you've received.

---

#### Installing the Android App

[Download the app from the Play Store](https://play.google.com/store/apps/details?id=will.subtexting)

Use the key you've received to log in the app and select the contacts you'd like SubTexting to know about.

SubTexting <b>DOES NOT</b> store the phone numbers of your contacts! To learn more information about how we store your information, see the [I Don't Want My Contacts Stored In The Cloud!](#i-dont-want-my-contacts-stored-in-the-cloud)

---

#### Loading Contacts Onto SubTexting

Once you've loaded your contacts through the Android app, press

<kbd>CTRL</kbd> + <kbd>SHIFT</kbd> + <kbd>P</kbd> -> **SubTexting: Load Contacts**

This will download the uploaded contacts to SubTexting.

## Usage

#### Sending Messages

<kbd>CTRL</kbd> + <kbd>SHIFT</kbd> + <kbd>P</kbd> -> SubTexting: Send Message

![Sending Message](/doc/img/send_msg_01.png?raw=true "Send 01")

![Choosing a contact](/doc/img/send_msg_02.png?raw=true "Send 02")

![Typing text message](/doc/img/send_msg_03.png?raw=true "Send 03")

---

#### Receiving Messages

#### **STILL UNDER DEVELOPMENT. Feature not stable.**


## I Don't Want My Contacts Stored In The Cloud!

We don't want your contacts either!

The only information sent to the SubTexting server is:

1.  Contact name and
2.  The "local ID" of the contact. Plus they are only stored temporarily!

### "Local ID" of the contact?

Well! Let us explain!

We don't want to be sending the number of your contacts around! So instead, we just pass the id of a contact.

That id is stored only on your device! Say you have a contact whose name is "John Smith" with the phone number: 123-456-7890. When you first saved that contact, your phone stored it with an id. Say the id is `234`. Now, when you upload your contact so it can be accessed be the SubTexting, we won't be sending John's number. Instead, we'll reference his id. In addition to that, the SubTexting server will store that information temporarily!

Once you fetch that information down using the plugin, that information is deleted from our servers!
