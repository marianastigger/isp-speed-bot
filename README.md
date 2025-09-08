# isp-speed-bot
Automated Internet Speed Monitoring &amp; ISP Complaint Bot using Selenium and X

**Overview**

This Python script automatically measures your internet speed and tweets at your ISP whenever performance drops below the advertised rates. Inspired by the Comcast Bot project, it ensures your provider is held accountable in real time.

**Features**

- Authenticates into X/Twitter.
- Runs internet speed tests at configurable intervals.
- Compares measured speeds against your subscribed plan.
- Tweets a complaint directly to your ISP when speeds fall short.
- Easily customizable for different ISPs and speed thresholds.

**Setup**

To use this bot, you must:
- Sign up for an X/Twitter Developer Account.
- Create an application in the X Developer Portal.
- Generate your own consumer_key, consumer_secret, access_token, and access_token_secret.
- Store these credentials in a .env file before running.
