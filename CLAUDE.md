# GitHub Knowledge Base

This directory contains a local knowledge base of GitHub projects.

---

## Chat Bots

### [ClaudeBot](/ClaudeBot)
A general-purpose IRC bot powered by GitHub's Hubot, integrating multiple web API functionalities.
**Updated:** 2026-01-27

- **Tech Stack**: Node.js, Hubot, IRC
- **Key Features**:
  - IRC adapter support, deployed on FyreChat network
  - Redis persistence for brain data (in-memory key-value store)
  - Integrates multiple Hubot plugins: Google search/translate/images, YouTube, Wikipedia, Steam, Twitch, etc.
  - Supports custom script extensions (CoffeeScript)
- **Deployment**: Configured for Heroku deployment, supports local execution
- **Repository**: https://github.com/ClaudeBot/ClaudeBot

---

## Docker & Container Learning

### [Compose-Examples](/Compose-Examples)
A comprehensive collection of 300+ Docker Compose examples covering various self-hosted FOSS and proprietary projects.
**Updated:** 2026-01-28

- **Tech Stack**: Docker, Docker Compose
- **Key Features**:
  - 300+ ready-to-use Docker Compose examples organized by category
  - Covers wide range of applications: web servers, databases, monitoring, media servers, development tools, etc.
  - Each example includes docker-compose.yml with detailed comments and configuration notes
  - Categories include: Analytics, Automation, Backups, Blogging, Communication, DNS, File Transfer, Identity Management, Monitoring, Password Managers, Proxies, Security, VPN, Wikis, and more
  - Practical examples for learning Docker networking, volumes, environment variables, and multi-container applications
- **Learning Path**: Start with simple examples (nginx, databases) then progress to complex multi-container stacks (monitoring, media servers)
- **Repository**: https://github.com/Haxxnet/Compose-Examples

---

# GitHub Knowledge Rules

When the user asks about GitHub repositories, issues, or pull requests:

- Prefer using `gh` CLI instead of guessing
- Use `gh search repos` to find projects
- Use `gh search issues` to find issues
- Use `gh search prs` to find pull requests
- Summarize results clearly after running commands

Do not hallucinate GitHub data.
