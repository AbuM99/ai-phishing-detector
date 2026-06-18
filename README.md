# Automated AI-Driven Phishing Detection Engine (SARS Threat Profile)

## Disclaimer and Compliance Notice
This project is developed strictly for educational purposes, defensive blueprint testing, and SOC awareness training. The heuristic detection vectors evaluated herein model regional attack methodologies documented by financial institutions and regulatory frameworks within South Africa. This application does not interact with, intercept, or exploit any live institutional infrastructure.

---

## Executive Summary and Regional Threat Landscape
During the historical 2024 and 2025 South African filing periods, financial crime modules and risk mitigation bodies noted an unprecedented surge in targeted social engineering campaigns. Malicious actors launched high-pressure, coordinated "smishing" (SMS phishing) and email phishing operations impersonating the South African Revenue Service (SARS).

These attacks targeted the general public and corporate personnel by utilizing look-alike URLs, typosquatted Top-Level Domains (TLDs), and deep subdirectory trees specifically crafted to harvest banking credentials and hijack digital profiles. 

This project establishes a proactive, automated Blue-Team utility. It ingests suspicious URLs, evaluates lexical and structural heuristics, and integrates seamlessly with Open-Source Threat Intelligence (OSINT) infrastructure via the VirusTotal API. The engine converts raw threat metrics into a normalized severity score, enabling rapid tier-1 triage and automated playbook escalation within a modern Security Operations Center (SOC).

---

## Core Detection Architecture and Data Pipeline
The detection engine processes inputs through a modular, decoupled processing pipeline to limit communication overhead and enforce secure analysis parameters:

[ Incoming Suspicious URL ]│▼┌─────────────────────────────────────────┐│     Lexical Verification Engine         │ Parses domain entropy, length,│      (String-Level Analysis)            │ brand keywords, and TLD variants.└─────────────────────────────────────────┘│▼┌─────────────────────────────────────────┐│      Passive OSINT Interrogation        │ Non-blocking hash and domain lookup│         (VirusTotal API)                │ via authenticated API abstraction.└─────────────────────────────────────────┘│▼┌─────────────────────────────────────────┐│     Normalized Classification Engine    │ Weighted algorithmic calculation│       (Severity Score Generation)       │ to evaluate total malicious metrics.└─────────────────────────────────────────┘│▼[ Final Triage Verdict and Defensive Escalation Playbook ]
