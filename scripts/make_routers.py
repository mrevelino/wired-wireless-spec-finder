"""Generate data/routers.json: current enterprise routers from Cisco, HPE Aruba and Juniper (checked 15 Nov 2026).
End-of-life models are excluded (see README). Fortinet is excluded by request."""
import json, sys

V, P = "Verified", "Partly verified"
CS = "https://www.cisco.com/site/us/en/products/collateral/networking/sdwan-routers/8000-secure-routers/"
ISR = "https://www.cisco.com/c/en/us/products/collateral/routers/1000-series-integrated-services-routers-isr/datasheet-c78-739512.html"
C8KV = "https://www.cisco.com/c/en/us/products/collateral/routers/catalyst-8000v-edge-software/datasheet-c78-744101.html"
EC = "https://www.hpe.com/us/en/collaterals/collateral.a50004289enw.html"
PS = lambda i: "https://www.hpe.com/psnow/doc/" + i

rows = []
def add(base, **kw):
    r = dict(base); r.update(kw); rows.append(r)

# ---------------- Cisco 8000 Series Secure Routers ----------------
c = dict(vendor="Cisco", sdwan="Cisco Catalyst SD-WAN or Meraki", verified=V, storage_gb=None, dram_gb=None, slots="None",
         cellular="No", psu_redundant=None, max_sessions=None)
c81 = dict(c, family="Cisco 8100 Secure Router", segment="Small branch", form="Desktop", datasheet=CS + "8100-series-secure-routers-ds.html",
           notes="Desktop, wall, DIN-rail or rack mount. External power adapter. Throughput: forwarding / IPsec / SD-WAN (IPsec+QoS+DPI+FNF), 512-byte packets.")
add(c81, model="C8130-G2", ports="1x 1G RJ-45 + 1x 1G combo WAN, 2x 1G flex, 2x 1G LAN", port_max_gbps=1, throughput_gbps=1.9, ipsec_gbps=1.5,
    throughput_text="1.9 / 1.5 / 0.9 Gbps")
add(c81, model="C8130H-G2", ports="1x 1G combo + 1x 10G BASE-T WAN, 2x 1G flex, 2x 1G LAN", port_max_gbps=10, throughput_gbps=1.9, ipsec_gbps=1.5,
    throughput_text="1.9 / 1.5 / 0.9 Gbps")
add(c81, model="C8140-G2", ports="2x 1G combo WAN, 2x 1G flex, 6x 1G LAN", port_max_gbps=1, throughput_gbps=5.6, ipsec_gbps=1.5,
    throughput_text="5.6 / 1.5 / 0.9 Gbps")
add(c81, model="C8151-G2", ports="2x 1G combo WAN, 2x 1G flex, 6x 1G LAN", port_max_gbps=1, throughput_gbps=5.6, ipsec_gbps=1.5,
    throughput_text="5.6 / 1.5 / 0.9 Gbps (threat protection 1 Gbps)", slots="1 PIM", cellular="Optional (LTE Cat 7 or 5G PIM)")
add(c81, model="C8161-G2", ports="2x 1G combo WAN, 2x 1G flex, 6x 1G LAN (PoE/PoE+, 80 W)", port_max_gbps=1, throughput_gbps=5.6, ipsec_gbps=1.5,
    throughput_text="5.6 / 1.5 / 0.9 Gbps (threat protection 1 Gbps)", slots="1 PIM", cellular="Optional (LTE Cat 7 or 5G PIM)")
add(c81, model="C8151H-C-G2", ports="1x 1G combo + 1x 10G BASE-T WAN, 8x 1G RJ-45", port_max_gbps=10, throughput_gbps=5.6, ipsec_gbps=1.5,
    throughput_text="5.6 / 1.5 / 0.9 Gbps (threat protection 1 Gbps)", cellular="Built-in 5G RedCap (dual SIM)")
c82 = dict(c, family="Cisco 8200 Secure Router", datasheet=CS + "8200-series-secure-routers-ds.html",
           notes="Throughput: forwarding / IPsec / SD-WAN, 512-byte packets.")
add(c82, model="C8235-E-G2", segment="Medium branch", form="1RU", ports="2x 1/10G SFP+ + 2x 2.5G mGig (UPoE+) WAN, 4x 2.5G LAN", port_max_gbps=10,
    throughput_gbps=19, ipsec_gbps=5, throughput_text="19 / 5 / 4 Gbps (threat protection 2.4 Gbps)", dram_gb=16, storage_gb=16,
    slots="1 NIM, 1 PIM", cellular="Optional (5G or LTE PIM)", notes=c82["notes"] + " Storage upgradeable to 600 GB.")
