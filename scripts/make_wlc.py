"""Generate data/wireless_controllers.json: on-premises and cloud wireless controllers (checked 15 Nov 2026)."""
import json, sys

V, P, N = "Verified", "Partly verified", "Not verified"
CC = "https://www.cisco.com/c/en/us/products/collateral/"
QS = lambda i: "https://www.hpe.com/us/en/collaterals/collateral.%s.html" % i
FMX = "https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/Fortinet_Wireless_Product_Matrix.pdf"

rows = []
def add(base, **kw):
    r = dict(base); r.update(kw); rows.append(r)

# ---------------- Cisco ----------------
c = dict(vendor="Cisco", deployment="On-premises", verified=V, ha="SSO (1:1 active/standby) and N+1", max_aps_text=None, throughput_text=None)
add(c, family="Cisco Wireless 9800", model="CW9800H1", form="Appliance", size="1RU", max_aps=6000, max_clients=64000, throughput_gbps=100,
    ports="8x 1/10G SFP+ + 4x 25G SFP+", psu_redundant="Yes", datasheet=CC + "networking/wireless/wireless-lan-controllers/cat-cw9800h1-cw9800h2-wireless-controllers-ds.html",
    notes="Redundant AC or DC power modules.")
add(c, family="Cisco Wireless 9800", model="CW9800H2", form="Appliance", size="1RU", max_aps=6000, max_clients=64000, throughput_gbps=100,
    ports="8x 1/10G SFP+ + 2x 40G", psu_redundant="Yes", datasheet=CC + "networking/wireless/wireless-lan-controllers/cat-cw9800h1-cw9800h2-wireless-controllers-ds.html",
    notes="Redundant AC or DC power modules.")
add(c, family="Cisco Wireless 9800", model="CW9800M", form="Appliance", size="1RU", max_aps=3000, max_clients=32000, throughput_gbps=50,
    ports="4x 1/10G SFP+ + 2x 25G SFP+", psu_redundant="Optional", datasheet=CC + "networking/wireless/wireless-lan-controllers/catalyst-cw9800m-wireless-controller-ds.html",
    notes="Ships with one AC power supply; redundant supply sold separately.")
add(c, family="Cisco Wireless 9800", model="CW9800L", form="Appliance", size="1RU (compact)", max_aps=500, max_clients=10000, throughput_gbps=10,
    ports="2x 1/10G SFP+", ha="SSO (redundancy port)", psu_redundant="Optional", datasheet=CC + "networking/wireless/wireless-lan-controllers/cw9800l-wireless-controller-ds.html",
    notes="Optional redundant power (CW9800L-RPS=).")
add(c, family="Catalyst 9800", model="Catalyst 9800-80", form="Appliance", size="2RU", max_aps=6000, max_clients=64000, throughput_gbps=80,
    ports="8x 10G (or 6x 10G + 2x 1G) + optional modular uplinks up to 100G", psu_redundant="Yes",
    datasheet=CC + "wireless/catalyst-9800-series-wireless-controllers/nb-06-cat9800-80-wirel-mod-data-sheet-ctp-en.html",
    notes="Announced end of life; successor is the CW9800H1/H2.")
add(c, family="Catalyst 9800", model="Catalyst 9800-40", form="Appliance", size="1RU", max_aps=2000, max_clients=32000, throughput_gbps=40,
    ports="4x 1/10G SFP+", psu_redundant="Optional", datasheet=CC + "wireless/catalyst-9800-series-wireless-controllers/nb-06-cat9800-wirel-cont-data-sheet-ctp-en.html",
    notes="Announced end of life; successor is the CW9800M.")
for m, p in [("Catalyst 9800-L-C (copper)", "2x 10G mGig copper + 4x 2.5G/1G RJ-45"), ("Catalyst 9800-L-F (fiber)", "2x 10G SFP+ + 4x 2.5G/1G RJ-45")]:
    add(c, family="Catalyst 9800", model=m, form="Appliance", size="1RU half-width", max_aps=500, max_aps_text="250 (500 with Performance license)",
        max_clients=10000, throughput_gbps=10, throughput_text="5 Gbps (10 Gbps with Performance license)", ports=p, ha="SSO and N+1", psu_redundant="No",
        datasheet=CC + "wireless/catalyst-9800-series-wireless-controllers/datasheet-c78-742434.html",
        notes="5,000 clients (10,000 with Performance license). External AC/DC adapter.")
