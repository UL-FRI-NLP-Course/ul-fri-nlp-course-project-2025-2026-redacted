# AMD Ryzen 7 9800X3D Review - The Best Gaming Processor | TechPowerUp

**Site:** techpowerup

---

## Introduction

[Image: AMD Logo]

The new AMD Ryzen 7 9800X3D is an unexpected entry to the 2024 processor product launch cycle—gamers will be happy. AMD's X3D processor lineup features 3D vertical-stacked cache, or 3D V-Cache. AMD designed the CPU complex dies (CCDs) of recent Ryzen CPUs in a way that the 32 MB on-die L3 cache can be expanded to 96 MB with stacked cache dies. This large cache is known to have a profound impact on gaming performance. With the X3D processors, AMD is going for gaming performance leadership. It knows the enthusiast PC segment as well as Intel does, and how big a role gaming performance plays in processor and platform selection. This is why the company innovated the X3D series.


The Ryzen 7 9800X3D comes in just three months after the company's debut of the Ryzen 9000 series processors powered by the latest Zen 5 microarchitecture. It is widely believed that the November 2024 launch of the 9800X3D was deliberate, so the chip could clash with Intel Core Ultra Series 200 family powered by the Arrow Lake microarchitecture. Before we could get our hands on the latest Intel chips, we had honestly expected Arrow Lake to deliver a significant gaming performance improvement over Raptor Lake, and we're sure AMD did the same. Not wanting to end up with a situation where processors such as the 7800X3D are wildly outclassed by Intel, the company probably rushed in the 9800X3D, the 8-core, single-CCD chip with the best chance at having the highest generational gaming performance leap.


Alas, interesting things happened over the past three months. The Zen 5 microarchitecture barely posted a 5% gaming performance increase over Zen 4, and worse, Arrow Lake barely beat Raptor Lake in gaming, in many cases ending up slower, albeit with an energy efficiency leap. Even the fastest Core Ultra 9 285K could not trump the Ryzen 7 7800X3D in gaming, and so the 9800X3D has a rather easy task ahead—simply to beat the 7800X3D, and extend AMD's gaming performance leadership over Intel.


Likely anticipating Arrow Lake to be much faster at gaming than it ended up being, AMD gave the 9800X3D two key improvements over the 7800X3D. Firstly, the company increased clock speeds. The 9800X3D ticks at a base frequency of 4.70 GHz, which is a 500 MHz increase over that of the 7800X3D. The maximum boost frequency is 200 MHz higher, at 5.20 GHz. This increase in base frequency means that the average clock frequencies over multiple cores will end up higher, even if the new Zen 5 microarchitecture doesn't have a significant contribution to gaming performance from its generational IPC increase, these clock speeds should see the 9800X3D through. 


The second, and perhaps bigger innovation, is at a physical level—AMD inverted the CCD+L3D stack. In the past two generations of X3D desktop processors, namely the 7800X3D Raphael-X powered by Zen 4 and the 5800X3D Vermeer-X powered by Zen 3, the 3D V-Cache die is stacked on top of the CPU complex die (CCD). The chip would stack over the central region of the CCD that has the 32 MB on-die L3 cache, while structural silicon would top the peripheral regions of the CCD that had the CPU cores. This structural silicon levels out the stack, and handles the crucial task of transferring heat from the CPU cores to the surface, where it's picked up by the solder TIM, and transferred to the integrated heat spreader (IHS). With the new 9800X3D Granite Ridge-X, AMD has inverted the CCD+L3D stack. The CCD is now on top, and the L3D is below it. The L3D now has not just the 64 MB add-on L3 cache memory, but also serves as a sort of base tile for the CCD on top. It is peppered with TSVs in the peripheral region, so it could connect the Zen 5 CPU cores from the CCD to the fiberglass substrate below.


This inversion of the 3D V-Cache stack has the obvious advantage of the CCD's thermals behaving like they do on the regular Ryzen 9000 series processors without 3D V-Cache. There should be a marked improvement in heat transfer from the CPU cores to the STIM and IHS, which is how AMD was able to increase the base frequency significantly. Then there's also how Zen 5 X3D is said to now have the same overclocking capabilities as the regular 9000-series processors.