add(c82, model="C8231-E-G2", segment="Medium branch", form="1RU", ports="2x 1/10G SFP+ + 2x 2.5G mGig (UPoE+) WAN", port_max_gbps=10,
    throughput_gbps=19, ipsec_gbps=5, throughput_text="19 / 5 / 4 Gbps (threat protection 1 Gbps)", dram_gb=8, storage_gb=16, slots="1 NIM")
add(c82, model="C8235-G2", segment="Medium branch", form="Desktop", ports="2x 1/10G SFP+, 2x 2.5G flex, 4x 2.5G LAN", port_max_gbps=10,
    throughput_gbps=19, ipsec_gbps=5, throughput_text="19 / 5 / 4 Gbps (threat protection 2.4 Gbps)", dram_gb=16, storage_gb=16,
    slots="1 PIM", cellular="Optional (5G or LTE PIM)", psu_redundant="Optional")
add(c82, model="C8231-G2", segment="Medium branch", form="Desktop", ports="2x 1/10G SFP+, 4x 2.5G mGig, 4x 1G", port_max_gbps=10,
    throughput_gbps=19, ipsec_gbps=5, throughput_text="19 / 5 / 4 Gbps (threat protection 1 Gbps)", dram_gb=8, storage_gb=16, psu_redundant="Optional")
add(c82, model="C8225-G2", segment="Medium branch", form="Desktop", ports="2x 1/10G SFP+ + 2x 1G WAN, 4x 1G LAN", port_max_gbps=10,
    throughput_gbps=19, ipsec_gbps=5, throughput_text="19 / 5 / 4 Gbps (threat protection 2.4 Gbps)", dram_gb=16, storage_gb=16, psu_redundant="Yes (dual input)")
add(c82, model="C8211-G2", segment="Small branch", form="Desktop", ports="2x 1G combo WAN, 4x 1G LAN", port_max_gbps=1,
    throughput_gbps=5.6, ipsec_gbps=3, throughput_text="5.6 / 3 / 2 Gbps (threat protection 1 Gbps)", psu_redundant="Yes (dual input)")
c83 = dict(c, family="Cisco 8300 Secure Router", segment="Large branch", form="1RU", datasheet=CS + "8300-series-secure-routers-ds.html",
           notes="Throughput: forwarding / IPsec / SD-WAN, 512-byte packets.")
add(c83, model="C8375-E-G2", ports="2x 10G SFP+ + 4x 2.5G mGig (2x UPoE+)", port_max_gbps=10, throughput_gbps=38, ipsec_gbps=20,
    throughput_text="38 / 20 / 12 Gbps (threat protection 7 Gbps)", dram_gb=16, storage_gb=16, slots="1 NIM, 1 SM, 1 PIM",
    cellular="Optional (5G or LTE PIM)", psu_redundant="Yes",
    notes=c83["notes"] + " DRAM up to 32 GB; storage options to 2 TB. Dual power supplies by default.")
add(c83, model="C8355-G2", ports="4x 10G SFP+, 4x 5G mGig (UPoE+), 2x 1G", port_max_gbps=10, throughput_gbps=38, ipsec_gbps=20,
    throughput_text="38 / 20 / 8.7 Gbps (threat protection 3.9 Gbps)", dram_gb=16, storage_gb=16, slots="1 PIM", cellular="Optional (cellular PIM)")
c84 = dict(c, family="Cisco 8400 Secure Router", segment="Head office / hub", form="1RU", datasheet=CS + "8400-series-secure-routers-ds.html",
           notes="Throughput: forwarding / IPsec / SD-WAN. AC, DC and HVDC power options.")
add(c84, model="C8455-G2", ports="8x 1G SFP + 2x 1/10G SFP+ + 2x 10/25G SFP28", port_max_gbps=25, throughput_gbps=67, ipsec_gbps=31,
    throughput_text="67 / 31 / 15.5 Gbps (security 9.5 Gbps)", dram_gb=32, storage_gb=64)
add(c84, model="C8475-G2", ports="8x 1G SFP + 8x 1/10G SFP+ + 4x 10/25G SFP28", port_max_gbps=25, throughput_gbps=91, ipsec_gbps=45,
    throughput_text="91 / 45 / 21.7 Gbps (security 10.9 Gbps)", dram_gb=32, storage_gb=64)
