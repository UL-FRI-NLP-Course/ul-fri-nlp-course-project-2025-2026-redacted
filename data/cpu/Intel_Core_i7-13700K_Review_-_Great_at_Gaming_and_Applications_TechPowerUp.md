# Intel Core i7-13700K Review - Great at Gaming and Applications | TechPowerUp

**Site:** techpowerup

---

## Introduction

[Image: Intel Logo]

The Core i7-13700K "Raptor Lake" is one of the three processor models that Intel launched this month. While we reviewed the i9-13900K and the i5-13600K, we're posting our i7-13700K review just now. The 13th Gen Core "Raptor Lake" desktop processor family gains significance as it's the last processor lineup from Intel to use a monolithic silicon, as the company plans to pivot to chiplets with its IDM 2.0 manufacturing strategy, with Meteor Lake and beyond. Raptor Lake also doubles down on the company's Hybrid architecture, which let it win big against AMD's rampaging "Zen 3." The idea behind this is that even the most demanding client workloads don't need more than 8 high-performance cores (P-cores), and a large number of power-optimized yet reasonably fast efficiency cores (E-cores) should fit the bill for multi-threaded workloads.


With the 13th Gen Core "Raptor Lake" series, Intel increased the CPU core-counts, but using more E-cores only. The P-core counts remain the same generationally, although the P-cores themselves received a performance uplift (to a smaller extent, so did the E-cores). The top Core i9-13900K has 8 P-cores and 16 E-cores (8P+16E), while the Core i5-13600K has a 6P+8E configuration. The new Core i7-13700K in this review attempts to strike a middle-ground, with an 8P+8E configuration which resembles that of the previous-gen flagship i9-12900K. This is not to say that Intel is repeating what it did with the Core i9-9900K and Core i7-10700K (which were functionally the same chip). The i7-13700K is physically different from the i9-12900K.


Each of the eight P-cores on the i7-13700K is a new-gen "Raptor Cove" core, featuring larger 2 MB dedicated L2 caches (compared to 1.25 MB on the "Golden Cove" P-cores); while each of the two "Gracemont" E-core clusters gets 4 MB of L2 cache shared among the four E-cores in the cluster (an increase from 2 MB per cluster on "Alder Lake"). Both the P-cores and E-cores receive updates to the L2 cache hardware-prefetchers; the 30 MB of L3 cache that's shared among the eight P-cores and two E-core clusters now gets new inclusive/non-inclusive cache partitioning mode; and overall, the i7-13700K comes with higher clock-speeds than the i9-12900K. The P-cores are clocked at 3.40 GHz, with 5.40 GHz boost frequency; while the E-cores run at 2.50 GHz, with 4.20 GHz boost—both of which are higher than the clocks on the i9-12900K.


Perhaps the most attractive aspect of the Core i7-13700K is its price of $410. For just $90 more than the i5-13600K (6P+8E), you're getting two additional P-cores; whereas the Core i9-13900K is $180 more, and only gives you two additional E-core clusters (8 more E-cores); besides slightly higher clock-speeds. Intel carved the i7-13700K out of the "Raptor Lake" silicon by simply disabling two of the four E-core clusters, and reducing the L3 cache from 36 MB down to 30 MB. If you're sure you don't need integrated graphics, you can save $25, by opting for the Core i7-13700KF at $385. In this review we tell you if this part can potentially save you $180-$205 over the Core i9 part, and yet give you everything you need.


