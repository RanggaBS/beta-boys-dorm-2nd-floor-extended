# Beta Boys' Dorm 2nd Floor Extended

[![Mod Showcase](https://img.youtube.com/vi/3tbJK_lIytA/maxresdefault.jpg)](https://youtu.be/3tbJK_lIytA)

> Bringing life back to a forgotten floor — restored, expanded, and made functional.

## Download

| NexusMods                                                                                                                                                      | Mirror                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| [![Download on NexusMods](https://img.shields.io/badge/DOWNLOAD-NEXUSMODS-orange?style=for-the-badge)](https://nexusmods.com/bullyscholarshipedition/mods/306) | [![Download SE](https://img.shields.io/badge/DOWNLOAD-MIRROR-blue?style=for-the-badge)](https://sfl.gl/hELKAquA) |

---

## Overview

**Beta Boys' Dorm 2nd Floor Extended** is an enhancement and continuation of the original _Beta Boys' Dorm 2nd Floor_ mod released by **Cautious** in 2020.

While the original mod successfully restored the cut second floor of the Boys’ Dorm, several elements were still missing: no NPC activity upstairs, incomplete lighting, and non-functional bathroom interiors.

This extension focuses on **immersion and usability** — adding pedestrian activity, refined lighting, atmospheric effects, and fully functional bathroom props to make the second floor feel like a real, lived-in space rather than a static restoration.

---

## Features

- 5 **pedestrian spawners** placed behind room doors on the 2nd floor
- Improved and adjusted **interior lighting**
- Subtle **window haze / mist effects** to enhance atmosphere
- Multiple **Points of Interest (POIs)** (crying, hanging out, smoking, wall-leaning)
- Fully **functional bathroom props**:
  - Toilets
  - Sinks
  - Urinals

---

## Installation

> 💡 **Important**  
> Always back up your game folder or modified files before installing any mod.

1. Install **IMG Factory 1.2**  
   (Recommended over G-IMG)

   - Download:  
     [IMGF 1.2 Installer](https://github.com/MexUK/IMGF/releases/download/1.2.revived.1/IMGF.1.2.Installer.2024.zip)

2. Follow the original installation steps shown in **Cautious’ showcase video**  
   (linked below).

   - ⚠️ Note: This version specifically uses **IMG Factory 1.2**.

3. Replace the following files using the contents of this mod:

   - **DAT / Trigger.img**

     - `BDorm_Doors.dat`
     - `eventsBDorm.dat`

   - **Graphics/**

     - `gsa_info.dat`

   - **Scripts / Scripts.img**

     - `SWinEff.lur`
     - `Bdorm.lur`

   - **Stream / World.img**
     - `isc_dorm.col`

4. Rebuild all IMG archives using **IMG Factory**.

---

## Known Issues

- **Occasional light flickering** may occur due to overlapping light sources.  
  Fine-tuning interior lighting in this area is particularly sensitive.
- **Pedestrian stacking** can happen when multiple NPCs spawn at the same door position, which may cause brief lag or stuck behavior.

---

## Changelog

> **EA** = Early Access

### 1.1.0

- script/Bdorm.lua
  - Added Pedro and Sheldon spawning in the Boys Dorm
  - Restored their night pajama appearances

### 1.0.0

- Initial public release

### EA_2025-11-07

- **Lighting**

  - Added lighting to the attic area
  - Added light fills to stairwell windows
  - Added light fill below the foyer railing near the stairs
  - Adjusted hallway light source angles
  - Added light fills to the player room windows (2x)
  - Added light fill to the small room leading to the attic
  - Reduced light ranges to prevent crashes
  - Removed one spotlight in the toilet room (now using a single spotlight)
  - Adjusted spotlight placement:
    - Stairwell windows
    - Bathroom windows (3x)

- **DAT**

  - Fixed crying POI pedestrian facing direction in the attic access room

- **Scripts**

  - Adjusted stairwell window haze angle and distance
  - Added invisible bathroom props to enable interaction

---

### EA_2025-09-21

- Initial Early Access release for supporters.

---

## Support the Development

If you enjoy this mod and want to support future updates or new projects, you can support me on Ko-fi:

[![Ko-fi](https://img.shields.io/badge/Support-Ko--fi-FF5A16?logo=kofi&style=flat-square)](https://ko-fi.com/ranggabs)
[![Trakteer](https://img.shields.io/badge/Support-Trakteer-E50027?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAEFklEQVRogdWaz28aRxTHP28gjusWe6VWiiIqZX2p6Sn0whnU3Gv+ARvfkZprcjG+1MfEku+x8w/Y+QMskyuX0lOcUzaVt1arRN1A6jbE7PQApvyG3R3X5CshscPue9/HvJn33ZkRxuCMlN2ELOi7grYEsQEbQINF62MCnoDX/u4Ang+OQj8XVPU2J86oB2VY4ympgkKva8gaIhgRuqpRO19zstf/S08AZ6RsH/8AJP2/cQsGRyG57h7pBHBGytboY91OkRlGTxDqsvUTIQ/QzpIWFLRy/hMh34akT0kVoNMD+sdrZBMKCr0OIK2Bq1+ZMjyXzTCXTgHw9+ERTcc1ZXoAClmWX/lmNYYcTL59Mqwn2ywU8j1t9dIu9a1dE+YHoJENpZCsCWNLjx4OkAdIlIp8fn/NhIsh0GklcMeEqXEkv9gsmnAxAEEvKTEgB2J2cuRv53sHePkinxXyzGUzUV31QFB2HMQGHcmQ9upD2+tbu6Dhy+Onnbam4/Imt2ZkcGu0rSbfNhm+V+NDudLTduG4NB2XRKk3fWJ2EuvJtgm3ACiNNqIovY0HXHT9qxe/vBiZMjezmbFpFwCWwpAkbjoub3Nr1Ld2aZQrNPp65IpgictKtAEwBguF/NB0uXBc/lj+3ogPYwGMSon4kHbfq/Ox+sKEW+ImjCw9ehi4WJ3vHeBtPIjs28gsFG9rn2DPfGvCdfQemF+9R+N5hebr3nl9YX1QVnQjZiVYKOQ534smwyKNgWHiLSiiplLoFFoo5COTv7QTReyF7oFbr45MFSOajsvvIafVUD2grMWR5JtejUa50lOVh7V1I2YnUdZiGCrhBvEo8u93nlK7/1PnOlEq4ns1/nr8n5iz9raHDnBlJ/GrtcBcQqXQXDbDV10KE4JV11t/Voj1/eNvcmuh5IeROgDwz7Oj6e/dPzTl1lwA1wVjAdy4O301nv/BjJADgwHczGZITPHum9gsGpt+wXAKJUrFsUEkNosDb2hRYXwMjAriKshDKwBv4l0B0R/EVZEHvLggXtD34lGrEN1IlIrcaMvs+dV74ehNhheqEvvedBUzCPGwyywKtBP0oabj0pwyiKnsebVQAQjiKB95HcapyWr64XD6Kt4NjX6nQIcaxO8f749Ul0Fw4bihV681OAqkGubhy3Wg8/3wr4SNcoW3EZYZFapsZINDWYvE06lOhR22lAJ0ekx7dRrlytSTwUi/yLIA/MbK8ezsCU+NapKX3ykAH9m/bjZBoZEd6Nondln5GZjVDe5+OEleLkOXFlJIXlrnFGYdjkJylxedAG5z4giSm+0gdHXkUYNunJIqSGvveCZSSpCyD/sTD3v044yU/RE/LUg2hrpDS/TZAG0BaPC4jXSO22hwfPQ7QaoxKI87bvMvhqeFrYuJbTEAAAAASUVORK5CYII=&style=flat-square)](https://trakteer.id/ranggabs)
[![Saweria](https://img.shields.io/badge/Support-Saweria-FAAE2B?style=flat-square)](https://saweria.co/ranggabs)

---

## Credits

- **Cautious**  
  Original _Beta Boys' Dorm 2nd Floor_ mod (2020)

- **Simon Bestia**  
  _One Percent Better Project_ (NexusMods)  
  Base lighting file (`gsa_info.dat`, compiled from `gsa_info.xml`)

- **marcdred**  
  Navigation mesh for the 2nd floor (`isc_dorm.col`)

- **RBS ID**  
  Extension work: pedestrian spawns, lighting adjustments, atmospheric effects, and gameplay improvements

---

## Showcase & Resources

- Original mod showcase by **Cautious**:  
  [YouTube – Beta Boys' Dorm 2nd Floor](https://youtube.com/watch?v=eWqNxDWXlZc)

- IMG Factory 1.2:  
  [IMGF 1.2 Installer](https://github.com/MexUK/IMGF/releases/download/1.2.revived.1/IMGF.1.2.Installer.2024.zip)

---

## ⚠️ Redistribution Notice

Redistribution or re-uploading of this mod is **strictly prohibited**.  
You may only share links to the **official NexusMods page** or the **GitHub repository**.
