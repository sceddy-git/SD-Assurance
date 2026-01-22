# SD-Assurance Application Requirements Document

**Version:** 1.0  
**Date:** 2025  
**Status:** Implemented

---

## Table of Contents

1. [Document Information](#document-information)
2. [Executive Summary](#executive-summary)
3. [Application Overview](#application-overview)
4. [Functional Requirements](#functional-requirements)
5. [Non-Functional Requirements](#non-functional-requirements)
6. [Technical Requirements](#technical-requirements)
7. [User Interface Requirements](#user-interface-requirements)
8. [Data Requirements](#data-requirements)
9. [Security Requirements](#security-requirements)
10. [Integration Requirements](#integration-requirements)
11. [Deployment Requirements](#deployment-requirements)

---

## Document Information

**Project Name:** SD-Assurance (ThousandEyes Endpoint Agents Budget Calculator and Operational Enablement)  
**Document Type:** Software Requirements Specification  
**Target Audience:** Developers, Product Managers, Stakeholders  
**Related Documents:**
- USER_GUIDE.md - User documentation
- README.md - Project overview and setup instructions

---

## Executive Summary

The SD-Assurance application is a browser-based, client-side tool designed to help organizations plan, budget, license, and operate Cisco ThousandEyes Endpoint Agents (EPA) and Cloud/App Synthetics tests. The application provides comprehensive calculators, licensing management, scheduling capabilities, and cost estimation tools for ThousandEyes services.

**Key Value Propositions:**
- Budget planning and cost optimization for ThousandEyes deployments
- Operational automation for endpoint agent management
- Multi-currency support for global organizations
- No backend infrastructure required (fully client-side)
- Direct integration with ThousandEyes API

---

## Application Overview

### Purpose
The SD-Assurance application provides a suite of tools to help organizations:
1. Calculate budget requirements and agent capacity for ThousandEyes Endpoint Agents
2. Manage and monitor endpoint agent licenses
3. Automate endpoint agent scheduling based on time-of-day rules
4. Calculate units and costs for Cloud and App Synthetics tests
5. Estimate costs for ThousandEyes Cloud Insights Flow Logs integration

### Target Users
- Network engineers and administrators
- IT budget planners and financial analysts
- ThousandEyes account administrators
- DevOps and SRE teams managing monitoring infrastructure

### Application Architecture
- **Type:** Single Page Application (SPA)
- **Technology:** HTML5, CSS3, Vanilla JavaScript
- **Storage:** Browser LocalStorage
- **Deployment:** Static file hosting (GitHub Pages compatible)
- **Dependencies:** None (no external libraries required)

---

## Functional Requirements

### FR-1: EPA Calculator

#### FR-1.1: Budget Input
- **REQ-1.1.1:** The system SHALL accept a budget amount as numeric input
- **REQ-1.1.2:** The system SHALL validate that budget is a positive number
- **REQ-1.1.3:** The system SHALL persist budget value in browser local storage

#### FR-1.2: Pricing Configuration
- **REQ-1.2.1:** The system SHALL support simple pricing (single price per agent) for Advantage licenses
- **REQ-1.2.2:** The system SHALL support simple pricing (single price per agent) for Essentials licenses
- **REQ-1.2.3:** The system SHALL support tiered pricing with multiple tiers for Advantage licenses
- **REQ-1.2.4:** The system SHALL support tiered pricing with multiple tiers for Essentials licenses
- **REQ-1.2.5:** The system SHALL allow users to add custom pricing tiers
- **REQ-1.2.6:** The system SHALL allow users to remove pricing tiers
- **REQ-1.2.7:** The system SHALL provide a "Reset to defaults" function to restore standard tiered pricing
- **REQ-1.2.8:** The system SHALL persist pricing configuration in browser local storage

#### FR-1.3: Calculation Logic
- **REQ-1.3.1:** The system SHALL calculate maximum agents purchasable for Advantage licenses based on budget and pricing
- **REQ-1.3.2:** The system SHALL calculate maximum agents purchasable for Essentials licenses based on budget and pricing
- **REQ-1.3.3:** The system SHALL apply tiered pricing correctly when multiple tiers are configured
- **REQ-1.3.4:** The system SHALL support "Round Down" rounding mode (floor to whole agents)
- **REQ-1.3.5:** The system SHALL support "Round Nearest" rounding mode (round to nearest whole number)
- **REQ-1.3.6:** The system SHALL calculate unspent budget for Advantage licenses
- **REQ-1.3.7:** The system SHALL calculate unspent budget for Essentials licenses
- **REQ-1.3.8:** The system SHALL calculate effective average price per agent when tiered pricing is used (optional display)

#### FR-1.4: Results Display
- **REQ-1.4.1:** The system SHALL display maximum Advantage agents count
- **REQ-1.4.2:** The system SHALL display maximum Essentials agents count
- **REQ-1.4.3:** The system SHALL display unspent budget for Advantage
- **REQ-1.4.4:** The system SHALL display unspent budget for Essentials
- **REQ-1.4.5:** The system SHALL provide toggle to show/hide effective average price per agent
- **REQ-1.4.6:** The system SHALL provide toggle to show/hide multi-currency comparison
- **REQ-1.4.7:** The system SHALL display results in the selected currency

### FR-2: EPA Licensing

#### FR-2.1: Authentication
- **REQ-2.1.1:** The system SHALL accept ThousandEyes API Bearer token as input
- **REQ-2.1.2:** The system SHALL store API token securely in browser local storage
- **REQ-2.1.3:** The system SHALL never transmit API token to third-party servers (except ThousandEyes API)
- **REQ-2.1.4:** The system SHALL provide visual indication of token storage status

#### FR-2.2: Account Group Management
- **REQ-2.2.1:** The system SHALL fetch available account groups from ThousandEyes API
- **REQ-2.2.2:** The system SHALL display account groups in a dropdown selector
- **REQ-2.2.3:** The system SHALL display account group name and ID in format: "Account Name (ID)"
- **REQ-2.2.4:** The system SHALL handle API errors gracefully with user-friendly messages
- **REQ-2.2.5:** The system SHALL support CORS error handling and display appropriate warnings

#### FR-2.3: Label Management
- **REQ-2.3.1:** The system SHALL automatically fetch available labels when an account group is selected
- **REQ-2.3.2:** The system SHALL display labels in a multi-select dropdown
- **REQ-2.3.3:** The system SHALL support multi-select using Ctrl (Windows/Linux) or Cmd (Mac)
- **REQ-2.3.4:** The system SHALL allow empty label selection (include all agents)
- **REQ-2.3.5:** The system SHALL filter agents based on selected labels

#### FR-2.4: Dry Run Mode
- **REQ-2.4.1:** The system SHALL provide a toggle for "Dry run mode"
- **REQ-2.4.2:** The system SHALL simulate API calls when dry run mode is enabled
- **REQ-2.4.3:** The system SHALL log simulated actions when in dry run mode
- **REQ-2.4.4:** The system SHALL prevent actual API modifications when dry run mode is enabled
- **REQ-2.4.5:** The system SHALL persist dry run mode preference in local storage

#### FR-2.5: License Count Retrieval
- **REQ-2.5.1:** The system SHALL fetch current agent counts from ThousandEyes API
- **REQ-2.5.2:** The system SHALL display count of agents with Advantage licenses
- **REQ-2.5.3:** The system SHALL display count of agents with Essentials licenses
- **REQ-2.5.4:** The system SHALL display last refresh timestamp and status
- **REQ-2.5.5:** The system SHALL handle API errors and display error messages
- **REQ-2.5.6:** The system SHALL filter agents by selected labels before counting

### FR-3: EPA Scheduler

#### FR-3.1: Scheduler Control
- **REQ-3.1.1:** The system SHALL provide a toggle to enable/disable the scheduler
- **REQ-3.1.2:** The system SHALL only execute schedules when scheduler is enabled
- **REQ-3.1.3:** The system SHALL execute schedules only while the page is open in browser
- **REQ-3.1.4:** The system SHALL persist scheduler enabled state in local storage

#### FR-3.2: Check Frequency Configuration
- **REQ-3.2.1:** The system SHALL accept check frequency in seconds as input
- **REQ-3.2.2:** The system SHALL enforce minimum check frequency of 15 seconds
- **REQ-3.2.3:** The system SHALL validate check frequency is a positive number
- **REQ-3.2.4:** The system SHALL persist check frequency in local storage

#### FR-3.3: Schedule Management
- **REQ-3.3.1:** The system SHALL allow users to create new schedules
- **REQ-3.3.2:** The system SHALL require Account ID (Account Group ID) for each schedule
- **REQ-3.3.3:** The system SHALL require Authentication Token for each schedule
- **REQ-3.3.4:** The system SHALL require Label Name for each schedule
- **REQ-3.3.5:** The system SHALL require Action (Enable/Disable) for each schedule
- **REQ-3.3.6:** The system SHALL require "From" time (24-hour format) for each schedule
- **REQ-3.3.7:** The system SHALL require "To" time (24-hour format) for each schedule
- **REQ-3.3.8:** The system SHALL support wrap-around time windows (e.g., 18:00 to 08:00)
- **REQ-3.3.9:** The system SHALL allow editing existing schedules
- **REQ-3.3.10:** The system SHALL allow deleting schedules with confirmation
- **REQ-3.3.11:** The system SHALL group schedules by Organization Name (derived from Account Group ID)
- **REQ-3.3.12:** The system SHALL provide collapsible groups for organization schedules
- **REQ-3.3.13:** The system SHALL persist all schedules in local storage
- **REQ-3.3.14:** The system SHALL support creating multiple labels in a single schedule entry

#### FR-3.4: Schedule Execution
- **REQ-3.4.1:** The system SHALL evaluate schedules at the configured check frequency
- **REQ-3.4.2:** The system SHALL determine which labels should be enabled/disabled based on current time
- **REQ-3.4.3:** The system SHALL execute API calls to enable/disable agents when schedules trigger
- **REQ-3.4.4:** The system SHALL respect dry run mode setting from EPA Licensing tab
- **REQ-3.4.5:** The system SHALL handle multiple schedules for the same label
- **REQ-3.4.6:** The system SHALL log all scheduler actions with timestamps

#### FR-3.5: Status Display
- **REQ-3.5.1:** The system SHALL display currently active instructions (which labels are being enabled/disabled)
- **REQ-3.5.2:** The system SHALL update active instructions in real-time
- **REQ-3.5.3:** The system SHALL maintain a scheduler log with all actions
- **REQ-3.5.4:** The system SHALL display timestamps for each log entry
- **REQ-3.5.5:** The system SHALL display API call results in the log
- **REQ-3.5.6:** The system SHALL display error messages in the log
- **REQ-3.5.7:** The system SHALL auto-scroll log to show latest entries

### FR-4: Cloud and App Synthetics Calculator

#### FR-4.1: Agent Type Selection
- **REQ-4.1.1:** The system SHALL allow selection between Cloud and Enterprise agent types
- **REQ-4.1.2:** The system SHALL calculate Cloud units (C) for Cloud agents
- **REQ-4.1.3:** The system SHALL calculate Enterprise units (E) for Enterprise agents, where E = C / 2
- **REQ-4.1.4:** The system SHALL persist agent type selection in local storage

#### FR-4.2: Test Type Support
- **REQ-4.2.1:** The system SHALL support BGP test type
- **REQ-4.2.2:** The system SHALL support Network (Agent-to-Server) test type
- **REQ-4.2.3:** The system SHALL support Network (Agent-to-Agent) test type
- **REQ-4.2.4:** The system SHALL support DNS Server test type
- **REQ-4.2.5:** The system SHALL support DNS Trace test type
- **REQ-4.2.6:** The system SHALL support HTTP Server test type
- **REQ-4.2.7:** The system SHALL support Page Load test type
- **REQ-4.2.8:** The system SHALL support Transaction test type
- **REQ-4.2.9:** The system SHALL support SIP-RTP test type
- **REQ-4.2.10:** The system SHALL support Voice Calls test type

#### FR-4.3: Test Parameter Configuration
- **REQ-4.3.1:** The system SHALL accept test interval in minutes
- **REQ-4.3.2:** The system SHALL accept number of agents
- **REQ-4.3.3:** The system SHALL accept timeout in seconds
- **REQ-4.3.4:** The system SHALL accept number of DNS servers (for DNS Server tests)
- **REQ-4.3.5:** The system SHALL accept two-way test flag (for Agent-to-Agent tests)
- **REQ-4.3.6:** The system SHALL accept page load timeout (for Page Load tests)
- **REQ-4.3.7:** The system SHALL accept page load interval (for Page Load tests)
- **REQ-4.3.8:** The system SHALL accept HTTP timeout (for Page Load tests)
- **REQ-4.3.9:** The system SHALL accept HTTP interval (for Page Load tests)
- **REQ-4.3.10:** The system SHALL accept SIP timeout (for Voice Calls tests)
- **REQ-4.3.11:** The system SHALL accept RTP timeout (for Voice Calls tests)
- **REQ-4.3.12:** The system SHALL show/hide parameters based on selected test type

#### FR-4.4: Unit Calculation
- **REQ-4.4.1:** The system SHALL calculate units using correct formulas for each test type
- **REQ-4.4.2:** The system SHALL account for test interval in calculations
- **REQ-4.4.3:** The system SHALL account for monthly timeframe (31 days) in calculations
- **REQ-4.4.4:** The system SHALL account for test-specific multipliers (timeouts, agent counts, etc.)
- **REQ-4.4.5:** The system SHALL display calculation breakdown showing formulas
- **REQ-4.4.6:** The system SHALL display total units (C or E based on agent type)

#### FR-4.5: Cost Calculation
- **REQ-4.5.1:** The system SHALL calculate monthly cost based on unit price and selected currency
- **REQ-4.5.2:** The system SHALL use unit price from currency configuration
- **REQ-4.5.3:** The system SHALL display cost in selected currency

#### FR-4.6: Configuration List Management
- **REQ-4.6.1:** The system SHALL allow adding test configurations to a list
- **REQ-4.6.2:** The system SHALL display all saved configurations in a table
- **REQ-4.6.3:** The system SHALL display test type, agent type, interval, parameters, units, and cost for each configuration
- **REQ-4.6.4:** The system SHALL allow removing configurations from the list
- **REQ-4.6.5:** The system SHALL calculate total units across all configurations
- **REQ-4.6.6:** The system SHALL calculate total monthly cost across all configurations
- **REQ-4.6.7:** The system SHALL persist configuration list in local storage

#### FR-4.7: CCW Integration
- **REQ-4.7.1:** The system SHALL provide "Create CCW Estimate" button
- **REQ-4.7.2:** The system SHALL open Cisco Commerce Workspace in a new tab
- **REQ-4.7.3:** The system SHALL provide configuration data for CCW estimate creation

### FR-5: Cloud and Traffic Insight Flow Calculator

#### FR-5.1: ThousandEyes Flow Cost Estimator
- **REQ-5.1.1:** The system SHALL accept daily flows as input
- **REQ-5.1.2:** The system SHALL convert daily flows to flows per second (FPS)
- **REQ-5.1.3:** The system SHALL accept unit cost per month in USD (default $0.85)
- **REQ-5.1.4:** The system SHALL calculate total units required
- **REQ-5.1.5:** The system SHALL calculate monthly cost
- **REQ-5.1.6:** The system SHALL calculate yearly cost
- **REQ-5.1.7:** The system SHALL display costs in selected currency

#### FR-5.2: Cloud Size Estimate
- **REQ-5.2.1:** The system SHALL accept VPC count as input
- **REQ-5.2.2:** The system SHALL accept monthly traffic volume in GB
- **REQ-5.2.3:** The system SHALL accept log retention period in days
- **REQ-5.2.4:** The system SHALL estimate flows based on VPC count and traffic
- **REQ-5.2.5:** The system SHALL calculate costs based on estimated flows

#### FR-5.3: AWS Cost Calculator
- **REQ-5.3.1:** The system SHALL accept VPC Flow Logs capture volume in GB
- **REQ-5.3.2:** The system SHALL accept S3 storage volume in GB
- **REQ-5.3.3:** The system SHALL accept S3 PUT requests count
- **REQ-5.3.4:** The system SHALL accept SNS requests count
- **REQ-5.3.5:** The system SHALL accept data transfer volume in GB
- **REQ-5.3.6:** The system SHALL calculate VPC Flow Logs cost at $0.50 per GB
- **REQ-5.3.7:** The system SHALL calculate S3 storage cost at ~$0.023 per GB/month
- **REQ-5.3.8:** The system SHALL calculate S3 PUT requests cost at $0.005 per 1,000 requests
- **REQ-5.3.9:** The system SHALL calculate SNS notifications cost at $0.50 per 1 million requests
- **REQ-5.3.10:** The system SHALL calculate data transfer cost at $0.09 per GB
- **REQ-5.3.11:** The system SHALL calculate total monthly AWS cost
- **REQ-5.3.12:** The system SHALL display AWS costs in selected currency (converted from USD)

#### FR-5.4: AWS Integration Guide
- **REQ-5.4.1:** The system SHALL provide "View AWS Integration Guide" button
- **REQ-5.4.2:** The system SHALL display detailed AWS setup instructions in a modal
- **REQ-5.4.3:** The system SHALL include IAM role setup instructions
- **REQ-5.4.4:** The system SHALL include S3 bucket configuration instructions
- **REQ-5.4.5:** The system SHALL include SNS topic configuration instructions
- **REQ-5.4.6:** The system SHALL include VPC Flow Logs setup instructions
- **REQ-5.4.7:** The system SHALL include integration verification steps

### FR-6: Common Features

#### FR-6.1: Currency Management
- **REQ-6.1.1:** The system SHALL support USD currency
- **REQ-6.1.2:** The system SHALL support EUR currency
- **REQ-6.1.3:** The system SHALL support JPY currency
- **REQ-6.1.4:** The system SHALL support AUD currency
- **REQ-6.1.5:** The system SHALL support MXN currency
- **REQ-6.1.6:** The system SHALL provide currency selector in sidebar
- **REQ-6.1.7:** The system SHALL apply selected currency across all tools
- **REQ-6.1.8:** The system SHALL fetch exchange rates from public API
- **REQ-6.1.9:** The system SHALL cache exchange rates for 1 hour
- **REQ-6.1.10:** The system SHALL provide "Update Rates" button to refresh exchange rates
- **REQ-6.1.11:** The system SHALL convert all monetary values to selected currency
- **REQ-6.1.12:** The system SHALL persist currency preference in local storage

#### FR-6.2: Theme Management
- **REQ-6.2.1:** The system SHALL support dark theme (ThousandEyes dark blue)
- **REQ-6.2.2:** The system SHALL support light theme (ThousandEyes light orange)
- **REQ-6.2.3:** The system SHALL provide theme toggle button (moon/sun icon)
- **REQ-6.2.4:** The system SHALL apply theme across all pages
- **REQ-6.2.5:** The system SHALL persist theme preference in local storage
- **REQ-6.2.6:** The system SHALL load saved theme preference on page load

#### FR-6.3: Navigation
- **REQ-6.3.1:** The system SHALL provide sidebar navigation
- **REQ-6.3.2:** The system SHALL support navigation to "Endpoint Experience" page
- **REQ-6.3.3:** The system SHALL support navigation to "Cloud and App Synthetics" page
- **REQ-6.3.4:** The system SHALL support navigation to "Cloud and Traffic Insight Flow Calculator" page
- **REQ-6.3.5:** The system SHALL highlight active page in navigation
- **REQ-6.3.6:** The system SHALL provide tab navigation within Endpoint Experience page

#### FR-6.4: Data Persistence
- **REQ-6.4.1:** The system SHALL persist all user inputs in browser local storage
- **REQ-6.4.2:** The system SHALL restore saved data on page load
- **REQ-6.4.3:** The system SHALL persist calculator configurations
- **REQ-6.4.4:** The system SHALL persist API tokens (encrypted in storage)
- **REQ-6.4.5:** The system SHALL persist scheduler configurations
- **REQ-6.4.6:** The system SHALL persist test configurations
- **REQ-6.4.7:** The system SHALL persist currency and theme preferences

---

## Non-Functional Requirements

### NFR-1: Performance
- **REQ-NFR-1.1:** The application SHALL load in less than 2 seconds on standard broadband connection
- **REQ-NFR-1.2:** The application SHALL respond to user input within 100ms
- **REQ-NFR-1.3:** The application SHALL handle calculations for up to 1000 agents without performance degradation
- **REQ-NFR-1.4:** The application SHALL support up to 100 scheduler entries without performance issues

### NFR-2: Usability
- **REQ-NFR-2.1:** The application SHALL be intuitive for users with basic ThousandEyes knowledge
- **REQ-NFR-2.2:** The application SHALL provide clear error messages
- **REQ-NFR-2.3:** The application SHALL provide helpful hints and tooltips
- **REQ-NFR-2.4:** The application SHALL support keyboard navigation
- **REQ-NFR-2.5:** The application SHALL be accessible (WCAG 2.1 Level AA compliance)

### NFR-3: Compatibility
- **REQ-NFR-3.1:** The application SHALL support Chrome browser (latest 2 versions)
- **REQ-NFR-3.2:** The application SHALL support Edge browser (latest 2 versions)
- **REQ-NFR-3.3:** The application SHALL support Safari browser (latest 2 versions)
- **REQ-NFR-3.4:** The application SHALL support Firefox browser (latest 2 versions)
- **REQ-NFR-3.5:** The application SHALL be responsive and work on desktop screens (1024px and above)

### NFR-4: Reliability
- **REQ-NFR-4.1:** The application SHALL handle API failures gracefully
- **REQ-NFR-4.2:** The application SHALL handle network errors gracefully
- **REQ-NFR-4.3:** The application SHALL validate all user inputs
- **REQ-NFR-4.4:** The application SHALL prevent data loss during browser refresh
- **REQ-NFR-4.5:** The application SHALL handle CORS errors with informative messages

### NFR-5: Maintainability
- **REQ-NFR-5.1:** The application SHALL be self-contained in a single HTML file
- **REQ-NFR-5.2:** The application SHALL not require build tools or compilation
- **REQ-NFR-5.3:** The application SHALL use clear, readable code structure
- **REQ-NFR-5.4:** The application SHALL include inline documentation for complex logic

---

## Technical Requirements

### TR-1: Technology Stack
- **REQ-TR-1.1:** The application SHALL use HTML5
- **REQ-TR-1.2:** The application SHALL use CSS3 with CSS Variables for theming
- **REQ-TR-1.3:** The application SHALL use Vanilla JavaScript (ES6+)
- **REQ-TR-1.4:** The application SHALL NOT require external JavaScript libraries
- **REQ-TR-1.5:** The application SHALL use Browser LocalStorage API

### TR-2: API Integration
- **REQ-TR-2.1:** The application SHALL integrate with ThousandEyes REST API v7
- **REQ-TR-2.2:** The application SHALL use Bearer token authentication
- **REQ-TR-2.3:** The application SHALL handle CORS restrictions
- **REQ-TR-2.4:** The application SHALL use HTTPS for all API calls
- **REQ-TR-2.5:** The application SHALL handle API rate limiting

### TR-3: External Services
- **REQ-TR-3.1:** The application SHALL fetch exchange rates from public exchange rate API
- **REQ-TR-3.2:** The application SHALL handle exchange rate API failures gracefully
- **REQ-TR-3.3:** The application SHALL cache exchange rates locally

### TR-4: Browser Requirements
- **REQ-TR-4.1:** The application SHALL require JavaScript enabled
- **REQ-TR-4.2:** The application SHALL require LocalStorage support
- **REQ-TR-4.3:** The application SHALL require modern browser with ES6+ support

---

## User Interface Requirements

### UI-1: Layout
- **REQ-UI-1.1:** The application SHALL use a sidebar navigation layout
- **REQ-UI-1.2:** The sidebar SHALL be 240px wide
- **REQ-UI-1.3:** The main content area SHALL have maximum width of 1200px
- **REQ-UI-1.4:** The application SHALL be responsive for desktop screens

### UI-2: Styling
- **REQ-UI-2.1:** The application SHALL use ThousandEyes brand colors
- **REQ-UI-2.2:** Dark theme SHALL use dark blue color scheme
- **REQ-UI-2.3:** Light theme SHALL use light orange color scheme
- **REQ-UI-2.4:** The application SHALL use consistent spacing and typography
- **REQ-UI-2.5:** The application SHALL use rounded corners and shadows for panels

### UI-3: Components
- **REQ-UI-3.1:** The application SHALL use consistent button styling
- **REQ-UI-3.2:** The application SHALL use consistent input field styling
- **REQ-UI-3.3:** The application SHALL use consistent panel/card styling
- **REQ-UI-3.4:** The application SHALL use consistent result display styling
- **REQ-UI-3.5:** The application SHALL provide visual feedback for user actions

### UI-4: Accessibility
- **REQ-UI-4.1:** The application SHALL use semantic HTML elements
- **REQ-UI-4.2:** The application SHALL provide ARIA labels where appropriate
- **REQ-UI-4.3:** The application SHALL support keyboard navigation
- **REQ-UI-4.4:** The application SHALL have sufficient color contrast (WCAG AA)

---

## Data Requirements

### DR-1: Data Storage
- **REQ-DR-1.1:** The application SHALL store all data in browser LocalStorage
- **REQ-DR-1.2:** The application SHALL use JSON format for complex data structures
- **REQ-DR-1.3:** The application SHALL use clear, namespaced keys for storage
- **REQ-DR-1.4:** The application SHALL handle LocalStorage quota exceeded errors

### DR-2: Data Validation
- **REQ-DR-2.1:** The application SHALL validate numeric inputs
- **REQ-DR-2.2:** The application SHALL validate time format inputs
- **REQ-DR-2.3:** The application SHALL validate required fields
- **REQ-DR-2.4:** The application SHALL sanitize user inputs

### DR-3: Data Persistence
- **REQ-DR-3.1:** The application SHALL save data automatically on input change
- **REQ-DR-3.2:** The application SHALL restore data on page load
- **REQ-DR-3.3:** The application SHALL handle missing or corrupted stored data

---

## Security Requirements

### SR-1: API Token Security
- **REQ-SR-1.1:** The application SHALL store API tokens only in browser LocalStorage
- **REQ-SR-1.2:** The application SHALL never transmit API tokens to third-party servers
- **REQ-SR-1.3:** The application SHALL use HTTPS for all API communications
- **REQ-SR-1.4:** The application SHALL provide warnings about token security

### SR-2: Data Privacy
- **REQ-SR-2.1:** The application SHALL not collect or transmit user data to third parties
- **REQ-SR-2.2:** The application SHALL not use analytics or tracking
- **REQ-SR-2.3:** All data SHALL remain in user's browser

### SR-3: Input Validation
- **REQ-SR-3.1:** The application SHALL validate all user inputs
- **REQ-SR-3.2:** The application SHALL prevent injection attacks
- **REQ-SR-3.3:** The application SHALL sanitize data before storage

### SR-4: Dry Run Protection
- **REQ-SR-4.1:** The application SHALL default to dry run mode
- **REQ-SR-4.2:** The application SHALL clearly indicate when dry run mode is active
- **REQ-SR-4.3:** The application SHALL prevent accidental API modifications

---

## Integration Requirements

### IR-1: ThousandEyes API
- **REQ-IR-1.1:** The application SHALL integrate with ThousandEyes API v7
- **REQ-IR-1.2:** The application SHALL support Account Groups endpoint
- **REQ-IR-1.3:** The application SHALL support Endpoint Agents endpoint
- **REQ-IR-1.4:** The application SHALL support Labels endpoint
- **REQ-IR-1.5:** The application SHALL support Agent enable/disable endpoints
- **REQ-IR-1.6:** The application SHALL handle API version changes gracefully

### IR-2: Exchange Rate API
- **REQ-IR-2.1:** The application SHALL integrate with public exchange rate API
- **REQ-IR-2.2:** The application SHALL support USD, EUR, JPY, AUD, MXN currencies
- **REQ-IR-2.3:** The application SHALL handle API failures gracefully

### IR-3: Cisco Commerce Workspace
- **REQ-IR-3.1:** The application SHALL provide link to Cisco Commerce Workspace
- **REQ-IR-3.2:** The application SHALL open CCW in new tab

---

## Deployment Requirements

### DEP-1: Hosting
- **REQ-DEP-1.1:** The application SHALL be deployable as static files
- **REQ-DEP-1.2:** The application SHALL be compatible with GitHub Pages
- **REQ-DEP-1.3:** The application SHALL work when opened directly as file (file://)
- **REQ-DEP-1.4:** The application SHALL not require server-side processing

### DEP-2: Build and Deployment
- **REQ-DEP-2.1:** The application SHALL not require build process
- **REQ-DEP-2.2:** The application SHALL be deployable via GitHub Actions
- **REQ-DEP-2.3:** The application SHALL include deployment workflow configuration

### DEP-3: Version Control
- **REQ-DEP-3.1:** The application SHALL be version controlled
- **REQ-DEP-3.2:** The application SHALL include README with setup instructions
- **REQ-DEP-3.3:** The application SHALL include user documentation

---

## Appendix A: Glossary

- **EPA:** Endpoint Agent - ThousandEyes agent software installed on endpoints
- **Advantage:** Premium license tier for Endpoint Agents
- **Essentials:** Standard license tier for Endpoint Agents
- **CCW:** Cisco Commerce Workspace - Cisco's quoting and ordering platform
- **CORS:** Cross-Origin Resource Sharing - Browser security mechanism
- **FPS:** Flows Per Second - Network flow measurement unit
- **VPC:** Virtual Private Cloud - AWS networking construct
- **S3:** Amazon Simple Storage Service
- **SNS:** Amazon Simple Notification Service
- **IAM:** Identity and Access Management - AWS service for access control
- **BGP:** Border Gateway Protocol
- **DNS:** Domain Name System
- **HTTP:** Hypertext Transfer Protocol
- **SIP:** Session Initiation Protocol
- **RTP:** Real-time Transport Protocol

---

## Appendix B: Test Types and Formulas

### BGP Tests
- Units = 8 × (monthly minutes / 15)

### Network Tests
- Agent-to-Server: Units = 5 × (60 / interval) × monthly days × agents
- Agent-to-Agent: Units = 5 × (60 / interval) × monthly days × (agents × 2 if two-way)

### DNS Tests
- DNS Server: Units = 5 × (60 / interval) × monthly days × agents × servers
- DNS Trace: Units = 5 × (60 / interval) × monthly days × agents

### HTTP Server Tests
- Units = timeout × (60 / interval) × monthly days × agents

### Page Load Tests
- Complex formula accounting for page load and HTTP test components

### Transaction/SIP-RTP Tests
- Units = timeout × (60 / interval) × monthly days × agents

### Voice Calls Tests
- Units = (SIP timeout + RTP timeout) × (60 / interval) × monthly days × agents

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025 | System | Initial requirements document based on implemented application |

---

**End of Document**