c85 = dict(c, family="Cisco 8500 Secure Router", segment="WAN aggregation", form="1RU", datasheet=CS + "8500-series-secure-routers-ds.html",
           notes="Throughput: forwarding / IPsec / SD-WAN. DRAM upgradeable to 64 GB. AC or DC power.")
add(c85, model="C8550-G2", ports="12x 1/10G SFP+", port_max_gbps=10, throughput_gbps=115, ipsec_gbps=48,
    throughput_text="115 / 48 / 19 Gbps", dram_gb=32, storage_gb=480)
add(c85, model="C8570-G2", ports="12x 1/10G SFP+ + 2x 40G QSFP+ + 2x 40/100G QSFP28", port_max_gbps=100, throughput_gbps=190, ipsec_gbps=63,
    throughput_text="190 / 63 / 21 Gbps", dram_gb=32, storage_gb=480)
ci = dict(c, family="Cisco ISR 1000 (C1121)", segment="Small branch", form="Desktop", datasheet=ISR,
          notes="Throughput: SD-WAN IPsec / SD-WAN profile / autonomous forwarding, 512-byte packets. External power adapter.")
add(ci, model="C1121-4P", ports="2x WAN + 4x 1G LAN", port_max_gbps=1, throughput_gbps=1.6, ipsec_gbps=0.45,
    throughput_text="0.45 / 0.2 / 1.6 Gbps", dram_gb=4, storage_gb=4)
add(ci, model="C1121-4PLTEP", ports="2x WAN + 4x 1G LAN", port_max_gbps=1, throughput_gbps=1.6, ipsec_gbps=0.45,
    throughput_text="0.45 / 0.2 / 1.6 Gbps", dram_gb=4, storage_gb=4, slots="1 PIM", cellular="Yes (LTE PIM; 5G option)")
add(ci, model="C1121-8P", ports="2x WAN + 8x 1G LAN", port_max_gbps=1, throughput_gbps=1.6, ipsec_gbps=0.7,
    throughput_text="0.7 / 0.25 / 1.6 Gbps", dram_gb=4, storage_gb=4)
add(ci, model="C1121X-8P", ports="2x WAN + 8x 1G LAN", port_max_gbps=1, throughput_gbps=1.6, ipsec_gbps=0.7,
    throughput_text="0.7 / 0.25 / 1.6 Gbps", dram_gb=8, storage_gb=8)
add(ci, model="C1121-8PLTEP", ports="2x WAN + 8x 1G LAN", port_max_gbps=1, throughput_gbps=1.6, ipsec_gbps=0.7,
    throughput_text="0.7 / 0.25 / 1.6 Gbps", dram_gb=4, storage_gb=4, slots="1 PIM", cellular="Yes (LTE PIM; 5G option)")
add(c, family="Cisco Catalyst 8000V", model="Catalyst 8000V Edge Software", segment="Virtual / cloud", form="Virtual",
    ports="Virtual NICs (up to 26 on KVM, 8 on ESXi)", port_max_gbps=None, throughput_gbps=40, ipsec_gbps=None,
    throughput_text="50 Mbps to 40 Gbps by license tier and vCPUs", dram_gb=16, storage_gb=None, slots="n/a",
    cellular="No", psu_redundant=None, datasheet=C8KV, verified=P,
    notes="Virtual router for private and public cloud (AWS, Azure, GCP). 2-16 vCPU, 4-16 GB memory. Throughput depends on the license tier and host.")

# ---------------- HPE Aruba EdgeConnect SD-WAN ----------------
a = dict(vendor="HPE Aruba", family="EdgeConnect SD-WAN gateway", sdwan="HPE Aruba EdgeConnect SD-WAN", verified=V,
         dram_gb=None, storage_gb=None, slots="None", cellular="No", ipsec_gbps=None, datasheet=EC)
note = "Throughput is the typical WAN bandwidth (bidirectional; double it for total Rx+Tx). IDS/IPS included."
add(a, model="EC-10104", segment="Small branch", form="Desktop", ports="4x 1G RJ-45", port_max_gbps=1, throughput_gbps=0.5,
    throughput_text="2-500 Mbps WAN; WAN optimization up to 200 Mbps", max_sessions=256000, psu_redundant="No", notes="Small branch or home office. " + note)
add(a, model="EC-XS", segment="Small branch", form="Desktop", ports="4x 1G RJ-45", port_max_gbps=1, throughput_gbps=1,
    throughput_text="2-1,000 Mbps WAN; WAN optimization 250 Mbps", max_sessions=256000, psu_redundant="No", notes=note)