add(c, family="Catalyst 9800-CL", model="Catalyst 9800-CL (private cloud)", form="Virtual", size="VM (ESXi, KVM, Hyper-V, NFVIS)",
    max_aps=6000, max_aps_text="100 / 1,000 / 3,000 / 6,000 by VM profile", max_clients=64000, throughput_gbps=5,
    throughput_text="2.1 Gbps (5 Gbps with SR-IOV on ESXi/KVM)", ports="Virtual NICs", psu_redundant=None,
    datasheet=CC + "wireless/catalyst-9800-cl-wireless-controller-cloud/nb-06-cat9800-cl-cloud-wirel-data-sheet-ctp-en.html",
    notes="Runs on your own servers. SSO on Small/Medium/Large profiles.")
add(c, family="Catalyst 9800-CL", model="Catalyst 9800-CL (public cloud)", deployment="Cloud", form="Virtual (public cloud)", size="AWS, Azure, GCP or OCI",
    max_aps=6000, max_clients=64000, throughput_gbps=None, throughput_text="Local switching at the AP (no central data path)", ports="Virtual NICs",
    ha="N+1 only", psu_redundant=None,
    datasheet=CC + "wireless/catalyst-9800-cl-wireless-controller-cloud/nb-06-cat9800-cl-cloud-wirel-data-sheet-ctp-en.html",
    notes="Controller hosted in your own public cloud account; all client traffic is switched locally at the AP.")
add(c, family="Catalyst 9800 embedded", model="Embedded Wireless Controller on Catalyst APs (EWC-AP)", form="Embedded in AP", size="Runs on a Catalyst 9100 AP",
    max_aps=50, max_clients=1000, throughput_gbps=None, ports="AP uplink", ha="Active and standby AP", psu_redundant=None,
    datasheet=CC + "wireless/catalyst-9800-series-wireless-controllers/nb-o6-embded-wrls-cont-ds-cte-en.html",
    notes="Controller software running on one of the APs (C9105, C9115, C9117, C9120, C9130). For small sites.")
add(dict(vendor="Cisco", deployment="Cloud", verified=P), family="Cisco Meraki", model="Meraki cloud dashboard", form="Cloud service", size="Hosted by Cisco Meraki",
    max_aps=None, max_aps_text="No fixed limit (licensed per AP)", max_clients=None, throughput_gbps=None, throughput_text="Local switching at the AP",
    ports=None, ha="Cisco-hosted service", psu_redundant=None, max_aps_note=None,
    datasheet="https://www.cisco.com/site/us/en/products/collateral/networking/wireless/access-points/wireless-9176-series-access-points-ds.html",
    notes="Cisco Wireless (CW) APs can be managed from the Meraki cloud instead of a 9800 controller; the AP datasheets describe both options. No capacity figures are published.")

# ---------------- HPE Aruba ----------------
a = dict(vendor="HPE Aruba", deployment="On-premises", verified=V, ha="Clustering with redundancy and live upgrades")
g = QS("a50004272enw")
for lic, aps, cl, tp in [("base", 4096, 32000, 20), ("Silver license", 8192, 48000, 30), ("Gold license", 16384, 64000, 40)]:
    add(a, family="9200 Series Campus Gateway", model="9240 Campus Gateway (" + lic + ")", form="Appliance", size="1RU",
        max_aps=aps, max_aps_text=["4K", "8K", "16K"][[4096, 8192, 16384].index(aps)] + " (up to " + ["8K", "16K", "32K"][[4096, 8192, 16384].index(aps)] + " per cluster)",
        max_clients=cl, throughput_gbps=tp, throughput_text=None, ports="4x 25G SFP28", psu_redundant="Yes", datasheet=g,
        notes="AOS-10 figures. Firewall throughput " + str(tp) + " Gbps; capacity grows with the Silver and Gold licenses. 1 + redundant power supply slots.")
