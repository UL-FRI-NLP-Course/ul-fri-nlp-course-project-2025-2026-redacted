# NVIDIA GeForce RTX 3080 Founders Edition Review - Must-Have for 4K Gamers | TechPowerUp

**Site:** techpowerup

---

## Introduction

[Image: NVIDIA Logo]

Ampere is here! We have with us in this comprehensive performance review the NVIDIA GeForce RTX 3080 Founders Edition graphics card. NVIDIA shook things up early this month by announcing not just the RTX 3080, but also the larger RTX 3090 and more affordable RTX 3070. Curiously, the GeForce RTX 3080 is being labeled as a "flagship product," while the RTX 3090 is being extensively compared to past-generation TITAN cards. With a starting price of $699, the RTX 3080 is designed to offer 4K UHD gameplay at frame-rates in excess of 60 FPS, 100+ FPS at 1440p, and extreme refresh-rate (360 Hz) gameplay.


The Ampere architecture, which we extensively detailed in our dedicated NVIDIA Ampere architecture article, heralds the 2nd generation of NVIDIA's path-breaking RTX real-time raytracing technology, with a design goal of making RTX go above and beyond the DirectX Raytracing feature set, and for raytracing to have as little impact on game playability as possible. With the new RTX 3080 and RTX 3090, NVIDIA is also introducing a new dual axial flow through cooling solution, which we detailed in our RTX 3080 Unboxing & Preview article from last week. To make this design work, NVIDIA also introduced an all new 12-pin power input, which we hope becomes a standard going forward.


The "Ampere" architecture itself debuted in Spring 2020 as part of the A100 Tensor Core scalar HPC processor targeted at AI DNN researchers. As a consumer graphics architecture, "Ampere" is debuting today, and our first coverage is this GeForce RTX 3080 Founders Edition review. The A100 Tensor Core processor has certain architectural bits that aren't relevant to the gaming segment, such as FP64 cores and HBM2E memory, and completely lacks all raster graphics machinery, which is required for gaming. The GeForce "Ampere" architecture does away with FP64 cores, has a supremely modernized raster hardware components, and new 2nd generation RT cores. What's common between the two are the awesome new 3rd generation Tensor cores that leverage sparsity to increase AI inference performance by an order of magnitude; and the new "Ampere" FP32 CUDA core with more efficient utilization of its number-crunching machinery.


NVIDIA has over the past decade perfected the art of presenting GeForce graphics cards as not just pieces of hardware, but complete consumer graphics solutions with software features that enhance the PC gaming experience. The company finds itself as a bulwark platform of PC gaming while the gaming experience on consoles is getting closer to the PC than ever. With new-generation Xbox and PlayStation consoles promising 4K UHD gaming, NVIDIA probably feels PC gaming can only survive if it maintains a vast technological superiority that translates into an experience that's proportionately superior. This appears to be the main reason behind the company's push toward real-time raytracing. While fully raytraced rendering continues to remain theoretical in consumer use cases, NVIDIA figured out a way to compose conventional raster 3D graphics with cleverly raytraced elements (such as lighting, shadows, reflections, and more). With the second generation of RTX, NVIDIA is adding more true-to-life effects, such as raytraced motion blur. The company even designed special hardware just for this effect!


NVIDIA is also sending the message that GeForce "Ampere" represents "the best of next-gen," and wants to show that merely being first to market with something doesn't automatically make the product superior. The "GA102" chip at the heart of the RTX 3080 Founders Edition is built on the new 8 nm silicon fabrication node by Samsung, offering comparable transistor densities and iso-power to TSMC 7 nm. It also implements PCI-Express Gen 4 for better IO connectivity with the latest desktop platforms, such as 3rd Gen Ryzen and the upcoming Intel Core processors. In the separate NVIDIA RTX 3080 PCI-Express Scaling article, we will take a closer look at the bus interface, and in yet another article, we compare the RTX 3080 on similarly priced premium processors by Intel and AMD, with the RTX 3080 benchmarked on the Core i9-10900K vs. the Ryzen 9 3900XT.


The NVIDIA GeForce RTX 3080 Founders Edition feels like a piece of jewelry in hand. That's because NVIDIA has for the past many generations stopped looking at its reference design products as baselines set for its board partners to improve upon, as they are, rather, high engineering standards their partners can aspire to meet or exceed with custom-design products. This is why NVIDIA refrains from using the term "reference design" when talking about Founders Edition products. Unlike the previous-generation RTX 2080 Founders Edition, which came at a premium price above the starting price, the new RTX 3080 Founders Edition will be launched at the $699 price. In this review, we take the GeForce RTX 3080 Founders Edition for a spin across our updated test suite of real world gaming benchmarks. We also explore the card's unique new design in detail by disassembling it, and test the card's new thermal and electrical features.


Our NVIDIA GeForce RTX 3080 Founders Edition launch-day coverage includes:
- The NVIDIA GeForce RTX 3080 Founders Edition main review (this review)
- NVIDIA GeForce RTX 3080 with AMD Ryzen 3900XT vs Intel Core i9-10900K
- NVIDIA GeForce RTX 3080 PCI-Express Scaling
- NVIDIA GeForce Ampere Architecture, Board Design, Gaming Tech & Software (last week)
- NVIDIA GeForce RTX 3080 Unboxing (last week)

We have several custom-design RTX 3080 graphics card reviews lined up for you in the days to come, from all the major vendors.


| | Price | Shader Units | ROPs | Core Clock | Boost Clock | Memory Clock | GPU | Transistors | Memory |
|---|---|---|---|---|---|---|---|---|---|
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
