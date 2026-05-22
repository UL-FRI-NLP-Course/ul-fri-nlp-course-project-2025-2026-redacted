# NVIDIA GeForce RTX 4070 Founders Edition Review | TechPowerUp

**Site:** techpowerup

---

## Introduction

[Image: NVIDIA Logo]

Today NVIDIA releases the GeForce RTX 4070 Ada—we have the review. The new RTX 4070 (non Ti) is the most affordable graphics card in the RTX 40-series so far, which also makes it the most important one. At a starting price of $600, and with the promise of maxed out 1440p gaming, or 4K gaming with fairly high settings the card could bring fresh wind to the gaming segment. You also get the force multiplier that is DLSS 3, to achieve significantly higher framerates.


The GeForce RTX 4070 in this review has a lot in common with the recently launched RTX 4070 Ti, in that it's based on a cut-down version of the same silicon, and offers the same 12 GB of GDDR6X memory; but at a much lower wattage class. In fact, many custom-design RTX 4070 cards, including some factory-overclocked ones, make do with just one 8-pin PCIe power connector (a 225 W power configuration when you count in the PCIe slot). Of course, NVIDIA also lets board partners use the newer ATX 12VHPWR power connector that can provide a lot more power.


The GeForce "Ada Lovelace" graphics architecture that the RTX 4070 is based on, debuts the third generation of RTX, NVIDIA's ground-breaking technology that ups realism in games by fusing real-time ray traced elements with classic raster 3D graphics. Even this bit of ray tracing requires enormous compute power, and so the company created dedicated hardware inside the GPU that takes care of these workloads. Ada debuts the 3rd generation RT core with a generational uplift in ray tracing intersection performance; and 4th generation Tensor cores, which accelerate AI deep-learning neural nets, by tapping into even newer capabilities. The Ada CUDA core, plus higher GPU clock-speeds, and a completely redesigned memory sub-system with larger on-die caches, make up the new architecture. Putting it all together is the new TSMC 4N (5 nm with 4 nm-class characteristics) process.


The GeForce RTX 4070 that we test in this review is based on the same AD104 silicon that powers the RTX 4070 Ti, but while the latter maxes out all available hardware on the silicon, the former is heavily cut down. The RTX 4070 has just 46 out of 60 streaming multiprocessors (SM) physically present; which works out to an identical shader count to its predecessor, of 5,888 CUDA cores. It also features 184 Tensor cores, 46 RT cores, 184 TMUs, and 64 ROPs (out of 80 present). Thankfully, the memory itself is unchanged, you get 12 GB of 21 Gbps GDDR6X across the chip's 192-bit memory bus; yielding 504 GB/s bandwidth, which is generationally higher than the 448 GB/s of the RTX 3070.


While NVIDIA didn't release a Founders Edition for the GeForce RTX 4070 Ti, they've engineered one for the RTX 4070. The Founders Edition is no longer a pure reference design, but a slightly more premium one, that still comes at MSRP.


The RTX 4070 Founders Edition design is based on the same Dual Axial Flow-through philosophy as the RTX 3080 FE, or even the latest RTX 4090 FE, but in a much more compact form. While NVIDIA does allow its board partners to use legacy 8-pin power connectors, the Founders Edition relies on the 16-pin 12VHPWR connector, but features the same clocks and power limit as the other cards we're testing today.


| | Price | Cores | ROPs | Core Clock | Boost Clock | Memory Clock | GPU | Transistors | Memory |
|---|---|---|---|---|---|---|---|---|---|
| Arc A770 | $290 | 4096 | 128 | 2100 MHz | N/A | 2187 MHz | ACM-G10 | 21700M | 16 GB, GDDR6, 256-bit |
| RTX 2080 | $310 | 2944 | 64 | 1515 MHz | 1710 MHz | 1750 MHz | TU104 | 13600M | 8 GB, GDDR6, 256-bit |
| RTX 3060 Ti | $320 | 4864 | 80 | 1410 MHz | 1665 MHz | 1750 MHz | GA104 | 17400M | 8 GB, GDDR6, 256-bit |
| RX 6700 XT | $320 | 2560 | 64 | 2424 MHz | 2581 MHz | 2000 MHz | Navi 22 | 17200M | 12 GB, GDDR6, 192-bit |
| RTX 2080 Ti | $420 | 4352 | 88 | 1350 MHz | 1545 MHz | 1750 MHz | TU102 | 18600M | 11 GB, GDDR6, 352-bit |
| RTX 3070 | $400 | 5888 | 96 | 1500 MHz | 1725 MHz | 1750 MHz | GA104 | 17400M | 8 GB, GDDR6, 256-bit |
| RTX 3070 Ti | $500 | 6144 | 96 | 1575 MHz | 1770 MHz | 1188 MHz | GA104 | 17400M | 8 GB, GDDR6X, 256-bit |
| RX 6800 | $450 | 3840 | 96 | 1815 MHz | 2105 MHz | 2000 MHz | Navi 21 | 26800M | 16 GB, GDDR6, 256-bit |
| RX 6800 XT | $510 | 4608 | 128 | 2015 MHz | 2250 MHz | 2000 MHz | Navi 21 | 26800M | 16 GB, GDDR6, 256-bit |
| RTX 3080 | $550 | 8704 | 96 | 1440 MHz | 1710 MHz | 1188 MHz | GA102 | 28000M | 10 GB, GDDR6X, 320-bit |
| RTX 4070 | $600 | 5888 | 64 | 1920 MHz | 2475 MHz | 1313 MHz | AD104 | 35800M | 12 GB, GDDR6X, 192-bit |
| RTX 3080 Ti | $750 | 10240 | 112 | 1365 MHz | 1665 MHz | 1188 MHz | GA102 | 28000M | 12 GB, GDDR6X, 384-bit |
| RX 6900 XT | $620 | 5120 | 128 | 2015 MHz | 2250 MHz | 2000 MHz | Navi 21 | 26800M | 16 GB, GDDR6, 256-bit |
| RX 6950 XT | $680 | 5120 | 128 | 2100 MHz | 2310 MHz | 2250 MHz | Navi 21 | 26800M | 16 GB, GDDR6, 256-bit |
| RTX 3090 | $800 | 10496 | 112 | 1395 MHz | 1695 MHz | 1219 MHz | GA102 | 28000M | 24 GB, GDDR6X, 384-bit |
| RTX 4070 Ti | $800 | 7680 | 80 | 2310 MHz | 2610 MHz | 1313 MHz | AD104 | 35800M | 12 GB, GDDR6X, 192-bit |
| RX 7900 XT | $800 | 5376 | 192 | 2000 MHz | 2400 MHz | 2500 MHz | Navi 31 | 57700M | 20 GB, GDDR6, 320-bit |
| RTX 3090 Ti | $1000 | 10752 | 112 | 1560 MHz | 1950 MHz | 1313 MHz | GA102 | 28000M | 24 GB, GDDR6X, 384-bit |
| RTX 4080 | $1150 | 9728 | 112 | 2205 MHz | 2505 MHz | 1400 MHz | AD103 | 45900M | 16 GB, GDDR6X, 256-bit |
| RX 7900 XTX | $960 | 6144 | 192 | 2300 MHz | 2500 MHz | 2500 MHz | Navi 31 | 57700M | 24 GB, GDDR6, 384-bit |
| RTX 4090 | $1600 | 16384 | 176 | 2235 MHz | 2520 MHz | 1313 MHz | AD102 | 76300M | 24 GB, GDDR6X, 384-bit |
