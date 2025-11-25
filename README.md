## ThousandEyes Endpoint Agents Budget Calculator and Operational Enablement

This repository hosts a lightweight, browser‑only tool that helps you plan, license, and operate Cisco ThousandEyes Endpoint Agents (EPA). Open `index.html` directly or host it via GitHub Pages (workflow provided) to get a fully client‑side experience—no backend or build step required.

### Features
- **EPA Calculator** – Enter a budget, tiered pricing for Advantage/Essentials, and rounding preferences. The tool computes:
  - Maximum agents under the supplied budget (tier-aware)
  - Unspent budget and effective blended price (optional toggle)
  - Persistent values via `localStorage`
- **EPA Licensing** – Manage operational insights with:
  - API base/token/account group configuration + dry-run toggle
  - Agent tag filters and list endpoint path
  - Live counts of Advantage vs Essentials agents (simulated in dry-run mode)
- **EPA Scheduler** – Automate enabling/disabling agents by label:
  - Time-of-day schedules with wrap-around support (e.g., 18:00–08:00)
  - Adjustable polling frequency and dedicated endpoint path
  - Uses the same API credentials/dry-run toggle as Licensing
  - Shows current instructions and the latest action log

### Local Usage
1. Clone/download this repository.
2. Open `index.html` in any modern browser (Chrome, Edge, Safari, Firefox).
3. Configure the EPA Licensing tab with your ThousandEyes API base URL, token, account group, and tag filters.  
   - Keep “Dry run mode” enabled while experimenting; disable it only when ready to call production APIs.
4. Use the EPA Scheduler tab to define labels, time windows, and desired enable/disable actions. Leave the tab open for the scheduler to keep running.

### GitHub Pages Deployment
This repo includes `.github/workflows/deploy.yml`, which publishes the site to GitHub Pages whenever `main` is updated.

Steps:
1. Ensure Actions are enabled for the repository.
2. Push changes to `main`; the **Deploy site** workflow uploads the root of the repo (including `index.html`) as the Pages artifact.
3. The first successful run automatically provisions the `github-pages` environment and outputs the public URL (visible in the workflow summary).

> **Note:** Because everything is client-side, GitHub Pages hosting works without extra configuration. If you later add additional static assets (images, JS modules, etc.), keep them in the repo root so the workflow bundles them automatically.

### Security Considerations
- API tokens are stored only in the browser via `localStorage`.
- Always keep “Dry run mode” enabled until you’ve confirmed endpoint paths, request bodies, and desired behavior.
- If hosting publicly, avoid sharing real credentials in screencasts or documentation. Consider adding a banner reminding viewers to configure their own tokens.

### Contributing
Feel free to fork and adapt. If you add new flows (e.g., EPA inventory exports or alerting hooks), update the README and consider extending the GitHub Pages workflow to include those assets.

