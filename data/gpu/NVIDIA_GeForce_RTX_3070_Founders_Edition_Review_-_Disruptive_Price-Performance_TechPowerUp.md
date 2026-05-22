# NVIDIA GeForce RTX 3070 Founders Edition Review - Disruptive Price-Performance | TechPowerUp

**Site:** techpowerup

---

## Introduction

[Image: NVIDIA Logo]

NVIDIA GeForce RTX 3070 "Ampere" is the third new graphics card launch from the RTX 30-series, and possibly the most important one so far. The company debuted the GeForce "Ampere" graphics card family with the $700 RTX 3080 and $1,500 RTX 3090 in quick succession, and we today have the $500 GeForce RTX 3070 Founders Edition for review. Owing to its attractive price, this card is expected to sell in droves given how successful the RTX 2070 Super and RX 5700 XT are. As we get to the bottom of NVIDIA's pyramidal product stack, we'll see products that sell in larger volumes. Still, the RTX 3070 is a highly important product as it's designed to offer AAA gaming with RTX-on at the growingly popular 1440p resolution and is 4K-capable, as well as the gateway to the high-end segment. Consider the RTX 3070 to be the BMW 3-series for "Ampere," which, despite the 5 and 7-series being around, remains eminently desirable if it can deliver. 


With the GeForce RTX 3070, NVIDIA is releasing its second largest GeForce "Ampere" silicon, the 8 nm "GA104." It has lighter specifications than the RTX 3080, but its SIMD muscle is double that of its predecessor, the RTX 2070. In fact, right in its launch event, NVIDIA claimed that the RTX 3070 is faster than the RTX 2080 Ti, the previous-generation flagship card that retailed at well over $1000. This would mean the RTX 3070 isn't just capable of maxed-out gaming with RTX raytracing at 1440p, but also 4K Ultra HD gaming with fairly high settings. One could also expect high refresh-rate (>120 Hz) e-sports gaming at Full HD resolution to be one of the RTX 3070's core use-cases given the RTX 2080 Ti fits this bill.


The "Ampere" graphics architecture heralds the 2nd generation of NVIDIA's groundbreaking RTX technology, which introduces real-time raytracing to the gaming segment. NVIDIA figured out a way to combine conventional raster 3D graphics with raytraced components, such as lighting, shadows, reflections, ambient-occlusion, global illumination, and, with "Ampere," even raytraced motion blur—a difficult effect to pull off in real time. 2nd generation RTX is a combination of the new "Ampere" CUDA core that nearly doubles the compute throughput over the previous generation "Turing" by implementing full concurrent INT32+FP32 math operations; the second generation RT core, which has double the intersection throughput as previous generation and introduces new hardware to accelerate raytraced motion-blur; and the 3rd generation Tensor core, which leverages the sparsity phenomenon in deep-learning neural nets to increase AI inference performance by an order of magnitude. 


As we mentioned earlier, the GeForce RTX 3070 in this review is based on the "GA104" silicon with 46 of 48 streaming multiprocessors (23 out of 24 TPCs) enabled, amounting to a staggering 5,888 "Ampere" CUDA cores, 184 third generation Tensor cores, 46 RT cores, and 184 TMUs. There's a 50% increase in raster performance because of 96 ROPs, instead of the 64 on the RTX 2070. The memory sub-system surprisingly hasn't changed over the previous generation. You still get 8 GB of conventional GDDR6 memory across a 256-bit wide memory interface. It still ticks at 14 Gbps, which amounts to the same 448 GB/s bandwidth. No GDDR6X magic to be had here, NVIDIA had to cut costs somewhere to sell this card at $500. The card's typical board power is rated at 220 W, which may be much higher than the 185 W of the RTX 2070, but is significantly lower than the 320 W of the RTX 3080. This also means that custom-design RTX 3070 cards can make do with single 8-pin PCIe power inputs if the board partners chooses. 


