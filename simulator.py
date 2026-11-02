import             severity = 'CRITICAL'
            risk_score = random.randint(92, 99)
            raw_content = (
                f"[UNRELEASED EXPLOIT BROKERAGE]\n"
                f"Weaponized zero-day PoC targeting enterprise perimeter appliances.\n"
                f"Affected vendor advisory: {cve}\n"
                f"Reliability: 100% remote code execution without authentication.\n"
                f"Includes Python bypass harness, memory corruption trigger, and C2 beacon.\n"
                f"Sold to 1 buyer exclusively. Proof-of-concept video available upon PGP negotiation."
            )
            entities = {
                'cve_refs': [cve],
                'exploit_type': 'Unauthenticated Remote Code Execution',
                'pgp_id': f"0x{random.randint(10000000, 99999999):X}"
            }
        else: # Insider Threat
            severity = 'HIGH'
            risk_score = random.randint(75, 89)
            raw_content = (
                f"[INSIDER ACCESS OFFERED]\n"
                f"Current senior DevOps engineer at {company} offering internal GitHub repository dumps, AWS infrastructure Terraform scripts, and private API keys (AWS_SECRET_ACCESS_KEY).\n"
                f"Monero payment only. Serious threat syndicates only."
            )
            entities = {
                'domains': [domain],
                'leaked_assets': ['AWS_SECRET_ACCESS_KEY', 'Terraform State', 'GitHub Repositories']
            }
        return {
            'log_id': log_id,
            'timestamp': timestamp,
            'source': source_name,
            'source_url': source_url,
            'threat_category': category,
            'severity': severity,
            'risk_score': risk_score,
            'threat_actor': actor_name,
            'actor_id': actor_id,
            'raw_content': raw_content,
            'extracted_entities': entities,
            'mitre_attack': mitre
        }
# Global simulator instance
simulator = DarkWebSimulator()