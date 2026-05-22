# Intel Core i9-14900K Review - Reaching for the Performance Crown | TechPowerUp

**Site:** techpowerup

---

## Introduction

[Image: Intel Logo]

Intel refreshed its desktop processor lineup quite literally, with today's launch of the 14th Gen Core series based on the Raptor Lake Refresh silicon. The 14th Gen Core forms Intel's final series in the current nomenclature for client processors, with the company switching over to a newer branding scheme for the next generation with Core and Core Ultra; and the doing away of generational numbering, but making it more implicit in the specific processor model number. This series aims to restore Intel's competitiveness against AMD's Ryzen 7000X3D series, and should see the company's client desktop competitiveness through at least until the second half of 2024.


As a refresh, the 14th Gen Core processors are fully compatible with all Socket LGA1700 motherboards available in the market, including those based on the older 600-series chipset, and the current 700-series chipset; however some of the older boards may require a BIOS firmware update. With the socket infrastructure remaining the same, those with older 12th Gen processors or lower models of the 13th Gen, have a new processor series to upgrade to with minimal effort.


Raptor Lake Refresh is not a new microarchitecture, much in the same way the 9th Gen Coffee Lake Refresh wasn't. It is an exercise in shoring up the competitiveness across price-points, by introducing new processor SKUs with increased clock speeds, a few new performance enhancements for select SKUs, and CPU core-count increases for the Core i7 SKUs.


Intel isn't introducing a new silicon with this series, and so we're still left with the Raptor Lake silicon built on the Intel 7 process. This monolithic die comes with 8 P-cores (performance cores), 16 E-cores (efficiency cores), with 2 MB of L2 cache per P-core, 4 MB of L2 cache per E-core cluster of 4 cores each; and 36 MB of shared L3 cache. Compared to its predecessor, the i9-13900K, the new i9-14900K comes with increased clock speeds. The P-cores come with a base frequency of 3.20 GHz, and a maximum boost frequency of 6.00 GHz, on par with the Limited Edition Core i9-13900KS which was sold at a $100 premium. The E-cores see frequency upticks, too, with 2.40 GHz base, and 4.40 GHz maximum turbo. Both these constitute a 200 MHz uplift over the clock speeds of the i9-13900K.


At launch, the Core i9-14900K gets an exclusive feature in the form of the Intel Application Optimization (APO). An extension of Intel Dynamic Tuning framework, the feature promises game-specific optimizations for the processor, resulting in performance uplifts to the tune of 13% for "Tom Clancy's Rainbow Six Siege," and 16% for "Metro Exodus." It works by optimizing the machine's thread scheduling and manages application resource allocation in real-time. At launch, APO is exclusive to the 14th Gen Core i9 series, and only benefits two games, but the company plans to add more titles through software updates. Intel also introduced the AI Assist feature to Extreme Tuning Utility (XTU), which works exclusively for the 14th Gen Core i9. This feature uses a localized AI DNN to determine the best automated performance tuning settings specific to the user's hardware.


Intel is pricing the Core i9-14900K at $589, you can save a further $25 by opting for the i9-14900KF, which lacks integrated graphics if you don't need it. This launch price is the same as the i9-13900K, and since the two chips share a platform, it is expected that Intel may get its retail channel partners to trim prices of the older 13th Gen chips.


## Short 5-Minute Summary of this Review

Our goal with the videos is to create short summaries, not go into all the details and test results, which can be found on the following pages of this review.