Our NVIDIA GeForce RTX 3070 Founders Edition graphics card review covers this beautiful card, which is designed in-house by NVIDIA. The Founders Edition isn't intended to serve as a reference design, but, rather, an above baseline implementation of the silicon by NVIDIA; a reference-design serves as a baseline for board partners to better with their custom designs. The Founders Edition card is designed to raise the bar for custom-design cards to catch up with. The card uses the same "dual-axial flow-through" cooler design philosophy as the RTX 3080 and RTX 3090 Founders Edition cards, but with both the fans on the same side. The second fan still moves air through the card because of a large cutout in the backplate. NVIDIA also retained the space-saving 12-pin power input despite the fact that with a board power of 220 W, a single 8-pin connector would have sufficed. The included 12-pin to 8-pin adapter only has one 8-pin input. 


In this review, we take the NVIDIA GeForce RTX 3070 Founders Edition for a spin and test the company's claim of the card being faster than the RTX 2080 Ti, and how it changes the performance-segment landscape. If the claim holds, this would be the first performance-segment card from NVIDIA to beat a previous-generation flagship since 2016 "Pascal."


| | Price | Shader Units | ROPs | Core Clock | Boost Clock | Memory Clock | GPU | Transistors | Memory |
|---|---|---|---|---|---|---|---|---|---|
| RX 5700 | $330 | 2304 | 64 | 1465 MHz | 1625 MHz | 1750 MHz | Navi 10 | 10300M | 8 GB, GDDR6, 256-bit |
| GTX 1080 | $330 | 2560 | 64 | 1607 MHz | 1733 MHz | 1251 MHz | GP104 | 7200M | 8 GB, GDDR5X, 256-bit |
| RTX 2060 Super | $380 | 2176 | 64 | 1470 MHz | 1650 MHz | 1750 MHz | TU106 | 10800M | 8 GB, GDDR6, 256-bit |
| RX Vega 64 | $400 | 4096 | 64 | 1247 MHz | 1546 MHz | 953 MHz | Vega 10 | 12500M | 8 GB, HBM2, 2048-bit |
| GTX 1080 Ti | $650 | 3584 | 88 | 1481 MHz | 1582 MHz | 1376 MHz | GP102 | 12000M | 11 GB, GDDR5X, 352-bit |
| RX 5700 XT | $370 | 2560 | 64 | 1605 MHz | 1755 MHz | 1750 MHz | Navi 10 | 10300M | 8 GB, GDDR6, 256-bit |
| RTX 2070 | $340 | 2304 | 64 | 1410 MHz | 1620 MHz | 1750 MHz | TU106 | 10800M | 8 GB, GDDR6, 256-bit |
| RTX 2070 Super | $450 | 2560 | 64 | 1605 MHz | 1770 MHz | 1750 MHz | TU104 | 13600M | 8 GB, GDDR6, 256-bit |
| Radeon VII | $680 | 3840 | 64 | 1802 MHz | N/A | 1000 MHz | Vega 20 | 13230M | 16 GB, HBM2, 4096-bit |
| RTX 2080 | $600 | 2944 | 64 | 1515 MHz | 1710 MHz | 1750 MHz | TU104 | 13600M | 8 GB, GDDR6, 256-bit |
| RTX 2080 Super | $690 | 3072 | 64 | 1650 MHz | 1815 MHz | 1940 MHz | TU104 | 13600M | 8 GB, GDDR6, 256-bit |
| RTX 2080 Ti | $1000 | 4352 | 88 | 1350 MHz | 1545 MHz | 1750 MHz | TU102 | 18600M | 11 GB, GDDR6, 352-bit |
| RTX 3070 | $500 | 5888 | 96 | 1500 MHz | 1725 MHz | 1750 MHz | GA104 | 17400M | 8 GB, GDDR6, 256-bit |
| RTX 3080 | $700 | 8704 | 96 | 1440 MHz | 1710 MHz | 1188 MHz | GA102 | 28000M | 10 GB, GDDR6X, 320-bit |
| RTX 3090 | $1500 | 10496 | 112 | 1395 MHz | 1695 MHz | 1219 MHz | GA102 | 28000M | 24 GB, GDDR6X, 384-bit |
