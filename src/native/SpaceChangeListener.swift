import Foundation
import Cocoa

var callback: (() -> Void)?
var appDelegate: AppDelegate? 


@objc class AppDelegate: NSObject {
    @objc func activeSpaceDidChange(_ notification: Notification) {
        callback?()
    }
}

@_cdecl("startSpaceChangeListener")
public func startSpaceChangeListener(_ cb: @escaping @convention(c) () -> Void) {
    print("startSpaceChangeListener")
    callback = cb
    appDelegate = AppDelegate()

    guard let appDelegate = appDelegate else {
        print("Failed to initialize AppDelegate")
        return
    }

    NSWorkspace.shared.notificationCenter.addObserver(
        appDelegate,
        selector: #selector(AppDelegate.activeSpaceDidChange(_:)),
        name: NSWorkspace.activeSpaceDidChangeNotification,
        object: nil
    )

    // Keep the run loop running to listen for notifications
    DispatchQueue.global().async {
        print("DispatchQueue.global().async")
        RunLoop.current.run()
    }
}