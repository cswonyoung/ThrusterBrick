# Durable-publication checklist

Goal: put this set somewhere it can't be quietly removed, with a fixed date and a
clear CC0 dedication, even with no audience. Redundancy across *independent*
systems is what makes it effectively irrevocable. Do the prep once, then push to
several archives.

## 0 · Before uploading (prep — mostly done)
- [x] CC0 dedication inside every file (banner / header / DXF comment).
- [x] `LICENSE` (full CC0 legal code) + `NOTICE.md` + `MANIFEST.md` in the folder.
- [x] `CHECKSUMS.sha256` covering every file.
- [ ] Fill the date (and optional country) in `NOTICE.md`.
- [ ] **Timestamp:** `ots stamp CHECKSUMS.sha256` → keep `CHECKSUMS.sha256.ots`
      alongside the files (see `TIMESTAMPING.md`).
- [ ] Verify locally: `sha256sum -c CHECKSUMS.sha256`.

## 1 · Zenodo — permanent record + DOI  (do this first)
- [ ] Create the record at https://zenodo.org, upload the whole folder (or the zip).
- [ ] License = **CC0-1.0**; author = Croft Swonyoung; add a short description.
- [ ] Publish → you get a **DOI** and a fixed date. CERN-backed, built to persist.
- [ ] Record the DOI in your README and anywhere you post.

## 2 · Public git repo → Software Heritage  (auto-preserved)
- [ ] Push the folder to a public repo on **GitHub** *and* a mirror (**Codeberg**
      or **GitLab**) — two hosts, so no single account/host is a chokepoint.
- [ ] Keep `LICENSE` at the repo root (hosts auto-detect CC0).
- [ ] Save it at https://archive.softwareheritage.org ("Save code now"). Once
      archived it is preserved automatically and independently of the repo.

## 3 · Internet Archive  (item + snapshots)
- [ ] Upload the zip as an item at https://archive.org (set license to CC0).
- [ ] Also paste each public URL (Zenodo, the repos) into the **Wayback Machine**
      "Save Page Now" at https://web.archive.org so the pages themselves are captured.

## 4 · Permanent / decentralised copies  (hard to remove by design)
- [ ] **Arweave** — pay-once permanent storage (e.g. via ArDrive). Immutable and
      timestamped; about as close to un-deletable as exists.
- [ ] **IPFS** — add the folder and pin it with a pinning service (so it stays up);
      record the CID. Content-addressed = the CID *is* the integrity check.

## 5 · Optional reach (so it isn't only preserved, but findable)
- [ ] Post the DOI + repo links anywhere relevant (a forum, a mailing list, your
      own page). Being indexed/linked is what gets a no-audience work noticed and
      re-mirrored by others.
- [ ] Anyone can verify authorship + integrity from `NOTICE.md` + `CHECKSUMS.sha256`
      + the `.ots` proof.

## Verify the redundancy worked
- [ ] The set exists at **3+ independent** places (e.g. Zenodo + GitHub + Codeberg +
      Software Heritage + Internet Archive + Arweave).
- [ ] Each carries the CC0 `LICENSE` and the checksums.
- [ ] The `.ots` proof verifies.

## Two honest caveats
- **CC0 is irrevocable.** Once dedicated and mirrored, you cannot pull it back or
  change your mind — that's the point, but be sure.
- **CC0 ≠ patent waiver.** It waives copyright, not patents. What prevents someone
  patenting this and using that to suppress it is the **dated public disclosure**
  (prior art) — which is exactly what steps 1–4 + the timestamp create.
