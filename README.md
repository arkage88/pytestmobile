# UI Automation Testing Project (Mobile)

This project contains a framework for UI automation testing on Web and Mobile (Android) platforms. The framework is built using Python with Pytest as the test runner, Selenium for browser interaction, and Appium for mobile device interaction.


## Project Structure
```
pytestmobile/
├── mobile/                 # All Mobile testing related code
│   ├── config/             # Appium & device configuration
│   ├── locators/           # UI element locators for each page
│   ├── pages/              # Page Objects implementation
│   └── tests/              # Test scripts
├── reports/                # Output directory for test reports
│   ├── allure/
│   └── html/
├── test_data/              # Data files for testing (e.g., JSON)
├── utils/                  # Utilities and helper functions
├── conftest.py             # Global Pytest fixtures & configuration
├── requirements.txt        # List of Python dependencies
└── README.md               # This file
```

## Prerequisites
Before you begin, ensure your machine has the following software installed:
1.  **Python** (version 3.10 or higher)
2.  **Node.js** and **npm** (to install Appium)
3.  **Java Development Kit (JDK)** (required by Appium)
4.  **Android Studio** (for the Android SDK and emulator management)
5.  **Appium Server**: `npm install -g appium`
6.  **Appium UIAutomator2 Driver**: `appium driver install uiautomator2`

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/arkage88/pytestmobile
cd pytestmobile
```

### 2. Create a Virtual Environment
It is highly recommended to use a virtual environment to keep project dependencies isolated from your global Python installation.


### 3. Install Python Dependencies
Install all required Python packages from the `requirements.txt` file.
```bash
pip install -r requirements.txt
```

### 4. Appium & Android Emulator Setup
1.  Setting Real Device to Developer options on plugin used usb and turn on usb debuging and type in terminal ```bash
    adb devices
    ```.
2. Record App Activity to get "appium:appPackage": "id.edot.ework",
        "appium:appActivity": "id.edot.onboarding.ui.splash.SplashScreenActivity"
```
adb logcat | grep START > activity_log.txt
```

.
3.  Ensure your emulator's name matches the one in your configuration (`appium:udid` in tests file).
4.  Run the Appium Server in a separate terminal:
    ```bash
    appium --allow-cors
    ```

```

## Running Tests
Ensure the Appium server is running for mobile tests.

### Running All Tests
```bash
pytest
```

### Running Mobile Tests
```bash
pytest mobile/tests
```
