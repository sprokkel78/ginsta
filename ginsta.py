#!/usr/bin/env python3
import gi

gi.require_version("Gtk", "3.0")
gi.require_version("WebKit2", "4.1")  # voor GTK3 is het meestal "4.0"

from gi.repository import Gtk, WebKit2, GLib

class BrowserWindow(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.sprokkel78.ginsta")
        GLib.set_application_name("gInsta")

    def do_activate(self):
        win=Gtk.ApplicationWindow(application=self, title="ginsta")
        win.set_default_size(800, 600)

	# Create a web context for the WebView
        context = WebKit2.WebContext.get_default()

        # Get the cookie manager
        cookie_manager = context.get_cookie_manager()

        # Store cookies persistently in a local file
        cookie_manager.set_persistent_storage(
            "/tmp/ginsta-cookies.db", WebKit2.CookiePersistentStorage.SQLITE
        )

        # Create WebView using this context
        webview = WebKit2.WebView.new_with_context(context)
        webview.load_uri("https://www.instagram.com")
        webview.set_zoom_level(1.2)

	# Scrolled window (optioneel)
        scrolled = Gtk.ScrolledWindow()
        scrolled.add(webview)

        win.add(scrolled)
        win.present()
        scrolled.show()
        webview.show()

# START THE APPLICATION
def main():
    app = BrowserWindow()
    app.run(None)

if __name__ == "__main__":
    main()
