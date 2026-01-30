# GitHub Knowledge Base

A curated local knowledge base of GitHub projects with automated internship/job tracking and notifications.

## Overview

This repository serves as a personal knowledge base for tracking interesting GitHub projects and automating job search workflows. It integrates with Claude Code's `github-kb` skill to provide intelligent project discovery and management.

## Features

### 1. Knowledge Base Management

- **Centralized Documentation**: All tracked projects are documented in `CLAUDE.md`
- **Claude Code Integration**: Use the `github-kb` skill to query and manage projects
- **Categorized Projects**: Organized by domain (Chat Bots, Docker, Internships, etc.)
- **Auto-Updated Metadata**: Tracks last update dates and key features

### 2. Automated Internship Tracking

Track and get notified about new internship/job postings from multiple sources:

#### Tracked Repositories
- **Summer2026-Internships**: 1,205+ internship positions (SimplifyJobs)
- **New-Grad-Positions-2027**: 361+ full-time positions (SimplifyJobs)

#### Notification Systems

**Discord Notifications** (Recommended)
```bash
./auto-update-internships-discord.sh
```
- Sends rich embed notifications to Discord webhook
- Shows company names and position counts
- Includes direct links to GitHub repo

**Email Notifications**
```bash
./auto-update-internships.sh
```
- Sends email alerts via macOS mail command
- Lists up to 20 new companies
- Includes local file path for quick access

#### Advanced Job Scrapers

**job-scraper** (Python)
- Scrapes LinkedIn, GitHub, and Simplify.jobs
- Monitors 10+ company career pages
- Discord + Email notifications
- See: `job-scraper/README.md`

**SimplifyJobsDaemon** (Go)
- Monitors SimplifyJobs repos in real-time
- Scrapes full job descriptions
- LLM-powered analysis and resume generation
- Desktop notifications
- See: `SimplifyJobsDaemon/README.md`

### 3. Docker Learning Resources

- **docker-tutorial**: Complete Chinese Docker tutorial with video guides
- **Compose-Examples**: 300+ Docker Compose examples for self-hosted apps

## Quick Start

### Setup Internship Notifications

1. **Configure Discord Webhook** (Recommended)
   ```bash
   # Follow the guide
   cat DISCORD_SETUP.md

   # Edit webhook URL in the script
   nano auto-update-internships-discord.sh
   ```

2. **Set up Cron Job** (Auto-run every 2 hours)
   ```bash
   ./setup-cron.sh
   ```

3. **Manual Test**
   ```bash
   ./auto-update-internships-discord.sh
   ```

### Using with Claude Code

The `github-kb` skill is automatically available in Claude Code when working in this directory.

**Example queries:**
```
"What Docker learning resources do we have?"
"Show me all internship tracking tools"
"Find repos related to job search automation"
"What's new in the Summer2026-Internships repo?"
```

**Adding new projects:**
1. Clone the repo into this directory
2. Update `CLAUDE.md` with project details
3. Claude Code will automatically index it

## Directory Structure

```
github-kb/
├── CLAUDE.md                          # Main knowledge base catalog
├── README.md                          # This file
├── DISCORD_SETUP.md                   # Discord webhook setup guide
├── DOCKER_LEARNING_GUIDE.md           # Docker resources overview
│
├── Summer2026-Internships/            # 1,205+ internship positions
├── New-Grad-Positions-2027/           # 361+ full-time positions
│
├── auto-update-internships-discord.sh # Discord notification script
├── auto-update-internships.sh         # Email notification script
├── setup-cron.sh                      # Cron job setup
│
├── job-scraper/                       # Python job scraper
├── SimplifyJobsDaemon/                # Go daemon with LLM analysis
│
├── docker-tutorial/                   # Chinese Docker tutorial
├── Compose-Examples/                  # 300+ Docker Compose examples
└── ClaudeBot/                         # IRC bot project
```

## Notification Script Details

### How It Works

1. **Fetch Updates**: `git fetch origin dev` from SimplifyJobs repos
2. **Compare Commits**: Check if remote has new commits
3. **Parse Diff**: Extract new company names and position counts
4. **Send Notification**: Discord webhook or email
5. **Pull Changes**: Update local repo

### Notification Behavior

- ✅ **Sends notification**: When remote has new commits
- ❌ **No notification**: When already up-to-date
- 📊 **Includes**: Company names, position count, GitHub link
- 📝 **Logs**: All activity to `internship-updates.log`

### Customization

Edit the scripts to customize:
- `DISCORD_WEBHOOK_URL`: Your Discord webhook
- `EMAIL_TO`: Your email address
- `REPO_DIR`: Path to internship repo
- Notification frequency (via cron)

## Advanced Usage

### Job Scraper Setup

For more aggressive job tracking with company-specific monitoring:

```bash
cd job-scraper
# Follow setup instructions in job-scraper/README.md
```

### SimplifyJobsDaemon Setup

For LLM-powered job analysis and auto-resume generation:

```bash
cd SimplifyJobsDaemon
# Follow setup instructions in SimplifyJobsDaemon/README.md
```

## Maintenance

### Update All Repos
```bash
# Update internship listings
cd Summer2026-Internships && git pull origin dev
cd ../New-Grad-Positions-2027 && git pull origin dev

# Update other projects
cd ../docker-tutorial && git pull
cd ../Compose-Examples && git pull
```

### Check Notification Logs
```bash
tail -f internship-updates.log
```

### Test Discord Webhook
```bash
curl -H "Content-Type: application/json" \
  -d '{"content": "Test notification from github-kb"}' \
  YOUR_DISCORD_WEBHOOK_URL
```

## Contributing to Knowledge Base

When adding new projects to the knowledge base:

1. Clone the repo into this directory
2. Update `CLAUDE.md` with:
   - Project name and path
   - Tech stack
   - Key features
   - Repository URL
   - Last updated date
3. Add any setup guides as separate `.md` files
4. Commit changes

## Resources

- [SimplifyJobs Summer 2026 Internships](https://github.com/SimplifyJobs/Summer2026-Internships)
- [SimplifyJobs New Grad Positions](https://github.com/SimplifyJobs/New-Grad-Positions)
- [Docker Tutorial (Chinese)](https://github.com/twtrubiks/docker-tutorial)
- [Compose Examples](https://github.com/Haxxnet/Compose-Examples)

## License

This is a personal knowledge base. Individual projects retain their original licenses.

---

**Last Updated**: 2026-01-29
**Maintained by**: Kyle
**Claude Code Skill**: `github-kb`
