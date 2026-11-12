# A+ — Category Product Feasibility v1

> DRI: A Long — Product Expert  
> Issue: https://github.com/anhnv14994/web-aff/issues/3  
> Evidence checked: 12/11/2026 (Vietnam time)  
> Status: Expert feasibility assessment; NOT an MVP decision.

## 1. Executive summary

This report compares all four assigned categories: computer monitors, audio (personal headphones/headsets), air purifiers and laptops. It assesses the work required to build a reliable Product Knowledge Base and normalize 100–300 models. It does not estimate market demand, search volume, conversion, commission or revenue.

**Recommended catalog feasibility pilot:** ten model candidates across two categories: five monitors and five wireless over-ear headphones. This is a recommendation about a bounded knowledge/catalog experiment only. It is not a recommendation to select either category as A+'s commercial MVP. CEO retains that decision.

The ten models are exact manufacturer model names where identified. Retailer P/N, Vietnam-specific warranty SKU, current stock, price and affiliate eligibility are not asserted. No item is represented as personally tested by A Long.

### Comparative scorecard

Scores are structured expert judgment (1 = difficult/weak, 5 = favorable/easier), not measured market data.

| Dimension | Monitor | Audio | Air purifier | Laptop |
|---|---:|---:|---:|---:|
| Taxonomy/spec normalization ease | 4 | 3 | 4 | 2 |
| Independent verification availability | 5 | 4 | 4 | 4 |
| Model/variant identity stability | 4 | 3 | 3 | 2 |
| Cross-model comparability | 4 | 3 | 4 | 2 |
| Claim/interpretation risk manageability | 4 | 3 | 2 | 3 |
| 100–300 model catalog effort (5=easier) | 4 | 3 | 4 | 2 |
| Overall expert feasibility / 5 | **4.2** | **3.2** | **3.5** | **2.5** |

Monitors balance stable core specifications with measurable independent tests. Audio requires more listening, fit, ANC and call evidence. Air purifiers have relatively clear CADR/filter attributes but high risk of misleading room-size and health-adjacent claims. Laptops have the highest configuration and regional SKU burden.

## 2. Method and confidence

Criteria: taxonomy clarity; stable units/definitions; manufacturer and independent evidence; exact model/generation/region identification; risk of confusing marketing with comparable measurement; estimated effort for 100–300 records.

Confidence:
- **High:** exact identity/value visible on an official manufacturer, standards-body or test-method page.
- **Medium:** authoritative source exists but is regional, family-level, configuration-dependent or only a manufacturer claim.
- **Low/Pending:** local retail P/N, Vietnam warranty/stock, field performance or variant has not been established.

Manufacturer specifications prove what the manufacturer publishes, not independent real-world performance.

## 3. Category A — Computer monitors

### Taxonomy
- Office/study: text clarity, ergonomics, glare, ports, flicker.
- Productivity/docking: USB-C video, Power Delivery, hub/KVM, daisy-chain.
- Design/color: gamut, calibration, Delta E method, uniformity, bit depth, LUT.
- Gaming: refresh, response behavior, overshoot, input lag, VRR, motion clarity, HDR.
- Portable/specialist: size, power, touch, pen and industrial/medical-specific needs.

### Mandatory attributes
**Identity:** manufacturer, exact model, regional suffix, manufacturer P/N, generation, panel revision if published, color, included stand/accessories, firmware and region.

**Display:** diagonal, aspect ratio, native resolution, PPI, panel technology, surface, curvature, backlight/local dimming, native contrast, SDR sustained brightness, HDR peak brightness and measurement window, refresh by input, native vs overclocked refresh, bit depth (native/FRC), gamut by named color space, accuracy and test condition.

**Motion:** GtG method/transitions, MPRT/strobing mode, overshoot, overdrive setting, input lag, VRR range and standards. Never collapse these into one “1 ms” field.

