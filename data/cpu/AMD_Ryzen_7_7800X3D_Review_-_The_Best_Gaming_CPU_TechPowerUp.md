# AMD Ryzen 7 7800X3D Review - The Best Gaming CPU | TechPowerUp

**Site:** techpowerup

---

## Introduction

[Image: AMD Logo]

In this review we're testing AMD's new Ryzen 7 7800X3D, which is the company's latest gaming monster based on the 3D Vertical Cache technology. It features an 8-core Zen 4 CCD with high frequencies, and should be able to provide a generational gaming performance uplift, letting AMD surpass even the fastest of Intel's 13th Gen Core Raptor Lake processors at gaming. For the bulk of gamers and e-sports athletes that aren't big on "gaming++" workloads such as streaming, heavy video processing, and live social media; and just need a processor for maxed out AAA gaming at the highest resolutions, with the fastest graphics cards available, the 7800X3D is supposed to be their knight in shining armor.


So what exactly is it? The Ryzen 7 7800X3D in this review is an 8-core/16-thread Socket AM5 processor based on the same Zen 4 microarchitecture the company debuted its Ryzen 7000 series desktop processor family with, but featuring the 3D Vertical Cache technology that had a transformative impact on gaming performance in the previous-generation Ryzen 7 5800X3D. AMD discovered that a large cache significantly improves gaming performance, and cuts down round-trips to main memory. It hence innovated additional silicon that has 64 MB of fast SRAM cache, which is stacked on top of the CCD (CPU core complex die), and is made contiguous with the 32 MB on-die L3 cache. The CPU cores and software see a 96 MB single L3 cache. 


AMD released the Ryzen 7 5800X3D around the time when its Ryzen 5000 Zen 3 series found itself bested by Intel's 12th Gen Core Alder Lake. The 5800X3D beat the fastest Core i9-12900K in gaming, forcing Intel to scamper for Special Edition chips with limited availability, such as the i9-12900KS, that level up to the 5800X3D, but at enormous power needed to maintain a 5.00 GHz all-core boost for the processor's eight P-cores. Fast forward to 2023 and we see the 7800X3D wanting to eat Intel's lunch in the high-end gaming CPU market once again, with its sights set on the Core i9-13900K.


Games don't need more than eight high-performance cores, and even Intel agrees with this notion. This is why the 5800X3D dominated the i9-12900K despite the lack of E-cores. Intel's 24-core i9-13900K only comes with eight P-cores, which handle gaming workloads. If the E-cores can get a nibble out of the processor's power-budget, they can handle background tasks. Intel is working with game developers to optimize for the Hybrid architecture and take advantage of the E-cores at a game-engine level, but so far we haven't come across a game that does this the way Intel means it. Besides, getting the E-core clusters busy would mean reduced power budget and boost-residency for the P-cores.


The sharpest critique for the 5800X3D has been that since it only has eight cores, it falls behind competing Intel processors that additionally have E-cores, in multi-threaded productivity workloads. AMD doesn't want Intel to get away making the same argument this time, and released the 16-core and 12-core 7950X3D and 7900X3D last month, which use 3D Vertical Cache on one of the two CCDs, while the other is a regular Zen 4 CCD with just 32 MB on-die cache. For non-gaming, multi-threaded productivity workloads, you get the full benefit of the high core-count, and our testing has shown the 7950X3D to present itself as a strong competitor to the i9-13900K. As a dual-CCD processor, however, there are some drawbacks, the biggest of which is to ensure that gaming workloads reside on the CCD with the 3D Vertical Cache, and there is no mis-scheduling to the other CCD. AMD released several software-based mechanisms to ensure the 7950X3D and 7900X3D work as intended. As you will see throughout this review, there's no such issue with the 7800X3D, as all its CPU cores are localized to a single CCD with 96 MB of L3 cache.


