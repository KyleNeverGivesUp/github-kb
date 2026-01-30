#!/bin/bash

# Discord webhook notification script for internship updates

# Configuration
REPO_DIR="/Users/kyle/Projects/github-kb/Summer2026-Internships"
LOG_FILE="/Users/kyle/Projects/github-kb/internship-updates.log"
DIFF_FILE="/tmp/internship-diff.txt"
DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/1466595869175578716/4B7F9ytNsBa-8A0Xc7_2ZthQRBB7Hnl5_9DaiViLAp_Df6nINUEsRz2z3T9d5yIfkp96"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo "========================================" | tee -a "$LOG_FILE"
echo "$(date): Checking for new internships..." | tee -a "$LOG_FILE"

# Navigate to repo
cd "$REPO_DIR" || exit 1

# Get current commit hash
OLD_COMMIT=$(git rev-parse HEAD)

# Fetch latest changes
git fetch origin dev

# Check if there are updates
NEW_COMMIT=$(git rev-parse origin/dev)

if [ "$OLD_COMMIT" = "$NEW_COMMIT" ]; then
    echo -e "${YELLOW}No new updates found.${NC}" | tee -a "$LOG_FILE"
    exit 0
fi

# Get the diff of new positions
git diff HEAD origin/dev README.md > "$DIFF_FILE"

# Count new positions
NEW_POSITIONS=$(grep -c "^+<td><strong><a href" "$DIFF_FILE" || echo "0")

echo -e "${GREEN}Found $NEW_POSITIONS new internship postings!${NC}" | tee -a "$LOG_FILE"

# Pull the changes
git pull origin dev

# Extract new company names
NEW_JOBS=$(grep "^+<td><strong><a href" "$DIFF_FILE" | sed 's/.*company">\(.*\)<\/a>.*/\1/' | head -10 | tr '\n' ', ' | sed 's/, $//')

# Send Discord notification
if [ -z "$DISCORD_WEBHOOK_URL" ]; then
    echo -e "${RED}Discord webhook URL not set.${NC}" | tee -a "$LOG_FILE"
    echo -e "${YELLOW}Please add your webhook URL to the script.${NC}" | tee -a "$LOG_FILE"
else
    DISCORD_MESSAGE="{
        \"embeds\": [{
            \"title\": \"🚨 $NEW_POSITIONS New Summer 2026 Internships!\",
            \"description\": \"New positions just posted!\",
            \"color\": 3447003,
            \"fields\": [
                {
                    \"name\": \"Companies\",
                    \"value\": \"$NEW_JOBS \",
                    \"inline\": false
                },
                {
                    \"name\": \"View All Positions\",
                    \"value\": \"[GitHub Repo](https://github.com/SimplifyJobs/Summer2026-Internships)\",
                    \"inline\": false
                }
            ],
            \"timestamp\": \"$(date -u +%Y-%m-%dT%H:%M:%S.000Z)\"
        }]
    }"

    HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" -H "Content-Type: application/json" \
        -d "$DISCORD_MESSAGE" \
        "$DISCORD_WEBHOOK_URL")

    if [ "$HTTP_CODE" = "204" ]; then
        echo -e "${GREEN}Discord notification sent successfully!${NC}" | tee -a "$LOG_FILE"
    else
        echo -e "${RED}Failed to send Discord notification (HTTP $HTTP_CODE)${NC}" | tee -a "$LOG_FILE"
    fi
fi

# Display summary
echo "========================================" | tee -a "$LOG_FILE"
echo "Summary:" | tee -a "$LOG_FILE"
echo "- New positions: $NEW_POSITIONS" | tee -a "$LOG_FILE"
echo "- Companies: $NEW_JOBS" | tee -a "$LOG_FILE"
echo "- Updated at: $(date)" | tee -a "$LOG_FILE"
echo "========================================" | tee -a "$LOG_FILE"

# Clean up
rm -f "$DIFF_FILE"
