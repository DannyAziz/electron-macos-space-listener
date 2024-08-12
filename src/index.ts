const {
  startSpaceChangeListener: startSpaceChangeListenerNative,
} = require("./spaceChangeListener.node");

const startSpaceChangeListener = (callback: () => void) => {
  startSpaceChangeListenerNative(callback);
};

module.exports = {
  startSpaceChangeListener,
};
