// @ts-ignore
const {
  startSpaceChangeListener: startSpaceChangeListenerNative,
} = require("./spaceChangeListener.node");

const startSpaceChangeListener = (callback: () => void) => {
  startSpaceChangeListenerNative(callback);
};

export { startSpaceChangeListener };
