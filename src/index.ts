// @ts-ignore
import { startSpaceChangeListener as startSpaceChangeListenerNative } from "./spaceChangeListener.node";

const startSpaceChangeListener = (callback: () => void) => {
  startSpaceChangeListenerNative(callback);
};

export { startSpaceChangeListener };
