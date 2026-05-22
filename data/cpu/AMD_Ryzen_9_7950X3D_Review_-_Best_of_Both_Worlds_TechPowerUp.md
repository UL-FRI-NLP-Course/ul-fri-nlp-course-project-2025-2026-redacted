# AMD Ryzen 9 7950X3D Review - Best of Both Worlds | TechPowerUp

**Site:** techpowerup

---

## Introduction

[Image: AMD Logo]

The Ryzen 9 7950X3D review is here, AMD is ready to take on Intel's mighty Raptor Lake. Bringing the latest upgrades to the Ryzen 7000 "Zen 4" family, this processor rocks 3D Vertical Cache technology along with a massive 16-core/32-thread count, and its makers claim that it levels up to the Core i9-13900K both in gaming and multi-threaded productivity, making it the most powerful desktop processor you can buy from the AMD camp. The best part? It's being launched at the same $700 MSRP as the standard 7950X, which is now $50-75 cheaper in the market; and remains drop-in compatible with Socket AM5 motherboards, although using the latest BIOS and drivers is required.


The 3D Vertical Cache technology proved its mettle with the Ryzen 7 5800X3D 8-core/16-thread processor AMD launched in 2022, where it elevated the processor's gaming performance to match that of the fastest Intel processor of the time, the i9-12900K "Alder Lake," despite being based on the generationally older "Zen 3" architecture. While the "Zen 4" architecture matches "Alder Lake" on its own, without 3D Vertical Cache, it was found falling short of "Raptor Lake" in gaming. All eyes are now on 3D Vertical Cache to work its magic again, to bring "Zen 4" into the same league as "Raptor Lake," so you're once again spoiled for choice between the two brands. While the older 5800X3D matched the i9-12900K in gaming, its lower CPU core-count meant that the "Alder Lake" zoomed past in multi-threaded productivity. This time around, AMD isn't in the mood to compromise on core-counts, and brings 3D Vertical Cache to 16-core, 12-core and 8-core Ryzen 7000X3D-series models. 


The 3D Vertical Cache is a 64 MB fast SRAM cache that's stacked on top of the "Zen 4" CCD (CPU complex die), over the region of the die that has the on-die 32 MB L3 cache. This 6 nm die, called simply the L3D (L3 cache die), expands the L3 cache available to the 8 CPU cores on that CCD, from 32 MB to 96 MB. It's contiguous with the on-die L3 cache, and operates at the same speed. The vast 96 MB of last-level cache has a profound impact on gaming performance, as was proven with the 5800X3D reviews.


There's only one catch, though. The Ryzen 9 7950X3D is a 16-core processor, which means it has two 8-core CCDs. It turns out that one of the two is a regular "Zen 4" CCD with just 32 MB on-die L3 cache, like the one found in the 7950X. AMD's explanation for this design-choice is rather complex: it saves on cost, given that games need no more than 8 CPU cores (as is reaffirmed by Intel's decision to give its desktop processors no more than 8 performance-cores); and that the second CCD that's unsaddled with stacked cache is free to boost to higher frequencies. We'll explain more on how this works later in this review.


The Ryzen 9 7950X3D has all the goodies Socket AM5 brings to the table, including PCI-Express Gen 5 for not just the main PCIe slot, but also a CPU-attached NVMe SSD without eating into the x16 lanes (something that's lacking on the current Intel platform); and support for the latest DDR5 memory. There is, however, no DDR4 memory support, and motherboard prices are just as steep as Intel, so your price for entry into this platform is slightly higher compared to Intel, where you have the option of using cheaper DDR4 memory and motherboards. We take the AMD Ryzen 9 7950X3D for a spin through a vast new selection of gaming and productivity benchmarks to tell you if AMD is back on the top.


| | Price | Cores / Threads | Base Clock | Max. Boost | L3 Cache | TDP | Architecture | Process | Socket |
|---|---|---|---|---|---|---|---|---|---|
| Ryzen 7 5800X | $240 | 8 / 16 | 3.8 GHz | 4.7 GHz | 32 MB | 105 W | Zen 3 | 7 nm | AM4 |
| Ryzen 7 5800X3D | $310 | 8 / 16 | 3.4 GHz | 4.5 GHz | 96 MB | 105 W | Zen 3 | 7 nm | AM4 |
| Ryzen 9 3900X | $350 | 12 / 24 | 3.8 GHz | 4.6 GHz | 64 MB | 105 W | Zen 2 | 7 nm | AM4 |
| Ryzen 5 7600 | $230 | 6 / 12 | 3.8 GHz | 5.1 GHz | 32 MB | 105 W | Zen 4 | 5 nm | AM5 |
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
| Ryzen 9 7900X | $440 | 12 / 24 | 4.7 GHz | 5.6 GHz | 64 MB | 170 W | Zen 4 | 5 nm | AM5 |
| Ryzen 9 7900X3D | $600 | 12 / 24 | 4.4 GHz | 5.6 GHz | 128 MB | 120 W | Zen 4 | 5 nm | AM5 |
| Ryzen 9 7950X | $590 | 16 / 32 | 4.5 GHz | 5.7 GHz | 64 MB | 170 W | Zen 4 | 5 nm | AM5 |
| Ryzen 9 7950X3D | $700 | 16 / 32 | 4.2 GHz | 5.7 GHz | 128 MB | 120 W | Zen 4 | 5 nm | AM5 |
| Core i9-13900K | $570 | 8+16 / 32 | 3.0 / 2.2 GHz | 5.8 / 4.3 GHz | 36 MB | 125 W | Raptor Lake | 10 nm | LGA 1700 |
| Core i9-13900KS | $730 | 8+16 / 32 | 3.2 / 2.4 GHz | 6.0 / 4.3 GHz | 36 MB | 150 W | Raptor Lake | 10 nm | LGA 1700 |
