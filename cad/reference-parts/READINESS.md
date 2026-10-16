# CAD library readiness

Generated offline from [catalog.json](catalog.json) by `python3 scripts/reference_parts_triage.py --write-report`.

Metadata audit, not source availability polling or permission to act. Counts overlap across axes. A URL may be a landing page or unconfigured portal. Commit pins identify source bytes, not physical revisions. Named physical revisions also need correspondence review. No record establishes physical fit. Cloud upload and model training are outside the five permission fields and remain unauthorized.

## Counts

- group: `{"authorized-local-record": 1, "prepare-authorization-request": 2, "resolve-inspection-rights": 42}`
- source_status: `{"listed": 15, "not-located": 17, "portal-unconfigured": 13}`
- source_pin: `{"commit-pinned": 5, "review-source-version": 40}`
- physical_revision: `{"1.02": 1, "C04": 1, "V1.0": 1, "V3.0": 1, "V3.1": 1, "V4": 1, "unknown": 39}`
- geometry_confidence: `{"dimension-checked": 1, "documentation-only": 44}`
- local_status: `{"not-cataloged": 44, "not-checked": 1}`
- authorization: `{"approved": 1, "not-requested": 44}`
- permissions: `{"commercial_reuse": {"allowed": 3, "conditional": 3, "unknown": 39}, "derivative_use": {"allowed": 3, "conditional": 3, "unknown": 39}, "download": {"allowed": 3, "conditional": 3, "unknown": 39}, "local_ai_processing": {"allowed": 3, "conditional": 1, "unknown": 41}, "public_redistribution": {"allowed": 3, "conditional": 1, "unknown": 41}}`

## Per-record gates

D/A/U/P/C = download / local AI processing / derivative use / public redistribution / commercial reuse. A=allowed, C=conditional, U=unknown, P=prohibited. These are documented readings with evidence in the catalog. All nonlocal records remain link-only. Local `not-checked` means this generated report does not inspect the filesystem.

