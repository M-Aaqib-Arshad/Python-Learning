## GitHub Copilot Chat

- Extension Version: 0.25.1 (prod)
- VS Code: vscode/1.98.2
- OS: Windows

## Network

User Settings:
```json
  "github.copilot.advanced.debug.useElectronFetcher": false,
  "github.copilot.advanced.debug.useNodeFetcher": false,
  "github.copilot.advanced.debug.useNodeFetchFetcher": false
```

Connecting to https://api.github.com:
- DNS ipv4 Lookup: 20.207.73.85 (10 ms)
- DNS ipv6 Lookup: Error (6 ms): getaddrinfo ENOTFOUND api.github.com
- Proxy URL: None (318 ms)
- Electron fetch (configured): HTTP 200 (416 ms)
- Node.js https: HTTP 200 (619 ms)
- Node.js fetch: HTTP 200 (655 ms)
- Helix fetch: HTTP 200 (508 ms)

Connecting to https://api.individual.githubcopilot.com/_ping:
- DNS ipv4 Lookup: 140.82.114.21 (22 ms)
- DNS ipv6 Lookup: Error (17 ms): getaddrinfo ENOTFOUND api.individual.githubcopilot.com
- Proxy URL: None (11 ms)
- Electron fetch (configured): HTTP 200 (866 ms)
- Node.js https: HTTP 200 (890 ms)
- Node.js fetch: HTTP 200 (944 ms)
- Helix fetch: HTTP 200 (912 ms)

## Documentation

In corporate networks: [Troubleshooting firewall settings for GitHub Copilot](https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-firewall-settings-for-github-copilot).