add(a, model="EC-10106", segment="Small branch", form="Desktop", ports="2x 1/10G SFP+, 2x combo (SFP/1G), 2x 1G (PoE)", port_max_gbps=10,
    throughput_gbps=1, throughput_text="2-1,000 Mbps WAN; WAN optimization 250 Mbps", max_sessions=256000, psu_redundant="No", notes=note)
add(a, model="EC-10108", segment="Medium branch", form="Desktop", ports="2x 1/10G SFP+, 2x combo (SFP/1G), 2x 1G (PoE)", port_max_gbps=10,
    throughput_gbps=2, throughput_text="2-2,000 Mbps WAN; WAN optimization up to 500 Mbps", max_sessions=256000, psu_redundant="No", notes=note)
add(a, model="EC-M-H", segment="Head office / hub", form="1RU", ports="8x 1G RJ-45 + 4x 1/10G optical", port_max_gbps=10, throughput_gbps=5,
    throughput_text="50-5,000 Mbps WAN; WAN optimization 1 Gbps", max_sessions=2000000, psu_redundant="Yes (FRU, extra SKU)",
    notes="Head office or data-center hub. SSD and power supply are field-replaceable. " + note)
add(a, model="EC-L-H", segment="Head office / hub", form="1RU", ports="6x 1/10G optical", port_max_gbps=10, throughput_gbps=10,
    throughput_text="2-10 Gbps WAN; WAN optimization 1 Gbps", max_sessions=2000000, psu_redundant="Yes (FRU, extra SKU)", notes="Data-center hub. " + note)
add(a, model="EC-XL-H", segment="Head office / hub", form="1RU", ports="6x 1/10/25G optical (10G version: 6x 1/10G)", port_max_gbps=25, throughput_gbps=10,
    throughput_text="2-10 Gbps WAN; WAN optimization 5 Gbps", max_sessions=2000000, psu_redundant="Yes (FRU, extra SKU)",
    notes="Data-center hub with NVMe for WAN optimization. " + note)
add(a, model="EC-10150", segment="Head office / hub", form="1RU", ports="2x 1G RJ-45 + 8x 1/10G SFP+ or 10/25G SFP28", port_max_gbps=25, throughput_gbps=12,
    throughput_text="Up to 12 Gbps WAN; WAN optimization 8 Gbps", max_sessions=2000000, psu_redundant="Yes (FRU, extra SKU)",
    notes="Data-center hub. " + note)

# ---------------- Juniper (HPE Networking) ----------------
j = dict(vendor="Juniper", verified=V, slots="None", max_sessions=None)
ssr = dict(j, family="Session Smart Router", sdwan="HPE Mist WAN Assurance (Session Smart)", cellular="No", ipsec_gbps=None)
add(ssr, model="SSR120", segment="Small branch", form="Desktop", ports="4x 1G RJ-45 + 2x 1G RJ-45/SFP combo", port_max_gbps=1,
    throughput_gbps=1.5, ipsec_gbps=0.25, throughput_text="Unencrypted 1.5 Gbps / encrypted 750 Mbps / encrypted+HMAC 250 Mbps (IMIX)",
    dram_gb=None, storage_gb=None, cellular="Optional (LTE SKUs SSR120-AA / -AE)", psu_redundant=None, datasheet=PS("a00150824enw"),
    notes="Managed from HPE Mist. Throughput as measured on Session Smart software v5, IMIX packets.")
add(ssr, model="SSR130", segment="Medium branch", form="Desktop", ports="6x 1G RJ-45 + 2x 1G RJ-45/SFP combo", port_max_gbps=1,
    throughput_gbps=2, ipsec_gbps=1, throughput_text="Unencrypted 2 Gbps (line rate) / encrypted 1.8 Gbps / encrypted+HMAC 1 Gbps (IMIX)",
    dram_gb=None, storage_gb=None, cellular="Optional (LTE SKUs SSR130-AA / -AE)", psu_redundant=None, datasheet=PS("a00150824enw"),
    notes="Managed from HPE Mist. Throughput as measured on Session Smart software v5, IMIX packets.")
s1k = dict(ssr, form="1RU", psu_redundant="Yes", datasheet=PS("a00150832enw"),
           notes="Managed from HPE Mist. Redundant AC power (1+1) included. Throughput: unencrypted / encrypted / encrypted+HMAC, IMIX.")
add(s1k, model="SSR1200", segment="Large branch", ports="7x 1G RJ-45 + 4x 1/10G SFP+", port_max_gbps=10, throughput_gbps=10, ipsec_gbps=2.5,
    throughput_text="10 / 7 / 2.5 Gbps", dram_gb=64, storage_gb=256)
