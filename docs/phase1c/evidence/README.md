# Retained Phase 1C Fusion observations

This bundle preserves **maintainer-run** Fusion Personal/macOS observations
inspected by an agent, not a new live rerun or physical measurement. It contains
the 35 matrix reports (33 PASS, two expected rejections), plus the original
`mm0alj_4` trapezoid failure. All 36 source files were available at extraction;
all 11 previously published SHA-256 values matched. Originals remain untouched.

[runtime-observations.json.gz](runtime-observations.json.gz) is gzip-compressed
UTF-8 JSON (schema 1), readable with Python's standard library. Compression and
shared component observations reduce the original 8,175,179 bytes to about
123 KiB. This is a **selected evidence extraction**, not a byte-for-byte raw
archive. Original hashes identify the source reports, not the sanitized JSON.

Retained: every report's original hash/size/outcome, input and derived parameter
expressions/internal values, component names, actual/expected bounds and deltas,
compute/timeline/transform evidence, model parameters, sketch dimensions and
constraint/health state, extrusion health/suppression, and the failed report's
actual vertices/dimension references. Repeated component snapshots share a
content hash. No new measurements are calculated. Early domain/sequence failures
have no component snapshots because the original checks exited before those reads.

Omitted: private source/traceback paths, repetitive before/after parameter dumps,
duplicate fixed-carrier blocks, repeated native/proxy bounds and traceback frames.
No document names, credentials, account identities or private machine paths are
committed. The [extractor](preserve_reports.py) selects a fixed list of original
report IDs so later synthetic test reports cannot be mistaken for Fusion runs.

## Provenance and limits

- Corrected matrix source attribution comes from the contemporaneous
  [verification record](../verification.md): published `ecdd68e`, also present
  at reviewed head `c8dcc50d58cc9718823994c1ebbce8b60a400ba7`. The entry-point hash
  recorded at inspection was
  `4a9c5ad2c7df53dfd2579199ae63fc78810304994689aac5703ab56bc6370398`.
  Reports contain a local source path, **not embedded source hashes**. This
  attribution is not a cryptographic binding of the executed source to a run.
- `mm0alj_4` observed an older unconstrained design using the diagnostic CHECK.
  Exact executed source hash and generation-source revision are **unknown**.
  Do not attribute its defective timeline to the corrected generator merely
  because it was inspected later.
- Fusion version, macOS version, execution timestamps, document IDs and
  generation-source IDs are **unknown** for these reports. Historical platform
  attribution is maintainer-reported. Current installed versions cannot fill
  historical gaps. Filename IDs identify files, not independently proven runs.
- Equal hashes on separate reports do not prove separate executions. Manual
  continuity and visual inspection remain maintainer observations.
- Mounting evidence records four named cut/sketch histories and driving
  coordinates/diameters. Historical CHECK did **not** independently measure
  final bore centers or through-cut rims. This bundle does not retroactively
  apply the new acceptance checks or turn the earlier volume check into a
  location check.
- Tests of the extractor and CHECK use Python data/API-shaped doubles. They do
  not constitute Fusion solver or physical verification.

## Read or reproduce

From the repository root, inspect one report and its retained component data:

```sh
python3 - <<'PY'
import gzip, json
with gzip.open('docs/phase1c/evidence/runtime-observations.json.gz', 'rt') as f:
    bundle = json.load(f)
report = bundle['reports']['mm0alj_4']
print(json.dumps(report, indent=2))
key = report['components']['Fixed_cold_carrier']
print('\n'.join(bundle['component_observations'][key]))
PY
```

To extract again **only if the original reports are available**, write a separate
output and compare decompressed JSON; gzip headers may differ across Python/zlib
versions. This command never modifies the input reports:

```sh
python3 -B docs/phase1c/evidence/preserve_reports.py /tmp /tmp/tesseract-evidence-recheck.json.gz
```

The JSON stores parameter values in Fusion internal cm (yaw unitless); bounds,
vertices and explicit geometric diagnostics are mm. Health enum `0` means
healthy, not false. `mm0alj_4` demonstrates healthy features can still have
underconstrained sketches and incorrect geometry.

## Original report index

All IDs expand to `tesseract-phase1c-check-ID.txt`. Outcomes are historical.

