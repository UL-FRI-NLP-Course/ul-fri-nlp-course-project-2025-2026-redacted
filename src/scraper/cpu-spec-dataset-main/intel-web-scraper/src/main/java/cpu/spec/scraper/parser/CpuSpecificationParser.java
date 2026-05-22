package cpu.spec.scraper.parser;

import cpu.spec.scraper.CpuSpecificationModel;
import cpu.spec.scraper.exception.ElementNotFoundException;
import cpu.spec.scraper.factory.JsoupFactory;
import cpu.spec.scraper.validator.JsoupValidator;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;

public abstract class CpuSpecificationParser {
    /**
     * @param url <a href="https://ark.intel.com/content/www/us/en/ark/products/226449/intel-pentium-gold-processor-8500-8m-cache-up-to-4-40-ghz.html">Intel Processor Specification Page</a>
     * @return cpu specification model
     * @throws IOException              if page cannot be retrieved
     * @throws ElementNotFoundException if element cannot be retrieved
     */
    public static CpuSpecificationModel extractSpecification(String url) throws IOException, ElementNotFoundException {
        Document page = JsoupFactory.getConnection(url).get();
        JsoupValidator validator = new JsoupValidator(url);
        CpuSpecificationModel specification = new CpuSpecificationModel();

        Element titleElement = validator.selectFirst(page, "div.product-details > h2");

        specification.id = selectId(url);
        specification.cpuName = titleElement.text();
        specification.sourceUrl = url;

        for (Element dataElement : page.select("div.tech-section-row")) {
            Elements subElements = dataElement.children();
            String dataKey = "";
            String dataValue = "";
            for(Element subElement : subElements)
            {
                if(subElement.hasClass("tech-label"))
                {
                    dataKey = subElement.text().trim();
                }
                else if(subElement.hasClass("tech-data"))
                {
                    dataValue = subElement.text().trim();
                }
            }
            if (isKeyIgnored(dataKey)) {
                continue;
            }

            if (dataValue.isBlank()) {
                specification.dataValues.put(dataKey, null);
                continue;
            }
            specification.dataValues.put(dataKey, dataValue);
        }
        return specification;
    }

    private static String selectId(String url) {
        try {
            return new URI(url).getPath().trim().split("/")[7];
        } catch (URISyntaxException e) {
            return e.getClass().getSimpleName();
        }
    }

    private static boolean isKeyIgnored(String key) {
        return key.equalsIgnoreCase("DatasheetUrl");
    }
}
