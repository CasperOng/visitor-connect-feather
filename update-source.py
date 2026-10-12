#!/usr/bin/env python3
import json
import plistlib
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
IPA = ROOT / "ipas" / "VisitorConnect-unsigned.ipa"
SOURCE = ROOT / "apps.json"
RAW_BASE = "https://raw.githubusercontent.com/CasperOng/visitor-connect-feather/main"
BUNDLE_ID = "com.casperong.visitorconnect"


def main() -> None:
    with zipfile.ZipFile(IPA) as archive:
        info = plistlib.loads(archive.read("Payload/VisitorConnect.app/Info.plist"))

    if info.get("CFBundleIdentifier") != BUNDLE_ID:
        raise SystemExit("IPA bundle identifier does not match Visitor Connect")

    privacy = {
        key: value for key, value in info.items()
        if key.endswith("UsageDescription") and isinstance(value, str)
    }
    icon_url = f"{RAW_BASE}/icons/VisitorConnect.png"
    source = {
        "name": "Visitor Connect",
        "subtitle": "Open Day iPad companion",
        "description": "Unsigned Visitor Connect builds for signing with Feather.",
        "iconURL": icon_url,
        "tintColor": "#315FD5",
        "apps": [{
            "name": "Visitor Connect",
            "bundleIdentifier": BUNDLE_ID,
            "developerName": "Casper Ong",
            "subtitle": "Open Day check-in",
            "localizedDescription": "Staff check-in companion for the school's information day.",
            "iconURL": icon_url,
            "tintColor": "#315FD5",
            "category": "utilities",
            "appPermissions": {"entitlements": [], "privacy": privacy},
            "versions": [{
                "version": str(info["CFBundleShortVersionString"]),
                "buildVersion": str(info["CFBundleVersion"]),
                "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
                "localizedDescription": "Codemagic build",
                "downloadURL": f"{RAW_BASE}/ipas/VisitorConnect-unsigned.ipa",
                "size": IPA.stat().st_size,
                "minOSVersion": str(info.get("MinimumOSVersion", "17.0")),
            }],
        }],
    }
    SOURCE.write_text(json.dumps(source, indent=2, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
