# CAJViewer binaries

Unofficial archive of original CAJViewer installers for reproducible testing.
This repository is not affiliated with CNKI. Installers are stored in GitHub
Releases, not Git history. No document corpus is included.

## Downloads

See [catalog.json](catalog.json) for exact versions, original URLs, sizes,
SHA-256 hashes and permanent release URLs. Initially available:

| OS | Architecture | Version | Package |
| --- | --- | --- | --- |
| Linux | x86_64 | 9.0.0-24093 | deb |

Download a pinned release and verify it before use:

```sh
gh release download linux-9.0.0-24093 --repo rwv/cajviewer-binaries --dir downloads
cd downloads
sha256sum -c SHA256SUMS
```

The installer is unchanged; only its asset filename is normalized. A mirror
checksum establishes identity with our recorded file, not a vendor signature.

## Adding platforms and versions

The catalog separates `os`, `arch`, `format`, `variant` and `version`.
Use `linux`, `windows`, or `macos` for OS; architectures may include `x86`,
`x86_64`, `aarch64`, `universal`, `loongarch64`, or `mips64el` when verified.
Never infer an ISA from a vendor/CPU brand or claim untested platforms work.
Windows EXE/MSI and macOS DMG/PKG/ZIP can be added without changing the schema.
Use separate records for each actual installer; OS versions need not match.

1. Obtain an original vendor installer and retain its embedded notices.
2. Inspect package metadata; record source URL, actual acquisition date, size,
   version, OS, architecture, package format and SHA-256.
3. Create a new platform/version release (include variant if needed).
4. Upload the unchanged installer, catalog snapshot, THIRD_PARTY_NOTICES.md
   and SHA256SUMS. Never replace existing versioned assets silently.
5. Run `python3 scripts/validate.py` and verify the downloaded release payload.

Do not commit installers, extracted vendor code, login profiles or license keys.
Use Conventional Commits for repository changes.

## Licensing

Our original scripts and metadata are MIT licensed. **CAJViewer installers are
proprietary and are not covered by MIT.** See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