| | Price | Cores / Threads | Base Clock | Max. Boost | L3 Cache | TDP | Architecture | Process | Socket |
|---|---|---|---|---|---|---|---|---|---|
| Core i7-13700K | $410 | 8+8 / 24 | 3.4 / 2.5 GHz | 5.4 / 4.2 GHz | 30 MB | 125 W | Raptor Lake | 10 nm | LGA 1700 |
| Core i7-14700K | $410 | 8+12 / 28 | 3.4 / 2.5 GHz | 5.6 / 4.3 GHz | 33 MB | 125 W | Raptor Lake | 10 nm | LGA 1700 |
| Ryzen 7 5800X | $260 | 8 / 16 | 3.8 GHz | 4.7 GHz | 32 MB | 105 W | Zen 3 | 7 nm | AM4 |
| Ryzen 7 5800X3D | $360 | 8 / 16 | 3.4 GHz | 4.5 GHz | 96 MB | 105 W | Zen 3 | 7 nm | AM4 |
| Ryzen 9 3900X | $350 | 12 / 24 | 3.8 GHz | 4.6 GHz | 64 MB | 105 W | Zen 2 | 7 nm | AM4 |
| Ryzen 5 7600 | $225 | 6 / 12 | 3.8 GHz | 5.1 GHz | 32 MB | 65 W | Zen 4 | 5 nm | AM5 |
| Ryzen 5 7600X | $250 | 6 / 12 | 4.7 GHz | 5.3 GHz | 32 MB | 105 W | Zen 4 | 5 nm | AM5 |
| Ryzen 9 5900X | $350 | 12 / 24 | 3.7 GHz | 4.8 GHz | 64 MB | 105 W | Zen 3 | 7 nm | AM4 |
| Core i9-10900K | $350 | 10 / 20 | 3.7 GHz | 5.3 GHz | 20 MB | 125 W | Comet Lake | 14 nm | LGA 1200 |
| Core i9-11900K | $330 | 8 / 16 | 3.5 GHz | 5.3 GHz | 16 MB | 125 W | Rocket Lake | 14 nm | LGA 1200 |
| Ryzen 9 5950X | $490 | 16 / 32 | 3.4 GHz | 4.9 GHz | 64 MB | 105 W | Zen 3 | 7 nm | AM4 |
| Ryzen 7 7700 | $330 | 8 / 16 | 3.8 GHz | 5.3 GHz | 32 MB | 65 W | Zen 4 | 5 nm | AM5 |
| Ryzen 7 7700X | $350 | 8 / 16 | 4.5 GHz | 5.4 GHz | 32 MB | 105 W | Zen 4 | 5 nm | AM5 |
| Core i9-12900K | $425 | 8+8 / 24 | 3.2 / 2.4 GHz | 5.2 / 3.9 GHz | 30 MB | 125 W | Alder Lake | 10 nm | LGA 1700 |
| Core i9-12900KS | $620 | 8+8 / 24 | 3.4 / 2.5 GHz | 5.5 / 4.0 GHz | 30 MB | 125 W | Alder Lake | 10 nm | LGA 1700 |
| Ryzen 7 7800X3D | $400 | 8 / 16 | 4.2 GHz | 5.0 GHz | 96 MB | 120 W | Zen 4 | 5 nm | AM5 |
| Ryzen 9 7900 | $410 | 12 / 24 | 3.7 GHz | 5.4 GHz | 64 MB | 65 W | Zen 4 | 5 nm | AM5 |
| Ryzen 9 7900X | $450 | 12 / 24 | 4.7 GHz | 5.6 GHz | 64 MB | 170 W | Zen 4 | 5 nm | AM5 |
| Ryzen 9 7900X3D | $600 | 12 / 24 | 4.4 GHz | 5.6 GHz | 128 MB | 120 W | Zen 4 | 5 nm | AM5 |
| Ryzen 9 7950X | $590 | 16 / 32 | 4.5 GHz | 5.7 GHz | 64 MB | 170 W | Zen 4 | 5 nm | AM5 |
| Ryzen 9 7950X3D | $685 | 16 / 32 | 4.2 GHz | 5.7 GHz | 128 MB | 120 W | Zen 4 | 5 nm | AM5 |
| Core i9-13900K | $570 | 8+16 / 32 | 3.0 / 2.2 GHz | 5.8 / 4.3 GHz | 36 MB | 125 W | Raptor Lake | 10 nm | LGA 1700 |
| Core i9-13900KS | $730 | 8+16 / 32 | 3.2 / 2.4 GHz | 6.0 / 4.3 GHz | 36 MB | 150 W | Raptor Lake | 10 nm | LGA 1700 |
| Core i9-14900K | $590 | 8+16 / 32 | 3.2 / 2.4 GHz | 6.0 / 4.4 GHz | 36 MB | 125 W | Raptor Lake | 10 nm | LGA 1700 |
