# AMD Ryzen 5 9600X Review - The Best Sub-$300 Gaming CPU | TechPowerUp

**Site:** techpowerup

---

## Introduction

[Image: AMD Logo]

AMD Ryzen 5 9600X is the latest kid on the block, and the most affordable ticket to the Ryzen 9000 series Granite Ridge desktop processor family powered by the new Zen 5 architecture. The processor is targeted at the upper mid-range, with enough processing muscle on offer for a feature-packed gaming PC build. This processor can be paired with even a high-end graphics card, and play at the highest resolutions, with no noticeable performance drops compared to processors from a higher segment. It's only when you combine gaming with streaming, video effects and overlays on the side like popular creators do, that you might miss having more cores. AMD is positioning the Ryzen 5 9600X against its main rival from the Intel camp, the Core i5-14600K. 


The AMD Ryzen 5 9600X is a classic multicore processor with a 6-core/12-thread configuration. The company continues to stick to CPU core counts from its past three generations, as each new generation of Zen delivered on IPC gains, energy efficiency, and competitiveness with Intel in key client desktop applications such as AAA games, and popular creativity suites. AMD held a technological edge over Intel in foundry process each generation thanks to its partnership with TSMC, so the company never really needed efficiency cores (E-cores), either to shore up core counts, or reduce power-draw in light workloads.


The new Zen 5 microarchitecture is claimed by AMD to offer a roughly 16% increase in IPC over Zen 4, which when paired with the nominal increases in clock speeds, should account for increased gaming performance over the previous generation, at comparable power. Besides the new architecture, AMD is also building its CPU core complex dies (CCDs) on the more refined 4 nm TSMC N4P foundry node, which is claimed to offer 22% improved power characteristics over the 5 nm TSMC N5 node that AMD built its Zen 4 CCDs on. Both the Ryzen 5 9600X, and the 8-core Ryzen 7 9700X that are launching today come with a 65 W TDP, compared to the 105 W that the 7600X and 7700X launched with.


The new Zen 5 microarchitecture introduces several design updates across the length and breadth of the core, as you'll learn on the next page. There is a larger share of engineering focus on the core's execution engine, which includes the integer and floating point units. The FPU is now bolstered with a real 512-bit data-path, compared to the dual-pumped 256-bit data-path on Zen 4, which AMD claims increases performance of 512-bit SIMD workloads by 20-35%, when using instruction-sets such as AVX-512, VNNI, etc., AMD also worked to increase the intra-core bandwidth, and made all on-die caches faster. 


The Ryzen 5 9600X ticks at a base frequency of 3.90 GHz, with a maximum boost frequency of 5.40 GHz. Each of its six Zen 5 cores comes with 1 MB of dedicated L2 cache, and the six cores share 32 MB of L3 cache. AMD has given this chip a TDP of 65 W. Since it's built for the existing Socket AM5, the 9600X is compatible with all AMD 600-series chipset motherboards with a BIOS update, as well as being drop-in compatible with motherboards based on the upcoming 800-series chipset. AMD is pricing the Ryzen 5 9600X at $280. This is $20 less than what the 7600X launched at.


## Short 9-Minute Summary of this Review

Our goal with the videos is to create short summaries, not go into all the details and test results, which can be found on the following pages of this review.


