import     if fmt == 'csv':
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(['Log ID', 'Timestamp', 'Source', 'Threat Category', 'Severity', 'Risk Score', 'Threat Actor', 'Content', 'MITRE ATT&CK', 'Is Alert'])
        for l in raw:
            writer.writerow([
                l['log_id'], l['timestamp'], l['source'], l['threat_category'],
                l['severity'], l['risk_score'], l['threat_actor'],
                l['raw_content'].replace('\n', ' '), l['mitre_attack'], l['is_alert']
            ])
        output.seek(0)
        return Response(output.getvalue(), mimetype='text/csv', headers={
            'Content-Disposition': 'attachment; filename=darkweb_security_logs.csv'
        })
    elif fmt == 'cef':
        # Common Event Format: CEF:Version|Device Vendor|Device Product|Device Version|Device Event Class ID|Name|Severity|[Extension]
        lines = []
        for l in raw:
            cef_sev = 10 if l['severity'] == 'CRITICAL' else (7 if l['severity'] == 'HIGH' else (4 if l['severity'] == 'MEDIUM' else 1))
            ext = f"msg={l['raw_content'][:120]} src={l['source']} suser={l['threat_actor']} cs1={l['mitre_attack']} cs1Label=MITRE_TTP"
            cef_line = f"CEF:0|SPECTRE-CTI|DarkWebMonitor|2.0|{l['threat_category']}|{l['threat_category']}|{cef_sev}|{ext}"
            lines.append(cef_line)
        return Response('\n'.join(lines), mimetype='text/plain', headers={
            'Content-Disposition': 'attachment; filename=darkweb_logs.cef'
        })
    else: # Default JSON
        return jsonify(raw)
if __name__ == '__main__':
    # Initialize SQLite database
    db.init_db()
    print("=================================================================")
    print("  SPECTRE CTI - DARK WEB MONITORING & DE-ANONYMIZATION PLATFORM  ")
    print("  Server listening on http://127.0.0.1:5000                       ")
    print("=================================================================")
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)