h = QS("a50006999enw")
add(a, family="9100 Series Hybrid Gateway", model="9106 Gateway", form="Appliance", size=None, max_aps=2048, max_aps_text="2K (4K per cluster)",
    max_clients=8000, throughput_gbps=10, throughput_text=None, ports="2x SFP+ + 2x combo (SFP/1G copper) + 2x 1G (60 W PoE out)", psu_redundant=None,
    datasheet=h, notes="Firewall throughput 10 Gbps. For large branches and small campuses.")
add(a, family="9100 Series Hybrid Gateway", model="9114 Gateway", form="Appliance", size=None, max_aps=4096, max_aps_text="4K (8K per cluster)",
    max_clients=10000, throughput_gbps=20, throughput_text=None, ports="4x SFP+ + 4x combo (SFP/1G copper)", psu_redundant=None,
    datasheet=h, notes="Firewall throughput 20 Gbps.")
add(dict(vendor="HPE Aruba", deployment="Cloud", verified=P), family="HPE Aruba Networking Central", model="HPE Aruba Networking Central (cloud)",
    form="Cloud service", size="Hosted by HPE", max_aps=None, max_aps_text="No fixed limit (licensed per device)", max_clients=None,
    throughput_gbps=None, throughput_text="Local switching at the AP, or tunnelled to a gateway", ports=None, ha="HPE-hosted service", psu_redundant=None,
    datasheet=QS("a00140933enw").replace("collaterals/collateral.a00140933enw.html", "collaterals/collateral.a50006999enw.html"),
    notes="Cloud management for HPE Aruba APs, switches and gateways. The gateway QuickSpecs describe the gateways as cloud-optimized; no capacity figures are published for Central itself.")

# ---------------- Juniper (HPE Mist) ----------------
add(dict(vendor="Juniper", deployment="Cloud", verified=P), family="Juniper Mist", model="Juniper Mist cloud (HPE Mist)", form="Cloud service",
    size="Hosted by HPE Mist", max_aps=None, max_aps_text="No fixed limit (subscription per AP)", max_clients=None, throughput_gbps=None,
    throughput_text="Local switching at the AP (or tunnelled to Mist Edge)", ports=None, ha="Microservices cloud, HPE-hosted", psu_redundant=None,
    datasheet="https://www.hpe.com/psnow/doc/a00150816enw",
    notes="Juniper APs are managed only from the Mist cloud; there is no on-premises wireless controller. Mist Edge (below) adds on-site tunnel termination.")
me = dict(vendor="Juniper", family="Mist Edge", deployment="On-premises", form="Appliance (tunnel termination)", ha="Clustered Mist Edges")
add(me, model="Mist Edge ME-X1", size=None, max_aps=500, max_aps_text=None, max_clients=5000, throughput_gbps=2, throughput_text=None,
    ports="2x 1G RJ-45 data", psu_redundant="No", verified=V,
    datasheet="https://networkingdocs.hpe.com/documentation/us/en/hardware/me-x1/topics/concept/me-x1-overview.html",
    notes="On-site data plane for Mist-managed APs (tunnelling, guest anchoring). One 250 W power supply.")
add(me, model="Mist Edge ME-X5", size=None, max_aps=5000, max_aps_text=None, max_clients=50000, throughput_gbps=20, throughput_text="20 Gbps (some sources say 40 Gbps)",
    ports="2x 10G SFP+ data", psu_redundant="Yes", verified=N, datasheet="https://www.juniper.net/gb/en/products/access-points/edge.html",
    notes="Official hardware page is no longer online; figures from Juniper's Mist Edge product page and partner copies, which disagree on throughput.")
add(me, model="Mist Edge ME-X10", size=None, max_aps=10000, max_aps_text="10,000 (some sources say 5,000)", max_clients=100000, throughput_gbps=40, throughput_text=None,
    ports="4x 10G SFP+ data", psu_redundant="Yes", verified=N, datasheet="https://www.juniper.net/gb/en/products/access-points/edge.html",
    notes="Official hardware page is no longer online; figures from Juniper's Mist Edge product page and partner copies.")

