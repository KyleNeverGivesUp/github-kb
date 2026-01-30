# Discord Webhook Setup (1 minute)

## Step 1: Create Discord Webhook

1. Open Discord (desktop or web)
2. Go to any server you're in (or create a new one)
3. Right-click on a text channel → "Edit Channel"
4. Go to "Integrations" → "Webhooks"
5. Click "New Webhook"
6. Name it: "Internship Tracker"
7. Click "Copy Webhook URL"
   - It looks like: https://discord.com/api/webhooks/123456789/abcdefg...

## Step 2: Configure Script

```bash
nano /Users/kyle/Projects/github-kb/auto-update-internships-discord.sh
```

Find this line:
```
DISCORD_WEBHOOK_URL=""
```

Change to:
```
DISCORD_WEBHOOK_URL="paste-your-webhook-url-here"
```

Save: Ctrl+X, Y, Enter

## Step 3: Test

```bash
/Users/kyle/Projects/github-kb/auto-update-internships-discord.sh
```

Check Discord - you should see a notification!

## Step 4: Update Cron Job

```bash
crontab -e
```

Change the script path to:
```
/Users/kyle/Projects/github-kb/auto-update-internships-discord.sh
```

---

## Why Discord?

✅ Setup in 1 minute (vs 5+ minutes for Gmail)
✅ Mobile push notifications
✅ No email spam folder issues
✅ Rich formatting with embeds
✅ Can use alongside Gmail (dual notifications)

---

## Need Help?

If you don't have Discord:
1. Download: https://discord.com/download
2. Create account (free)
3. Create a server (click + button)
4. Follow steps above
