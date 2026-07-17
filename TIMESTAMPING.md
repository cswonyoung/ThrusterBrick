# Timestamping — proving these files existed on a given date

## What a timestamp buys you
A trusted timestamp binds a cryptographic hash of your files to a point in time
that you cannot back-date and others cannot dispute. Combined with public
publication, it establishes **priority** (you had this on date X) and pins the
**prior-art date** that blocks later patents over the same disclosure. It does
*not* need anyone to trust you — it's math plus a public ledger.

## The hash is the anchor
`CHECKSUMS.sha256` in this folder contains a SHA-256 fingerprint of every file.
Change a single byte in any file and its hash no longer matches — so timestamping
just this one small manifest effectively timestamps the entire set. Verify anytime:

```
sha256sum -c CHECKSUMS.sha256
```

## What has already been done (offline)
- SHA-256 computed for every file in both document directories (`docs-rotor/`, `docs-flight/`) + the metadata files → `CHECKSUMS.sha256`.
- This machine has **no network access**, so the blockchain anchoring step below
  has NOT been performed yet. It is one command on any online machine. Nothing
  about the anchor depends on this machine; the manifest is the whole input.

## Anchor it yourself — OpenTimestamps (free, Bitcoin-anchored)
```
pip install opentimestamps-client        # one time
cd znvo-nanovoid-public-domain
ots stamp CHECKSUMS.sha256               # creates CHECKSUMS.sha256.ots immediately
```
`CHECKSUMS.sha256.ots` is your proof. Keep it *with* the files everywhere you
upload. The proof "upgrades" as it gets confirmed into the Bitcoin blockchain
(minutes to a few hours); run this later and re-save:
```
ots upgrade CHECKSUMS.sha256.ots
ots verify CHECKSUMS.sha256.ots         # confirms the manifest existed by a block's time
```
(You can also drag the file onto https://opentimestamps.org to stamp/verify in a
browser — no install needed.)

## You get independent timestamps for free from the archives too
Each of these is a separate, credible dated record — do several so no single one
is a point of failure:
- **Zenodo** issues a DOI with a fixed publication date and preserves the files.
- **A git commit** (GitHub/GitLab/Codeberg) is dated; once **Software Heritage**
  archives the repo, that date is independently preserved.
- **The Internet Archive** records the date it captured your item/URL.
- **Arweave** writes an immutable, timestamped transaction.

Belt and suspenders: OpenTimestamps for a trustless cryptographic anchor, plus a
Zenodo DOI for a human-institutional one.