add(s1k, model="SSR1300", segment="Head office / hub", ports="4x 1G RJ-45 + 4x 10G SFP+ + 4x 1/10G SFP+", port_max_gbps=10, throughput_gbps=20,
    ipsec_gbps=5, throughput_text="20 / 18 / 5 Gbps", dram_gb=128, storage_gb=256)
add(s1k, model="SSR1400", segment="Head office / hub", ports="4x 1G RJ-45 + 4x 10G SFP+ + 4x 1/10/25G SFP28", port_max_gbps=25, throughput_gbps=40,
    ipsec_gbps=10, throughput_text="40 / 25 / 10 Gbps", dram_gb=256, storage_gb=512)
add(s1k, model="SSR1500", segment="WAN aggregation", ports="4x 1G RJ-45 + 12x 1/10/25G SFP28", port_max_gbps=25, throughput_gbps=50,
    ipsec_gbps=30, throughput_text="50 / 45 / 30 Gbps", dram_gb=512, storage_gb=1000)
mx = dict(j, family="MX Universal Routing Platform", sdwan="Junos (no SD-WAN orchestration)", cellular="No", ipsec_gbps=None, dram_gb=None, storage_gb=None)
add(mx, model="MX301", segment="WAN aggregation", form="1RU", ports="Up to 16x 1-50G, 10x 100G or 4x 400G", port_max_gbps=400, throughput_gbps=1600,
    throughput_text="Up to 1.6 Tbps", psu_redundant="Yes", datasheet=PS("a00155177enw"),
    notes="Enterprise WAN edge, core and secure SD-WAN head end. MACsec on 100G/400G. 1+1 power supplies, N+1 fans.")
add(mx, model="MX304", segment="WAN aggregation", form="2RU", ports="Modular MICs: 1G to 400G", port_max_gbps=400, throughput_gbps=4800,
    throughput_text="Up to 4.8 Tbps", slots="MIC slots", psu_redundant="Yes", datasheet=PS("a00150831enw"),
    notes="Dual routing engines, 1+1 power. Line-rate 400G MACsec; inline IPsec in the forwarding engine.")

EOL_EXCLUDED = {
    "Cisco Catalyst 8200 Edge (C8200-1N-4T, C8200L-1N-4T)": "EOL15955, end of sale 31 Jul 2027",
    "Cisco Catalyst 8300 Edge (C8300-1N1S, C8300-2N2S)": "EOL15950 / EOL15955, end of sale 31 Jan / 31 Jul 2027",
    "Cisco Catalyst 8500 Edge (C8500-12X, -12X4QC, -20X6C, C8500L-8S4X)": "EOL15949 / EOL15954 / EOL15950, end of sale 2027",
    "Cisco ISR 1100/1100X, 1101, 1109, 1111": "end of sale 28 Jul 2026",
    "Cisco ISR 1112/1113/1116/1117/1131/1161": "EOL15945, end of sale 31 Jan 2027",
    "Juniper MX204": "TSB107750, last order 15 Jun 2027",
    "HPE Aruba EdgeConnect EC-S-P": "end of sale 31 Dec 2024 (HPE warranty quick reference)",
}

cols = ["vendor", "family", "model", "segment", "form", "ports", "port_max_gbps", "throughput_gbps", "ipsec_gbps", "throughput_text",
        "dram_gb", "storage_gb", "slots", "cellular", "psu_redundant", "max_sessions", "sdwan", "verified", "notes", "datasheet"]
out = []
for r in rows:
    missing = [k for k in cols if k not in r]
    if missing: sys.exit(f"{r.get('model')}: missing {missing}")
    out.append({k: r[k] for k in cols})
assert len({o["model"] for o in out}) == len(out), "duplicate model"
json.dump({"rows": out, "meta": [{"label": "How made", "value": "Checked by Claude on 15 Nov 2026 against Cisco 8000 Secure Router, ISR 1000 and Catalyst 8000V datasheets, the HPE Aruba EdgeConnect SD-WAN QuickSpecs and HPE-hosted Juniper SSR and MX datasheets. End-of-life models excluded."},
                             {"label": "End-of-life models excluded", "value": "; ".join(f"{k}: {v}" for k, v in EOL_EXCLUDED.items())}]},
          open(sys.argv[1], "w"), indent=0)
from collections import Counter
print(len(out), "routers", Counter(o["vendor"] for o in out))
