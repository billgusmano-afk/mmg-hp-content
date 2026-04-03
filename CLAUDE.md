# MMG HP Content Engine — Claude Code Master Context
# Updated: April 2026
# READ THIS FULLY before doing anything.
# This file is the communication bridge between Claude Chat and Claude Code.
# Claude Chat updates this file when decisions are made.
# Claude Code reads this automatically every session.

---

## WHO YOU ARE WORKING FOR

Company: The Motivated Mind Group (MMG)
Owner: Bill Gusmano (bill.gusmano@themotivatedmindgroup.com)
GitHub: https://github.com/billgusmano-afk/mmg-hp-content
Live dashboard: https://billgusmano-afk.github.io/mmg-hp-content
Client: HP Inc. consumer products

---

## MMG BRAND — ALWAYS USE THIS

Primary: Master Pink #FF97A9 · Black #1D1D1B · White #FFFFFF
Secondary: Lavender #8A5FBE · Light Green #B4EBCA · Yellow #F5E663
           Light Blue #BCF4F5 · Medium Slate Blue #8075FF
Fonts: Source Serif Pro (headings) · Open Sans (body)
Background: Warm cream #F8F4F1
HP Blue #0096D6 = HP's color only. NEVER use as MMG primary.
NEVER use navy #0A1628 or cyan #00C8FF — those are wrong brand colors.

---

## MMG TEAM

Bill Gusmano     bill.gusmano@themotivatedmindgroup.com  Owner · Final approver · CAN flag HP
Jeff             Jeff@themotivatedmindgroup.com          Account Manager · CAN flag HP
Bryan            Bryan@themotivatedmindgroup.com         Creative Director · CAN flag HP
Deni             Deni@themotivatedmindgroup.com          Project Manager · CAN flag HP
Rob              Rob@themotivatedmindgroup.com           Content Creator · CAN flag HP
Tracy            Tracy@themotivatedmindgroup.com         Visual Designer · CANNOT flag HP
Paul             Paul@themotivatedmindgroup.com          Creative Dir/Visual · CANNOT flag HP

Dashboard login: first name (bill, jeff, etc.) OR full email + password: hp2025
Bill has FINAL approval on all assets before HP sees them.

---

## HP CONTENT PIPELINE

Monthly target: 3 TikToks + 4 Memes
Categories (rotate, never repeat same category 2 months in a row):
  1. Ink-InstantInk-Tank
  2. Laptops-Desktops-PCs
  3. Printers-Scanners-MFP
  4. Monitors
  5. Accessories

Workflow stages:
  01-AI-Draft → 02-MMG-Review → 03-Approved-Internal → 04-Client-Feedback → 05-FINAL

File naming: [Type]_[Category]_[###]_[Stage].[ext]
Example: Meme_InkInstantInkTank_003_Draft.jpg

---

## BOX STORAGE — ALL LIVE IN BILL'S ACCOUNT

Root: HP-Content-Engine (ID: 374589121452)
URL: https://app.box.com/folder/374589121452

### April 2026 (current batch) — ID: 374603913307
Ink-InstantInk-Tank:
  draft:374600284092 review:374603080762 approved:374602727145
  client:374603644738 final:374603564671

Laptops-Desktops-PCs:
  draft:374603776671 review:374603521444 approved:374600163635
  client:374598222237 final:374604032964

Printers-Scanners-MFP:
  draft:374602221381 review:374603288886 approved:374603649384
  client:374601851573 final:374604478863

Monitors:
  draft:374599525775 review:374603778599 approved:374600032308
  client:374600068484 final:374600233495

Accessories:
  draft:374602655660 review:374598122307 approved:374602158523
  client:374599381401 final:374601849583

### March 2026 — ID: 374604714372
Ink: draft:374605514345 review:374604606219 approved:374605540716
Laptops: draft:374603051147 review:374604822961 approved:374604772062
Printers: draft:374606411798 review:374606975294 approved:374606065462
Monitors: draft:374607621068 review:374606866868 approved:374605677257
Accessories: draft:374607097601 review:374605674356 approved:374605098219

### May 2025 (archive) — ID: 374587418151
Ink: draft:374590983871 | Laptops: draft:374592210038
Printers: draft:374591927364 | Monitors: draft:374594182862
Accessories: draft:374591984867

Real files confirmed in April 2026 Ink draft:
  Meme_InkInstantInkTank_003_Draft.jpg (ID: 2185779801496)
  TikTok_InkInstantInkTank_001_Draft_ConceptCard.jpg (ID: 2185682367976)
  TikTok_InkInstantInkTank_001_Draft_Script.txt (ID: 2185683275148)

Box comments confirmed working — used as permanent activity log.
When a file is uploaded or approved, write a Box comment with:
  [action] · [date/time] · Category: [cat] · Batch: [month] · File: [name]

---

## DASHBOARD — index.html

Single HTML file — NO build process, NO server needed.
Deploy by dragging index.html to GitHub (commits to main branch).
GitHub Pages auto-deploys from main branch root.

CRITICAL deployment rules:
  - Deploy ONLY index.html — never a folder, never with netlify.toml
  - Box API called directly from browser — no server/functions needed
  - Netlify account is SUSPENDED (used free credits) — do NOT use Netlify

Box connection in dashboard:
  - After login, user pastes Box developer token into Connect modal
  - Token stored in sessionStorage (session only, not committed)
  - Approve/Reject/Flag call Box API directly from browser
  - All actions write permanent Box comments
  - Activity log reads Box comments as audit trail
  - Upload sends files directly to Box upload API

Login: first name OR full email + hp2025
HP client portal: REMOVED — internal MMG tool only for now

Dashboard features:
  ✓ Monthly accordion in Content Review (April open, March collapsed)
  ✓ Monthly accordion in Approvals Log
  ✓ Activity Log tab with Box comment integration
  ✓ Box Storage tab — 100 folders, all clickable
  ✓ Upload Asset — 4-step flow routing to correct Box folder
  ✓ Team Members tab with roles and permissions
  ✓ Connect to Box modal after login
  ✓ Reconnect Box in sidebar for token refresh

---

## GITHUB WORKFLOW (Chat ↔ Code bridge)

When Claude Chat makes changes:
  1. Chat builds/updates files
  2. Chat tells you what changed and what to commit
  3. You run in Claude Code: git add . && git commit -m "description" && git push
  4. GitHub Pages updates the live site automatically

When Claude Code makes changes:
  1. Code edits files in the cloned repo folder
  2. Code runs: git add . && git commit -m "description" && git push
  3. Live site updates, Chat can see latest version

ALWAYS run git pull at the start of every Claude Code session:
  cd mmg-hp-content && git pull

---

## CURRENT STATUS (April 2026)

✓ Box: 100 folders live across 4 months
✓ Dashboard: Built with real MMG brand, Box connection
✓ Team: Emailed with login instructions
✓ Feedback received from Paul and Tracy — addressed in v2
✓ GitHub repo: billgusmano-afk/mmg-hp-content (making public)
→ Next: Complete Box connection testing
→ Next: Send team update email with list of improvements
→ Future: Option 3 full backend when MMG grows

---

## MONTHLY PIPELINE (run_monthly.py)

Run on 1st of each month from the mmg-hp-content folder.
Generates 7 assets → uploads to Box 01-AI-Draft → notifies team.
Reads history.json to avoid repeating formats/categories.
Requires .env with ANTHROPIC_API_KEY and BOX_DEVELOPER_TOKEN.

Last batch: April 2026
  Categories used: Ink, Laptops, Printers, Monitors
  Formats used: drake, green_screen, couple_relatable, comparison, pov, duet, iykyk
