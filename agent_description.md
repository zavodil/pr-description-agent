# AI PR Description Bot

A GitHub App that automatically generates comprehensive pull request descriptions using AI, helping developers save time and maintain consistent documentation standards.

## Overview

This bot integrates with GitHub repositories to analyze code changes and generate detailed PR descriptions. It can operate in two modes:
- **Automatic Generation**: Generates descriptions for newly opened PRs that have empty descriptions or contain the `/ai-describe` trigger
- **Manual Generation**: Responds to `/describe` commands in PR comments from the PR author

## Main Functions

### 1. Webhook Processing
- Listens for GitHub webhook events on pull requests
- Verifies webhook signatures for security
- Processes both new PR events and PR comments

### 2. PR Analysis
- Fetches pull request diffs and metadata
- Analyzes code changes to understand modifications
- Extracts context from PR title and existing information

### 3. AI-Powered Description Generation
- Uses OpenAI's API to generate professional PR descriptions
- Creates structured descriptions including:
  - What changed (bullet-point summary)
  - Why changes were made
  - Technical implementation details
- Maintains concise, professional formatting

### 4. GitHub Integration
- Authenticates as a GitHub App using JWT tokens
- Updates PR descriptions automatically
- Deletes trigger comments after processing

## Inputs

### HTTP Webhook (POST /webhook)
- **Source**: GitHub webhook events
- **Content**: JSON payload containing PR or comment event data
- **Authentication**: Verified using webhook signature

### Environment Configuration
- GitHub App credentials (App ID, private key)
- OpenAI API credentials
- Webhook secret for verification

## Outputs

### GitHub Pull Request Updates
- **Medium**: GitHub API
- **Content**: Generated markdown-formatted PR descriptions
- **Target**: Pull request body/description field

### HTTP Responses
- **Medium**: HTTP JSON responses
- **Content**: Processing status and success indicators

## Health Check Endpoints

- `GET /` - Basic health check
- `GET /health` - Detailed health status with version information