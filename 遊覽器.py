# Import necessary modules
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

# Create main browser window
class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle("Simple Browser")
        # Set window size
        self.setGeometry(100, 100, 1200, 800)

        # Create web engine view (main browser area)
        self.browser = QWebEngineView()
        # Set default URL
        self.browser.setUrl(QUrl("https://www.google.com"))
        # Set browser as central widget
        self.setCentralWidget(self.browser)

        # Create navigation toolbar
        navtb = QToolBar("Navigation")
        self.addToolBar(navtb)

        # Back button
        back_btn = QAction("Back", self)
        back_btn.triggered.connect(self.browser.back)  # Go back in history
        navtb.addAction(back_btn)

        # Forward button
        forward_btn = QAction("Forward", self)
        forward_btn.triggered.connect(self.browser.forward)  # Go forward in history
        navtb.addAction(forward_btn)

        # Reload button
        reload_btn = QAction("Reload", self)
        reload_btn.triggered.connect(self.browser.reload)  # Reload page
        navtb.addAction(reload_btn)

        # URL bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)  # Press Enter to navigate
        navtb.addWidget(self.url_bar)

        # Update URL bar when URL changes
        self.browser.urlChanged.connect(self.update_url)

    # Navigate to URL typed in URL bar
    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "http://" + url
        self.browser.setUrl(QUrl(url))

    # Update URL bar to show current URL
    def update_url(self, q):
        self.url_bar.setText(q.toString())

# Run application
app = QApplication(sys.argv)
window = Browser()
window.show()  # Show the browser window
sys.exit(app.exec_())