# ---------------- Fortinet ----------------
f = dict(vendor="Fortinet", family="FortiGate wireless controller", deployment="On-premises", form="Appliance (integrated in FortiGate)",
         verified=V, max_clients=None, ports=None, ha="FortiGate HA cluster / AP failover between FortiGates", psu_redundant=None, datasheet=FMX)
for model, size, tun, tot, aps_n, tp_text, tp in [
    ("FortiGate / FortiWiFi 30 & 40 Series", "Desktop", "8", "16", 16, "3.5 Gbps", 3.5),
    ("FortiGate / FortiWiFi 60 & 70 Series", "Desktop", "32", "64", 64, "8 to 8.5 Gbps", 8.5),
    ("FortiGate / FortiWiFi 80 & 90 Series", "Desktop", "48-64", "96-128", 128, "9 to 23.6 Gbps", 23.6),
    ("FortiGate 100 Series", "1RU", "64", "128", 128, "15 to 35 Gbps", 35),
    ("FortiGate 200 Series", "1RU", "128", "256", 256, "20 Gbps", 20),
    ("FortiGate 400 Series", "1RU", "256", "512", 512, "14.8 to 65 Gbps", 65),
    ("FortiGate 600 to 900 Series", "1RU", "512-1,024", "1,024-2,048", 2048, "18 to 70 Gbps", 70),
    ("FortiGate 1000 to 3000 Series", "2-3RU", "2,048", "4,096-8,192", 8192, "11 to 65 Gbps", 65),
    ("FortiGate 4000 Series", "3RU", "4,096", "8,192", 8192, "47 to 63 Gbps", 63)]:
    add(f, model=model, size=size, max_aps=aps_n, max_aps_text=tot + " total (" + tun + " in tunnel mode)", throughput_gbps=tp,
        throughput_text=tp_text + " CAPWAP", notes="Wireless controller is built into every FortiGate (FortiOS 7.4+) with no extra license. Figures are per series; check the model datasheet.")
add(f, model="FortiGate-VM", form="Virtual", size="VM", max_aps=4096, max_aps_text="64-4,096 total (32-2,048 tunnel) by VM size", throughput_gbps=None,
    throughput_text="See the FortiGate-VM datasheet", notes="Virtual FortiGate acting as wireless controller.")
add(dict(vendor="Fortinet", deployment="Cloud", verified=P), family="FortiManagement Cloud", model="FortiManagement Cloud", form="Cloud service",
    size="Hosted by Fortinet", max_aps=None, max_aps_text="A handful to thousands of FortiAPs", max_clients=None, throughput_gbps=None,
    throughput_text="Local switching at the AP", ports=None, ha="Fortinet-hosted service", psu_redundant=None, datasheet=FMX,
    notes="Hosted cloud control of standalone FortiAPs; a subscription adds advanced features, troubleshooting and log retention.")

cols = ["vendor", "family", "model", "deployment", "form", "size", "max_aps", "max_aps_text", "max_clients", "throughput_gbps", "throughput_text",
        "ports", "ha", "psu_redundant", "verified", "notes", "datasheet"]
out = []
for r in rows:
    r.setdefault("max_aps_text", None); r.setdefault("throughput_text", None)
    missing = [k for k in cols if k not in r]
    if missing: sys.exit(f"{r.get('model')}: missing {missing}")
    out.append({k: r[k] for k in cols})
assert len({o["model"] for o in out}) == len(out), "duplicate model"
json.dump({"rows": out, "meta": [{"label": "How made", "value": "Checked by Claude on 15 Nov 2026 against the Cisco controller datasheets, HPE Aruba gateway QuickSpecs, HPE Mist Edge documentation and Fortinet's Wireless Product Matrix (Nov 2026)."}]},
          open(sys.argv[1], "w"), indent=0)
from collections import Counter
print(len(out), "controllers", Counter(o["vendor"] for o in out), Counter(o["deployment"] for o in out))
