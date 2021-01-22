from npa_ingestion_tool import parse_rss, sqlite3_database, get_archives_rss_urls

def main():

    # RSS Parsing; input is urls to RSS feeds
    test = parse_rss("""<?xml version="1.0" encoding="UTF-8"?>
<rss xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:feedburner="http://rssnamespace.org/feedburner/ext/1.0" version="2.0">
  <channel>
    <title>Journal of Natural Products: Latest Articles (ACS Publications)</title>
    <link>http://pubs.acs.org</link>
    <description>latest articles published in Journal of Natural Products</description>
    <language>en-US</language>
    <copyright>Copyright 2018 American Chemical Society</copyright>
    <dc:language>en-US</dc:language>
    <dc:rights>Copyright 2018 American Chemical Society</dc:rights>
    <atom10:link xmlns:atom10="http://www.w3.org/2005/Atom" rel="self" type="application/rss+xml" href="http://feeds.feedburner.com/acs/jnprdf" /><feedburner:info uri="acs/jnprdf" /><atom10:link xmlns:atom10="http://www.w3.org/2005/Atom" rel="hub" href="http://pubsubhubbub.appspot.com/" /><item>
      <title>Correction to Eudesmane Sesquiterpenes from Verbesina lanata with Inhibitory Activity against Grapevine
Downy Mildew</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/IYkFoUC_YQM/acs.jnatprod.8b00140</link>
      <description>&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.8b00140&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=IYkFoUC_YQM:8PnZvjy3kFQ:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/IYkFoUC_YQM" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Fri, 16 Feb 2018 18:02:35 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.8b00140</guid>
      <dc:creator>Justine Ramseyer, Barbara Thuerig, Maria De Mieri, Hans-Jakob Schärer, Thomas Oberhänsli, Mahabir P. Gupta, Lucius Tamm, Matthias Hamburger and Olivier Potterat</dc:creator>
      <dc:date>2018-02-16T18:02:35Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.8b00140</feedburner:origLink></item>
    <item>
      <title>Concise Total Synthesis of (±)-Deguelin and (±)-Tephrosin
Using a Vinyl Iodide as a Key Building Block</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/sinNXrakerE/acs.jnatprod.7b00794</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00794/20180214/images/medium/np-2017-00794m_0005.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00794&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=sinNXrakerE:nr7o8AJHNW8:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/sinNXrakerE" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Wed, 14 Feb 2018 14:56:29 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00794</guid>
      <dc:creator>Shengtao Xu, Guangyu Wang, Feijie Xu, Wenlong Li, Aijun Lin, Hequan Yao and Jinyi Xu</dc:creator>
      <dc:date>2018-02-14T14:56:29Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00794</feedburner:origLink></item>
    <item>
      <title>Cybastacines A and B: Antibiotic Sesterterpenes from
a Nostoc sp. Cyanobacterium</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/WjnJDKyszEo/acs.jnatprod.7b00638</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00638/20180212/images/medium/np-2017-00638q_0004.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00638&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=WjnJDKyszEo:Qw4ev7HOmz4:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/WjnJDKyszEo" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Mon, 12 Feb 2018 19:28:21 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00638</guid>
      <dc:creator>Alfredo H. Cabanillas, Víctor Tena Pérez, Santiago Maderuelo Corral, Diego Fernando Rosero Valencia, Antera Martel Quintana, Montserrat Ortega Doménech and Ángel Rumbero Sánchez</dc:creator>
      <dc:date>2018-02-12T19:28:21Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00638</feedburner:origLink></item>
    <item>
      <title>Advanced NMR-Based Structural Investigation of Glucosinolates and Desulfoglucosinolates</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/0xxrbs8df5Y/acs.jnatprod.7b00776</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00776/20180212/images/medium/np-2017-00776b_0009.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00776&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=0xxrbs8df5Y:GP0Ehi44JMw:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/0xxrbs8df5Y" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Mon, 12 Feb 2018 15:55:58 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00776</guid>
      <dc:creator>Nada Ibrahim, Ingrid Allart-Simon, Gina R. De Nicola, Renato Iori, Jean-Hugues Renault, Patrick Rollin and Jean-Marc Nuzillard</dc:creator>
      <dc:date>2018-02-12T15:55:58Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00776</feedburner:origLink></item>
    <item>
      <title>Marine Invertebrate Natural Products that Target Microtubules</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/oVCr1ezNn9A/acs.jnatprod.7b00964</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00964/20180212/images/medium/np-2017-00964n_0004.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00964&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=oVCr1ezNn9A:kk3jRMpp8eQ:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/oVCr1ezNn9A" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Mon, 12 Feb 2018 14:57:03 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00964</guid>
      <dc:creator>John H. Miller, Jessica J. Field, Arun Kanakkanthara, Jeremy G. Owen, A. Jonathan Singh and Peter T. Northcote</dc:creator>
      <dc:date>2018-02-12T14:57:03Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00964</feedburner:origLink></item>
    <item>
      <title>Modified Abietane Diterpenoids from Whole Plants of Selaginella moellendorffii</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/wq5_Dfx2x2o/acs.jnatprod.7b00909</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00909/20180207/images/medium/np-2017-00909w_0005.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00909&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=wq5_Dfx2x2o:PQWdUmdUzM4:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/wq5_Dfx2x2o" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Wed, 07 Feb 2018 18:46:44 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00909</guid>
      <dc:creator>Lei-Yu Ke, Yu Zhang, Meng-Yuan Xia, Jing-Xian Zhuo, Yue-Hu Wang and Chun-Lin Long</dc:creator>
      <dc:date>2018-02-07T18:46:44Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00909</feedburner:origLink></item>
    <item>
      <title>Review of Botanical Medicine. From Bench to Bedside</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/fc316XAOF6A/acs.jnatprod.8b00010</link>
      <description>&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.8b00010&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=fc316XAOF6A:Qaga-pRaN1A:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/fc316XAOF6A" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Tue, 06 Feb 2018 20:13:47 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.8b00010</guid>
      <dc:creator>Abir T. El-Alfy</dc:creator>
      <dc:date>2018-02-06T20:13:47Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.8b00010</feedburner:origLink></item>
    <item>
      <title>Metabolomics Analysis Reveals that Ethylene and Methyl
Jasmonate Regulate Different Branch Pathways to Promote the Accumulation
of Terpenoid Indole Alkaloids in Catharanthus roseus</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/7CEP_SYrnT0/acs.jnatprod.7b00782</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00782/20180206/images/medium/np-2017-007822_0005.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00782&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=7CEP_SYrnT0:hThTUIroJak:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/7CEP_SYrnT0" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Tue, 06 Feb 2018 19:08:26 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00782</guid>
      <dc:creator>Xiao-Ning Zhang, Jia Liu, Yang Liu, Yu Wang, Ann Abozeid, Zhi-Guo Yu and Zhong-Hua Tang</dc:creator>
      <dc:date>2018-02-06T19:08:26Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00782</feedburner:origLink></item>
    <item>
      <title>Capsicodendrin from Cinnamosma fragrans Exhibits
Antiproliferative and Cytotoxic Activity in Human Leukemia
Cells: Modulation by Glutathione</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/LIHwpYbyqYc/acs.jnatprod.7b00887</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00887/20180206/images/medium/np-2017-008876_0010.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00887&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=LIHwpYbyqYc:siiUgTfrxxs:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/LIHwpYbyqYc" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Tue, 06 Feb 2018 19:07:48 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00887</guid>
      <dc:creator>Soumendrakrishna Karmahapatra, Corey Kientz, Shruthi Shetty, Jack C. Yalowich and L. Harinantenaina Rakotondraibe</dc:creator>
      <dc:date>2018-02-06T19:07:48Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00887</feedburner:origLink></item>
    <item>
      <title>Metabolomics-Guided Discovery of Microginin Peptides
from Cultures of the Cyanobacterium Microcystis aeruginosa</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/tDif2eK1NxA/acs.jnatprod.7b00829</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00829/20180206/images/medium/np-2017-008298_0003.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00829&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=tDif2eK1NxA:urEz9uK6UDE:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/tDif2eK1NxA" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Tue, 06 Feb 2018 15:10:23 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00829</guid>
      <dc:creator>Allison K. Stewart, Rudravajhala Ravindra, Ryan M. Van Wagoner and Jeffrey L. C. Wright</dc:creator>
      <dc:date>2018-02-06T15:10:23Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00829</feedburner:origLink></item>
    <item>
      <title>Mucroniferanines A–G, Isoquinoline Alkaloids
from Corydalis mucronifera</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/4777Y1RgpCU/acs.jnatprod.7b00847</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00847/20180205/images/medium/np-2017-008475_0005.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00847&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=4777Y1RgpCU:6Kx-OWeiihE:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/4777Y1RgpCU" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Mon, 05 Feb 2018 18:25:18 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00847</guid>
      <dc:creator>Jun Zhang, Qing-Ying Zhang, Peng-Fei Tu, Fu-Chun Xu and Hong Liang</dc:creator>
      <dc:date>2018-02-05T18:25:18Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00847</feedburner:origLink></item>
    <item>
      <title>Total Synthesis of Scytonemide A Employing Weinreb AM Solid-Phase Resin</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/JMaxoO3qImM/acs.jnatprod.7b00912</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00912/20180205/images/medium/np-2017-00912v_0007.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00912&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=JMaxoO3qImM:pZSMe4Mh-qc:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/JMaxoO3qImM" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Mon, 05 Feb 2018 18:24:39 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00912</guid>
      <dc:creator>Tyler A. Wilson, Robert J. Tokarski, Peter Sullivan, Robert M. Demoret, Jimmy Orjala, L. Harinantenaina Rakotondraibe and James R. Fuchs</dc:creator>
      <dc:date>2018-02-05T18:24:39Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00912</feedburner:origLink></item>
    <item>
      <title>Peloruside A-Induced Cell Death in Hypoxia
Is p53 Dependent in HCT116 Colorectal Cancer Cells</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/__ggO1LI-mk/acs.jnatprod.7b00961</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00961/20180204/images/medium/np-2017-00961h_0007.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00961&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=__ggO1LI-mk:QcxA5A_Swu4:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/__ggO1LI-mk" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Mon, 05 Feb 2018 16:12:13 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00961</guid>
      <dc:creator>Jiří Řehulka, Narendran Annadurai, Ivo Frydrych, Petr Džubák, John H. Miller, Marián Hajdúch and Viswanath Das</dc:creator>
      <dc:date>2018-02-05T16:12:13Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00961</feedburner:origLink></item>
    <item>
      <title>Structurally Diverse Cytotoxic Dimeric Chalcones from Oxytropis
chiliophylla</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/Jl45X0Laic8/acs.jnatprod.7b00736</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00736/20180204/images/medium/np-2017-00736w_0006.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00736&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=Jl45X0Laic8:ZMu2TwQ9cAs:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/Jl45X0Laic8" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Mon, 05 Feb 2018 16:11:51 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00736</guid>
      <dc:creator>Yang Liu, Xiaojing Zhang, Norbo Kelsang, Guangzhong Tu, Dexin Kong, Jianghai Lu, Yingtao Zhang, Hong Liang, Pengfei Tu and Qingying Zhang</dc:creator>
      <dc:date>2018-02-05T16:11:51Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00736</feedburner:origLink></item>
    <item>
      <title>Highly Oxidized Guaianolide Sesquiterpenoids with
Potential Anti-inflammatory Activity from Chrysanthemum indicum</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/okJWaDvoTpU/acs.jnatprod.7b00867</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00867/20180203/images/medium/np-2017-00867h_0010.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00867&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=okJWaDvoTpU:fn99cHnE0dQ:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/okJWaDvoTpU" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Mon, 05 Feb 2018 15:42:59 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00867</guid>
      <dc:creator>Gui-Min Xue, Xiao-Qing Li, Chen Chen, Kang Chen, Xiao-Bing Wang, Yu-Cheng Gu, Jian-Guang Luo and Ling-Yi Kong</dc:creator>
      <dc:date>2018-02-05T15:42:59Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00867</feedburner:origLink></item>
    <item>
      <title>Crispenes F and G, cis-Clerodane Furanoditerpenoids from Tinospora crispa, Inhibit
STAT3 Dimerization</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/x6-0oUoqWXw/acs.jnatprod.7b00377</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00377/20180203/images/medium/np-2017-00377m_0007.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00377&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=x6-0oUoqWXw:k-1hKCNBnQw:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/x6-0oUoqWXw" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Sat, 03 Feb 2018 05:11:56 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00377</guid>
      <dc:creator>Md. Abdullah Al Noman, Tasnova Hossain, Monira Ahsan, Shirin Jamshidi, Choudhury Mahmood Hasan and Khondaker Miraz Rahman</dc:creator>
      <dc:date>2018-02-03T05:11:56Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00377</feedburner:origLink></item>
    <item>
      <title>ent-Jungermannenone C Triggers Reactive
Oxygen Species-Dependent Cell Differentiation in Leukemia Cells</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/Ewt0kIUONeM/acs.jnatprod.7b00722</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00722/20180202/images/medium/np-2017-00722h_0007.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00722&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=Ewt0kIUONeM:r_o25Xb3CV0:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/Ewt0kIUONeM" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Fri, 02 Feb 2018 05:19:22 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00722</guid>
      <dc:creator>Zongwei Yue, Xinhua Xiao, Jinbao Wu, Xiaozhou Zhou, Weilong Liu, Yaxi Liu, Houhua Li, Guoqiang Chen, Yingli Wu and Xiaoguang Lei</dc:creator>
      <dc:date>2018-02-02T05:19:22Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00722</feedburner:origLink></item>
    <item>
      <title>Total Synthesis of the Flavonoid Natural Product Houttuynoid
A</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/cir5NpEdNrM/acs.jnatprod.7b00791</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00791/20180202/images/medium/np-2017-00791n_0003.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00791&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=cir5NpEdNrM:Hk2dljtQkbg:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/cir5NpEdNrM" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Fri, 02 Feb 2018 05:18:47 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00791</guid>
      <dc:creator>Jie Jian, Jilin Fan, Hui Yang, Ping Lan, Manmei Li, Peijun Liu, Hao Gao and Pinghua Sun</dc:creator>
      <dc:date>2018-02-02T05:18:47Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00791</feedburner:origLink></item>
    <item>
      <title>Anti-Influenza Triterpene Saponins from the Bark of Burkea
africana</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/zm1f_wLM_w4/acs.jnatprod.7b00774</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00774/20180202/images/medium/np-2017-00774t_0002.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00774&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=zm1f_wLM_w4:TMkW65oUxAk:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/zm1f_wLM_w4" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Fri, 02 Feb 2018 05:17:48 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00774</guid>
      <dc:creator>Christina E. Mair, Ulrike Grienke, Anke Wilhelm, Ernst Urban, Martin Zehl, Michaela Schmidtke and Judith M. Rollinger</dc:creator>
      <dc:date>2018-02-02T05:17:48Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00774</feedburner:origLink></item>
    <item>
      <title>Can Stereoclusters Separated by Two Methylene Groups
Be Related by DFT Studies? The Case of the Cytotoxic Meroditerpenes
Halioxepines</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/7SXjaQEsvKo/acs.jnatprod.7b00807</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00807/20180201/images/medium/np-2017-008074_0008.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00807&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=7SXjaQEsvKo:eZM5QVolcvE:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/7SXjaQEsvKo" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Fri, 02 Feb 2018 15:43:34 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00807</guid>
      <dc:creator>Guillermo Tarazona, Gonzalo Benedit, Rogelio Fernández, Marta Pérez, Jaime Rodríguez, Carlos Jiménez and Carmen Cuevas</dc:creator>
      <dc:date>2018-02-02T15:43:34Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00807</feedburner:origLink></item>
    <item>
      <title>An Anti-Inflammatory PPAR-γ Agonist from
the Jellyfish-Derived Fungus Penicillium chrysogenum J08NF-4</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/9E-KiaO9rW8/acs.jnatprod.7b00846</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00846/20180201/images/medium/np-2017-008469_0008.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00846&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=9E-KiaO9rW8:H1DDTtLnJhE:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/9E-KiaO9rW8" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Thu, 01 Feb 2018 05:48:54 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00846</guid>
      <dc:creator>Sen Liu, Mingzhi Su, Shao-Jiang Song, Jongki Hong, Hae Young Chung and Jee H. Jung</dc:creator>
      <dc:date>2018-02-01T05:48:54Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00846</feedburner:origLink></item>
    <item>
      <title>Biomimetic Stereoselective Sulfa-Michael Addition
Leads to Platensimycin and Platencin Sulfur Analogues against Methicillin-Resistant Staphylococcus aureus</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/aAAj_S9cPJE/acs.jnatprod.7b00745</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00745/20180201/images/medium/np-2017-007458_0007.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00745&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=aAAj_S9cPJE:SOuhNelAsmA:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/aAAj_S9cPJE" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Thu, 01 Feb 2018 05:48:29 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00745</guid>
      <dc:creator>Lin Qiu, Kai Tian, Zhongqing Wen, Youchao Deng, Dingding Kang, Haoyu Liang, Xiangcheng Zhu, Ben Shen, Yanwen Duan and Yong Huang</dc:creator>
      <dc:date>2018-02-01T05:48:29Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00745</feedburner:origLink></item>
    <item>
      <title>Cyclizidine-Type Alkaloids from Streptomyces sp. HNA39</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/2W5TIBkxSrg/acs.jnatprod.7b01055</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b01055/20180201/images/medium/np-2017-01055m_0007.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b01055&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=2W5TIBkxSrg:O3acjQ4G6Uw:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/2W5TIBkxSrg" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Thu, 01 Feb 2018 05:47:54 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b01055</guid>
      <dc:creator>Yong-Jun Jiang, Jia-Qi Li, Hao-Jian Zhang, Wan-Jing Ding and Zhong-Jun Ma</dc:creator>
      <dc:date>2018-02-01T05:47:54Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b01055</feedburner:origLink></item>
    <item>
      <title>Anti-Staphylococcal Calopins from Fruiting Bodies
of Caloboletus radicans</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/AsMNLDDblwM/acs.jnatprod.7b00525</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00525/20180130/images/medium/np-2017-005257_0002.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00525&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=AsMNLDDblwM:mS_PJfHi3FU:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/AsMNLDDblwM" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Tue, 30 Jan 2018 21:28:20 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00525</guid>
      <dc:creator>Fakir Shahidullah Tareq, Choudhury Mahmood Hasan, M. Mukhlesur Rahman, Mohd Mukrish Mohd Hanafi, Lucio Colombi Ciacchi, Monika Michaelis, Tilmann Harder, Jan Tebben, Md. Tofazzal Islam and Peter Spiteller</dc:creator>
      <dc:date>2018-01-30T21:28:20Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00525</feedburner:origLink></item>
    <item>
      <title>Halogenated C15 Acetogenin Analogues of
Obtusallene III from a Laurenciella sp. Collected
in Corsica</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/Su9YsLei4Dk/acs.jnatprod.7b00706</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00706/20180130/images/medium/np-2017-00706g_0006.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00706&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=Su9YsLei4Dk:cFHh-lpgSpY:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/Su9YsLei4Dk" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Tue, 30 Jan 2018 18:11:58 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00706</guid>
      <dc:creator>Sylvain Sutour, Bruno Therrien, Stephan H. von Reuss and Félix Tomi</dc:creator>
      <dc:date>2018-01-30T18:11:58Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00706</feedburner:origLink></item>
    <item>
      <title>Ribocyclophanes A–E, Glycosylated Cyclophanes
with Antiproliferative Activity from Two Cultured Terrestrial Cyanobacteria</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/C7FEsejZPuY/acs.jnatprod.7b00954</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00954/20180130/images/medium/np-2017-00954b_0004.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00954&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=C7FEsejZPuY:gVXYr6zL_Ko:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/C7FEsejZPuY" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Tue, 30 Jan 2018 18:07:18 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00954</guid>
      <dc:creator>Daniel S. May, Hahk-Soo Kang, Bernard D. Santarsiero, Aleksej Krunic, Qi Shen, Joanna E. Burdette, Steven M. Swanson and Jimmy Orjala</dc:creator>
      <dc:date>2018-01-30T18:07:18Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00954</feedburner:origLink></item>
    <item>
      <title>Neothioviridamide, a Polythioamide Compound Produced
by Heterologous Expression of a Streptomyces sp.
Cryptic RiPP Biosynthetic Gene Cluster</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/drIhoRtADVc/acs.jnatprod.7b00607</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00607/20180130/images/medium/np-2017-006079_0005.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00607&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=drIhoRtADVc:MnF7RPbg1xc:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/drIhoRtADVc" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Tue, 30 Jan 2018 15:42:34 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00607</guid>
      <dc:creator>Teppei Kawahara, Miho Izumikawa, Ikuko Kozone, Junko Hashimoto, Noritaka Kagaya, Hanae Koiwai, Mamoru Komatsu, Manabu Fujie, Noriyuki Sato, Haruo Ikeda and Kazuo Shin-ya</dc:creator>
      <dc:date>2018-01-30T15:42:34Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00607</feedburner:origLink></item>
    <item>
      <title>Probing the Antiallergic and Anti-inflammatory Activity
of Biflavonoids and Dihydroflavonols from Dietes bicolor</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/2vUpmoiojKw/acs.jnatprod.7b00476</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00476/20180130/images/medium/np-2017-00476r_0004.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00476&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=2vUpmoiojKw:ZkFgv6EASGI:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/2vUpmoiojKw" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Tue, 30 Jan 2018 15:42:22 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00476</guid>
      <dc:creator>Iriny M. Ayoub, Michal Korinek, Tsong-Long Hwang, Bing-Hung Chen, Fang-Rong Chang, Mohamed El-Shazly and Abdel Nasser B. Singab</dc:creator>
      <dc:date>2018-01-30T15:42:22Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00476</feedburner:origLink></item>
    <item>
      <title>Cytotoxic and Noncytotoxic Metabolites from Teratosphaeria sp. FL2137, a Fungus Associated with Pinus clausa</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/3K4Xb9Frb7Y/acs.jnatprod.7b00838</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00838/20180126/images/medium/np-2017-00838e_0002.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00838&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=3K4Xb9Frb7Y:rtPVsAYW8Es:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/3K4Xb9Frb7Y" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Fri, 26 Jan 2018 23:38:59 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00838</guid>
      <dc:creator>Chayanika Padumadasa, Ya-Ming Xu, E. M. Kithsiri Wijeratne, Patricia Espinosa-Artiles, Jana M. U’Ren, A. Elizabeth Arnold and A. A. Leslie Gunatilaka</dc:creator>
      <dc:date>2018-01-26T23:38:59Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00838</feedburner:origLink></item>
    <item>
      <title>Structure Reassignment of Cryptorigidifoliols E and
K</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/Mb0rpDjQbZE/acs.jnatprod.7b00830</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00830/20180126/images/medium/np-2017-00830w_0007.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00830&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=Mb0rpDjQbZE:Syeug5fn_KI:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/Mb0rpDjQbZE" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Fri, 26 Jan 2018 23:38:49 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00830</guid>
      <dc:creator>Yongle Du and David G. I. Kingston</dc:creator>
      <dc:date>2018-01-26T23:38:49Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00830</feedburner:origLink></item>
    <item>
      <title>Lipovelutibols A–D: Cytotoxic Lipopeptaibols
from the Himalayan Cold Habitat
Fungus Trichoderma velutinum</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/eYj3ltm2R2g/acs.jnatprod.6b00873</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.6b00873/20180126/images/medium/np-2016-00873x_0003.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.6b00873&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=eYj3ltm2R2g:4h6BDhsaDIA:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/eYj3ltm2R2g" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Fri, 26 Jan 2018 23:38:39 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.6b00873</guid>
      <dc:creator>Varun Pratap Singh, Nalli Yedukondalu, Vandana Sharma, Manoj Kushwaha, Richa Sharma, Asha Chaubey, Anil Kumar, Deepika Singh and Ram A. Vishwakarma</dc:creator>
      <dc:date>2018-01-26T23:38:39Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.6b00873</feedburner:origLink></item>
    <item>
      <title>Hamigerans R and S: Nitrogenous Diterpenoids from
the New Zealand Marine Sponge Hamigera tarangaensis</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/VX0UIMEVoow/acs.jnatprod.7b00960</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00960/20180125/images/medium/np-2017-009602_0005.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00960&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=VX0UIMEVoow:DqXsUs5plpk:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/VX0UIMEVoow" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Fri, 26 Jan 2018 21:38:46 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00960</guid>
      <dc:creator>Ethan F. Woolly, A. Jonathan Singh, Euan R. Russell, John H. Miller and Peter T. Northcote</dc:creator>
      <dc:date>2018-01-26T21:38:46Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00960</feedburner:origLink></item>
    <item>
      <title>Natural Products Containing a Nitrogen–Sulfur
Bond</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/N6vrruH9fgA/acs.jnatprod.7b00921</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00921/20180124/images/medium/np-2017-00921r_0007.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00921&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=N6vrruH9fgA:Z1F7nA4Paw8:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/N6vrruH9fgA" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Wed, 24 Jan 2018 20:40:09 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00921</guid>
      <dc:creator>Janusz J. Petkowski, William Bains and Sara Seager</dc:creator>
      <dc:date>2018-01-24T20:40:09Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00921</feedburner:origLink></item>
    <item>
      <title>Revision of the Phytochemistry of Eremophila
sturtii and E. mitchellii</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/E5MNJ1Q9Xrg/acs.jnatprod.7b00616</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00616/20180124/images/medium/np-2017-006163_0003.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00616&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=E5MNJ1Q9Xrg:iGVIHfVsHZw:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/E5MNJ1Q9Xrg" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Wed, 24 Jan 2018 05:36:06 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00616</guid>
      <dc:creator>Nicholas J. Sadgrove, Julian Klepp, Sarah V.A.-M. Legendre, Dane Lyddiard, Christopher J. Sumby and Ben W. Greatrex</dc:creator>
      <dc:date>2018-01-24T05:36:06Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00616</feedburner:origLink></item>
    <item>
      <title>Total Synthesis of Pyrophen and Campyrones A–C</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/_ukPMae5glg/acs.jnatprod.7b00720</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00720/20180124/images/medium/np-2017-00720b_0008.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00720&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=_ukPMae5glg:EQkLCZfbejM:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/_ukPMae5glg" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Wed, 24 Jan 2018 15:43:23 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00720</guid>
      <dc:creator>Keith P. Reber and Hannah E. Burdge</dc:creator>
      <dc:date>2018-01-24T15:43:23Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00720</feedburner:origLink></item>
    <item>
      <title>Taccalonolide Microtubule Stabilizers Generated Using
Semisynthesis Define the Effects of Mono Acyloxy Moieties at C-7
or C-15 and Disubstitutions at C-7 and C-25</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/AknMLL9RBWM/acs.jnatprod.7b00967</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00967/20180123/images/medium/np-2017-00967m_0009.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00967&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=AknMLL9RBWM:vq7qus9_Wwo:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/AknMLL9RBWM" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Tue, 23 Jan 2018 19:13:45 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00967</guid>
      <dc:creator>Antonius R. B. Ola, April L. Risinger, Lin Du, Cynthia L. Zammiello, Jiangnan Peng, Robert H. Cichewicz and Susan L. Mooberry</dc:creator>
      <dc:date>2018-01-23T19:13:45Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00967</feedburner:origLink></item>
    <item>
      <title>Multiflorumisides A–G, Dimeric Stilbene Glucosides
with Rare Coupling Patterns from the Roots of Polygonum multiflorum</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/eyZl7CFKoLk/acs.jnatprod.7b00540</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00540/20180123/images/medium/np-2017-00540t_0009.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00540&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=eyZl7CFKoLk:PBitpOaFibA:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/eyZl7CFKoLk" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Tue, 23 Jan 2018 14:30:56 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00540</guid>
      <dc:creator>Shuo-Guo Li, Xiao-Jun Huang, Man-Mei Li, Qing Liu, Hui Liu, Ying Wang and Wen-Cai Ye</dc:creator>
      <dc:date>2018-01-23T14:30:56Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00540</feedburner:origLink></item>
    <item>
      <title>A Series of Enthalpically Optimized Docetaxel Analogues
Exhibiting Enhanced Antitumor Activity and Water Solubility</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/Q9vOa30TBkc/acs.jnatprod.7b00857</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00857/20180122/images/medium/np-2017-00857k_0010.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00857&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=Q9vOa30TBkc:1xH5Nhu3pVY:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/Q9vOa30TBkc" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Tue, 23 Jan 2018 13:55:38 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00857</guid>
      <dc:creator>Yun-Tao Ma, Yanting Yang, Pei Cai, De-Yang Sun, Pedro A. Sánchez-Murcia, Xiao-Ying Zhang, Wen-Qiang Jia, Lei Lei, Mengqi Guo, Federico Gago, Hongbo Wang and Wei-Shuo Fang</dc:creator>
      <dc:date>2018-01-23T13:55:38Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00857</feedburner:origLink></item>
    <item>
      <title>Cysteine-Derived Pleurotin Congeners from the Nematode-Trapping
Basidiomycete Hohenbuehelia grisea</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/K3-sRQh_95s/acs.jnatprod.7b00713</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00713/20180122/images/medium/np-2017-00713t_0005.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00713&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=K3-sRQh_95s:VeDB9kmqXCg:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/K3-sRQh_95s" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Mon, 22 Jan 2018 21:02:53 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00713</guid>
      <dc:creator>Birthe Sandargo, Benjarong Thongbai, Marc Stadler and Frank Surup</dc:creator>
      <dc:date>2018-01-22T21:02:53Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00713</feedburner:origLink></item>
    <item>
      <title>Neuroprotective Dihydroagarofuran Sesquiterpene Derivatives
from the Leaves of Tripterygium wilfordii</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/EjBzvwApXLU/acs.jnatprod.7b00615</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00615/20180119/images/medium/np-2017-00615a_0006.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00615&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=EjBzvwApXLU:itErbq8AdYk:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/EjBzvwApXLU" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Mon, 22 Jan 2018 14:59:56 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00615</guid>
      <dc:creator>Fang-You Chen, Chuang-Jun Li, Jie Ma, Jian Zhou, Li Li, Zhao Zhang, Nai-Hong Chen and Dong-Ming Zhang</dc:creator>
      <dc:date>2018-01-22T14:59:56Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00615</feedburner:origLink></item>
    <item>
      <title>Crystal Structures and Human Leukemia Cell Apoptosis
Inducible Activities of Parthenolide Analogues Isolated from Piptocoma rufescens</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/OsQsojQRA1I/acs.jnatprod.7b01079</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b01079/20180119/images/medium/np-2017-010799_0007.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b01079&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=OsQsojQRA1I:I_Tf2u6XF6c:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/OsQsojQRA1I" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Fri, 19 Jan 2018 19:31:41 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b01079</guid>
      <dc:creator>Yulin Ren, Judith C. Gallucci, Xinxin Li, Lichao Chen, Jianhua Yu and A. Douglas Kinghorn</dc:creator>
      <dc:date>2018-01-19T19:31:41Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b01079</feedburner:origLink></item>
    <item>
      <title>Discovery of Alternative Producers of the Enediyne
Antitumor Antibiotic C-1027 with High Titers</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/HRFvbyF8b0w/acs.jnatprod.7b01013</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b01013/20180118/images/medium/np-2017-01013s_0004.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b01013&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=HRFvbyF8b0w:OzqqoLZakSc:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/HRFvbyF8b0w" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Thu, 18 Jan 2018 21:17:48 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b01013</guid>
      <dc:creator>Xiaohui Yan,  Hindra, Huiming Ge, Dong Yang, Tingting Huang, Ivana Crnovcic, Chin-Yuan Chang, Shi-Ming Fang, Thibault Annaval, Xiangcheng Zhu, Yong Huang, Li-Xing Zhao, Yi Jiang, Yanwen Duan and Ben Shen</dc:creator>
      <dc:date>2018-01-18T21:17:48Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b01013</feedburner:origLink></item>
    <item>
      <title>Seco-Dendrobine-Type Alkaloids and Bioactive Phenolics
from Dendrobium findlayanum</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/Racnmo-XFwA/acs.jnatprod.7b00150</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00150/20180122/images/medium/np-2017-00150z_0013.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00150&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=Racnmo-XFwA:xsAaFshiB4Y:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/Racnmo-XFwA" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Wed, 17 Jan 2018 15:50:37 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00150</guid>
      <dc:creator>Dan Yang, Zhong-Quan Cheng, Liu Yang, Bo Hou, Jing Yang, Xiao-Nian Li, Cheng-Ting Zi, Fa-Wu Dong, Zheng-Hua Liu, Jun Zhou, Zhong-Tao Ding and Jiang-Miao Hu</dc:creator>
      <dc:date>2018-01-17T15:50:37Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00150</feedburner:origLink></item>
    <item>
      <title>Taburnaemines A–I, Cytotoxic Vobasinyl-Iboga-Type
Bisindole Alkaloids from Tabernaemontana corymbosa</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/ZppDjfazE30/acs.jnatprod.7b00949</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00949/20180110/images/medium/np-2017-00949b_0008.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00949&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=ZppDjfazE30:pJnMKAUrKUA:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/ZppDjfazE30" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Wed, 10 Jan 2018 16:13:32 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00949</guid>
      <dc:creator>Yu Zhang, Yu-Xi Yuan, Masuo Goto, Ling-Li Guo, Xiao-Nian Li, Susan L. Morris-Natschke, Kuo-Hsiung Lee and Xiao-Jiang Hao</dc:creator>
      <dc:date>2018-01-10T16:13:32Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00949</feedburner:origLink></item>
    <item>
      <title>Antineoplastic Agents. 606. The Betulastatins</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/rlMW0hzmQRc/acs.jnatprod.7b00536</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00536/20180105/images/medium/np-2017-00536f_0005.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00536&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=rlMW0hzmQRc:eXjsxeqRpJ4:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/rlMW0hzmQRc" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Fri, 05 Jan 2018 16:01:35 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00536</guid>
      <dc:creator>George R. Pettit, Noeleen Melody and Jean-Charles Chapuis</dc:creator>
      <dc:date>2018-01-05T16:01:35Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00536</feedburner:origLink></item>
    <item>
      <title>Phenanthrenes: A Promising Group of Plant Secondary
Metabolites</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/pIannFM3ThQ/acs.jnatprod.7b00619</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00619/20171227/images/medium/np-2017-00619t_0013.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00619&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=pIannFM3ThQ:S2P4bnNq7Rc:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/pIannFM3ThQ" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Wed, 27 Dec 2017 16:23:06 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00619</guid>
      <dc:creator>Barbara Tóth, Judit Hohmann and Andrea Vasas</dc:creator>
      <dc:date>2017-12-27T16:23:06Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00619</feedburner:origLink></item>
    <item>
      <title>Iodine-Promoted Aromatization of p-Menthane-Type
Phytocannabinoids</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/Nl4NPyttayQ/acs.jnatprod.7b00946</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00946/20171214/images/medium/np-2017-00946k_0002.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00946&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=Nl4NPyttayQ:4VqQNGCfiFg:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/Nl4NPyttayQ" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Thu, 14 Dec 2017 20:31:04 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00946</guid>
      <dc:creator>Federica Pollastro, Diego Caprioglio, Patrizia Marotta, Aniello Schiano Moriello, Luciano De Petrocellis, Orazio Taglialatela-Scafati and Giovanni Appendino</dc:creator>
      <dc:date>2017-12-14T20:31:04Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00946</feedburner:origLink></item>
    <item>
      <title>Anti-inflammatory Dimeric 2-(2-Phenylethyl)chromones from the Resinous Wood of Aquilaria sinensis</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/Kcn9IBW6vP8/acs.jnatprod.7b00919</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00919/20171211/images/medium/np-2017-00919u_0007.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00919&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=Kcn9IBW6vP8:I_1_5S-aKaQ:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/Kcn9IBW6vP8" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Mon, 11 Dec 2017 21:12:38 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00919</guid>
      <dc:creator>Hui-Xia Huo, Zhi-Xiang Zhu, Yue-Lin Song, She-Po Shi, Jing Sun, Hui Sun, Yun-Fang Zhao, Jiao Zheng, Daneel Ferreira, Jordan K. Zjawiony, Peng-Fei Tu and Jun Li</dc:creator>
      <dc:date>2017-12-11T21:12:38Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00919</feedburner:origLink></item>
    <item>
      <title>Marine Natural Product Honaucin A Attenuates Inflammation
by Activating the Nrf2-ARE Pathway</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/sVrHDF9Gbww/acs.jnatprod.7b00734</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00734/20171211/images/medium/np-2017-00734v_0006.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00734&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=sVrHDF9Gbww:IgHqARFlMP0:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/sVrHDF9Gbww" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Thu, 07 Dec 2017 16:33:13 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00734</guid>
      <dc:creator>Samantha J. Mascuch, Paul D. Boudreau, Tristan M. Carland, N. Tessa Pierce, Joshua Olson, Mary E. Hensler, Hyukjae Choi, Joseph Campanale, Amro Hamdoun, Victor Nizet, William H. Gerwick, Teresa Gaasterland and Lena Gerwick</dc:creator>
      <dc:date>2017-12-07T16:33:13Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00734</feedburner:origLink></item>
    <item>
      <title>Cytotoxicity, Hemolytic Toxicity, and Mechanism of Action of Pulsatilla Saponin D
and Its Synthetic Derivatives</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/aidOChGkrA4/acs.jnatprod.7b00578</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00578/20171113/images/medium/np-2017-00578c_0007.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00578&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=aidOChGkrA4:NqgrCqZpRQw:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/aidOChGkrA4" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Mon, 13 Nov 2017 16:58:16 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00578</guid>
      <dc:creator>Zhong Chen, Huaqing Duan, Xiaohang Tong, Peiling Hsu, Li Han, Susan L. Morris-Natschke, Shilin Yang, Wei Liu and Kuo-Hsiung Lee</dc:creator>
      <dc:date>2017-11-13T16:58:16Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00578</feedburner:origLink></item>
    <item>
      <title>Biochemometrics to Identify Synergists and Additives
from Botanical Medicines: A Case Study with Hydrastis canadensis (Goldenseal)</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/wRlEtWDzYu4/acs.jnatprod.7b00654</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00654/20171101/images/medium/np-2017-00654r_0006.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00654&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=wRlEtWDzYu4:CdycZe34gJE:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/wRlEtWDzYu4" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Wed, 01 Nov 2017 17:18:19 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00654</guid>
      <dc:creator>Emily R. Britton, Joshua J. Kellogg, Olav M. Kvalheim and Nadja B. Cech</dc:creator>
      <dc:date>2017-11-01T17:18:19Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00654</feedburner:origLink></item>
    <item>
      <title>Antiplasmodial Chromanes and Chromenes from the Monotypic
Plant Species Koeberlinia spinosa</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/jsxybT59W3M/acs.jnatprod.7b00579</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00579/20171019/images/medium/np-2017-005799_0007.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00579&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=jsxybT59W3M:eil_w5E5_fQ:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/jsxybT59W3M" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Thu, 19 Oct 2017 19:04:25 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00579</guid>
      <dc:creator>Christopher Charles Presley, Ana Lisa Valenciano, Maria L. Fernández-Murga, Yongle Du, Narasimhamurthy Shanaiah, Maria B. Cassera, Michael Goetz, Jason A. Clement and David G. I. Kingston</dc:creator>
      <dc:date>2017-10-19T19:04:25Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00579</feedburner:origLink></item>
    <item>
      <title>Zampanolide Binding to Tubulin Indicates Cross-Talk
of Taxane Site with Colchicine and Nucleotide Sites</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/gaeCdLxZZ98/acs.jnatprod.7b00704</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00704/20171012/images/medium/np-2017-00704a_0009.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00704&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=gaeCdLxZZ98:8PXSoQ8ZIqw:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/gaeCdLxZZ98" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Thu, 12 Oct 2017 04:47:10 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00704</guid>
      <dc:creator>Jessica J. Field, Benet Pera, Juan Estévez Gallego, Enrique Calvo, Javier Rodríguez-Salarichs, Gonzalo Sáez-Calvo, Didier Zuwerra, Michel Jordi, José M. Andreu, Andrea E. Prota, Grégory Ménchon, John H. Miller, Karl-Heinz Altmann and J. Fernando Díaz</dc:creator>
      <dc:date>2017-10-12T04:47:10Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00704</feedburner:origLink></item>
    <item>
      <title>Chemical Constituents of Bryophytes: Structures and
Biological Activity</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/HdHIpemOUKQ/acs.jnatprod.6b01046</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.6b01046/20171011/images/medium/np-2016-01046c_0001.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.6b01046&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=HdHIpemOUKQ:JBwWS3buPqE:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/HdHIpemOUKQ" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Wed, 11 Oct 2017 15:07:13 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.6b01046</guid>
      <dc:creator>Yoshinori Asakawa and Agnieszka Ludwiczuk</dc:creator>
      <dc:date>2017-10-11T15:07:13Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.6b01046</feedburner:origLink></item>
    <item>
      <title>Antineoplastic Agents. 605.
Isoquinstatins</title>
      <link>http://feedproxy.google.com/~r/acs/jnprdf/~3/apFMuTMYAp4/acs.jnatprod.7b00352</link>
      <description>&lt;p&gt;&lt;img src="http://pubs.acs.org/appl/literatum/publisher/achs/journals/content/jnprdf/0/jnprdf.ahead-of-print/acs.jnatprod.7b00352/20170919/images/medium/np-2017-003527_0005.gif" alt="TOC Graphic"/&gt;&lt;/p&gt;&lt;div&gt;&lt;cite&gt;Journal of Natural Products&lt;/cite&gt;&lt;/div&gt;&lt;div&gt;DOI: 10.1021/acs.jnatprod.7b00352&lt;/div&gt;&lt;div class="feedflare"&gt;
&lt;a href="http://feeds.feedburner.com/~ff/acs/jnprdf?a=apFMuTMYAp4:fXDxkCFHYps:yIl2AUoC8zA"&gt;&lt;img src="http://feeds.feedburner.com/~ff/acs/jnprdf?d=yIl2AUoC8zA" border="0"&gt;&lt;/img&gt;&lt;/a&gt;
&lt;/div&gt;&lt;img src="http://feeds.feedburner.com/~r/acs/jnprdf/~4/apFMuTMYAp4" height="1" width="1" alt=""/&gt;</description>
      <pubDate>Tue, 19 Sep 2017 19:41:38 GMT</pubDate>
      <guid isPermaLink="false">http://dx.doi.org/10.1021/acs.jnatprod.7b00352</guid>
      <dc:creator>George R. Pettit, Noeleen Melody and Jean-Charles Chapuis</dc:creator>
      <dc:date>2017-09-19T19:41:38Z</dc:date>
    <feedburner:origLink>http://dx.doi.org/10.1021/acs.jnatprod.7b00352</feedburner:origLink></item>
  </channel>
</rss>""")
    #test = parse_rss("http://feeds.feedburner.com/acs/jnprdf")
    # test = parse_rss("https://www.thieme-connect.de/rss/thieme/en/10.1055-s-00000058.xml")
    # test = parse_rss("http://feeds.nature.com/ja/rss/current")
    # test = parse_rss("https://chemistry-europe.onlinelibrary.wiley.com/feed/10990690/most-recent")
    #test = parse_rss("https://onlinelibrary.wiley.com/feed/15213773/most-recent")
    # test = parse_rss("https://www.mdpi.com/rss/journal/marinedrugs")
    # test = parse_rss("http://feeds.feedburner.com/acs/jnprdf")
    print(test)
    print(len(test))

    # Database Entry
    sqlite3_database(test)

    # RSS Feed archives
    get_archives_rss_urls('http://feeds.feedburner.com/acs/jnprdf')

if __name__ == "__main__":
    main()