The new AMD Zen 5 microarchitecture sees the company rework pretty much all key components of the core compared to Zen 4, with a focus particularly on the number crunching machinery. The core comes with a true 512-bit floating point data-path to more effectively execute 512-bit SIMD workloads that use instruction-sets such as AVX-512, VNNI, etc.; when compared to Zen 4, which uses a dual-pumped 256-bit data-path to execute these instruction-sets. AMD also increased the bandwidth and associativity of the per core caches, and improved the bandwidth of the L3 cache. There are also generational improvements to the branch prediction unit. The CCD is built on the newer TSMC N4P (4 nm) foundry node, which improves power and clock speeds. Besides the 4.70 GHz base frequency and 5.20 GHz boost frequency, the Ryzen 7 9800X3D comes with a TDP of 120 W, same as that of the 7800X3D.


AMD is pricing the eight-core Ryzen 7 9800X3D at an eye-watering $480, a $30 increase over the launch price of the 7800X3D. It's also roughly $80 higher than the 20-core Core Ultra 7 265K and Core i7-14700K, while being just $40 cheaper than the Core i9-14900K and $80 less than the 285K. This is, in the end, an 8-core/16-thread processor. Apparently eight cores is all that games need, even Intel thinks so, which is why the company's P-core count tops out at eight. So, as an 8-core chip, the 9800X3D is being targeted squarely at gamers. 


