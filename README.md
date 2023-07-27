# Discord AI Chatbot with gpt-4 🤖
#### Your Discord AI Companion! and she is smart

<div align="center">
  <a href="https://discord.gg/FXMS2stUpq">
    <img src="https://discord.com/api/guilds/1104204401771544608/widget.png?style=banner2">
  </a>
</div>

## Features and commands 🌟

</details>

<details>
<summary><strong>Features ✨ (Click to expand) </strong></summary>

- [x] Hybrid Command System: Get the best of slash and normal commands. It's like a buffet! ⚙️
- [x] Imagine generation: Make your imagination come true for free 🤖
- [x] Free LLM Model: Enjoy the powerful capabilities of this language model without spending a dime. 🤖
- [x] Mention Recognition: The bot always responds when you mention it or say its name. It's as attentive as a squirrel spotting a shiny acorn! ⚙️
- [x] Message Handling: The bot knows when you're replying to someone else, so it won't cause confusion. It's like having a mind reader in your server! 🪄
- [x] Channel-Specific Responses: Use the `/toggleactive` command to chill the bot in a specific channel. ⚙️
- [x] GPT 4 model: Leverage the power of GPT model for advanced language processing capabilities. 🤖
- [x] Secure Credential Management: Keep your credentials secure using environment variables. 🔑
- [x] Web Access: Web Access is now available! Unlock a whole new level of awesomeness. 🌐
- [ ] YouTube Video Summarizer: This is a feature that utilizes the power of the Language Model (LLM) to generate summaries of YouTube videos. 🌐
- [ ] Speech recognition: Coming soon! Get ready for an LLM-powered voice assistant.

</details>

<details>
<summary><strong>Commands ⚙️⚙️ (Click to expand) </strong></summary>

- [x] `/help`: Get all other commands. ⚙️
- [x] `/imagine`: Generate an image using `Imaginepy` 🖼️
- [x] `/ping`: Get a "Pong" response from the bot. 🏓
- [x] `/setup`: Toggle active channels. 🔀
- [x] `/clear`: Clear the message history. 🗑️
- [x] `/support`: Need Support?
</details>

## Additional configuration ⚙️

<details>
<summary><strong>Enabling Internet access 🌐🔍(Click to Expand)</strong></summary>

To ensure that the bot has access to the most up-to-date information, you can enable internet access by setting the `INTERNET_ACCESS` parameter to true in the `config.yml` file. This will allow the bot to retrieve information beyond the data it was initially trained on, which was only available up until 2021.

You can also set the maximum search results. that is max of 204,800,000,000 but may take more ram cuz 204,800,000,000 takes 2GB of ram. very big. 10240 takes up 64MB of ram that is okay 
  
</details>

<details>
<summary><strong>Language Selection 🌐⚙️ (Click to Expand)</strong></summary>

To select a Language, set the value of `"LANGUAGE"` of `config.yml` with the valid Language Codes listed below:
  
- `en` - English
- `fr` - French

Your language not listed? Create an issue.
  
</details>

<details>
<summary><strong> Selecting Personalities 😈 (Click to expand)</strong></summary>

To select one of the pre-existing Personalities set the values of "INSTRUCTIONS" with the current values of `none` or `ProjectExperimentalprompt` in `config.yml`
  
- `none`: An GPT-4 Bot without anything. no personality. nothing just GPT-4 without anything that is stock openai gpt

- `ProjectExperimentalprompt`:  an Lily-gpt.ai clone beta channel personality is a reliable and neutral companion. 🤖

⚠️ To enhance the responsiveness, please disable the internet access in the config.yml file.

</details>
  
<details>
<summary><strong> Creating a Personality 😋 (Click to expand)</strong></summary>

To create a custom personality, follow these steps:
1. Create a `.txt` file like `custom.txt` inside the `instructions` folder.
2. Add the the way you want to bot to act in `custom.txt`
3. Open the `config.yaml` file and locate [line 12](https://github.com/mishalhossin/Discord-AI-Chatbot/blob/2626075fda36fa6463cb857d9885e6b05f438f60/config.json#L12).
4. Set the value of INSTRUCTIONS at [line 12](https://github.com/mishalhossin/Discord-AI-Chatbot/blob/2626075fda36fa6463cb857d9885e6b05f438f60/config.json#L12) as `"custom"` to specify the custom persona.

  
⚠️ You don't explicitly need use the name `custom` for persona name and set it in `config.json` 
  
</details>

# Installation steps  🚩
### Step 1. 🎬 Git clone repository
```
git clone https://github.com/NotKaty/gpt-4freeapidiscordbot
```
### Step 2. 📁 Changing directory to cloned directory
```
cd gpt-4freeapidiscordbot
```
## Step 3. 💾 Install requirements
```
python3.10 -m pip install -r requirements.txt
```
### Step 4. 🔑 Getting discord bot token and enabling intents from [HERE](https://discord.com/developers/applications)
<details>
<summary><strong>Read more...  ⚠️  (Click to expand)</strong></summary>


##### Select [application](https://discord.com/developers/applications)

##### Enable intents. but all the intents


##### Get the token (You know that idiot)


### Step 4.
<strong>Getting a Free Reverse OpenAI proxy Key 🔑

Follow these steps:

1. Join the Discord server by clicking on the following invite link: [KeyNoteAPI](https://discord.gg/aMmnvHyh)
2. Once you have joined the server, run the `/key-get` command in any text channel.
3. This command will provide you with a reverse OpenAI key. Remove kn- and go put it in

You can additionally enable `gpt-4` in `config.yml`
</strong>

### Step 5. 🔐 Rename `example.env` to `.env` and put the Discord bot token and your KeyNote API It will look like this:
```
DISCORD_TOKEN=
KeyNoteAPI=YourAPIKey

# Get Your API KEY at https://discord.gg/FXMS2stUpq or it will not run without a api key
# Katy is owner of this bot and u need api key to run bot
```
### Step 6. 🚀 Run the bot
```
python main.py
```
#### You may need to run as admin if you are on windows
### Step 7. 🔗 Invite the bot 
You can Invite your bot using the link in console
![image](https://user-images.githubusercontent.com/91066601/236673317-64a1789c-f6b1-48d7-ba1b-dbb18e7d802a.png)

#### There are 2 ways to talk to the AI
- Invite your bot and DM (Direct message) it | ⚠️ Make sure you have DM enabled in confing.yaml
- if you want it in server channel use **/setup** 
- For more awesome commands use **/help**


### Crafted with Care: Made with lots of love and attention to detail. ❤️
