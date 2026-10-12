# Visitor Connect Feather Feed

This public repository holds the latest unsigned Visitor Connect iPad IPA built by Codemagic. Add this source URL in Feather:

```text
https://raw.githubusercontent.com/CasperOng/visitor-connect-feather/main/apps.json
```

Feather needs your own signing certificate and provisioning profile before it can install the app. An unsigned IPA cannot be installed directly. The app is for authorized school staff; the public feed does not grant access to its protected backend.

The source metadata is generated from `ipas/VisitorConnect-unsigned.ipa` by `update-source.py`. The source project's `Mirror Codemagic iPad IPA` GitHub workflow replaces that IPA and regenerates `apps.json` after each successful Codemagic build on `main`. The workflow uses a write-enabled deploy key limited to this repository.
