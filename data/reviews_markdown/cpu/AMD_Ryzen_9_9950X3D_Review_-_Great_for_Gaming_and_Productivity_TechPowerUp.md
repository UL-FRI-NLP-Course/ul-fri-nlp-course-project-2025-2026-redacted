# AMD Ryzen 9 9950X3D Review - Great for Gaming and Productivity | TechPowerUp

**Site:** techpowerup

---

## Introduction

[Image: AMD Logo]

AMD Ryzen 9 9950X3D is the company's new flagship desktop processor, and looks to round up AMD's leadership with not just gaming performance, but also productivity and content creation. The 9950X3D and 9900X3D are high core-count siblings of the Ryzen 7 9800X3D that launched in November 2024, extending AMD's leadership in gaming performance. AMD rushed the 9800X3D into the market to tap into the Holiday 2024 shopping season as it saw an opening, with Intel's latest Core Ultra 200 Arrow Lake desktop processors falling unexpectedly short in gaming performance, coming in slower than the 14th Gen Core Raptor Lake in gaming workloads, but winning big in energy efficiency. The 9800X3D plowed through gaming benchmarks, ending up double-digit percentages faster than Arrow Lake at gaming, but it's just that—an 8-core processor for strictly gaming workloads, which was overcome by 8P+16E core-count of Arrow Lake in productivity benchmarks, backed by its phenomenal Skymont E-cores. It is to counter exactly this that AMD is launching the Ryzen 9 9000X3D series today.


The new 16-core/32-thread Ryzen 9 9950X3D we are reviewing today, and its 12-core/24-thread sibling, the Ryzen 9 9900X3D, are based on a dual-CCD variant of the Granite Ridge-X package, and is powered by the AMD Zen 5 microarchitecture with 3D V-Cache technology. Much like the Ryzen 9 7000X3D series, stacked 3D V-Cache memory is only present on the first 8-core CCD, while the other is a regular one with just the 32 MB on-die L3 cache. AMD continues to rely on software level OS scheduler optimizations to ensure that gaming workloads are scheduled to the CCD with 3D V-Cache, while multithreaded productivity workloads are allowed to spread evenly among the two CCDs. The company released an update to AMD Chipset Software with a couple of new features that improve software-based scheduling compared to how it was with the Ryzen 9 7000X3D series at launch.


3D V-Cache technology has been the most impactful hardware-level innovation by AMD in recent times, which established the company as the makers of the world's fastest processors for PC gaming for the past three generations of processors. The Ryzen 7 5800X3D was able to match the gaming performance of the Intel Core i9-12900K despite being based on the generation older Zen 3 microarchitecture with slower DDR4 memory. The Ryzen 7 7800X3D dominated gaming performance over both the 13th- and 14th Gen Core Raptor Lake generations, remaining faster than even the latest Core Ultra 200 Arrow Lake. AMD likely anticipated a generational leap in single-threaded performance from the Lion Cove P-core powering the Arrow Lake, and began designing 3D V-Cache variants of its Zen 5 microarchitecture, which it debuted with the Ryzen 7 9800X3D last November, extending the company's gaming performance leadership.


AMD's Ryzen 9000 series powered by the Zen 5 microarchitecture launched back in August 2024, and it was a bit of a disappointment in the gaming performance front, with the Ryzen 7 9700X 8-core processor falling short of the gaming performance of the 7800X3D. The company continued to sell the 7800X3D at its launch price to maintain gaming performance leadership, which endured Intel's Arrow Lake launch. Much to AMD's relief, the 9800X3D was able to extend its gaming performance leadership, thanks to significant increases in clock speeds on top of the modest generational IPC increases posted by Zen 5. Besides increased clock speeds, AMD pulled off a major engineering feat that ensures its Ryzen 9000X3D chips offer superior thermals to the Ryzen 7000X3D series, and overclocking capabilities.


With Zen 5, AMD inverted the way the CPU complex die (CCD) and 3D V-Cache die (L3D) are stacked. On older generations of X3D processors, the CCD would have the L3D stacked on top of it, over the central region that has the on-die 32 MB L3 cache, while structural silicon stacked over the edges of the CCD leveled the L3D. This structural silicon carried with it the crucial task of conducting heat generated from the CPU cores up to the surface, where it's transferred via soldered TIM to the copper IHS, and then onward to the CPU cooler. With Zen 5, AMD inverted this—the CCD is now on top, with the L3D below it. With the CCD on top, the CPU cores directly dissipate heat to the cooling solution over STIM, with no structural silicon in the way, which means it could now have the same thermal and overclocking characteristics as non-X3D processor models. The L3D is peppered with through-silicon vias (TSVs), which connect the CCD to the package substrate below.


The Ryzen 9 9950X3D is designed to offer the gaming performance advantage of 3D V-Cache to the segment of the desktop PC market that wants a large core-count that's not large enough to warrant a workstation processor like the Ryzen Threadripper or the Xeon W. It comes with a core-count of 16-core/32-thread, all of which are full-size Zen 5 cores, and what Intel would classify as "performance cores." Subject to software-level OS scheduler optimizations, threads can migrate between the CCD with the 3D V-Cache and the one without, since the CPU core types and their ISA are identical.


The 9950X3D offers clock speeds of 4.30 GHz base, with up to 5.70 GHz boost. It comes with 144 MB of "total cache," which AMD defines as the sum of all L2 and L3 caches on the package. AMD has given the 9950X3D its highest power headroom, and a TDP of 170 W, along with 230 W package power tracking (PPT). The processor is compatible with all Socket AM5 motherboards, support on AMD 600-series chipset motherboards requires a BIOS update, and while the processor is drop-in compatible with AMD 800-series chipset motherboards, using the latest BIOS update is highly recommended. In any case, almost all Socket AM5 motherboards come with the USB BIOS Flashback feature, which lets you update BIOS even without a compatible processor installed. AMD is pricing the Ryzen 9 9950X3D at $700, which positions it above Intel's flagship, the Core Ultra 9 285K.


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
| Ryzen 7 7800X3D | $370 | 8 / 16 | 4.2 GHz | 5.0 GHz | 96 MB | 120 W | Zen 4 | 5 nm | AM5 |
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
| Ryzen 9 9950X | $545 | 16 / 32 | 4.3 GHz | 5.7 GHz | 64 MB | 170 W | Zen 5 | 4 nm | AM5 |
| Ryzen 9 9950X3D | $700 | 16 / 32 | 4.3 GHz | 5.7 GHz | 128 MB | 170 W | Zen 5 | 4 nm | AM5 |