**Connectivity:** exact HDMI/DP/USB-C versions, max resolution/refresh per port, DSC requirement, USB-C DP Alt Mode, PD wattage, USB data speed, KVM, audio, HDCP and cable requirements.

**Ergonomics:** height/tilt/swivel/pivot, VESA, stand footprint, flicker and low-blue-light claims/certifications.

### Model/marketing traps
- Same family name can hide different resolution, panel, refresh or region suffix.
- “200Hz” may be overclocked while native is 180Hz; port, cable and GPU requirements matter.
- GtG and MPRT are not interchangeable; MPRT may use backlight strobing and reduce brightness.
- Response-time headline may apply only to fastest overdrive mode with overshoot.
- HDR10 signal acceptance is not VESA DisplayHDR certification and neither alone proves good HDR performance.
- “99% DCI-P3” is gamut coverage, not Delta E accuracy or uniformity.
- USB-C connector presence does not guarantee video, data and laptop charging.
- Max refresh may differ by HDMI vs DisplayPort, resolution, bit depth and DSC.
- “Eye-care” marketing is not a guarantee of no eye strain.

### Feasibility
- Verification difficulty: **Medium**.
- Data stability: **Medium-high** for core panel/resolution/ports; medium for firmware, panel revision and regional suffix.
- 100–300 model estimate: **45–75 initial hours** after schema/source template; add 1–2 hours/model for deeper evidence review and periodic checks. Excludes retailer offers.
- Main bottleneck: exact local SKU/port capability and comparable independent response/HDR tests.
- Confidence: high for official specs; medium for real-world performance until matched test data exists.

## 4. Category B — Audio (scope: personal headphones/headsets)

### Taxonomy
- True wireless earbuds (in-ear, open-fit, stem, sealed).
- Wireless over-ear/on-ear headphones.
- Wired headphones/IEMs.
- Gaming headsets (mic-first).
- Speakers/soundbars are separate future subcategories; do not mix their schema with headphones.

### Mandatory attributes
**Identity:** exact model, generation, region, color, ear-tip/size bundle, case/transmitter variant, included cable/dongle, firmware/app version.

**Acoustics:** transducer type/size, manufacturer frequency-response claim vs independent measurement, tuning, EQ, codec/sample-rate support, wired/USB mode, impedance/sensitivity for wired devices, distortion/noise where measured.

**Wireless:** Bluetooth version/profile, codecs by platform, multipoint, LE Audio/LC3, latency/game mode, dongle protocol and range caveats.

**ANC/transparency:** modes, measured attenuation by frequency, wind handling, transparency, adaptive behavior. “X dB cancellation” requires method and frequency.

**Fit/comfort:** form factor, weight, clamping force where measured, tips, seal dependency, IP rating and controls. Fit is individual.

**Calls:** mic array, beamforming/AI claims, independent samples in quiet/noisy environments.

**Battery/durability:** playback with ANC on/off, test volume/codec, case capacity, charge time, replaceable battery/ear pads, warranty and spare parts.

### Model/marketing traps
- Similar names with different generation or SE/Plus/Pro/II suffix.
- Region can affect codec, assistant, radio or bundle.
- Frequency range does not predict neutral sound or quality.
- Codec support on headphone does not mean every phone/OS supports it.
- ANC maximum dB claims lack value without frequency and method.
- Runtime depends on ANC, codec, volume, multipoint and calls.
- Earbud per-charge runtime differs from total runtime including case.
- IP rating may apply to earbuds but not case.
- Hi-Res/LDAC support does not prove better perceived sound for every listener.
- Comfort, sound preference and seal cannot be inferred from a spec sheet.

### Feasibility
- Verification difficulty: **Medium-high**.
- Data stability: **Medium**; firmware, app, codec, region and accessories can change.
- 100–300 model estimate: **60–100 initial hours** plus 2–3 hours/model for independent evidence/use-case review.
- Main bottleneck: repeatable independent measurements plus qualitative fit/call assessment.
- Confidence: high for published connectivity/battery claims; medium for codec compatibility; medium-low for sound/comfort without test evidence and user context.