| | Price | Cores / Threads | Base Clock | Max. Boost | L3 Cache | TDP | Architecture | Process | Socket |
|---|---|---|---|---|---|---|---|---|---|
| Core i7-10700K | $325 | 8 / 16 | 3.8 GHz | 5.1 GHz | 16 MB | 125 W | Comet Lake | 14 nm | LGA 1200 |
| Core i7-11700K | $305 | 8 / 16 | 3.6 GHz | 5.0 GHz | 16 MB | 125 W | Rocket Lake | 14 nm | LGA 1200 |
| Ryzen 7 3700X | $215 | 8 / 16 | 3.6 GHz | 4.4 GHz | 32 MB | 65 W | Zen 2 | 7 nm | AM4 |
| Ryzen 7 5700G | $270 | 8 / 16 | 3.8 GHz | 4.6 GHz | 16 MB | 65 W | Zen 3 + Vega | 7 nm | AM4 |
| Core i7-12700K | $365 | 8+4 / 20 | 3.6 / 2.7 GHz | 5.0 / 3.8 GHz | 25 MB | 125 W | Alder Lake | 10 nm | LGA 1700 |
| Ryzen 7 5700X | $240 | 8 / 16 | 3.4 GHz | 4.6 GHz | 32 MB | 65 W | Zen 3 | 7 nm | AM4 |
| Core i7-13700K | $450 | 8+8 / 24 | 3.4 / 2.5 GHz | 5.4 / 4.2 GHz | 30 MB | 125 W | Raptor Lake | 10 nm | LGA 1700 |
| Ryzen 7 5800X | $270 | 8 / 16 | 3.8 GHz | 4.7 GHz | 32 MB | 105 W | Zen 3 | 7 nm | AM4 |
| Ryzen 7 5800X3D | $380 | 8 / 16 | 3.4 GHz | 4.5 GHz | 96 MB | 105 W | Zen 3 | 7 nm | AM4 |
| Core i9-10900 | $400 | 10 / 20 | 2.8 GHz | 5.2 GHz | 20 MB | 65 W | Comet Lake | 14 nm | LGA 1200 |
| Ryzen 9 3900X | $380 | 12 / 24 | 3.8 GHz | 4.6 GHz | 64 MB | 105 W | Zen 2 | 7 nm | AM4 |
| Ryzen 5 7600X | $300 | 6 / 12 | 4.7 GHz | 5.3 GHz | 32 MB | 105 W | Zen 4 | 5 nm | AM5 |
| Ryzen 9 5900X | $400 | 12 / 24 | 3.7 GHz | 4.8 GHz | 64 MB | 105 W | Zen 3 | 7 nm | AM4 |
| Core i9-10900K | $310 | 10 / 20 | 3.7 GHz | 5.3 GHz | 20 MB | 125 W | Comet Lake | 14 nm | LGA 1200 |
| Core i9-11900K | $360 | 8 / 16 | 3.5 GHz | 5.3 GHz | 16 MB | 125 W | Rocket Lake | 14 nm | LGA 1200 |
| Ryzen 9 3950X | $495 | 16 / 32 | 3.5 GHz | 4.7 GHz | 64 MB | 105 W | Zen 2 | 7 nm | AM4 |
| Ryzen 9 5950X | $550 | 16 / 32 | 3.4 GHz | 4.9 GHz | 64 MB | 105 W | Zen 3 | 7 nm | AM4 |
| Ryzen 7 7700X | $400 | 8 / 16 | 4.5 GHz | 5.4 GHz | 32 MB | 105 W | Zen 4 | 5 nm | AM5 |
| Core i9-12900K | $500 | 8+8 / 24 | 3.2 / 2.4 GHz | 5.2 / 3.9 GHz | 30 MB | 125 W | Alder Lake | 10 nm | LGA 1700 |
| Core i9-12900KS | $620 | 8+8 / 24 | 3.4 / 2.5 GHz | 5.5 / 4.0 GHz | 30 MB | 125 W | Alder Lake | 10 nm | LGA 1700 |
| Ryzen 9 7900X | $550 | 12 / 24 | 4.7 GHz | 5.6 GHz | 64 MB | 170 W | Zen 4 | 5 nm | AM5 |
| Ryzen 9 7950X | $700 | 16 / 32 | 4.5 GHz | 5.7 GHz | 64 MB | 170 W | Zen 4 | 5 nm | AM5 |
| Core i9-13900K | $590 | 8+16 / 32 | 3.0 / 2.2 GHz | 5.8 / 4.3 GHz | 36 MB | 125 W | Raptor Lake | 10 nm | LGA 1700 |
