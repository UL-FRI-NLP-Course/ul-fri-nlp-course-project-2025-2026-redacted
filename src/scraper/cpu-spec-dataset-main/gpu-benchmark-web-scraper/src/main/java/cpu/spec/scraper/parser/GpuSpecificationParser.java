package cpu.spec.scraper.parser;

import cpu.spec.scraper.GpuSpecificationModel;
import cpu.spec.scraper.exception.ElementNotFoundException;
import cpu.spec.scraper.factory.JsoupFactory;
import cpu.spec.scraper.validator.JsoupValidator;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;

import java.io.IOException;

public abstract class GpuSpecificationParser {
    /**
     * @param url <a href="https://www.videocardbenchmark.net/gpu.php?gpu=GeForce+RTX+5090+D&id=5898">Gpu Benchmark Specification Page</a>
     * @return gpu specification model
     * @throws IOException              if page cannot be retrieved
     * @throws ElementNotFoundException if element cannot be retrieved
     */
    public static GpuSpecificationModel extractSpecification(String url) throws IOException, ElementNotFoundException {
        Document page = JsoupFactory.getConnection(url).get();
        JsoupValidator validator = new JsoupValidator(url);
        GpuSpecificationModel specification = new GpuSpecificationModel();

        Element nameElement = validator.selectFirst(page, "span.cpuname");
        specification.gpuName = nameElement.text();

        Element busInterfaceElement = page.selectFirst("em.left-desc-cpu > p:contains(Bus Interface)");
        if (busInterfaceElement != null) {
            specification.busInterface = busInterfaceElement.ownText().trim();
        }

        Element maxMemoryElement = page.selectFirst("em.left-desc-cpu > p:contains(Max Memory Size)");
        if (maxMemoryElement != null) {
            specification.maxMemory = maxMemoryElement.ownText().trim();
        }

        Element coreClockElement = page.selectFirst("em.left-desc-cpu > p:contains(Core Clock)");
        if (coreClockElement != null) {
            specification.coreClock = coreClockElement.ownText().trim();
        }

        Element memoryClockElement = page.selectFirst("em.left-desc-cpu > p:contains(Memory Clock)");
        if (memoryClockElement != null) {
            specification.memoryClock = memoryClockElement.ownText().trim();
        }

        Element directXElement = page.selectFirst("em.left-desc-cpu > p:contains(DirectX)");
        if (directXElement != null) {
            specification.directX = directXElement.ownText().trim();
        }

        Element openGLElement = page.selectFirst("em.left-desc-cpu > p:contains(OpenGL)");
        if (openGLElement != null) {
            specification.openGL = openGLElement.ownText().trim();
        }

        Element tdpElement = page.selectFirst("em.left-desc-cpu > p:contains(TDP)");
        if (tdpElement != null) {
            specification.tdp = tdpElement.ownText().trim();
        }

        Element categoryElement = page.selectFirst("div.desc-foot > p:contains(Category)");
        if (categoryElement != null) {
            specification.category = categoryElement.ownText().trim();
        }

        Element g3dLabelElement = page.selectFirst("div:containsOwn(G3D Mark)");
        if (g3dLabelElement != null) {
            Element g3dValueElement = g3dLabelElement.nextElementSibling();
            if (g3dValueElement != null) {
                specification.g3dMark = g3dValueElement.text().trim();
            }
        }

        Element g2dLabelElement = page.selectFirst("div:containsOwn(G2D Mark)");
        if (g2dLabelElement != null) {
            Element g2dValueElement = g2dLabelElement.nextElementSibling();
            if (g2dValueElement != null) {
                specification.g2dMark = g2dValueElement.text().trim();
            }
        }

        Element marginLinkElement = page.selectFirst("a[href*=graph_notes]");
        if (marginLinkElement != null) {
            Element marginValueElement = marginLinkElement.nextElementSibling();
            if (marginValueElement != null) {
                specification.marginForError = marginValueElement.text().trim();
            }
        }

        Element releaseDateElement = page.selectFirst("div.desc-foot > p:contains(Videocard First Benchmarked)");
        if (releaseDateElement != null) {
            specification.releaseDate = releaseDateElement.ownText().trim();
        }

        Element priceElement = page.selectFirst("div.desc-foot > p:contains(Last Price Change)");
        if (priceElement != null) {
            specification.lastPriceChange = priceElement.ownText().trim();
        }

        specification.sourceUrl = url;
        return specification;
    }
}
