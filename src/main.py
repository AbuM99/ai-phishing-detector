# AI Phishing Detector — Project 1
# Inspired by SARS phishing campaigns in South Africa (2024-2025)
 
import re, json, sqlite3, requests, os
from datetime import datetime
from dotenv import load_dotenv
 
load_dotenv() # loads your .env file
 
# ── STEP 1: Extract features from the URL ──
def extract_features(url):
	features = {}
	features['url_length'] = len(url)
	features['has_ip'] = 1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0
	features['num_dots'] = url.count('.')
	features['has_https'] = 1 if url.startswith('https') else 0
	features['has_suspicious_words'] = 1 if any(w in url.lower()
											for w in ['login', 'secure', 'sars', 'refund', 'verify', 'bank']) else 0
	return features
 
# ── STEP 2: Check URL against VirusTotal ──
def check_virustotal(url):
	import base64
	api_key = os.getenv('VT_API_KEY')
	if not api_key:
		return 0
	url_id = base64.urlsafe_b64encode(url.encode()).decode().strip('=')
	try:
		r = requests.get(
			f'https://www.virustotal.com/api/v3/urls/{url_id}',
			headers={'x-apikey': api_key}, timeout=10)
		if r.status_code == 200:
			stats = r.json()['data']['attributes']['last_analysis_stats']
			return stats.get('malicious', 0)
	except Exception:
		return 0
	return 0
 
# ── STEP 3: Score and decide verdict ──
def analyse_url(url):
	f = extract_features(url)
	vt_hits = check_virustotal(url)
	# Simple scoring: each red flag adds points
	score = 0
	if f['url_length'] > 75: score += 20
	if f['has_ip']: score += 25
	if not f['has_https']: score += 15
	if f['has_suspicious_words']: score += 20
	if vt_hits > 5: score += 20
	if vt_hits > 15: score += 10
	verdict = 'PHISHING' if score >= 60 else 'SUSPICIOUS' if score >= 35 else 'CLEAN'
	result = {
		'url': url,
		'verdict': verdict,
		'phishing_score': score,
		'vt_malicious_engines': vt_hits,
		'mitre_technique': 'T1566.002' if verdict == 'PHISHING' else 'N/A',
		'recommended_action': 'Block & escalate to L2' if verdict == 'PHISHING' else 'Monitor',
		'timestamp': datetime.utcnow().isoformat()
	}
	return result
 
# ── STEP 4: Run it ──
if __name__ == '__main__':
	url = input("Enter a URL to check: ")
	result = analyse_url(url)
	print(json.dumps(result, indent=2))
    