| ID | Outcome | Components | Original SHA-256 |
| --- | --- | --- | --- |
| `041lzbqg` | PASS | 59 | `fe58e58556db7a0fe6da4bd131dd7f18e2fa192f845eecc966b2dfb6223da624` |
| `13jlczwi` | PASS | 59 | `e23e6043e18721fb2391c3ac4c90b78e71f3563c56c48881d9f95250d9bcb6b9` |
| `3nb7l73f` | PASS | 59 | `e23e6043e18721fb2391c3ac4c90b78e71f3563c56c48881d9f95250d9bcb6b9` |
| `493onqe6` | PASS | 59 | `884997fe28b2b38c0156f83c145d0420837297a04a4d7bf1b8255b499b350d4c` |
| `4lxhb_3v` | PASS | 59 | `d0fd99b484f30807732642341b0468683a4f3d1ba64ba3ce04a0c3a89860c3cc` |
| `4s22_vxj` | PASS | 59 | `4cb3619729a4a55c09a51b82b67ed4af59a030e5b01797775e054caf3e75aaeb` |
| `5_4b7dhl` | PASS | 59 | `aab7a2a3f83f129c8a4ccff5bf505747f6ece87dd47d47376a3af93c8122c19d` |
| `6ms7rolq` | PASS | 59 | `c2c606662647dcfed09b146033c49fd88933da0d1c5f745226120e61a1c35fe7` |
| `6suhxuzl` | PASS | 59 | `0be317e1a4996dc707be43e63170aab4eccf2971e4184e8293f2da4a93ae05f7` |
| `8_3_xzwm` | PASS | 59 | `e275a49138df3a6a47f5dc46117b8759c8254664631beb82173cd833ff50b556` |
| `99_zv4yv` | PASS | 51 | `fa897d6a0d3aeb72e83a08b82d8c6c02f666e6dc2c9f1addb99c97ee9142aad4` |
| `_hq6gs8v` | PASS | 59 | `e23e6043e18721fb2391c3ac4c90b78e71f3563c56c48881d9f95250d9bcb6b9` |
| `_nfqa89y` | PASS | 59 | `e23e6043e18721fb2391c3ac4c90b78e71f3563c56c48881d9f95250d9bcb6b9` |
| `b8y4p1hz` | PASS | 59 | `8c31ebad22b37526fd9f1e3962680e70755ac4887c9dc7470546d0527a79e29f` |
| `b_834fp4` | PASS | 59 | `6bd28cc7c43f4b0e334024f9d15e278c957b7cc45f4c72fc04f4e45881024129` |
| `by48kx2v` | PASS | 59 | `fe58e58556db7a0fe6da4bd131dd7f18e2fa192f845eecc966b2dfb6223da624` |
| `c8bl8bzi` | PASS | 59 | `659d82f91dd0e03d4184973b95741146624eeb560f643ad51604c674c6533152` |
| `flqonjex` | PASS | 59 | `7ea2ad061168767b840d9df91d7ca587f0b99bb46073dab21342431a85b9f3bc` |
| `g01ccjx0` | PASS | 59 | `6bd28cc7c43f4b0e334024f9d15e278c957b7cc45f4c72fc04f4e45881024129` |
| `h1or_1v8` | PASS | 59 | `264e9c55958b494dd72f711c36bf5c225c138f35bc4992a7daf9f77731bcdb4c` |
| `krnw8b8w` | PASS | 59 | `e23e6043e18721fb2391c3ac4c90b78e71f3563c56c48881d9f95250d9bcb6b9` |
| `ktzo4_2p` | PASS | 59 | `4cb3619729a4a55c09a51b82b67ed4af59a030e5b01797775e054caf3e75aaeb` |
| `lntp606d` | PASS | 59 | `ce66aa000c54165e2b98629548818437afdc412f0ad0d18d024f11a253a4f20d` |
| `m5w5komd` | PASS | 59 | `b0eb1cf0640c7a93f186987fa58fa277baa8f17167fe302f0d5f626f21067d66` |
| `mm0alj_4` | FAIL | 59 | `fbaf9ad3e82a8d521369a6757aae04cb4af3e6b4036a322cca60fb72b94fd251` |
| `mmm883gw` | PASS | 51 | `81ddc13314751edb8db9568593e14ac72fe0c06e71bd72e5702261517aa5048c` |
| `nu6ojds0` | PASS | 59 | `e23e6043e18721fb2391c3ac4c90b78e71f3563c56c48881d9f95250d9bcb6b9` |
| `oe73bpp7` | PASS | 59 | `883aef02540971a341d053005c297caadedc5a06ea290a692e71dafde7bb5d8f` |
| `qb3wy0p3` | PASS | 59 | `a0f45aec94e3c2900ce104dcc452b0044cef1d724b9279adcc433777656e3364` |
| `rlgahkc_` | PASS | 59 | `e23e6043e18721fb2391c3ac4c90b78e71f3563c56c48881d9f95250d9bcb6b9` |
| `sdagtrxu` | PASS | 59 | `5ba21785fc85964d03897969e00498876a04834fb3f3613e0811960f05905fcc` |
| `ukhsf0as` | PASS | 59 | `ef2c14965f4e5778b71cabbdfcfa70b5329d05b56a72f4a9d44c7de6c36e8270` |
| `uwuq5tzb` | FAIL | 0 | `d6d88978ff3b5667c99e198b527aefb67124c281845f8ab1e8a565116527067d` |
| `xhotdiee` | FAIL | 0 | `4181dc24a84833c0102c9ff258147e945f8e259abc75a025d9e01c4f108eaf47` |
| `xs753e5c` | PASS | 59 | `76ca02fa299a61022288cc37881c580f05c1b33b76ae60b4bb85579f9367b616` |
| `xzxem_9s` | PASS | 59 | `5d3b23ee2b47b3d607f6f1ac5e425058157ddff138d053cb437e6462719c6730` |

## Z-datum correction and targeted smoke follow-up

[z-datum-regression.json](z-datum-regression.json) retains selected diagnostic
properties from two failing pre-correction CHECKs, including their original hashes.
[targeted-smoke.json](targeted-smoke.json) retains nine later report observations:
four passes, three intended mutation rejections and two rolled-back missing-solid
failures. See [verification](../verification.md) for attribution and coverage limits,
including the supplied `rdx62f8q` versus actual `rdx62f8g` discrepancy.

Reproduce the latter without modifying originals:

```sh
python3 -B docs/phase1c/evidence/preserve_smoke_reports.py /tmp /tmp/phase1c-smoke-reproduced.json
```

The extractor selects fixed IDs, provenance, parameters, errors, timeline states,
bore measurements and relevant constraint/feature observations. It omits private
traceback paths and full raw diagnostics. Original report hashes permit local
comparison; neither bundle is a complete raw-report archive. Hashed document IDs
and source-file hashes have the provenance limits stated in verification.