## 5. Category C — Air purifiers

### Taxonomy
- Small bedroom/personal room.
- Medium/large living room.
- Particle filtration (HEPA-class).
- Particle + activated-carbon odor/VOC-focused devices.
- Smart/sensor-driven units.
- Commercial/HVAC/specialized units are separate categories.

### Mandatory attributes
**Identity:** exact model and regional suffix, filter cartridge code/revision, voltage, plug, generation and market.

**Performance:** CADR by smoke/dust/pollen where reported; test standard/report ID; airflow/speed; CADR at each speed if available; room-size assumptions and ACH; particle efficiency/size; gas/VOC test conditions and carbon mass if disclosed.

**Filter:** HEPA standard/grade (do not equate “HEPA-like” with certified HEPA), pre-filter, carbon, replacement filter SKU, availability and interval.

**Noise/energy:** dBA by mode and test distance, power by mode, standby power.

**Sensors/controls:** PM2.5/particle and VOC sensors, accuracy disclosure, auto mode, app, Wi-Fi, display and child lock.

**Maintenance/safety:** filter replacement, cleaning, ionizer/plasma/UV emissions and ozone evidence, warranty, spare filters and local service.

### Model/marketing traps
- Same chassis with different filter bundle/region suffix.
- “Room size up to X m²” depends on ACH, ceiling height and assumed operating speed.
- CADR must identify pollutant and test standard; do not compare incompatible methods without caveat.
- Maximum CADR may only occur in loud turbo mode.
- Particle CADR does not prove gas/VOC removal.
- Filter-media efficiency is not whole-device clean-air delivery.
- Virus-removal claim needs organism, chamber, time, distance and mode; it is not infection-prevention proof.
- Ionizer/plasma/UV claims need ozone/emissions evidence.
- Filter replacement interval depends on use and environment.

### Feasibility
- Verification difficulty: **Medium**.
- Data stability: **Medium-high** for CADR/filter SKU; medium for filter availability, local replacement cost and room-size claims.
- 100–300 model estimate: **40–70 initial hours** plus 1–2 hours/model for standards/report checks.
- Main bottleneck: comparable standards, room-size assumptions, gas/VOC evidence and replacement-filter ecosystem.
- Confidence: high with exact test standard/report ID; medium for manufacturer summary; low for broad health claims without underlying evidence.

## 6. Category D — Laptops

### Taxonomy
- Thin-and-light/office/study.
- Business/enterprise.
- Creator/workstation.
- Gaming/performance.
- 2-in-1/convertible/detachable.
- Chromebook/education/budget.
- Mobile workstation and gaming are distinct thermal/performance classes.

### Mandatory attributes
**Identity/configuration:** exact machine type/model (MTM), P/N, region, chassis, exact CPU/GPU SKU and GPU TGP, RAM capacity/type/channel/soldered/slots, SSD/capacity/slots, panel option, wireless module, OS, battery and charger.

**Performance:** sustained CPU/GPU under repeatable load, power limits, fan profile, thermal throttling, noise, benchmark version, RAM configuration and ambient conditions.

**Display:** panel technology, resolution, refresh, brightness, gamut, response, PWM/flicker, accuracy and panel option code.

**Mobility:** laptop and charger weight, dimensions, battery Wh, real-world runtime test method, charge rate, USB-C PD and ports.

**Upgrade/service:** RAM upgradeability, SSD slots, Wi-Fi card, battery replacement, keyboard layout, warranty, parts and Vietnam service.

**Compatibility:** USB-C/Thunderbolt/USB4, external display support, dock compatibility, drivers and charger wattage.

