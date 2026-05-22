package cpu.spec.scraper.file;

import cpu.spec.scraper.GpuSpecificationModel;

import java.io.FileWriter;
import java.io.IOException;
import java.util.List;

public abstract class GpuSpecificationWriter {
    /**
     * @param gpuSpecifications list with objects to write as csv
     * @param filePath          like "../dataset/benchmark-gpus.csv"
     * @throws IOException if target filePath is invalid
     */
    public static void writeCsvFile(List<GpuSpecificationModel> gpuSpecifications, String filePath) throws IOException {
        try (FileWriter writer = new FileWriter(filePath)) {
            writer.append(String.format("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\"%s\"\n",
                    "GpuName",
                    "BusInterface",
                    "MaxMemory",
                    "CoreClock",
                    "MemoryClock",
                    "DirectX",
                    "OpenGL",
                    "TDP",
                    "Category",
                    "G3DMark",
                    "G2DMark",
                    "MarginForError",
                    "ReleaseDate",
                    "LastPriceChange",
                    "SourceUrl"));

            for (GpuSpecificationModel spec : gpuSpecifications) {
                writer.append(String.format("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\"%s\"\n",
                        cleanValue(spec.gpuName),
                        cleanValue(spec.busInterface),
                        cleanValue(spec.maxMemory),
                        cleanValue(spec.coreClock),
                        cleanValue(spec.memoryClock),
                        cleanValue(spec.directX),
                        cleanValue(spec.openGL),
                        cleanValue(spec.tdp),
                        cleanValue(spec.category),
                        cleanValue(spec.g3dMark),
                        cleanValue(spec.g2dMark),
                        cleanValue(spec.marginForError),
                        cleanValue(spec.releaseDate),
                        cleanValue(spec.lastPriceChange),
                        spec.sourceUrl));
            }
        }
    }

    private static String cleanValue(String value) {
        if (value == null) {
            return "";
        } else {
            return value.replaceAll(",", ".");
        }
    }
}
