"""Build the one-file speaker kit PDF from index.html.

index.html is the single source of truth. This pulls the three bio versions and the
facts table straight out of it, so the PDF can never drift from the page. Rewrite the
bio on the page, run this, and the PDF follows.

The PDF is deliberately LIGHT while the web page is dark. A host forwards this to a
designer or drops it in a program packet, and a dark document prints badly and eats
toner. Same reason the portrait switches to the light-ground version here.

Usage:  python3 build_pdf.py
Output: scott-penberthy-bio.pdf
"""
import base64, html as _html, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
SRC = os.path.join(HERE, "index.html")
TMP = os.path.join(HERE, "_print.html")
OUT = os.path.join(HERE, "scott-penberthy-bio.pdf")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def read(path):
    with open(path) as f:
        return f.read()


def b64file(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


src = read(SRC)


def paragraphs(block_id):
    """Return the inner <p> markup of a bio block, whether div-wrapped or a bare <p>."""
    m = re.search(r'<div id="%s">(.*?)\n\s*</div>' % block_id, src, re.S)
    if m:
        return re.findall(r"<p>(.*?)</p>", m.group(1), re.S)
    m = re.search(r'<p id="%s">(.*?)</p>' % block_id, src, re.S)
    if not m:
        sys.exit("could not find block %s in index.html" % block_id)
    return [m.group(1)]


def strip_spans(t):
    return re.sub(r"</?span[^>]*>", "", t).strip()


full = [strip_spans(p) for p in paragraphs("t-full")]
short = [strip_spans(p) for p in paragraphs("t-short")]
spoken = [strip_spans(p) for p in paragraphs("t-spoken")]

# Facts table, minus the rows that only make sense on the web page itself.
facts = []
for th, td in re.findall(r"<tr><th>(.*?)</th><td>(.*?)</td></tr>", src, re.S):
    label = re.sub(r"<[^>]+>", "", th).strip()
    if label in ("This page",):
        continue
    value = re.sub(r'<a [^>]*href="([^"]*)"[^>]*>(.*?)</a>', r"\2", td)
    value = re.sub(r"<[^>]+>", "", value).strip()
    facts.append((label, value))

creds = re.findall(r"<li><b>(.*?)</b>\s*(.*?)</li>", src, re.S)
role = re.search(r'<p class="role">(.*?)</p>', src, re.S).group(1).strip()


def wc(blocks):
    return sum(len(_html.unescape(re.sub(r"<[^>]+>", "", b)).split()) for b in blocks)


PAGE = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Scott Penberthy — speaker kit</title>
<style>
@font-face{font-family:'EBG';src:url(data:font/woff2;base64,%(EBG)s) format('woff2');font-weight:400 700;font-style:normal}
@font-face{font-family:'EBG';src:url(data:font/woff2;base64,%(EBGI)s) format('woff2');font-weight:400 700;font-style:italic}
@font-face{font-family:'InterV';src:url(data:font/woff2;base64,%(INTER)s) format('woff2');font-weight:100 900;font-style:normal}
@page{size:letter;margin:16mm 17mm 14mm}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'EBG',Georgia,serif;font-size:10.6pt;line-height:1.52;color:#1a1917;background:#fff;
     -webkit-print-color-adjust:exact;print-color-adjust:exact}