A known design drawback with 3D Vertical Cache SKUs has been that AMD adjusted power, thermals, and frequency. The 3D Vertical Cache itself operates at the same frequency as the CPU cores, so it can only be stable up to a certain frequency. AMD set the maximum boost frequency of the 7800X3D at 5.00 GHz. The overclocking options are far too limited compared to the 7700X. The T-junction max temperature is lowered, which means the processor's boosting algorithm has narrower thermal headroom in which to sustain boost frequencies. The TDP, however, is slightly increased at 120 W, compared to 105 W of the 7700X. The 5.00 GHz frequency means that the 7800X3D relies heavily on the 3D Vertical Cache feature to achieve its gaming performance targets, while non-gaming workloads which aren't memory-intensive, could actually run faster on the 7700X, which can boost up to 5.40 GHz and has a higher thermal limit.


Today's review subject, the Ryzen 7 7800X3D, costs an eye-watering $450, which puts its price higher than not just the Core i7-13700K, but also two of AMD's own 12-core SKUs, namely the 7900X and 7900. It's still significantly lower than the $580 i9-13900K, and the $750 7950X3D. In return, AMD is promising the 7800X3D to be the fastest processor for gamers to max-out their games, and pair with the fastest graphics cards out there.


| | Price | Cores / Threads | Base Clock | Max. Boost | L3 Cache | TDP | Architecture | Process | Socket |
|---|---|---|---|---|---|---|---|---|---|
| Core i5-10600K | $170 | 6 / 12 | 4.1 GHz | 4.8 GHz | 12 MB | 125 W | Comet Lake | 14 nm | LGA 1200 |
| Core i5-11600K | $200 | 6 / 12 | 3.9 GHz | 4.9 GHz | 12 MB | 125 W | Rocket Lake | 14 nm | LGA 1200 |
| Ryzen 5 5600X | $170 | 6 / 12 | 3.7 GHz | 4.6 GHz | 32 MB | 65 W | Zen 3 | 7 nm | AM4 |
| Core i5-12600K | $210 | 6+4 / 16 | 3.7 / 2.8 GHz | 4.9 / 3.6 GHz | 20 MB | 125 W | Alder Lake | 10 nm | LGA 1700 |
| Core i5-13600K | $290 | 6+8 / 20 | 3.5 / 2.6 GHz | 5.1 / 3.9 GHz | 24 MB | 125 W | Raptor Lake | 10 nm | LGA 1700 |
| Core i7-10700K | $260 | 8 / 16 | 3.8 GHz | 5.1 GHz | 16 MB | 125 W | Comet Lake | 14 nm | LGA 1200 |
| Core i7-11700K | $240 | 8 / 16 | 3.6 GHz | 5.0 GHz | 16 MB | 125 W | Rocket Lake | 14 nm | LGA 1200 |
| Ryzen 7 3700X | $200 | 8 / 16 | 3.6 GHz | 4.4 GHz | 32 MB | 65 W | Zen 2 | 7 nm | AM4 |
| Ryzen 7 5700G | $200 | 8 / 16 | 3.8 GHz | 4.6 GHz | 16 MB | 65 W | Zen 3 + Vega | 7 nm | AM4 |
| Core i7-12700K | $320 | 8+4 / 20 | 3.6 / 2.7 GHz | 5.0 / 3.8 GHz | 25 MB | 125 W | Alder Lake | 10 nm | LGA 1700 |
| Ryzen 7 5700X | $190 | 8 / 16 | 3.4 GHz | 4.6 GHz | 32 MB | 65 W | Zen 3 | 7 nm | AM4 |
| Core i7-13700K | $425 | 8+8 / 24 | 3.4 / 2.5 GHz | 5.4 / 4.2 GHz | 30 MB | 125 W | Raptor Lake | 10 nm | LGA 1700 |
| Ryzen 7 5800X | $240 | 8 / 16 | 3.8 GHz | 4.7 GHz | 32 MB | 105 W | Zen 3 | 7 nm | AM4 |
| Ryzen 7 5800X3D | $310 | 8 / 16 | 3.4 GHz | 4.5 GHz | 96 MB | 105 W | Zen 3 | 7 nm | AM4 |
| Ryzen 9 3900X | $350 | 12 / 24 | 3.8 GHz | 4.6 GHz | 64 MB | 105 W | Zen 2 | 7 nm | AM4 |
| Ryzen 5 7600 | $230 | 6 / 12 | 3.8 GHz | 5.1 GHz | 32 MB | 65 W | Zen 4 | 5 nm | AM5 |
| Ryzen 5 7600X | $245 | 6 / 12 | 4.7 GHz | 5.3 GHz | 32 MB | 105 W | Zen 4 | 5 nm | AM5 |
| Ryzen 9 5900X | $345 | 12 / 24 | 3.7 GHz | 4.8 GHz | 64 MB | 105 W | Zen 3 | 7 nm | AM4 |
| Core i9-10900K | $350 | 10 / 20 | 3.7 GHz | 5.3 GHz | 20 MB | 125 W | Comet Lake | 14 nm | LGA 1200 |
| Core i9-11900K | $350 | 8 / 16 | 3.5 GHz | 5.3 GHz | 16 MB | 125 W | Rocket Lake | 14 nm | LGA 1200 |
| Ryzen 9 5950X | $500 | 16 / 32 | 3.4 GHz | 4.9 GHz | 64 MB | 105 W | Zen 3 | 7 nm | AM4 |
| Ryzen 7 7700 | $330 | 8 / 16 | 3.8 GHz | 5.3 GHz | 32 MB | 65 W | Zen 4 | 5 nm | AM5 |
| Ryzen 7 7700X | $325 | 8 / 16 | 4.5 GHz | 5.4 GHz | 32 MB | 105 W | Zen 4 | 5 nm | AM5 |
| Core i9-12900K | $430 | 8+8 / 24 | 3.2 / 2.4 GHz | 5.2 / 3.9 GHz | 30 MB | 125 W | Alder Lake | 10 nm | LGA 1700 |
| Core i9-12900KS | $620 | 8+8 / 24 | 3.4 / 2.5 GHz | 5.5 / 4.0 GHz | 30 MB | 125 W | Alder Lake | 10 nm | LGA 1700 |
| Ryzen 7 7800X3D | $450 | 8 / 16 | 4.2 GHz | 5.0 GHz | 96 MB | 120 W | Zen 4 | 5 nm | AM5 |
| Ryzen 9 7900 | $430 | 12 / 24 | 3.7 GHz | 5.4 GHz | 64 MB | 65 W | Zen 4 | 5 nm | AM5 |
| Ryzen 9 7900X | $425 | 12 / 24 | 4.7 GHz | 5.6 GHz | 64 MB | 170 W | Zen 4 | 5 nm | AM5 |
| Ryzen 9 7900X3D | $600 | 12 / 24 | 4.4 GHz | 5.6 GHz | 128 MB | 120 W | Zen 4 | 5 nm | AM5 |
| Ryzen 9 7950X | $575 | 16 / 32 | 4.5 GHz | 5.7 GHz | 64 MB | 170 W | Zen 4 | 5 nm | AM5 |
| Ryzen 9 7950X3D | $700 | 16 / 32 | 4.2 GHz | 5.7 GHz | 128 MB | 120 W | Zen 4 | 5 nm | AM5 |
| Core i9-13900K | $570 | 8+16 / 32 | 3.0 / 2.2 GHz | 5.8 / 4.3 GHz | 36 MB | 125 W | Raptor Lake | 10 nm | LGA 1700 |
| Core i9-13900KS | $730 | 8+16 / 32 | 3.2 / 2.4 GHz | 6.0 / 4.3 GHz | 36 MB | 150 W | Raptor Lake | 10 nm | LGA 1700 |