| | Price | Cores / Threads | Base Clock | Max. Boost | L3 Cache | TDP | Architecture | Process | Socket |
|---|---|---|---|---|---|---|---|---|---|
| Intel Core i5 | | | | | | | | | |
| Core i5-12400F | $150 | 6 / 12 | 2.5 GHz | 4.4 GHz | 18 MB | 65 W | Alder Lake | 10 nm | LGA 1700 |
| Core i5-13400F | $170 | 6+4 / 16 | 2.5 / 1.8 GHz | 4.6 / 3.3 GHz | 20 MB | 65 W | Raptor Lake | 10 nm | LGA 1700 |
| Core i5-12600K | $245 | 6+4 / 16 | 3.7 / 2.8 GHz | 4.9 / 3.6 GHz | 20 MB | 125 W | Alder Lake | 10 nm | LGA 1700 |
| Core i5-13600K | $240 | 6+8 / 20 | 3.5 / 2.6 GHz | 5.1 / 3.9 GHz | 24 MB | 125 W | Raptor Lake | 10 nm | LGA 1700 |
| Core i5-14600K | $300 | 6+8 / 20 | 3.5 / 2.6 GHz | 5.3 / 4.0 GHz | 24 MB | 125 W | Raptor Lake | 10 nm | LGA 1700 |
| AMD Ryzen 5 | | | | | | | | | |
| Ryzen 5 8500G | $160 | 6 / 12 | 3.5 GHz | 5.0 GHz | 16 MB | 65 W | Phoenix 2 | 4 nm | AM5 |
| Ryzen 5 5600X | $135 | 6 / 12 | 3.7 GHz | 4.6 GHz | 32 MB | 65 W | Zen 3 | 7 nm | AM4 |
| Ryzen 5 7600 | $185 | 6 / 12 | 3.8 GHz | 5.1 GHz | 32 MB | 65 W | Zen 4 | 5 nm | AM5 |
| Ryzen 5 7600X | $195 | 6 / 12 | 4.7 GHz | 5.3 GHz | 32 MB | 105 W | Zen 4 | 5 nm | AM5 |
| Ryzen 5 9600X | $280 | 6 / 12 | 3.9 GHz | 5.4 GHz | 32 MB | 65 W | Zen 5 | 4 nm | AM5 |
| Intel Core i7 | | | | | | | | | |
| Core i7-12700K | $315 | 8+4 / 20 | 3.6 / 2.7 GHz | 5.0 / 3.8 GHz | 25 MB | 125 W | Alder Lake | 10 nm | LGA 1700 |
| Core i7-13700K | $320 | 8+8 / 24 | 3.4 / 2.5 GHz | 5.4 / 4.2 GHz | 30 MB | 125 W | Raptor Lake | 10 nm | LGA 1700 |
| Core i7-14700K | $380 | 8+12 / 28 | 3.4 / 2.5 GHz | 5.6 / 4.3 GHz | 33 MB | 125 W | Raptor Lake | 10 nm | LGA 1700 |
| AMD Ryzen 7 | | | | | | | | | |
| Ryzen 7 5700G | $160 | 8 / 16 | 3.8 GHz | 4.6 GHz | 16 MB | 65 W | Zen 3 + Vega | 7 nm | AM4 |
| Ryzen 7 5700X | $160 | 8 / 16 | 3.4 GHz | 4.6 GHz | 32 MB | 65 W | Zen 3 | 7 nm | AM4 |
| Ryzen 7 7700 | $280 | 8 / 16 | 3.8 GHz | 5.3 GHz | 32 MB | 65 W | Zen 4 | 5 nm | AM5 |
| Ryzen 7 7700X | $290 | 8 / 16 | 4.5 GHz | 5.4 GHz | 32 MB | 105 W | Zen 4 | 5 nm | AM5 |
| Ryzen 7 9700X | $360 | 8 / 16 | 3.8 GHz | 5.5 GHz | 32 MB | 65 W | Zen 5 | 4 nm | AM5 |
| Ryzen 7 5800X | $175 | 8 / 16 | 3.8 GHz | 4.7 GHz | 32 MB | 105 W | Zen 3 | 7 nm | AM4 |
| Ryzen 7 5800X3D | $340 | 8 / 16 | 3.4 GHz | 4.5 GHz | 96 MB | 105 W | Zen 3 | 7 nm | AM4 |
| Ryzen 7 7800X3D | $370 | 8 / 16 | 4.2 GHz | 5.0 GHz | 96 MB | 120 W | Zen 4 | 5 nm | AM5 |
| Intel Core i9 | | | | | | | | | |
| Core i9-12900K | $425 | 8+8 / 24 | 3.2 / 2.4 GHz | 5.2 / 3.9 GHz | 30 MB | 125 W | Alder Lake | 10 nm | LGA 1700 |
| Core i9-13900K | $445 | 8+16 / 32 | 3.0 / 2.2 GHz | 5.8 / 4.3 GHz | 36 MB | 125 W | Raptor Lake | 10 nm | LGA 1700 |
| Core i9-14900K | $555 | 8+16 / 32 | 3.2 / 2.4 GHz | 6.0 / 4.4 GHz | 36 MB | 125 W | Raptor Lake | 10 nm | LGA 1700 |
| AMD Ryzen 9 | | | | | | | | | |
| Ryzen 9 5900X | $265 | 12 / 24 | 3.7 GHz | 4.8 GHz | 64 MB | 105 W | Zen 3 | 7 nm | AM4 |
| Ryzen 9 7900 | $370 | 12 / 24 | 3.7 GHz | 5.4 GHz | 64 MB | 65 W | Zen 4 | 5 nm | AM5 |
| Ryzen 9 7900X | $360 | 12 / 24 | 4.7 GHz | 5.6 GHz | 64 MB | 170 W | Zen 4 | 5 nm | AM5 |
| Ryzen 9 7900X3D | $395 | 12 / 24 | 4.4 GHz | 5.6 GHz | 128 MB | 120 W | Zen 4 | 5 nm | AM5 |
| Ryzen 9 9900X | $500 | 12 / 24 | 4.4 GHz | 5.6 GHz | 64 MB | 120 W | Zen 5 | 4 nm | AM5 |
| Ryzen 9 5950X | $355 | 16 / 32 | 3.4 GHz | 4.9 GHz | 64 MB | 105 W | Zen 3 | 7 nm | AM4 |
| Ryzen 9 7950X | $525 | 16 / 32 | 4.5 GHz | 5.7 GHz | 64 MB | 170 W | Zen 4 | 5 nm | AM5 |
| Ryzen 9 7950X3D | $530 | 16 / 32 | 4.2 GHz | 5.7 GHz | 128 MB | 120 W | Zen 4 | 5 nm | AM5 |
| Ryzen 9 9950X | $650 | 16 / 32 | 4.3 GHz | 5.7 GHz | 64 MB | 170 W | Zen 5 | 4 nm | AM5 |
