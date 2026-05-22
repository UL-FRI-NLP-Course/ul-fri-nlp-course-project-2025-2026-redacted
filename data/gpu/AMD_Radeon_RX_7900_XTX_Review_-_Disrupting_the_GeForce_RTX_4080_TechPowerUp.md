# AMD Radeon RX 7900 XTX Review - Disrupting the GeForce RTX 4080 | TechPowerUp

**Site:** techpowerup

---

## Introduction

[Image: AMD Logo]

The AMD next-generation we've long been waiting for is finally here! The new Radeon RX 7900 XTX in this review, and the Radeon RX 7900 XT, which we're also reviewing today, debut the company's 3rd generation RDNA graphics architecture, or RDNA 3. With it, the company is also introducing the world's first chiplet-based GPU in an effort to maximize utilization of the TSMC 5 nm foundry node, without compromising on performance, or too much on power. The RDNA 3 graphics architecture promises a similar 50% leap in performance/Watt over the previous-generation RDNA 2, which helped AMD compete in the high-end segment after a long gap of 7-odd years. The new architecture improves in many areas, including compute power, memory sub-system, display engine with support for the latest DisplayPort 2.1 standard, multiple-stream acceleration for the latest video formats, and most importantly, AI acceleration, and a more advanced ray tracing hardware.


AMD's decision to leverage chiplets to build the new "Navi 31" GPU powering the Radeon RX 7900 series, has to do with attempting to keep Moore's Law alive in spirit. The idea is to achieve high-end performance leadership at the same sub-$1000 price-points that we've had before. NVIDIA on the other hand considers Moore's Law dead, and says that it's no longer possible to economically build large high-end GPUs. AMD therefore identified all the components that can do with a slightly older foundry node—such as the L3 cache, memory controllers, and memory PHY, and moved them from the GPU, onto six little dies called MCDs (memory cache dies), which are built on the slightly older 6 nm process. The remaining GPU with all its compute-intensive hardware, would be called the GCD (graphics compute die). The GCD and MCDs would be connected by an extreme bandwidth Infinity Fabric Fanout interconnect, which enables 5.4 TB/s of bandwidth between the GCD and MCDs. Each MCD has a 16 MB segment of the GPU's total 96 MB Infinity Cache, which is a bit smaller than the 128 MB of the previous generation, but made up for by the 87% higher GDDR6 memory bandwidth from the GPU's 384-bit memory bus, handling 20 Gbps-rated memory, for 960 GB/s of bandwidth.


The RDNA 3 graphics architecture which we're reviewing today, introduces dual issue-rate compute units, with a high degree of optimization in the way idle SIMD resources are utilized, support for newer math formats, and a new AI accelerator that retasks the SIMDs for matrix math functions. Together, these optimizations produce a 17% IPC uplift over the previous-generation RDNA 2 CU. There are 96 CUs physically present in the silicon, which work out to 6,144 stream processors. The architecture also sees an increase in engine clocks, and a decoupling of the shader clock speeds to those of the GPU's Front End, which operates at a 10-15% higher frequency. The most striking aspect of the RDNA 3 architecture is that the typical board power of these GPUs is well contained, with the RX 7900 XTX rated at just 350 W, and the RX 7900 XT at 315 W—both of which can be fed by just two 8-pin PCIe power connectors, and cooled by solutions much smaller than those you find on the competing NVIDIA GeForce RTX 4080 or RTX 4090 "Ada."


The Radeon RX 7900 XTX we're reviewing here, maxes out the "Navi 31" silicon, featuring all 96 compute units, or all 6,144 stream processors, 96 second generation Ray Accelerators, 384 TMUs, a whopping 192 ROPs, and the GPU's whole 384-bit memory interface, holding 24 GB of 20 Gbps-rated GDDR6 memory. All this for "just" $1,000, or the same price the previous-generation RX 6900 XT debuted at. This is where AMD's choices with the chiplet architecture begins to make sense, as both of NVIDIA's competing GPUs are priced much higher.


We also have a second Navi 31 review for you today: the Radeon RX 7900 XT.


| | Price | Cores | ROPs | Core Clock | Boost Clock | Memory Clock | GPU | Transistors | Memory |
|---|---|---|---|---|---|---|---|---|---|
| RTX 3070 | $500 | 5888 | 96 | 1500 MHz | 1725 MHz | 1750 MHz | GA104 | 17400M | 8 GB, GDDR6, 256-bit |
| RTX 3070 Ti | $600 | 6144 | 96 | 1575 MHz | 1770 MHz | 1188 MHz | GA104 | 17400M | 8 GB, GDDR6X, 256-bit |
| RX 6800 | $510 | 3840 | 96 | 1815 MHz | 2105 MHz | 2000 MHz | Navi 21 | 26800M | 16 GB, GDDR6, 256-bit |
| RX 6800 XT | $650 | 4608 | 128 | 2015 MHz | 2250 MHz | 2000 MHz | Navi 21 | 26800M | 16 GB, GDDR6, 256-bit |
| RTX 3080 | $750 | 8704 | 96 | 1440 MHz | 1710 MHz | 1188 MHz | GA102 | 28000M | 10 GB, GDDR6X, 320-bit |
| RTX 3080 Ti | $950 | 10240 | 112 | 1365 MHz | 1665 MHz | 1188 MHz | GA102 | 28000M | 12 GB, GDDR6X, 384-bit |
| RX 6900 XT | $700 | 5120 | 128 | 2015 MHz | 2250 MHz | 2000 MHz | Navi 21 | 26800M | 16 GB, GDDR6, 256-bit |
| RX 6950 XT | $800 | 5120 | 128 | 2100 MHz | 2310 MHz | 2250 MHz | Navi 21 | 26800M | 16 GB, GDDR6, 256-bit |
| RTX 3090 | $950 | 10496 | 112 | 1395 MHz | 1695 MHz | 1219 MHz | GA102 | 28000M | 24 GB, GDDR6X, 384-bit |
| RX 7900 XT | $900 | 5376 | 192 | 2000 MHz | 2400 MHz | 2500 MHz | Navi 31 | 57700M | 20 GB, GDDR6, 320-bit |
| RTX 3090 Ti | $1400 | 10752 | 112 | 1560 MHz | 1950 MHz | 1313 MHz | GA102 | 28000M | 24 GB, GDDR6X, 384-bit |
| RTX 4080 | $1200 | 9728 | 112 | 2205 MHz | 2505 MHz | 1400 MHz | AD103 | 45900M | 16 GB, GDDR6X, 256-bit |
| RX 7900 XTX | $1000 | 6144 | 192 | 2300 MHz | 2500 MHz | 2500 MHz | Navi 31 | 57700M | 24 GB, GDDR6, 384-bit |
| RTX 4090 | $2400 | 16384 | 176 | 2235 MHz | 2520 MHz | 1313 MHz | AD102 | 76300M | 24 GB, GDDR6X, 384-bit |