### Model/marketing traps
- Family contains many CPU/GPU/panel/RAM configurations.
- Same model name may have different panel quality, battery or ports.
- “Up to” CPU/GPU/RAM does not identify the retail configuration.
- CPU family name hides architecture, core count, power limits and generation.
- GPU name alone is insufficient; laptop GPU TGP and cooling change performance.
- Soldered vs socketed RAM and single vs dual channel affect upgrades/performance.
- Display options vary in brightness, refresh, gamut, OLED/LCD and touch.
- Battery claims depend on workload, brightness, wireless and test method.
- Regional keyboard, OS, charger and warranty differ.
- Benchmarks across power modes, RAM configurations or test versions are invalid.

### Feasibility
- Verification difficulty: **High**.
- Data stability: **Low-medium** at family level; stable after exact MTM/configuration is known.
- 100–300 model estimate: **100–180 initial hours** plus 2–4 hours/model for configuration and independent performance review.
- Main bottleneck: exact local configuration identity and comparable sustained performance/battery data.
- Confidence: high for official MTM-specific PSREF/support docs; medium for independent tests when configuration differs; low for unspecified retail bundle.

## 7. Cross-category operations

| Category | Identity key | Critical normalized fields | Main mismatch risk | Initial effort for 100–300 | Refresh |
|---|---|---|---|---:|---|
| Monitor | Model + regional P/N + panel/revision | Resolution, panel, refresh by port, response method, color, HDR, USB-C PD | Native/OC, GtG/MPRT, port limits | 45–75h | 6 months / spec change |
| Audio | Model + generation + region + bundle | Form, codec, ANC, mic, battery condition, IP | Codec/platform, ANC claim, gen suffix | 60–100h | 3–6 months / firmware |
| Air purifier | Model + region + filter cartridge | CADR by pollutant/standard, ACH assumptions, filter, noise | Room area, test standard, filter variant | 40–70h | 6 months / filter revision |
| Laptop | MTM/P/N + CPU/GPU/RAM/display config | CPU/GPU/TGP, panel, memory, battery, ports | Same family with multiple configs | 100–180h | 3–6 months / SKU change |

Effort estimates are planning judgments after schema/source template exists. They exclude price/stock crawling, legal rights work, affiliate tracking, content production and full lab testing.

### Data model
Keep three distinct layers:
1. **Product family** — marketing family/group, never a purchasable identity.
2. **Canonical model/configuration** — exact manufacturer model + region + configuration.
3. **Retail offer** — seller SKU/P/N, price, stock, warranty, URL, timestamp and affiliate metadata.

Never merge a retail offer into a canonical model solely because title strings resemble each other. Maintain alias table, identity confidence, source timestamp and unresolved state. Every field should carry scope: family, model, configuration or offer.

## 8. Ten-model pilot shortlist

The sample contains five monitors and five over-ear headphones. This is a research shortlist, not a ranking. Vietnam retail P/N, warranty, stock and price are pending unless separately verified.

### Monitors — five candidates

| ID | Exact model | Use case | Manufacturer-published facts | Caveat |
|---|---|---|---|---|
| MON-01 | LG 27GS85Q-B | Gaming/motion | 27-inch QHD Nano IPS; 180Hz native, 200Hz O/C; 1ms GtG claim; DisplayHDR 400 claim | 200Hz requires supported DP 1.4 GPU/cable; 1ms requires Faster response mode. |
| MON-02 | ASUS ProArt PA279CRV | Design/creator/USB-C | 27-inch 4K IPS; 99% DCI-P3 and Adobe RGB claims; ΔE<2 claim; USB-C PD 96W; VESA DisplayHDR 400 | Validate calibration report scope and regional package. |
| MON-03 | BenQ GW2790Q | Office/study | 27-inch QHD IPS; 100Hz; 5ms GtG and 1ms MPRT separately listed; 99% sRGB | MPRT is not comparable to GtG; check local port limits. |
| MON-04 | BenQ MA270U | Mac/USB-C productivity | 27-inch 4K IPS; 60Hz; 99% sRGB, 95% P3; HDR10/DisplayHDR 400 claim | Verify PD wattage, port topology and host compatibility from full spec/manual. |
| MON-05 | ASUS TUF Gaming VG27AQ3A | Gaming/motion | Exact manufacturer model name identified; QHD gaming family | Full VN timing table and exact local P/N remain pending; do not publish port-specific claims until verified. |