| | Price | Cores / Threads | Base Clock | Max. Boost | L3 Cache | TDP | Architecture | Process | Socket |
|---|---|---|---|---|---|---|---|---|---|
| Intel Core i5 | | | | | | | | | |
| Core i5-12400F | $110 | 6 / 12 | 2.5 GHz | 4.4 GHz | 18 MB | 65 W | Alder Lake | 10 nm | LGA 1700 |
| Core i5-13400F | $170 | 6+4 / 16 | 2.5 / 1.8 GHz | 4.6 / 3.3 GHz | 20 MB | 65 W | Raptor Lake | 10 nm | LGA 1700 |
| Core i5-12600K | $170 | 6+4 / 16 | 3.7 / 2.8 GHz | 4.9 / 3.6 GHz | 20 MB | 125 W | Alder Lake | 10 nm | LGA 1700 |
| Core i5-13600K | $225 | 6+8 / 20 | 3.5 / 2.6 GHz | 5.1 / 3.9 GHz | 24 MB | 125 W | Raptor Lake | 10 nm | LGA 1700 |
| Core i5-14600K | $260 | 6+8 / 20 | 3.5 / 2.6 GHz | 5.3 / 4.0 GHz | 24 MB | 125 W | Raptor Lake | 10 nm | LGA 1700 |
| Intel Core Ultra 5 | | | | | | | | | |
| Core Ultra 5 245K | $310 | 6+8 / 14 | 4.2 / 3.6 GHz | 5.2 / 4.6 GHz | 24 MB | 159 W | Arrow Lake | 3 nm | LGA 1851 |
| AMD Ryzen 5 | | | | | | | | | |
| Ryzen 5 8500G | $150 | 6 / 12 | 3.5 GHz | 5.0 GHz | 16 MB | 65 W | Phoenix 2 | 4 nm | AM5 |
| Ryzen 5 5600X | $135 | 6 / 12 | 3.7 GHz | 4.6 GHz | 32 MB | 65 W | Zen 3 | 7 nm | AM4 |
| Ryzen 5 7600 | $185 | 6 / 12 | 3.8 GHz | 5.1 GHz | 32 MB | 65 W | Zen 4 | 5 nm | AM5 |
| Ryzen 5 7600X | $210 | 6 / 12 | 4.7 GHz | 5.3 GHz | 32 MB | 105 W | Zen 4 | 5 nm | AM5 |
| Ryzen 5 9600X | $250 | 6 / 12 | 3.9 GHz | 5.4 GHz | 32 MB | 65 W | Zen 5 | 4 nm | AM5 |
| Intel Core i7 | | | | | | | | | |
| Core i7-12700K | $210 | 8+4 / 20 | 3.6 / 2.7 GHz | 5.0 / 3.8 GHz | 25 MB | 125 W | Alder Lake | 10 nm | LGA 1700 |
| Core i7-13700K | $280 | 8+8 / 24 | 3.4 / 2.5 GHz | 5.4 / 4.2 GHz | 30 MB | 125 W | Raptor Lake | 10 nm | LGA 1700 |
| Core i7-14700K | $355 | 8+12 / 28 | 3.4 / 2.5 GHz | 5.6 / 4.3 GHz | 33 MB | 125 W | Raptor Lake | 10 nm | LGA 1700 |
| Intel Core Ultra 7 | | | | | | | | | |
| Core Ultra 7 265K | $395 | 8+12 / 20 | 3.9 / 3.3 GHz | 5.5 / 4.6 GHz | 30 MB | 250 W | Arrow Lake | 3 nm | LGA 1851 |
| AMD Ryzen 7 | | | | | | | | | |
| Ryzen 7 5700G | $165 | 8 / 16 | 3.8 GHz | 4.6 GHz | 16 MB | 65 W | Zen 3 + Vega | 7 nm | AM4 |
| Ryzen 7 5700X | $160 | 8 / 16 | 3.4 GHz | 4.6 GHz | 32 MB | 65 W | Zen 3 | 7 nm | AM4 |
| Ryzen 7 7700 | $280 | 8 / 16 | 3.8 GHz | 5.3 GHz | 32 MB | 65 W | Zen 4 | 5 nm | AM5 |
| Ryzen 7 7700X | $275 | 8 / 16 | 4.5 GHz | 5.4 GHz | 32 MB | 105 W | Zen 4 | 5 nm | AM5 |
| Ryzen 7 9700X | $330 | 8 / 16 | 3.8 GHz | 5.5 GHz | 32 MB | 65 W | Zen 5 | 4 nm | AM5 |
| Ryzen 7 5800X | $165 | 8 / 16 | 3.8 GHz | 4.7 GHz | 32 MB | 105 W | Zen 3 | 7 nm | AM4 |
| Ryzen 7 5800X3D | $340 | 8 / 16 | 3.4 GHz | 4.5 GHz | 96 MB | 105 W | Zen 3 | 7 nm | AM4 |
| Ryzen 7 7800X3D | $450 | 8 / 16 | 4.2 GHz | 5.0 GHz | 96 MB | 120 W | Zen 4 | 5 nm | AM5 |
| Ryzen 7 9800X3D | $480 | 8 / 16 | 4.7 GHz | 5.2 GHz | 96 MB | 120 W | Zen 5 | 4 nm | AM5 |
| Intel Core i9 | | | | | | | | | |
| Core i9-12900K | $280 | 8+8 / 24 | 3.2 / 2.4 GHz | 5.2 / 3.9 GHz | 30 MB | 125 W | Alder Lake | 10 nm | LGA 1700 |
| Core i9-13900K | $415 | 8+16 / 32 | 3.0 / 2.2 GHz | 5.8 / 4.3 GHz | 36 MB | 125 W | Raptor Lake | 10 nm | LGA 1700 |
| Core i9-14900K | $445 | 8+16 / 32 | 3.2 / 2.4 GHz | 6.0 / 4.4 GHz | 36 MB | 125 W | Raptor Lake | 10 nm | LGA 1700 |
| Intel Core Ultra 9 | | | | | | | | | |
| Core Ultra 9 285K | $590 | 8+16 / 24 | 3.7 / 3.2 GHz | 5.7 / 4.6 GHz | 36 MB | 250 W | Arrow Lake | 3 nm | LGA 1851 |
| AMD Ryzen 9 | | | | | | | | | |
| Ryzen 9 5900X | $265 | 12 / 24 | 3.7 GHz | 4.8 GHz | 64 MB | 105 W | Zen 3 | 7 nm | AM4 |
| Ryzen 9 7900 | $370 | 12 / 24 | 3.7 GHz | 5.4 GHz | 64 MB | 65 W | Zen 4 | 5 nm | AM5 |
| Ryzen 9 7900X | $400 | 12 / 24 | 4.7 GHz | 5.6 GHz | 64 MB | 170 W | Zen 4 | 5 nm | AM5 |
| Ryzen 9 7900X3D | $580 | 12 / 24 | 4.4 GHz | 5.6 GHz | 128 MB | 120 W | Zen 4 | 5 nm | AM5 |
| Ryzen 9 9900X | $430 | 12 / 24 | 4.4 GHz | 5.6 GHz | 64 MB | 120 W | Zen 5 | 4 nm | AM5 |
| Ryzen 9 5950X | $345 | 16 / 32 | 3.4 GHz | 4.9 GHz | 64 MB | 105 W | Zen 3 | 7 nm | AM4 |
| Ryzen 9 7950X | $510 | 16 / 32 | 4.5 GHz | 5.7 GHz | 64 MB | 170 W | Zen 4 | 5 nm | AM5 |
| Ryzen 9 7950X3D | $550 | 16 / 32 | 4.2 GHz | 5.7 GHz | 128 MB | 120 W | Zen 4 | 5 nm | AM5 |
| Ryzen 9 9950X | $600 | 16 / 32 | 4.3 GHz | 5.7 GHz | 64 MB | 170 W | Zen 5 | 4 nm | AM5 |