| Catalog ID | Source | D/A/U/P/C | Authorization | Local | Physical revision | Geometry | Next group |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 80-20-1010-s-12-inch-unmachined | portal-unconfigured | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| 80-20-20-2020-500mm-unmachined | portal-unconfigured | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| adafruit-1184-gt2-2mm-pitch-6mm-width-1164mm-loop | not-located | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| adafruit-1253-gt2-36-teeth-5mm-bore | listed | A/A/A/A/A | not-requested | not-cataloged | unknown | documentation-only | prepare-authorization-request |
| adafruit-4884-feather-rp2040 | listed | A/A/A/A/A | approved | not-checked | unknown | dimension-checked | authorized-local-record |
| aluminium-warehouse-20x20x2-1000 | not-located | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| antclabs-bltouch-smart-v3-1 | not-located | U/U/U/U/U | not-requested | not-cataloged | V3.1 | documentation-only | resolve-inspection-rights |
| bigtreetech-octopus-v1-0 | listed | U/U/U/U/U | not-requested | not-cataloged | V1.0 | documentation-only | resolve-inspection-rights |
| bigtreetech-skr-mini-e3-v3-0 | listed | U/U/U/U/U | not-requested | not-cataloged | V3.0 | documentation-only | resolve-inspection-rights |
| bondtech-bmg-standard-right-hand | listed | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| duet3d-duet-3-mini-5-wifi | listed | C/C/C/C/C | not-requested | not-cataloged | 1.02 | documentation-only | resolve-inspection-rights |
| e3d-revo-hemera-xs-direct-drive | listed | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| espressif-esp32-devkitc-esp32-wroom-32e-module | not-located | U/U/U/U/U | not-requested | not-cataloged | V4 | documentation-only | resolve-inspection-rights |
| gates-200-2mgt-06 | not-located | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| gates-2mr-20s-06 | not-located | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| hiwin-mgn09c-carriage-size-preload-accuracy-seal-options-unresolved | portal-unconfigured | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| hiwin-mgn09h-carriage-size-preload-accuracy-seal-options-unresolved | portal-unconfigured | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| hiwin-mgn12c-carriage-size-preload-accuracy-seal-options-unresolved | portal-unconfigured | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| hiwin-mgn12h-carriage-size-preload-accuracy-seal-options-unresolved | portal-unconfigured | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| igus-swm-08 | portal-unconfigured | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| igus-ws-10-40-cam-500 | portal-unconfigured | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| ldo-42sth40-1684cl350e-vrn | not-located | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| ldo-42sth48-2004ac-vrn | not-located | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| mean-well-lrs-350-24-24v | not-located | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| misumi-hfs5-2020-200-200mm | portal-unconfigured | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| misumi-hntt5-5-5-series-m5-pre-assembly-nut | portal-unconfigured | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| misumi-scbs4-10-m4-x-10-with-washer | portal-unconfigured | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| noctua-nf-a4x10-5v-3-pin | listed | C/U/C/U/C | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| noctua-nf-a4x20-5v-3-pin | listed | C/U/C/U/C | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| ntn-608zz | listed | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| ntn-625zz | listed | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| omron-d2f-01l-hinge-lever-pcb-terminals | not-located | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| online-metals-18014-12-inch | not-located | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| raspberry-pi-pico-rp2040-without-headers | listed | A/A/A/A/A | not-requested | not-cataloged | unknown | documentation-only | prepare-authorization-request |
| raspberry-pi-raspberry-pi-3-model-b-1gb | not-located | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| raspberry-pi-raspberry-pi-4-model-b-2gb | not-located | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| raspberry-pi-raspberry-pi-5-4gb | not-located | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| raspberry-pi-raspberry-pi-zero-2-w-unpopulated-gpio | not-located | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| skf-625-2z-cn-clearance | not-located | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| stepperonline-17hs08-1004s-short-body | listed | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| stepperonline-17hs19-2004s1-1m-cable | listed | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| stmicroelectronics-nucleo-f446re-mb1136-f446re-c04 | listed | U/U/U/U/U | not-requested | not-cataloged | C04 | documentation-only | resolve-inspection-rights |
| sunon-mf50151vx-1b00u-g99-50x50x15-blower | not-located | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| wago-221-412-lever-connector | portal-unconfigured | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |
| wago-221-413-lever-connector | portal-unconfigured | U/U/U/U/U | not-requested | not-cataloged | unknown | documentation-only | resolve-inspection-rights |

## Source revision register

Read exact notes and geometry checks with `--id CATALOG_ID --json`. The script does not infer a valid physical revision from a source commit or parse free text into engineering approval.

