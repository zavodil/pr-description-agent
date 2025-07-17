# AI PR Description Bot

A GitHub App that automatically generates comprehensive pull request descriptions using AI, helping developers save time and maintain consistent PR documentation.

## Overview

This bot integrates with GitHub repositories to automatically analyze code changes and generate detailed PR descriptions. It can work in two modes:
- **Automatic Generation**: Generates descriptions for newly opened PRs that have empty descriptions or contain the `/ai-describe` trigger
- **Manual Generation**: Generates descriptions when PR authors comment `/describe` on their pull requests

## Main Functions

- **Webhook Processing**: Listens for GitHub webhook events (new PRs and comments)
- **Code Analysis**: Retrieves and analyzes git diffs from pull requests
- **AI Description Generation**: Uses OpenAI's GPT models to create structured PR descriptions including:
  - Summary of changes (bullet points)
  - Reason for changes
  - Technical implementation details
- **PR Updates**: Automatically updates PR descriptions with generated content
- **Security**: Verifies webhook signatures and ensures only PR authors can trigger manual generation

## Inputs

### HTTP Webhook (POST /webhook)
- **GitHub Webhook Events**:
  - `pull_request.opened` events for automatic generation
  - `issue_comment.created` events containing `/describe` command
- **Headers**:
  - `X-Hub-Signature-256`: GitHub webhook signature for verification
  - `X-GitHub-Event`: Event type identifier

### HTTP Endpoints
- **GET /** - Basic health check
- **GET /health** - Detailed health status

## Outputs

### GitHub PR Updates (via GitHub API)
- **Updated PR Description**: Markdown-formatted description containing:
  - What changed (bullet-pointed list)
  - Why changes were made
  - Technical implementation notes
- **Comment Deletion**: Removes `/describe` trigger comments after processing

### HTTP Responses
- **Webhook Response**: JSON status indicating processing result
- **Health Check Response**: JSON with service status and version

## Configuration Requirements

The bot requires several environment variables for GitHub App authentication and OpenAI integration:
- GitHub App credentials (App ID, private key, webhook secret)
- OpenAI API credentials and model configuration
- Optional port configuration for the web server