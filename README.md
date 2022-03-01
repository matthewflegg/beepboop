# 🤖 Beep Boop Bot Documentation
Welcome to the official documentation for Beep Boop Bot.

Beep Boop Bot is provided under the *GNU General Public License 3.0*. This means you can run, share, study and modify the software as you wish. While you don't technically have to, if you use the souce code for this bot credit would be appreciated.

## 📒 Contents

1. [Getting Started](#🚀GettingStarted)
2. [Commands List](#📕CommandsList)

## 🚀 Getting Started

### ✔️ Pre-requisites
These steps need to be completed to set up the bot.
See [Resources](#Resources) for more information.

* An installation of **Python 3.9.7+**
* A **Discord API application with a bot added**

### ✔️ Setting Up the Bot For Self-Hosting

1. Verify your Python installation
On Windows, run:
<pre>python --version</pre>
Or, if you're on Linux, run:
<pre>python3 --version</pre>
2. Clone the Git Repository           

Run:
<pre>gh repo clone matthewflegg/beepboop</pre>
3. Navigate to the root directory, "./beepboop/".         

Depending on where the repository is on your machine, this may look different
<pre>cd beepboop</pre>
4. Install the bot's dependencies
<pre>pip install -r dependencires.txt</pre>
5. Create a .env file
On Windows:
<pre>notepad .env</pre>
If a window pops up and says "Cannot find the .env file. Do you want to create a new file?", click yes           
Write the following into the file, replace the [your_token] with your bot's token:
<pre>TOKEN=[your_token]</pre> 
On Linux:
Use the text editor of your choice:
<pre>vim .env</pre>
Press I to enter write mode, type:
<pre>TOKEN=[your_token]</pre>
Then press ESC, and type the following to save and exit:
<pre>:x ! sudo tee %</pre>
6. Run the bot         

On Windows, run:
<pre>python app.py</pre>
Or, on Linux, run:
<pre>python3 app.py</pre>

## 📕 Commands List

### 📄 Help/Docs
Commands for help and documentation

##### .docs
Sends an embed linking to this page
<pre>Usage: .docs</pre>

##### .help
Displays the default help message, showing all the commands. The official documentation (this page) is recommended, however, as it's a lot more helpful
<pre>Usage: .help</pre>

### 📢 Admin
Commands for administrators, mods, etc.

##### .ban
Bans a user from a server. Requires the 'Ban members' permission
<pre>Usage: .ban [discord user to ban] [reason (optional)]</pre>

##### .kick
Kicks a user from a server. Requires the 'Kick members' permission
<pre>Usage: .kick [discord user to kick] [reason (optional)]</pre>

##### .restrict
Assigns a role called 'Restrict' to a user. This role must exist on the server already - you can configure the restrictions however you'd like. Requires 'Manage roles' permission
<pre>Usage: .restrict [discord user to restrict] [duration in seconds]</pre>

### 👋 Greetings
Greeting related commands

##### .hello
Replies with hello to the user of the command. Replies with hello again if used twice in a row
<pre>Usage: .hello -> Beep Boop Bot: "Hello [user]!"</pre>
Alternatively, if you use it twice in a row:
<pre>-> Beep Boop Bot: "Hello again, [user]"</pre>

The greetings category also contains an event listener that mentions a user with a welcome message when they join a server. Currently, the welcome message is not customisable. However, this feature will be added

### ❓ Miscellaneous
Misc. commands for doing dumb stuff

##### .choose
Chooses a random option from a list.
<pre>Usage: .choose a b c -> Beep Boop Bot: "a"</pre>
If you're using more than one word as an option, use "" so the bot knows where one option starts and another ends
<pre>Usage: .choose "option a" "option b" "option c" -> Beep Boop Bot: option c</pre>

##### .russianroulette
Has a 1 in 6 chance of kicking the user
<pre>Usage: .russianroulette -> (NO KICK) Beep Boop Bot: "You were lucky... This time ;)"</pre>
If the user was unlucky and got kicked:
<pre>-> (KICK) Beep Boop Bot: "Oops... You lost"</pre>

##### .meme
Gets a random meme from Reddit
<pre>Usage: .meme</pre>

##### .beep
Beep Boop Bot replies with "boop"
<pre>Usage: .beep</pre>