### Audio — five candidates

| ID | Exact model | Use case | Evidence state | Caveat |
|---|---|---|---|---|
| AUD-01 | Sony WH-1000XM5 | ANC/travel/office | Sony Vietnam spec page: approx. 250g, Bluetooth 5.2, SBC/AAC/LDAC, up to 30h ANC on / 40h off | Runtime is manufacturer maximum, not independent battery test. |
| AUD-02 | Sennheiser MOMENTUM 4 Wireless | Travel/battery/sound | Exact model-family candidate | Capture official regional spec/support page and P/N before detailed comparison; no unverified codec/runtime claims. |
| AUD-03 | Bose QuietComfort Ultra Headphones (1st Gen) | ANC/comfort/travel | Generation explicitly specified | Do not merge with later generation; exact regional SKU/support page pending. |
| AUD-04 | JBL Tour One M2 | Calls/travel/ANC | Exact model name candidate | Attach official M2 spec page at ingest; do not reuse M3 or other Tour series data. |
| AUD-05 | Apple AirPods Max (USB-C) | Apple ecosystem/over-ear | USB-C version identified as distinct from Lightning version | Record connector version; features/compatibility vary by OS and ecosystem. |

**Pilot caveat:** the Sony WH-1000XM5 and four monitor candidates have directly accessible manufacturer evidence listed below. Other audio candidates are identity-workflow candidates only until their official regional spec pages and retail P/N are attached. If a page/P/N cannot be resolved, quarantine the record; do not substitute a similar model silently.

## 9. QA rules and test cases

Reject/quarantine if only a family name is known and configurations differ; regional P/N conflicts; key field comes only from a retailer title; method is absent for a measurement-dependent field; manufacturer claim is represented as independent test; connector shape/family name is used to infer features; or local warranty/stock/price/affiliate eligibility is guessed.

Required tests:
1. LG 27GS85Q-B: 180Hz native vs 200Hz O/C.
2. BenQ GW2790Q: 5ms GtG vs 1ms MPRT.
3. ASUS PA279CRV: gamut vs accuracy; USB-C PD distinct from data/video.
4. HDR10 support vs VESA DisplayHDR certification vs measured HDR performance.
5. Monitor max refresh by resolution, bit depth, DSC and port.
6. Sony WH-1000XM5 codec support vs source-device codec support.
7. Headphone runtime: ANC on/off, manufacturer max vs measured.
8. ANC marketing claim vs frequency-dependent independent attenuation.
9. Bose QC Ultra 1st Gen vs later generation.
10. Air purifier CADR pollutant/test standard; room area needs ACH assumptions.
11. Air purifier filter cartridge code and local replacement availability.
12. Laptop ASUS UX3405MA vs UX3405CA configuration distinction.
13. Laptop GPU model vs TGP/thermal design.
14. Laptop soldered RAM and panel option.
15. Across categories: manufacturer fact, independent measurement, expert inference and unknown are separate data types.

## 10. Evidence register — checked 12/11/2026

