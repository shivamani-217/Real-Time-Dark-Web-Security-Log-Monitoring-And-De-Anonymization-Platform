# SPECTRE CTI: Real-Time Dark Web Security Log Monitoring & De-Anonymization Platform
**SPECTRE CTI** is an enterprise-grade Cyber Threat Intelligence (CTI) and Threat Actor Attribution platform designed for Security Operations Centers (SOC), Incident Response (IR) teams, and forensic analysts.
The platform continuously monitors underground cybercrime ecosystems (Tor Hidden Services, I2P forums, ransomware leak blogs, paste sites, and illicit Telegram channels), detects compromised organizational assets in real time, and leverages **multi-vector entity correlation** to de-anonymize threat actors operating behind anonymity networks.
---
## 🎯 Key Capabilities
### 1. Real-Time Dark Web Security Log Monitoring
* **Continuous Ingestion Stream**: Ingests threat feeds from LockBit 3.0, BlackCat/ALPHV, RansomHub, BreachForums, Dread, Exploit.in, RAMP, DeepPaste, and underground Telegram channels.
* **Server-Sent Events (SSE)**: Ultra-low latency live event broadcast directly to the analyst dashboard without aggressive polling.
* **Granular Threat Categorization**:
  * Ransomware Double-Extortion & Data Leak Sites (DLS)
  * Database Breaches & Customer PII Auctions
  * Initial Access Brokerage (IAB) & Active Directory Privileges
  * Corporate Credential Combo Lists (RedLine, LummaC2 stealer logs)
  * Zero-Day & N-Day Exploit PoC Brokerage
  * Insider Threats & Leaked Cloud Credentials (AWS, Azure, GitHub)
* **MITRE ATT&CK® Mapping**: Automatic technique tagging (e.g., T1486, T1552, T1190, T1078, T1539).
### 2. Multi-Vector De-Anonymization & Attribution Engine
Threat actors hide behind pseudonyms and Tor/I2P routing. SPECTRE CTI de-anonymizes operators through **5-vector forensic correlation**:
1. **Financial Footprint (Blockchain KYC Off-Ramp Tracing)**:
   * Extracts Bitcoin & Monero ransom/market addresses.
   * Clusters multi-input transaction graphs to identify consolidation wallets.
   * Pinpoints direct transfers into KYC-regulated exchanges (Binance, Kraken, Coinbase, Garantex) subject to legal subpoena.
2. **Cryptographic Key Resolution (PGP & GPG Fingerprinting)**:
   * Extracts PGP public key fingerprints and subkeys from ransom negotiation notes and forum profiles.
   * Correlates key reuse against historic forum archives (2018–2026) and clearweb GPG keyservers (GitHub commit signing keys, Keybase, OpenPGP keyservers).
3. **Infrastructure & TLS Fingerprinting (JARM & Shodan Correlation)**:
   * Maps backend C2 staging nodes using JARM TLS fingerprints and SSL certificate serial numbers.
   * Detects self-signed certificates or Favicon mmh3 hashes exposed on public clearnet IPs.
4. **Temporal & Stylometric Profiling**:
   * Evaluates threat actor posting hour histograms to determine UTC timezone offsets.
   * Analyzes language quirks and Russian/Cyrillic keyboard transliteration patterns.
5. **Interactive Visual Force-Directed Attribution Graph**:
   * Canvas-based network graph mapping the entire evidence chain:
     $$\text{Threat Actor} \longrightarrow \text{Wallets} \longrightarrow \text{KYC Exchange} \longrightarrow \text{PGP Key} \longrightarrow \text{Clearnet Dev} \longrightarrow \text{De-Anonymized Persona}$$
   * Interactive node drag, zoom, pan, and click-to-trace forensic evidence drawer.
   * Mathematical Attribution Confidence Scoring (0–98%).
### 3. Corporate Watchlist & Real-Time Alert Engine
* Register organizational domains (e.g., `novacapital-fin.com`), executive VIP emails (`ciso@target.com`), cloud API key prefixes, or CIDR blocks.