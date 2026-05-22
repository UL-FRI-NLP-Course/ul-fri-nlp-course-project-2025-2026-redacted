package cpu.spec.scraper;

import cpu.spec.scraper.factory.LoggerFactory;
import cpu.spec.scraper.file.GpuSpecificationWriter;
import cpu.spec.scraper.parser.GpuMegaPageParser;
import cpu.spec.scraper.parser.GpuSpecificationParser;
import cpu.spec.scraper.utils.FileUtils;
import cpu.spec.scraper.utils.LogUtils;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.*;
import java.util.logging.Logger;

public class GpuBenchmarkScraperApp {
    private static final Logger LOGGER = LoggerFactory.getLogger();

    public static void main(String[] args) throws Exception {
        LOGGER.info("Starting Gpu Benchmark Scraper.");
        String outputDir = FileUtils.getOutputDirectoryPath("dataset");
        String outputFile = "benchmark-gpus.csv";

        List<String> specificationLinks = GpuMegaPageParser.extractSpecificationLinks();
        LOGGER.info("Extracted " + specificationLinks.size() + " GPU Specification Links.");

        List<GpuSpecificationModel> specifications = extractSpecifications(specificationLinks);
        LOGGER.info("Extracted " + specifications.size() + " GPU Specifications.");

        GpuSpecificationWriter.writeCsvFile(specifications, outputDir + outputFile);
        LOGGER.info("Finished Gpu Benchmark Scraper. Output at: " + outputDir + outputFile);
    }

    private static List<GpuSpecificationModel> extractSpecifications(List<String> specificationLinks) {
        int NUM_THREADS = 12;
        ExecutorService executor = Executors.newFixedThreadPool(NUM_THREADS);
        List<GpuSpecificationModel> specifications = new ArrayList<>();
        List<Future<GpuSpecificationModel>> futures = new ArrayList<>();

        for (String link : specificationLinks) {
            Callable<GpuSpecificationModel> task = () -> GpuSpecificationParser.extractSpecification(link);
            Future<GpuSpecificationModel> future = executor.submit(task);
            futures.add(future);
        }

        for (Future<GpuSpecificationModel> future : futures) {
            try {
                GpuSpecificationModel spec = future.get();
                specifications.add(spec);
                if (specifications.size() % 250 == 0) {
                    LOGGER.info(LogUtils.progressMessage(specifications, specificationLinks, "GPU Specifications"));
                }
            } catch (Exception e) {
                LOGGER.warning(LogUtils.exceptionMessage(e));
            }
        }

        executor.shutdown();
        try {
            executor.awaitTermination(Long.MAX_VALUE, TimeUnit.NANOSECONDS);
        } catch (InterruptedException e) {
            LOGGER.severe(LogUtils.exceptionMessage(e));
        }
        return specifications;
    }
}