| ID | Source | Supports | Type / confidence |
|---|---|---|---|
| E01 | https://www.lg.com/vn/man-hinh-may-tinh/man-hinh-gaming-ultragear/27gs85q-b/ | LG 27GS85Q-B identity, 180Hz native/200Hz O/C, QHD, 1ms mode condition | Manufacturer VN / High for stated spec |
| E02 | https://www.asus.com/vn/displays-desktops/monitors/proart/proart-display-pa279crv/techspec/ | PA279CRV resolution, gamut, ΔE, refresh, ports, PD and certification | Manufacturer VN / High for published claim |
| E03 | https://www.benq.com/vi-vn/monitor/home/gw2790q/spec.html | GW2790Q 100Hz, GtG vs MPRT, sRGB | Manufacturer VN / High |
| E04 | https://www.benq.com/vi-vn/monitor/home/ma270u/spec.html | MA270U resolution, refresh, gamut and HDR claim | Manufacturer VN / High; full PD/port table to confirm |
| E05 | https://www.rtings.com/monitor/learn/how-we-test | Common monitor test bench and bench-version caveat | Independent lab method / High |
| E06 | https://www.sony.com.vn/electronics/tai-nghe-choang-dau-tai-nghe/wh-1000xm5/specifications | WH-1000XM5 weight, BT, codecs and claimed battery | Manufacturer VN / High for published spec |
| E07 | https://www.rtings.com/headphones/learn/how-we-test | Repeatable headphone testing, purchased units and test philosophy | Independent lab method / High |
| E08 | https://www.philips.com.vn/c-p/AC1715_20/1000i-series-air-purifier-for-medium-rooms | Philips AC1715/20 CADR 300 m³/h, HEPA/carbon and room-area claim | Manufacturer VN / High for claim; standard assumptions need review |
| E09 | https://www.mi.com/vn/product/xiaomi-smart-air-purifier-4-pro/ | Xiaomi 4 Pro PM CADR 500 m³/h, report WCk-21-50469, stated 35–60m² | Manufacturer with cited test report / Medium-high; report not independently audited here |
| E10 | https://www.asus.com/vn/news/u7ptzawqintzxvit/ | UX3405 family CPU options and 3K OLED specs | Manufacturer VN / High for family-level variants |
| E11 | https://www.asus.com/us/laptops/for-home/zenbook/asus-zenbook-14-ux3405/techspec/ | UX3405MA vs UX3405CA processor/configuration distinction | Manufacturer US / High for US matrix; do not assume identical VN configs |
| E12 | https://psref.lenovo.com/product/ | Lenovo MTM-specific product specification reference | Manufacturer database / High; exact MTM required |
| E13 | https://displayhdr.org/ and https://compliance.vesa.org/ | DisplayHDR certification scheme | Standards body / High |
| E14 | https://ahamverifide.org/ahams-air-filtration-standards/ | CADR/air filtration standard framework | Industry certification body / High |
| E15 | https://www.energy.gov/sites/default/files/2023-02/air-cleaners-tp-fr.pdf | Air cleaner/CADR technical context and limitations | Government technical report / High for background |

Source rule: store URL, title, publisher, retrieval date, relevant section, exact model scope and whether manufacturer-declared or independently measured. Regional family page rather than exact SKU page means identity confidence Medium/Pending. Recheck redirects before publication.

## 11. Not concluded

- No demand, search-volume, TAM/SAM/SOM or competitor-share claim.
- No commission, EPC, conversion, payout or unit-economics claim.
- No claim any shortlist item is currently in stock, has a specific Vietnam warranty or is affiliate-eligible.
- No hands-on testing, listening session, room test or laptop benchmark by A Long.
- No final category/MVP choice.

## 12. Handoff

**A Long:** owns taxonomy, technical dictionary, identity, source confidence and QA; quarantine unresolved models.

**Vân Anh:** review whether use-case labels map to real purchase questions and decision barriers. Customer insight cannot validate technical specs. No review response is assumed or fabricated here.

**CEO/Engineering:** review feasibility separately from business choice. Engineering can use family → canonical configuration → retail offer. Do not scale to 100–300 records until the 10-model sample passes identity and evidence QA.

### Completion checklist
- [x] Compare all four categories.
- [x] Taxonomy and mandatory attributes per category.
- [x] Model/variant and marketing-claim traps.
- [x] Verification difficulty, data stability and 100–300 model effort estimates.
- [x] Ten-model shortlist across two categories, with unresolved fields marked.
- [x] Sources, checked date and confidence.
- [x] Distinguish manufacturer facts, independent evidence, expert judgment and unknown.
- [ ] CEO review/acceptance.
- [ ] Verify local retail P/N, warranty and offers before public catalog ingestion.
