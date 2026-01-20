# ThousandEyes Tools User Guide

Welcome to the ThousandEyes Endpoint Agents Budget Calculator and Operational Enablement tools. This guide provides comprehensive documentation for each tool in this application.

## Table of Contents

1. [Getting Started](#getting-started)
2. [EPA Calculator](#epa-calculator)
3. [EPA Licensing](#epa-licensing)
4. [EPA Scheduler](#epa-scheduler)
5. [Cloud and App Synthetics Calculator](#cloud-and-app-synthetics-calculator)
6. [Cloud and Traffic Insight Flow Calculator](#cloud-and-traffic-insight-flow-calculator)
7. [Common Features](#common-features)

---

## Getting Started

### Accessing the Application

1. Open `index.html` in any modern web browser (Chrome, Edge, Safari, Firefox)
2. The application loads with all settings saved in your browser's local storage
3. Use the sidebar navigation to switch between different tools

### Global Features

**Currency Selector** (Sidebar):
- Select from USD, EUR, JPY, AUD, or MXN
- Click "Update Rates" to fetch the latest exchange rates
- Currency preferences apply across all tools
- Exchange rates are cached for 1 hour

**Theme Toggle**:
- Click the moon/sun icon (🌙/☀️) in the top-right corner to switch between dark and light themes
- Theme preference is saved automatically

---

## EPA Calculator

### Overview
The EPA Calculator helps you determine how many Endpoint Agents you can purchase within your budget, considering tiered pricing for both Advantage and Essentials licenses.

### Features
- **Tiered Pricing Support**: Calculates costs based on quantity tiers
- **Round Down or Nearest**: Choose how to round agent counts
- **Multi-Currency Support**: View results in different currencies
- **Effective Average Price**: See the blended price per agent when using tiered pricing

### Step-by-Step Guide

#### 1. Enter Your Budget
- Enter your total budget in the "Budget" field
- The budget will be used to calculate maximum agents for both Advantage and Essentials

#### 2. Configure Pricing

**Option A: Simple Pricing (No Tiers)**
- Enter a single price per agent for Advantage in "Price (Advantage)"
- Enter a single price per agent for Essentials in "Price (Essentials)"
- The calculator uses these prices directly

**Option B: Tiered Pricing**
- Click "Add Tier" under either Advantage or Essentials sections
- Enter the tier threshold (e.g., "up to 249 agents") and price per agent for that tier
- Add multiple tiers (e.g., 1-249, 250-499, 500+)
- The calculator applies the appropriate tier price based on quantity

**Resetting Tiers:**
- Click "Reset to defaults" to restore standard tiered pricing

#### 3. Set Rounding Preference
- **Round Down**: Always rounds down to the nearest whole number (conservative estimate)
- **Round Nearest**: Rounds to the nearest whole number (may exceed budget slightly)

#### 4. View Results
The calculator displays:
- **Maximum agents** you can purchase for Advantage
- **Maximum agents** you can purchase for Essentials
- **Unspent budget** for each license type
- **Effective average price** (optional) - toggle "Show average price per agent" to see blended rates

#### 5. Multi-Currency View (Optional)
- Enable "Show multi-currency comparison" to see results in USD, EUR, JPY, AUD, and MXN
- Requires fetching exchange rates first using the sidebar "Update Rates" button

### Example Use Case

**Scenario:** You have a budget of $10,000 and want to purchase Advantage licenses.

1. Enter `10000` in the Budget field
2. Use tiered pricing:
   - Tier 1: 1-249 agents at $14.60/agent
   - Tier 2: 250-499 agents at $13.00/agent
   - Tier 3: 500+ agents at $11.75/agent
3. Select "Round Down" for conservative estimates
4. Results show you can purchase approximately 833 agents at an effective price of $12.00/agent

---

## EPA Licensing

### Overview
The EPA Licensing tool allows you to manage and monitor Endpoint Agent licenses through the ThousandEyes API. You can view current license counts and filter agents by account group and labels.

### Prerequisites
- **API Proxy Server Running**: The Python proxy server must be running (see Setup below)
- Valid ThousandEyes API token
- Access to at least one ThousandEyes Account Group

### Setup

**Start the API Proxy Server** (Required):
1. Install Python dependencies: `pip install -r requirements.txt`
2. Start the proxy: `python3 api_proxy.py`
3. The server runs on `http://localhost:5000` by default
4. See `README_API_PROXY.md` for detailed setup instructions

The proxy server is required because browsers block direct API calls to external domains due to CORS (Cross-Origin Resource Sharing) security restrictions.

### Step-by-Step Guide

#### 1. Enter API Token

**API Key (Token):**
- Enter your ThousandEyes Bearer token in the "API Key" field
- **Security Note:** Tokens are stored only in your browser's local storage
- Never share your token or commit it to version control
- After entering your token, click "Load Account Groups" to fetch available account groups

#### 2. Select Account Group

**Account Group:**
- Click "Load Account Groups" button to fetch account groups from the API
- The dropdown will populate with available account groups
- Each entry shows the account group name and ID: `Account Name (ID)`
- Select your desired account group from the dropdown
- **Note:** Labels will automatically populate once an account group is selected

#### 3. Select Labels (Optional)

**Labels:**
- After selecting an account group, the Labels dropdown automatically populates with available labels
- Hold **Ctrl** (Windows/Linux) or **Cmd** (Mac) to select multiple labels
- Selected labels filter which agents are included in license counts
- **Leave empty** to include all agents in the account group
- You can deselect all labels by clicking elsewhere

#### 4. Dry Run Mode (Recommended)
- **Always enable "Dry run mode" initially** to test without making actual API calls
- In dry run mode, the tool simulates actions and logs what would happen
- Disable only when ready to perform real API operations

#### 5. Refresh License Counts
- Click "Refresh license counts" to fetch current agent counts from the API
- Results display:
  - **Advantage agents (current)**: Count of agents with Advantage licenses
  - **Essentials agents (current)**: Count of agents with Essentials licenses
  - **Last refresh status**: Timestamp and success/error message

**Troubleshooting:**
- If account groups don't load, verify the API proxy server is running
- Check browser console (F12) for detailed error messages
- Verify your API token is correct and has appropriate permissions

### Use Cases

**Monitoring License Distribution:**
1. Start the API proxy server
2. Enter your API token and click "Load Account Groups"
3. Select an account group from the dropdown
4. Optionally select labels to filter specific agent groups
5. Enable dry run mode
6. Click "Refresh license counts"
7. Review the current distribution of Advantage vs Essentials licenses

**Filtering by Organization:**
- Use the account group dropdown to switch between different organizations
- Each organization's labels will load automatically
- Filter agents by selecting specific labels (multi-select)

**Filtering by Labels:**
- Select one or more labels to filter agents
- Only agents matching the selected labels will be counted
- Useful for segmenting agents by department, location, or function

### Security Best Practices
- Always use dry run mode when testing
- Never share screenshots or recordings showing your API token
- Consider using read-only API tokens for monitoring operations
- Keep the API proxy server local or in a trusted environment
- The proxy server does not store tokens but forwards them to ThousandEyes API

---

## EPA Scheduler

### Overview
The EPA Scheduler automates enabling and disabling Endpoint Agents based on time-of-day schedules and labels. This is useful for cost optimization by turning off agents during non-business hours.

### Key Features
- Time-based scheduling with wrap-around support (e.g., 18:00 to 08:00)
- Label-based agent management
- Multiple schedules organized by organization name
- Automatic polling and execution
- Real-time status display

### Step-by-Step Guide

#### 1. Enable the Scheduler
- Navigate to the "EPA Scheduler" tab
- Check the "Scheduler" checkbox to enable automatic execution
- **Note:** The scheduler only runs while the page is open in your browser

#### 2. Configure Check Frequency
- Set "Check frequency (seconds)" to how often the scheduler should evaluate schedules
- Minimum: 15 seconds
- Recommended: 60 seconds for most use cases
- Lower values check more frequently but use more API calls

#### 3. Create a Schedule

Click "Add schedule" to open the Label Management modal:

**Authentication:**
- Enter your **Account ID** (Account Group ID)
- Enter your **Authentication Token** (ThousandEyes API Bearer token)

**Creation Mode:**
- **Create single label**: Add one label schedule
- **Create multiple labels**: Add multiple labels at once

**For Single Label:**
1. Enter the **Label Name** (e.g., `production-servers`)
2. Select **Enable** or **Disable** action
3. Set **From** time (start of schedule window)
4. Set **To** time (end of schedule window)
5. Click "Create Schedule"

**For Multiple Labels:**
1. Click "Add Another Label" to add more label entries
2. Fill in label name, action, and time window for each
3. Click "Create Schedule" to save all at once

**Time Window Tips:**
- Use 24-hour format (e.g., 18:00, 09:00)
- **Wrap-around support**: If "To" time is earlier than "From" time, the schedule spans midnight
  - Example: From `18:00` to `08:00` means 6 PM to 8 AM the next day
- Multiple schedules for the same label can be combined

#### 4. Edit or Delete Schedules
- Click **Edit** on any schedule row to modify it
- Click **Delete** on any schedule row to remove it (requires confirmation)
- Schedules are organized by **Organization Name** (derived from Account Group ID)

#### 5. Monitor Scheduler Status

**Active Instructions Right Now:**
- Shows which labels are currently being enabled or disabled based on active schedules
- Updates in real-time as schedules trigger

**Scheduler Log:**
- Displays detailed log of all scheduler actions
- Includes timestamps, labels affected, and actions taken
- Shows API call results and any errors
- Logs auto-scroll to show the latest entries

### Example Scenarios

**Scenario 1: Business Hours Only**
- Label: `development-agents`
- Action: Enable
- From: `09:00`
- To: `17:00`
- Result: Agents are enabled during business hours (9 AM to 5 PM)

**Scenario 2: Nighttime Shutdown**
- Label: `cost-optimization`
- Action: Disable
- From: `18:00`
- To: `08:00`
- Result: Agents are disabled overnight (6 PM to 8 AM)

**Scenario 3: Multiple Organizations**
- Create schedules for different Account Group IDs
- Each organization's schedules are grouped together
- You can collapse/expand organization groups to organize schedules

### Best Practices
- **Start with dry run mode** enabled in the EPA Licensing tab (scheduler uses the same setting)
- Test schedules during low-impact periods first
- Monitor the scheduler log for any errors or unexpected behavior
- Keep the browser tab open for schedules to execute
- Use descriptive label names to clearly identify agent groups

### Troubleshooting
- **Scheduler not running**: Ensure the "Scheduler" checkbox is enabled
- **API errors**: Check your API token and Account Group ID in the modal
- **No actions taken**: Verify your time windows and ensure the current time falls within a schedule window
- **Label not found**: Ensure the label exists in your ThousandEyes account

---

## Cloud and App Synthetics Calculator

### Overview
The Cloud and App Synthetics Calculator helps you estimate the number of units required for different types of ThousandEyes synthetics tests, considering agent type, test intervals, and test-specific parameters.

### Supported Test Types
- **BGP**: Border Gateway Protocol tests
- **Network (Agent-to-Server)**: Network connectivity tests from agents to servers
- **Network (Agent-to-Agent)**: Bidirectional network tests between agents
- **DNS Server**: DNS resolution tests
- **DNS Trace**: DNS delegation chain tests
- **HTTP Server**: HTTP/HTTPS availability and performance tests
- **Page Load**: Full web page load tests with browser rendering
- **Transaction**: Multi-step web transaction tests
- **SIP-RTP**: Session Initiation Protocol and Real-time Transport Protocol tests
- **Voice Calls**: Voice call quality tests

### Key Concepts

**Cloud Units (C) vs Enterprise Units (E):**
- **Cloud Units (C)**: Standard unit calculation
- **Enterprise Units (E)**: Enterprise agents use half the units (E = C / 2)

**Agent Types:**
- **Cloud Agents**: Use Cloud units (C)
- **Enterprise Agents**: Use Enterprise units (E)

### Step-by-Step Guide

#### 1. Select Agent Type
- Choose **Cloud** or **Enterprise** agent type
- This determines whether Cloud units (C) or Enterprise units (E) are used

#### 2. Configure Test Parameters

**Test Interval:**
- Enter the interval in minutes between test runs
- Examples: `1` (every minute), `5` (every 5 minutes), `15` (every 15 minutes)
- Affects total units (more frequent = more units)

**Test Type:**
- Select from the dropdown of supported test types
- Additional parameters appear based on the selected test type

#### 3. Configure Test-Specific Parameters

**Common Parameters:**
- **Number of Agents**: How many agents run the test
- **Timeout**: Test timeout in seconds

**Test-Specific Parameters:**

**Network (Agent-to-Agent):**
- **Two-way test**: Check if testing in both directions (doubles agent count)

**DNS Server:**
- **Number of Servers**: How many DNS servers to query

**Page Load:**
- **Page Load Timeout**: Timeout for full page load
- **Page Load Interval**: Interval between page load tests
- **HTTP Timeout**: Timeout for HTTP requests
- **HTTP Interval**: Interval between HTTP tests

**Voice Calls:**
- **SIP Timeout**: SIP protocol timeout
- **RTP Timeout**: RTP protocol timeout

#### 4. View Calculation Results

The calculator displays:
- **Units**: Total units required (C for Cloud, E for Enterprise)
- **Calculation Breakdown**: Detailed formula showing how units are calculated
- **Monthly Cost**: Estimated cost based on unit price and selected currency

**Understanding the Calculation:**
- Formulas account for:
  - Test interval (how often tests run)
  - Monthly timeframe (typically 31 days)
  - Test-specific multipliers (timeouts, agent counts, etc.)

#### 5. Add to Configuration List

Once you've configured a test:
1. Review the units and cost
2. Click "Add to Configuration List"
3. The test configuration is saved to the list below
4. You can add multiple configurations to build a complete deployment plan

#### 6. Manage Configuration List

**Viewing Configurations:**
- All saved configurations appear in a table
- Shows test type, agent type, interval, parameters, units, and monthly cost

**Removing Configurations:**
- Click "Remove" on any row to delete it from the list

**Total Calculations:**
- **Total Units**: Sum of all configuration units
- **Total Monthly Cost**: Sum of all configuration costs (in selected currency)

#### 7. Export for CCW Estimate

- Click "Create CCW Estimate" at the bottom of the Bill of Materials
- This opens the Cisco Commerce Workspace in a new tab
- Use your configuration list to create official estimates

### Example Scenarios

**Scenario 1: Simple HTTP Server Test**
- Agent Type: Cloud
- Test Type: HTTP Server
- Test Interval: 5 minutes
- Number of Agents: 3
- Timeout: 5 seconds
- Result: ~67 Cloud units per month

**Scenario 2: Page Load Test**
- Agent Type: Enterprise
- Test Type: Page Load
- Test Interval: 10 minutes
- Number of Agents: 5
- Page Load Timeout: 30 seconds
- Page Load Interval: 10 minutes
- HTTP Timeout: 5 seconds
- HTTP Interval: 1 minute
- Result: Enterprise units (half of Cloud units)

**Scenario 3: Complex Multi-Test Setup**
1. Add HTTP Server test (3 agents, 5-min interval)
2. Add DNS Server test (5 agents, 1-min interval, 2 servers)
3. Add Page Load test (2 agents, 15-min interval)
4. View total units and cost across all tests

### Calculation Formulas Reference

**BGP:**
- Units = 8 × (monthly minutes / 15)

**Network Tests:**
- Agent-to-Server: Units = 5 × (60 / interval) × monthly days × agents
- Agent-to-Agent: Units = 5 × (60 / interval) × monthly days × (agents × 2 if two-way)

**DNS:**
- DNS Server: Units = 5 × (60 / interval) × monthly days × agents × servers
- DNS Trace: Units = 5 × (60 / interval) × monthly days × agents

**HTTP Server:**
- Units = timeout × (60 / interval) × monthly days × agents

**Page Load:**
- Complex formula accounting for page load and HTTP test components

**Transaction/SIP-RTP:**
- Units = timeout × (60 / interval) × monthly days × agents

**Voice Calls:**
- Units = (SIP timeout + RTP timeout) × (60 / interval) × monthly days × agents

### Tips
- Start with longer intervals (5-15 minutes) to minimize units
- Use Enterprise agents when possible to reduce units by 50%
- Monitor your total units across all configurations
- Adjust timeouts to match your actual test requirements (longer timeouts = more units)

---

## Cloud and Traffic Insight Flow Calculator

### Overview
The Cloud and Traffic Insight Flow Calculator helps you estimate costs for ThousandEyes Cloud Insights Flow Logs integration, including both ThousandEyes service costs and AWS infrastructure costs.

### Components

#### 1. ThousandEyes Flow Cost Estimator

Estimates the ThousandEyes service costs based on flow volume.

**Daily Flow Estimate Method:**
1. Enter **Daily Flows**: Total number of network flows per day
2. Enter **Unit Cost**: Cost per unit per month in USD (default: $0.85)
   - The calculator converts to your selected currency for display
3. View results:
   - **Flows per Second (FPS)**: Calculated from daily flows
   - **Units**: Total units required
   - **Monthly Cost**: Cost per month
   - **Yearly Cost**: Cost per year

**Cloud Size Estimate Method:**
1. Enter **VPC Count**: Number of VPCs in your AWS environment
2. Enter **Monthly Traffic (GB)**: Total traffic volume per month
3. Enter **Log Retention (days)**: How long to retain flow logs
4. View estimated flows and costs

#### 2. AWS Cost Calculator

Estimates the AWS infrastructure costs required to support Cloud Insights Flow Logs integration.

**Required Inputs:**
- **VPC Flow Logs Capture (GB)**: Volume of flow log data captured
- **S3 Storage (GB)**: Amount of data stored in S3
- **S3 PUT Requests**: Number of PUT requests to S3
- **SNS Requests**: Number of SNS notifications
- **Data Transfer (GB)**: Data transfer from S3 to ThousandEyes

**Cost Breakdown:**
- **VPC Flow Logs Capture**: $0.50 per GB
- **S3 Storage**: ~$0.023 per GB/month (Standard storage)
- **S3 PUT Requests**: $0.005 per 1,000 requests
- **SNS Notifications**: $0.50 per 1 million requests
- **Data Transfer**: $0.09 per GB (outbound from S3)

**Total Monthly Cost**: Sum of all AWS components

#### 3. AWS Integration Guide

Click "View AWS Integration Guide" to access detailed setup instructions:
- Step-by-step AWS configuration
- IAM role setup
- S3 bucket configuration
- SNS topic configuration
- VPC Flow Logs setup
- Integration verification steps

### Step-by-Step Guide

#### Estimating ThousandEyes Costs

**Method 1: Daily Flow Estimate**
1. Determine your daily flow volume (from AWS CloudWatch, VPC Flow Logs, or network monitoring)
2. Enter the number in "Daily Flows"
3. Adjust "Unit Cost" if you have custom pricing (default is $0.85/unit/month)
4. Review the monthly and yearly costs

**Method 2: Cloud Size Estimate**
1. Count your VPCs in AWS
2. Estimate monthly traffic volume (can use AWS Cost Explorer or CloudWatch)
3. Set log retention period (typically 7-30 days)
4. Review the estimated flows and costs

#### Estimating AWS Infrastructure Costs

1. **Estimate Flow Log Volume:**
   - Use AWS VPC Flow Logs metrics or CloudWatch
   - Typical: 1-5 GB per day per VPC (varies by traffic)

2. **Calculate S3 Storage:**
   - Storage = Flow log volume × Retention days
   - Example: 10 GB/day × 7 days = 70 GB storage

3. **Estimate PUT Requests:**
   - Based on flow log file creation frequency
   - Typical: Several thousand requests per day per VPC

4. **Calculate SNS Requests:**
   - One notification per flow log file created
   - Same order of magnitude as PUT requests

5. **Estimate Data Transfer:**
   - Volume of data transferred from S3 to ThousandEyes
   - Typically similar to storage volume per month

6. Enter all values in the AWS Cost Calculator
7. Review the total monthly AWS cost

#### Complete Cost Analysis

1. Calculate ThousandEyes service costs (Flow Cost Estimator)
2. Calculate AWS infrastructure costs (AWS Cost Calculator)
3. **Total Cost of Ownership = ThousandEyes Cost + AWS Cost**
4. Use this for budgeting and cost optimization decisions

### Example Scenario

**Scenario: Medium Enterprise AWS Environment**

**ThousandEyes Flow Cost:**
- Daily Flows: 50,000,000
- Unit Cost: $0.85/unit/month
- Result: ~1,667 FPS, ~1,666 units, ~$1,416/month ThousandEyes cost

**AWS Infrastructure:**
- VPC Count: 10 VPCs
- Flow Log Capture: 50 GB/day = 1,500 GB/month
- S3 Storage: 1,500 GB (with 30-day retention)
- PUT Requests: 300,000/month
- SNS Requests: 300,000/month
- Data Transfer: 1,500 GB/month

**AWS Costs:**
- Flow Logs: $750/month
- S3 Storage: $34.50/month
- PUT Requests: $1.50/month
- SNS: $0.15/month
- Data Transfer: $135/month
- **Total AWS: ~$921/month**

**Total TCO: $1,416 + $921 = $2,337/month**

### Tips for Cost Optimization

1. **Optimize Flow Log Capture:**
   - Filter out unnecessary flows if possible
   - Consider sampling for high-volume environments

2. **Adjust Retention:**
   - Reduce retention days to lower S3 storage costs
   - Balance between cost and compliance requirements

3. **Monitor Data Transfer:**
   - Use AWS Direct Connect or optimize transfer patterns
   - Consider regional data transfer costs

4. **Right-Size Your Integration:**
   - Start with critical VPCs only
   - Expand gradually based on value delivered

### Currency Support

All costs are displayed in your selected currency:
- Use the sidebar currency selector to choose USD, EUR, JPY, AUD, or MXN
- Exchange rates are applied automatically
- AWS costs (fixed in USD) are converted using current exchange rates

---

## Common Features

### Currency Management

**Unified Currency Selector:**
- Located in the left sidebar
- Applies to all tools simultaneously
- Supported currencies: USD, EUR, JPY, AUD, MXN

**Exchange Rates:**
- Click "Update Rates" to fetch latest exchange rates
- Rates are cached for 1 hour
- Rates are fetched from a public exchange rate API

**Currency Display:**
- All monetary values automatically convert to selected currency
- Original USD values are used for calculations
- Conversion happens at display time

### Theme Settings

**Dark Mode (Default):**
- ThousandEyes dark blue theme
- Optimized for low-light environments
- Reduces eye strain during extended use

**Light Mode:**
- ThousandEyes light orange theme
- Optimized for bright environments
- Better visibility in well-lit offices

**Switching Themes:**
- Click the moon/sun icon (🌙/☀️) in the top-right corner of any page
- Theme preference is saved automatically
- All pages share the same theme setting

### Data Persistence

**Local Storage:**
- All settings and configurations are saved automatically
- Data persists across browser sessions
- Stored only in your browser (not synced to cloud)

**What's Saved:**
- Calculator inputs and preferences
- API configurations (tokens, endpoints)
- Scheduler configurations
- Currency preferences
- Theme preferences
- Test configurations (Synthetics calculator)

**Clearing Data:**
- Clear your browser's local storage to reset all settings
- Settings are browser-specific (not shared across browsers)

### Security Considerations

**API Tokens:**
- Stored only in browser local storage
- Never transmitted to third-party servers (except ThousandEyes API)
- Not included in git commits or deployments
- Always use read-only tokens when possible

**Dry Run Mode:**
- Always test with dry run mode enabled first
- Prevents accidental API modifications
- Review logs before disabling

**Best Practices:**
- Use separate tokens for testing and production
- Rotate tokens regularly
- Never share tokens in screenshots or documentation
- Use environment-specific account group IDs

---

## Troubleshooting

### General Issues

**Page Not Loading:**
- Ensure you're using a modern browser (Chrome, Edge, Safari, Firefox)
- Check browser console for JavaScript errors
- Try clearing browser cache

**Settings Not Saving:**
- Check if local storage is enabled in your browser
- Ensure you're not in incognito/private mode (local storage may be limited)
- Check browser privacy settings

**Currency Not Updating:**
- Click "Update Rates" to fetch latest exchange rates
- Wait a moment for rates to load
- Check internet connection

### API-Related Issues

**API Calls Failing:**
- Verify API token is correct and not expired
- Check API base URL is correct
- Ensure Account Group ID is valid
- Check browser console for detailed error messages
- Verify CORS is enabled if accessing from a custom domain

**Dry Run Mode Not Working:**
- Dry run mode simulates API calls (no actual changes)
- Check the scheduler log or license count status for dry run indicators
- Review console logs for simulated responses

### Calculator Issues

**Incorrect Calculations:**
- Verify input values are correct
- Check that tiered pricing is configured correctly
- Ensure test parameters match your actual test configuration
- Review calculation breakdown for formula details

**Units Not Displaying:**
- Ensure all required fields are filled
- Check that test type is selected
- Verify agent type is selected
- Review browser console for errors

---

## Support and Feedback

For issues, questions, or feedback:
- Review this user guide first
- Check the browser console for error messages
- Ensure all prerequisites are met (API tokens, account access, etc.)

---

**Last Updated:** 2025
**Application Version:** 1.0
