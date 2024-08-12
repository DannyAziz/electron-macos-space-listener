# Electron Macos Space Change Listener

## Description

This package provides a way to listen for when your user changes their space on macOS.

## Table of Contents

- [Installation](#installation)
- [Todo](#todo)

## Installation

### Install using npm

```bash
npm install electron-macos-space-change-listener
```

### You may need to run rebuild to get the native module to work

```bash
npm run rebuild
```

### Require the package in your electron app

```javascript
const {
  startSpaceChangeListener,
} = require("electron-macos-space-change-listener");
```

### Start listening for space changes after app.ready

```javascript
app.on("ready", () => {
  startSpaceChangeListener(() => {
    console.log("Space changed");
  });
});
```

## Todo

- [ ] Verify it works on production builds
- [ ] Import support
- [ ] Unit tests?
- [ ] Better README