| Catalog ID | Pin classification | Recorded source revision |
| --- | --- | --- |
| 80-20-1010-s-12-inch-unmachined | review-source-version | Undated live source; revision not established |
| 80-20-20-2020-500mm-unmachined | review-source-version | Undated live source; revision not established |
| adafruit-1184-gt2-2mm-pitch-6mm-width-1164mm-loop | review-source-version | Undated product page |
| adafruit-1253-gt2-36-teeth-5mm-bore | commit-pinned | c128bceb1f96b6ea8b68f250bda986ba85da24ea |
| adafruit-4884-feather-rp2040 | commit-pinned | c128bceb1f96b6ea8b68f250bda986ba85da24ea |
| aluminium-warehouse-20x20x2-1000 | review-source-version | Undated live manufacturer/supplier source; checked 2026-10-15 |
| antclabs-bltouch-smart-v3-1 | review-source-version | Undated live manufacturer/supplier source; checked 2026-10-15 |
| bigtreetech-octopus-v1-0 | commit-pinned | 9526ff16f68839626cb8875a299e73f99f2e57e8 |
| bigtreetech-skr-mini-e3-v3-0 | commit-pinned | d7fd822006628143222d1c3c8cdea85ffee29e66 |
| bondtech-bmg-standard-right-hand | review-source-version | Undated live source; revision not established |
| duet3d-duet-3-mini-5-wifi | commit-pinned | 1dc1976f196fb968a4140397219c87f2c80efc38 |
| e3d-revo-hemera-xs-direct-drive | review-source-version | Undated live source; revision not established |
| espressif-esp32-devkitc-esp32-wroom-32e-module | review-source-version | Undated live source; revision not established |
| gates-200-2mgt-06 | review-source-version | Manufacturer Industrial Power Transmission catalog; indexed table inspected 2026-10-15, publication revision not established |
| gates-2mr-20s-06 | review-source-version | Manufacturer indexed catalog/manual tables checked 2026-10-15; exact drawing revision unresolved |
| hiwin-mgn09c-carriage-size-preload-accuracy-seal-options-unresolved | review-source-version | Live manufacturer MGN HIRES dimensional table; publication revision not stated |
| hiwin-mgn09h-carriage-size-preload-accuracy-seal-options-unresolved | review-source-version | Live manufacturer MGN HIRES dimensional table; publication revision not stated |
| hiwin-mgn12c-carriage-size-preload-accuracy-seal-options-unresolved | review-source-version | Live manufacturer MGN HIRES dimensional table; publication revision not stated |
| hiwin-mgn12h-carriage-size-preload-accuracy-seal-options-unresolved | review-source-version | Live manufacturer MGN HIRES dimensional table; publication revision not stated |
| igus-swm-08 | review-source-version | Undated live manufacturer/supplier source; checked 2026-10-15 |
| igus-ws-10-40-cam-500 | review-source-version | Undated live manufacturer/supplier source; checked 2026-10-15 |
| ldo-42sth40-1684cl350e-vrn | review-source-version | Undated live manufacturer/supplier source; checked 2026-10-15 |
| ldo-42sth48-2004ac-vrn | review-source-version | Undated live manufacturer/supplier source; checked 2026-10-15 |
| mean-well-lrs-350-24-24v | review-source-version | Undated live source; revision not established |
| misumi-hfs5-2020-200-200mm | review-source-version | Undated live source; revision not established |
| misumi-hntt5-5-5-series-m5-pre-assembly-nut | review-source-version | Undated live source; revision not established |
| misumi-scbs4-10-m4-x-10-with-washer | review-source-version | Undated live source; revision not established |
| noctua-nf-a4x10-5v-3-pin | review-source-version | Undated live source; revision not established |
| noctua-nf-a4x20-5v-3-pin | review-source-version | Undated live source; revision not established |
| ntn-608zz | review-source-version | Undated live manufacturer/supplier source; checked 2026-10-15 |
| ntn-625zz | review-source-version | Undated live manufacturer/supplier source; checked 2026-10-15 |
| omron-d2f-01l-hinge-lever-pcb-terminals | review-source-version | Undated live source; revision not established |
| online-metals-18014-12-inch | review-source-version | Undated live manufacturer/supplier source; checked 2026-10-15 |
| raspberry-pi-pico-rp2040-without-headers | review-source-version | RP-008311-DS redirects (HEAD only) to RP-008311-DS-1-Pico-R3-step.zip; documentation commit ddea98e98dafe9419feb4fd82710c2fbdef7dc44; internal STEP/physical revision unverified |
| raspberry-pi-raspberry-pi-3-model-b-1gb | review-source-version | Undated live source; revision not established |
| raspberry-pi-raspberry-pi-4-model-b-2gb | review-source-version | Undated live source; revision not established |
| raspberry-pi-raspberry-pi-5-4gb | review-source-version | Undated live source; revision not established |
| raspberry-pi-raspberry-pi-zero-2-w-unpopulated-gpio | review-source-version | Undated live source; revision not established |
| skf-625-2z-cn-clearance | review-source-version | Undated live source; revision not established |
| stepperonline-17hs08-1004s-short-body | review-source-version | Live listing checked 2026-10-15 versus older drawing approved 2018-08-18; physical revision unresolved |
| stepperonline-17hs19-2004s1-1m-cable | review-source-version | Undated live source; revision not established |
| stmicroelectronics-nucleo-f446re-mb1136-f446re-c04 | review-source-version | MB1136 design package 1.1, 2024-11-22; UM1724 Rev 17 identifies C04 |
| sunon-mf50151vx-1b00u-g99-50x50x15-blower | review-source-version | Undated live source; revision not established |
| wago-221-412-lever-connector | review-source-version | Undated live source; revision not established |
| wago-221-413-lever-connector | review-source-version | Undated live source; revision not established |