.sans{font-family:'InterV',Helvetica,Arial,sans-serif}
.eyebrow{font-family:'InterV',sans-serif;font-size:6.6pt;font-weight:600;letter-spacing:.26em;
         text-transform:uppercase;color:#9a7f30}
header{display:grid;grid-template-columns:1fr 30mm;gap:9mm;align-items:start;
       border-bottom:.7pt solid #cdc7ba;padding-bottom:6mm;margin-bottom:7mm}
h1{font-size:27pt;font-weight:400;line-height:1;letter-spacing:-.01em;margin:1.5mm 0 2mm}
.role{font-size:11.4pt;line-height:1.45;color:#3d3a34;max-width:78mm;margin:1mm 0 2.5mm}
.role b{color:#1a1917;font-weight:600}
.said{font-family:'InterV',sans-serif;font-size:8pt;color:#6d6a62}
.said b{color:#9a7f30;font-weight:600;letter-spacing:.03em}
header img{width:30mm;height:30mm;object-fit:cover;border:.7pt solid #cdc7ba}
.creds{list-style:none;display:flex;flex-wrap:wrap;gap:2.5mm;margin-top:4mm}
.creds li{font-family:'InterV',sans-serif;font-size:7.4pt;color:#55524b;border:.6pt solid #d8d2c6;padding:1.4mm 2.6mm}
.creds li b{color:#9a7f30;font-weight:600;margin-right:1.6mm}
h2{font-size:13pt;font-weight:400;margin:0 0 1mm}
.sec{margin-top:7mm}
.sec.tight{margin-top:5.5mm}
.hd{display:flex;align-items:baseline;gap:3mm;margin-bottom:2.5mm}
.hd .rule{flex:1;height:.6pt;background:#ded8cc;position:relative;top:-1mm}
.hd .len{font-family:'InterV',sans-serif;font-size:6.6pt;letter-spacing:.14em;text-transform:uppercase;color:#8d8a82}
p+p{margin-top:2.1mm}
.box{border:.7pt solid #ded8cc;border-left:1.6pt solid #c9a84c;background:#faf8f4;padding:4.5mm 5mm}
.box p{font-size:9.9pt;line-height:1.5}
.note{font-family:'InterV',sans-serif;font-size:7.6pt;color:#7a776f;margin-bottom:2mm}
table{border-collapse:collapse;width:100%%;font-family:'InterV',sans-serif;font-size:8.4pt}
th,td{text-align:left;padding:1.9mm 0;border-bottom:.5pt solid #e4dfd4;vertical-align:top}
th{font-size:6.6pt;letter-spacing:.16em;text-transform:uppercase;color:#9a7f30;font-weight:600;width:33mm;padding-right:5mm}
td{color:#3d3a34}
footer{margin-top:8mm;border-top:.7pt solid #cdc7ba;padding-top:3.5mm;
       font-family:'InterV',sans-serif;font-size:7.6pt;color:#7a776f;line-height:1.6}
footer b{color:#3d3a34;font-weight:600}
footer .url{color:#9a7f30;font-weight:600}
.pagebreak{break-before:page}
</style></head><body>

<header>
  <div>
    <div class="eyebrow">Speaker kit</div>
    <h1>Scott Penberthy</h1>
    <p class="role">%(ROLE)s</p>
    <div class="said">Said <b>Pen-ber-thee</b></div>
    <ul class="creds">%(CREDS)s</ul>
  </div>
  <img src="data:image/jpeg;base64,%(PHOTO)s" alt="Scott Penberthy">
</header>

<div class="sec" style="margin-top:0">
  <div class="hd"><h2>The bio</h2><span class="rule"></span><span class="len">%(NFULL)d words</span></div>
  <div class="note">For a program, a website, or a conference listing. This is the default.</div>
  %(FULL)s
</div>

<div class="sec">
  <div class="hd"><h2>Short version</h2><span class="rule"></span><span class="len">%(NSHORT)d words</span></div>
  <div class="note">For a panel listing, a slide, or anywhere with a tight word count.</div>
  <div class="box">%(SHORT)s</div>
</div>

<div class="sec">
  <div class="hd"><h2>Spoken introduction</h2><span class="rule"></span><span class="len">about %(SEC)d seconds</span></div>
  <div class="note">Written to be read aloud from a stage. The surname is said Pen-ber-thee. It ends on the handover, so whoever is introducing him knows where to stop.</div>
  <div class="box">%(SPOKEN)s</div>
</div>

<div class="sec tight">
  <div class="hd"><h2>The details programs ask for</h2><span class="rule"></span></div>
  <table>%(FACTS)s</table>
</div>

<footer>
  <b>Photographs, and the latest version of all of this, at <span class="url">scott.ai/bio</span></b><br>
  Three portraits are there to download, on light and dark grounds and one on stage, free to use with no credit needed.
  If this sheet has been sitting in a folder for a while, the page is the one that is current.<br>
  Views are his own and do not represent his employer or any advisory board he serves on.
</footer>

</body></html>"""

photo = b64file(os.path.join(SITE, "img", "scott-portrait.jpg"))

page = PAGE % dict(
    EBG=read(os.path.join(HERE, "EBGaramond.b64")).strip(),
    EBGI=read(os.path.join(HERE, "EBGaramond-Italic.b64")).strip(),
    INTER=read(os.path.join(HERE, "Inter.b64")).strip(),
    PHOTO=photo,
    ROLE=role,
    CREDS="".join("<li><b>%s</b>%s</li>" % (a, b.strip()) for a, b in creds),
    FULL="".join("<p>%s</p>" % p for p in full),
    SHORT="".join("<p>%s</p>" % p for p in short),
    SPOKEN="".join("<p>%s</p>" % p for p in spoken),
    FACTS="".join("<tr><th>%s</th><td>%s</td></tr>" % kv for kv in facts),
    NFULL=wc(full), NSHORT=wc(short),
    SEC=round(wc(spoken) / 150 * 60 / 5) * 5,
)

with open(TMP, "w") as f:
    f.write(page)

subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                "--print-to-pdf=" + OUT, "file://" + TMP],
               check=True, capture_output=True, timeout=120)
os.remove(TMP)
print("wrote %s  %.0f KB" % (OUT, os.path.getsize(OUT) / 1024))
